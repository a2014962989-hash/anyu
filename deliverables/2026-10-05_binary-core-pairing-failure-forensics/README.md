# Reviewed pairing-failure forensic evidence

One bounded CPU audit loaded the designated local checkpoint once in 0.187 seconds. Root reviewed saved results and exact audit mechanics without reloading the checkpoint. Six frozen small inputs matched; the independent saved-output review found zero numerical/static issues.

The initial candidate checkpoint and the control first-batch-before record differed in Python RNG; NumPy, Torch CPU and saved CUDA RNG components matched. These are different capture boundaries. The actual candidate first-step and after-state receipt was lost, so the exact guard trigger remains unobserved.

The source updates optimizer/counters before the pairing guard and saves the successful checkpoint afterwards. A guard exception therefore explains partial one versus saved zero. That historical candidate cannot resume from zero. A later after-state self-comparison is a separate bookkeeping defect.

The audit turn lasted about 20 minutes 51 seconds, exceeding its 20-minute source/read/report limit; this timing deviation is retained. The single checkpoint load remained within its limit.

Root accepted the forensic evidence and commissioned a separate static pairing/persistence correction. No new training, GPU, checkpoint loading or recovery budget was authorized. The method gate remains NOT_EVALUABLE; independent confirmation remains zero and research acceptance criteria remain incomplete.

Only this aggregate narrative and document hashes are published. Private records, RNG states, source code, checkpoints and annotation returns remain local.
