# MobileWork日志来源和字段

默认来源为 `%USERPROFILE%\.mobilework\xdg\data\opencode\opencode.db`，可通过命令行显式覆盖。该说明记录已核实的日志结构，不代表厂商的长期接口承诺。字段变更需要查看实际记录后修改适配器并重新验证。

message.data 中使用 role、time.created、time.completed、finish、modelID、tokens。只把同时具有完成时间和 finish 的助手消息作为已完成调用；缺少用量时保留缺失。 finish为空、完成时间等于创建时间、无错误且后续有正常完成消息的瞬时过渡记录，不计入调用与Token，也不影响结束判断；尾部未完成消息和运行中工具仍按记录不完整处理。part.data 中读取 type=tool、callID、tool、state.status、state.input、state.metadata.exit 和 state.time。

累计输入为 tokens.input + tokens.cache.read + tokens.cache.write；输出为 tokens.output；缓存读取量为 tokens.cache.read。存在 tokens.total 时核对其等于累计输入加输出，part 中的 step-finish 不再次累计。

模型重试从 event 中 type=session.next.retried.1、aggregate_id=会话ID 的记录读取 timestamp、attempt、error.message。模型重试和工具错误分别记录；缺少 event 表时重试数未记录。

记录不完整时可检查同用户目录下 .mobilework/plugin-reporting/model-raw/会话ID 中的辅助文件。单条 completed 原始模型记录不等于完整任务已完成；不能把未能对应到最终回复的局部用量混入完整任务统计。页面已完成但实际拒答时，通过页面观察文件保留用户提供的证据，对缺少完整执行记录的指标保持空值；已经取得完整数值的拒答执行仍参与统计。

专用搜索工具为 `mobilework_search`。成功交付工具为 `result_file`，从 `output_paths` 或 `files` 数组读取路径。路径相对工作目录解析后去重，逐个核验磁盘存在性；检查过程中的截图、脚本、临时文件不自动算作最终交付。

原始题目仅用于定位主任务，实际委派的各层子Agent继承对应独立测试归属，不新增测试次数。通过session.parent_id及task/Agent委派记录的state.metadata.sessionId关联各层子会话；兼容session_id、task_id及输出中的明确会话标识。旧日志只有parent_id时按已记录的父子关系发现子会话；有委派调用却无法定位子日志时记录覆盖问题。系统记忆等后台会话仍排除。 同一子会话被再次调用时，按委派调用界定新的执行窗口，避免将旧历史计入下一次测试；继续执行段仍并入原测试。

模型记录按原始消息或请求标识去重；工具按调用标识及调用时间去重，防止同一执行在父摘要、子日志中重复累计，也避免不同时间复用局部标识被合并。父工具结果中的汇总Token不重复累加。无法唯一归属或标识内容冲突时停止猜测值。

同一批数据默认读取两次并比较。若仍在写入、读取不一致或Token恒等关系变化，脚本停止并返回非零退出码；应查明实际记录后重跑，不能补猜测值。目录时间、session更新时间和数据库费用零值都不替代已核实的字段。
