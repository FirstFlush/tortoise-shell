#!/bin/env python3

import IPython
from traitlets.config import Config
from tortoise import Tortoise, run_async
import atexit
# atexit.register()

import asyncio
import sys

def main():
    c = Config()
    c.InteractiveShellApp.exec_lines = [
        'print()',
        # 'import atexit',
        # 'import asyncio',
        # 'from tortoise import Tortoise, run_async',
        'from tortoise_shell.config import TortoiseShellConfig',
        'ipython = get_ipython()',
        'ts_config = await TortoiseShellConfig.init(ipython.user_ns)',
        # 'atexit.register(lambda: asyncio.run(ts_config.close_db()))',
    ]


    IPython.start_ipython(argv=[], config=c)


def custom_exit():
    # Perform immediate cleanup before exiting
    asyncio.run(shutdown_tortoise())
    sys.exit(0)  # Force exit to avoid delays


async def shutdown_tortoise():
    print("Closing Tortoise ORM connections...")
    await Tortoise.close_connections()


if __name__ == '__main__':
    main()