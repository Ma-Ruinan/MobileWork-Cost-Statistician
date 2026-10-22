# MobileWork日志来源和字段

默认来源为 `%USERPROFILE%\.mobilework\xdg\data\opencode\opencode.db`，可通过命令行显式覆盖。该说明记录已核实的日志结构，不代表厂商的长期接口承诺。字段变更需要查看实际记录后修改适配器并重新验证。

message.data 中使用 role、time.created、time.completed、finish、modelID、tokens。只把同时具有完成时间和 finish 的助手消息作为已完成调用；缺少用量时保留缺失。part.data 中读取 type=tool、callID、tool、state.status、state.input、state.metadata.exit 和 state.time。

累计输入为 tokens.input + tokens.cache.read + tokens.cache.write；输出为 tokens.output；缓存读取量为 tokens.cache.read。存在 tokens.total 时核对其等于累计输入加输出，part 中的 step-finish 不再次累计。

模型重试从 event 中 type=session.next.retried.1、aggregate_id=会话ID 的记录读取 timestamp、attempt、error.message。模型重试和工具错误分别记录；缺少 event 表时重试数未记录。

记录不完整时可检查同用户目录下 .mobilework/plugin-reporting/model-raw/会话ID 中的辅助文件。单条 completed 原始模型记录不等于完整任务已完成；不能把未能对应到最终回复的局部用量混入完整任务统计。页面已完成但实际拒答时，通过页面观察文件保留用户提供的证据，对缺少完整执行记录的指标保持空值；已经取得完整数值的拒答执行仍参与统计。

专用搜索工具为 `mobilework_search`。成功交付工具为 `result_file`，从 `output_paths` 或 `files` 数组读取路径。路径相对工作目录解析后去重，逐个核验磁盘存在性；检查过程中的截图、脚本、临时文件不自动算作最终交付。

默认仅统计与题目明确匹配的主会话；独立子会话、后台会话和未匹配用户消息在JSON中单列排除原因。发现与任务相关的子会话时应在报告中记录范围，本版主会话统计不会自动并入其用量。完整输入文本、会话及用户消息标识共同用于关联，不能仅根据目录名称或相近时间配对。

同一批数据默认读取两次并比较。若仍在写入、读取不一致或Token恒等关系变化，脚本停止并返回非零退出码；应查明实际记录后重跑，不能补猜测值。目录时间、session更新时间和数据库费用零值都不替代已核实的字段。
