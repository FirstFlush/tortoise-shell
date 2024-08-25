import importlib
import toml
from tortoise import Tortoise, Model
import os
from pathlib import Path


class TortoiseShellConfig:

    def __init__(self):

        self.DIR = Path(__file__).parent
        self.TOML_FILE = 'config.toml'
        self._toml_configs()
        self.TEST_DB_URL = self.DB_URL#f"sqlite://{self.DIR.parent / 'tests' / 'db.sqlite3'}"
        # self.DB_URL = f"sqlite://{self.DIR.parent / 'tests' / 'db.sqlite3'}"


    def _toml_configs(self):

        with open(os.path.join(self.DIR, self.TOML_FILE), 'r') as toml_file:
            data = toml.load(toml_file)
        self.DB_URL = data['db']['DB_URL']
        self.all_models = data['models']['all_models']

    @classmethod
    async def init(cls, namespace) -> "TortoiseShellConfig":
        tortoise_shell_config = cls()
        await tortoise_shell_config.init_db(namespace)
        return tortoise_shell_config

    async def init_db(self, namespace):
        await Tortoise.init(db_url=self.DB_URL, modules={'models': self.all_models})
        await Tortoise.generate_schemas()
        self.import_tortoise_models(self.all_models, namespace)

    async def close_db(self):
        Tortoise.close_connections()
        print('Closing Tortoise connections..')
    

    def import_tortoise_models(self, model_modules, namespace):
        for module_path in model_modules:
            module = importlib.import_module(module_path)
            s = f"from {module_path} import "
            tables = []
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if isinstance(attr, type) and issubclass(attr, Model) and attr != Model:
                    namespace[attr_name] = attr
                    tables.append(f"\033[1m\033[34m{attr_name}\033[0m")
            print(f"{s}{', '.join(tables)}")




