# ConsensusRoute 离线候选改进

状态：开发诊断完成，最终分类性能改善尚未验证。

候选先保留双模型分歧，再把剩余批次预算分配给靠近实际阈值的一致样本。复核结构区分任务目标与当前商业行为，并保留待人工复核状态。程序不调用API，不需要原始文本或标签。

- 实现：`code/consensusroute_v2_policy.py`
- 默认参数记录：`config/consensusroute_v2_candidate.json`（命令行参数为实际设置）
- [开发诊断](development_diagnostic.json)：155条已用于模型/阈值选择的开发记录；只有汇总信息，不是独立验证。

最大8个复核名额时，旧分歧路由选择5条、覆盖4条本地错误；候选选择8条、覆盖5条本地错误。实际复核数量不同，而且被选中不等于被正确修复。不能据此声称同实际成本更优或Macro-F1上升。

输入CSV恰好包含 `sample_id,macbert_probability,roberta_probability`。默认阈值0.29/0.21；归一化阈值距离0.25是待验证工程初值，不是校准置信度。先在开发数据选择参数，再冻结并使用新的独立测试集。

```powershell
python code/consensusroute_v2_policy.py --input probabilities.csv --output routes.csv --budget 8
```

可选 `--responses responses.json`，键为选中样本ID，值包含 `target,current_commercial_act,evidence`。解释必须独立核验；结构验证不能证明解释为真。复核失败保留本地预测与待复核状态。比较时使用相同完整分母，并同时报告待复核比例。

没有公开原始数据、样本ID、逐条预测、提示词、API日志或作者声明。旧冻结实验保持原状。
