# Tortoise Shell

![Development Status](https://img.shields.io/badge/status-in_development-orange)

**Note:** This package is currently in development. Expect frequent updates and potential breaking changes.

Tortoise Shell is inspired by the awesome Django-Extensions package, particularly the `shell_plus` feature. This tool is like `shell_plus` for Tortoise ORM, designed to simplify your workflow by automatically loading your models and database connection into an interactive IPython shell.

## Features

- **Automatic Model Import**: Just like Django-Extension's `shell_plus`, Tortoise Shell automatically imports all your Tortoise ORM models into the IPython shell.
- **Easy Configuration**: Set your models and database connection string in a simple TOML file, and you're ready to go.

## Installation

1. Install Tortoise Shell:

    ```bash
    pip install tortoise-shell
    ```

2. Ensure you have Tortoise-ORM and IPython installed:

    ```bash
    pip install tortoise-orm ipython
    ```

## Setup

1. **Create a Configuration File**:

    Create a `tortoise_shell.toml` file in your project directory with the following content:

    ```toml
    [db]
    DB_URL = "your_app.config.POSTGRES_DB"  # Enter the module path to your DB connection string

    [models]
    all_models = "your_app.config.all_models"  # Enter the module path to your all_models list
    ```

    - `DB_URL`: The path to your database connection string.
    - `all_models`: The path to your list of model modules.

2. **Your Project's Configuration**:

    In your project’s `config.py` or `settings.py`, define your Tortoise ORM setup:

    ```python
    # config.py or settings.py

    POSTGRES_DB = "postgres://user:password@localhost:5432/mydatabase"

    all_models = [
        "app1.models",
        "app2.models",
    ]

    TORTOISE_ORM = {
        'connections': {
            'default': POSTGRES_DB
        },
        'apps': {
            'models': {
                'models': all_models,
                'default_connection': 'default',
            },
        },
    }
    ```

3. **Run Tortoise Shell**:

    Use the provided IPython launcher script to start the shell with your models preloaded:

    ```bash
    ./tortoise_shell.py
    ```

    The script will automatically import your models and establish a connection to your database, allowing you to interact with your Tortoise ORM models effortlessly.

## Usage

Once you've set up config.toml, simply run the shell script to start interacting with your models in IPython:

```bash
tortoise-shell
```