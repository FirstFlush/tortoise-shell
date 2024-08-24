#!/bin/env python3

import IPython
from traitlets.config import Config


c = Config()
c.InteractiveShellApp.exec_lines = [
    'print()',
    'from tortoise_shell_config import TortoiseShellConfig',
    'ipython = get_ipython()',
    'await TortoiseShellConfig.init(ipython.user_ns)'
]

IPython.start_ipython(argv=[], config=c)