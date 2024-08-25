from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSON NOT NULL
);
CREATE TABLE IF NOT EXISTS "address" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "street_address" VARCHAR(255) NOT NULL,
    "city" VARCHAR(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS "user" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "full_name" VARCHAR(255),
    "email" VARCHAR(255) NOT NULL,
    "is_active" INT NOT NULL  DEFAULT 1
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
