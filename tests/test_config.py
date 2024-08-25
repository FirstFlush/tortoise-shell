from tortoise_shell.config import TortoiseShellConfig
from tortoise import Tortoise, run_async


config = TortoiseShellConfig()
TORTOISE_ORM = {
    "connections": {"default": config.TEST_DB_URL},
    "apps": {
        "models": {
            "models": ["aerich.models"] + config.all_models,
            "default_connection": "default",
        },
    },
}



# async def init():
#     await Tortoise.init(db_url=config.TEST_DB_URL, modules={'models': config.all_models})
#     await Tortoise.generate_schemas()
    


# run_async(init())

# TORTOISE_ORM = {
#     "connections": {"default": "sqlite:///home/baga/tortoise-shell/tests/db.sqlite3"},
#     "apps": {
#         "models": {
#             "models": ["aerich.models",],
#             "default_connection": "default",
#         },
#     },
# }

