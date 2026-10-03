"""Reviewed deterministic geometry core; no data, tokenizer or model runner.

Body items are (token_id, start_char0, end_char0); evidence ordinals are
zero-based positions within that body. See PROTOCOL.md for prerequisites.
"""
import hashlib

NODE_CAP = 10000

class PreflightError(RuntimeError):
    pass


def evidence_fragments(evidence_ordinals: list[int], body: list[tuple[int, int, int]]) -> list[dict]:
    if not evidence_ordinals:
        return []
    ordinal_list = sorted(set(evidence_ordinals))
    groups: list[tuple[int, int]] = []
    start = previous = ordinal_list[0]
    for ordinal in ordinal_list[1:]:
        if ordinal == previous + 1:
            previous = ordinal
            continue
        groups.append((start, previous + 1))
        start = previous = ordinal
    groups.append((start, previous + 1))
    total_body = len(body)
    fragments = []
    for index, (start_ordinal, end_ordinal) in enumerate(groups):
        if not (0 <= start_ordinal < end_ordinal <= total_body):
            raise PreflightError("evidence_fragment_outside_body")
        fragments.append({
            "fragment_index": index,
            "start_ordinal": start_ordinal,
            "end_ordinal_exclusive": end_ordinal,
            "length": end_ordinal - start_ordinal,
            "start_quartile": (4 * start_ordinal) // total_body,
            "start_char0": body[start_ordinal][1],
            "end_char0": body[end_ordinal - 1][2],
        })
    return fragments


def placeholder_candidates(fragments: list[dict], body: list[tuple[int, int, int]],
                           evidence_ordinals: list[int], run_seed: int, blind_id: str) -> list[list[dict]]:
    total_body = len(body)
    evidence_set = set(evidence_ordinals)
    all_candidates = []
    for fragment in fragments:
        length = fragment["length"]
        candidates = []
        if length <= total_body:
            for start in range(0, total_body - length + 1):
                if (4 * start) // total_body != fragment["start_quartile"]:
                    continue
                end = start + length
                if any(ordinal in evidence_set for ordinal in range(start, end)):
                    continue
                key = (
                    f"20261002-evidence-placebo-v1:{run_seed}:{blind_id}:"
                    f"{fragment['fragment_index']}:{start}"
                ).encode("utf-8")
                candidates.append({
                    "start_ordinal": start,
                    "end_ordinal_exclusive": end,
                    "length": length,
                    "start_quartile": (4 * start) // total_body,
                    "sha256": hashlib.sha256(key).hexdigest(),
                })
        candidates.sort(key=lambda item: (item["sha256"], item["start_ordinal"]))
        all_candidates.append(candidates)
    return all_candidates


def select_geometry(fragments: list[dict], body: list[tuple[int, int, int]],
                    evidence_ordinals: list[int], run_seed: int, blind_id: str) -> dict:
    if not fragments or not body:
        return {"selected": False, "failure_reason": "no_exact_geometry_match", "nodes_visited": 0}
    candidates = placeholder_candidates(fragments, body, evidence_ordinals, run_seed, blind_id)
    selected: list[dict] = []
    nodes_visited = 0
    cap_reached_with_work_remaining = False

    def search(fragment_index: int) -> bool:
        nonlocal nodes_visited, cap_reached_with_work_remaining
        if fragment_index == len(fragments):
            return True
        for candidate in candidates[fragment_index]:
            if nodes_visited >= NODE_CAP:
                cap_reached_with_work_remaining = True
                return False
            # One node is one attempted placement, including a rejected overlap.
            nodes_visited += 1
            start = candidate["start_ordinal"]
            end = candidate["end_ordinal_exclusive"]
            if any(
                max(start, placed["start_ordinal"]) < min(end, placed["end_ordinal_exclusive"])
                for placed in selected
            ):
                continue
            selected.append(candidate)
            if search(fragment_index + 1):
                return True
            selected.pop()
            if cap_reached_with_work_remaining:
                return False
        return False

    found = search(0)
    if not found:
        reason = "selector_search_cap" if cap_reached_with_work_remaining else "no_exact_geometry_match"
        return {"selected": False, "failure_reason": reason, "nodes_visited": nodes_visited}

    chosen = []
    for fragment, candidate in zip(fragments, selected):
        start = candidate["start_ordinal"]
        end = candidate["end_ordinal_exclusive"]
        if candidate["length"] != fragment["length"]:
            raise PreflightError("selected_fragment_length_mismatch")
        if candidate["start_quartile"] != fragment["start_quartile"]:
            raise PreflightError("selected_fragment_quartile_mismatch")
        if any(ordinal in set(evidence_ordinals) for ordinal in range(start, end)):
            raise PreflightError("selected_window_contains_evidence")
        chosen.append({
            "fragment_index": fragment["fragment_index"],
            "start_ordinal": start,
            "end_ordinal_exclusive": end,
            "length": end - start,
            "start_quartile": candidate["start_quartile"],
            "start_char0": body[start][1],
            "end_char0": body[end - 1][2],
        })
    for previous, current in zip(
        sorted(chosen, key=lambda item: item["start_ordinal"]),
        sorted(chosen, key=lambda item: item["start_ordinal"])[1:],
    ):
        if previous["end_ordinal_exclusive"] > current["start_ordinal"]:
            raise PreflightError("selected_windows_overlap")
    return {
        "selected": True,
        "failure_reason": None,
        "nodes_visited": nodes_visited,
        "fragments": chosen,
    }
