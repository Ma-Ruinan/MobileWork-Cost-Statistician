# MobileWork��־��Դ���ֶ�

Ĭ����ԴΪ `%USERPROFILE%\.mobilework\xdg\data\opencode\opencode.db`����ͨ����������ʽ���ǡ���˵����¼�Ѻ�ʵ����־�ṹ�����������̵ĳ��ڽӿڳ�ŵ���ֶα����Ҫ�鿴ʵ�ʼ�¼���޸���������������֤��

message.data ��ʹ�� role��time.created��time.completed��finish��modelID��tokens��ֻ��ͬʱ�������ʱ��� finish ��������Ϣ��Ϊ����ɵ��ã�ȱ������ʱ����ȱʧ��part.data �ж�ȡ type=tool��callID��tool��state.status��state.input��state.metadata.exit �� state.time��

�ۼ�����Ϊ tokens.input + tokens.cache.read + tokens.cache.write�����Ϊ tokens.output�������ȡ��Ϊ tokens.cache.read������ tokens.total ʱ�˶�������ۼ�����������part �е� step-finish ���ٴ��ۼơ�

ģ�����Դ� event �� type=session.next.retried.1��aggregate_id=�ỰID �ļ�¼��ȡ timestamp��attempt��error.message��ģ�����Ժ͹��ߴ���ֱ��¼��ȱ�� event ��ʱ������δ��¼��

��¼������ʱ�ɼ��ͬ�û�Ŀ¼�� .mobilework/plugin-reporting/model-raw/�ỰID �еĸ����ļ������� completed ԭʼģ�ͼ�¼������������������ɣ����ܰ�δ�ܶ�Ӧ�����ջظ��ľֲ�����������������ͳ�ơ�ҳ������ɵ�ʵ�ʾܴ�ʱ��ͨ��ҳ��۲��ļ������û��ṩ��֤�ݣ���ȱ������ִ�м�¼��ָ�걣�ֿ�ֵ���Ѿ�ȡ��������ֵ�ľܴ�ִ���Բ���ͳ�ơ�

ר����������Ϊ `mobilework_search`���ɹ���������Ϊ `result_file`���� `output_paths` �� `files` �����ȡ·����·����Թ���Ŀ¼������ȥ�أ����������̴����ԣ��������еĽ�ͼ���ű�����ʱ�ļ����Զ��������ս�����

Ĭ�Ͻ�ͳ������Ŀ��ȷƥ������Ự�������ӻỰ����̨�Ự��δƥ���û���Ϣ��JSON�е����ų�ԭ�򡣷�����������ص��ӻỰʱӦ�ڱ����м�¼��Χ���������Ựͳ�Ʋ����Զ����������������������ı����Ự���û���Ϣ��ʶ��ͬ���ڹ��������ܽ�����Ŀ¼���ƻ����ʱ����ԡ�

ͬһ������Ĭ�϶�ȡ���β��Ƚϡ�������д�롢��ȡ��һ�»�Token��ȹ�ϵ�仯���ű�ֹͣ�����ط����˳��룻Ӧ����ʵ�ʼ�¼�����ܣ����ܲ��²�ֵ��Ŀ¼ʱ�䡢session����ʱ������ݿ������ֵ��������Ѻ�ʵ���ֶΡ�
