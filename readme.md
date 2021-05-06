# Description

A simple python module to handle your project settings. Currently this module will get all values from env code are runned in.

# Installation

    pip install pyconfiger

# Usage example

`foo.py`

    from pyconfiger import configer

    print(configer.get('ENV_NAME', 'default_value'))

# Notice

Please note that this code implements lazy loading. So env will be loaded only on first access.

# Advanced usage

## Required keys

This lib implements required check (no advanced validation). To add value to required see code below:

    from pyconfiger import configer
    from itertools import chain

    configer.required_keys = chain(configer.required_keys, ('ENV_VALUE_THAT_MUST_BE_DEFINED',))
    print(configer.get('ENV_VALUE_THAT_MUST_BE_DEFINED'))

Please notice that required check done only once on loading. So if value added to `required_keys` after first `get()` call. It wont affect.

## Building keys

Another feature is building value:

    from pyconfiger import configer
    from pyconfiger import key_builder

    @key_builder(use=(
        'POSTGRES_USER',
        'POSTGRES_DB',
        'POSTGRES_PORT',
        'POSTGRES_PASSWORD',
    ))
    def sqlalchemy_database_url(user, db_name, port, password):
        return f'postgresql://{user}:{password}@db:{port}/{db_name}'

    configer.built_keys['YOUR_KEY_NAME'] = sqlalchemy_database_url
    print(configer.get('YOUR_KEY_NAME'))

Explanation: `key_builder` decorator will accept names of env variables to load, and pass them as arguments to function, in order they provided in `use` tuple.

Please notice key building as well as requirement check done on loading stage. So if some values added to `built_keys` after first `get()` call it wont affect.

Also building keys wont add them to required so in case of missing value `ConfigError` will be raised.

# Future

    This lib created for self use. If you found some cool way to extend this please create issue or PR it would be very appreciated.
