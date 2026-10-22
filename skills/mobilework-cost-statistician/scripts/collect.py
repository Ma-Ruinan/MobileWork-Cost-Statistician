"""SQLite adapter. Product constants are specialized when this skill is packaged."""
from pathlib import Path
from common import DataError

PRODUCT = 'MobileWork'
SEARCH_TOOL = 'mobilework_search'
DELIVERY_TOOL = 'result_file'
METHOD = '只读opencode.db的session、message、part；主任务及递归委派子Agent读取Token，callID跨执行主体去重工具；event单列模型重试；result_file登记路径核验存在性'


def default_source(args):
    if args.logs_root:
        raise DataError('本对象使用SQLite，请使用--db指定源')
    if args.db:
        return Path(args.db).resolve()
    return Path.home()/'.mobilework'/'xdg'/'data'/'opencode'/'opencode.db'


def collect(source, tasks, args, mapping, tz):
    from sqlite_reader import collect_sqlite
    return collect_sqlite(source, tasks, args, mapping, tz, PRODUCT, SEARCH_TOOL, DELIVERY_TOOL)


if __name__ == '__main__':
    from common import run_cli
    raise SystemExit(run_cli(PRODUCT, collect, default_source, METHOD))
