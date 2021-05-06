import os
from collections import OrderedDict
from collections.abc import Iterable
from functools import wraps

KEYS_NOT_DEFINED = 'keys-not-defined'


class ConfigError(Exception):
    ...


def key_builder(use):
    if not isinstance(use, Iterable):
        raise ValueError('"use" should be iterable')

    def decorate(func):
        @wraps(func)
        def wrapped(keys):
            args = []
            for key in use:
                try:
                    args.append(keys[key])
                except KeyError:
                    raise ConfigError(f'"{key}" not found in config') from None
            return func(*args)
        return wrapped
    return decorate


@key_builder(use=(
    'POSTGRES_USER',
    'POSTGRES_DB',
    'POSTGRES_PORT',
    'POSTGRES_PASSWORD',
))
def sqlalchemy_database_url(user, db_name, port, password):
    return f'postgresql://{user}:{password}@db:{port}/{db_name}'


class Configer:
    required_keys = (
        'POSTGRES_USER',
        'POSTGRES_DB',
        'POSTGRES_PORT',
        'POSTGRES_PASSWORD',
    )

    built_keys = OrderedDict({
        'SQLALCHEMY_DATABASE_URL': sqlalchemy_database_url,
    })

    def __init__(self):
        self.keys = KEYS_NOT_DEFINED

    def load(self):
        self.keys = os.environ.copy()
        self._check_config()
        self._build_keys()

    def _check_config(self):
        for key in self.required_keys:
            if key not in self.keys:
                raise ConfigError(f'Missing "{key}". Please check config')

    def _build_keys(self):
        for key, func in self.built_keys.items():
            self.keys[key] = func(self.keys)

    def get(self, key, default=None):
        if self.keys == KEYS_NOT_DEFINED:
            self.load()
        try:
            return self.keys[key]
        except KeyError:
            if default:
                return default
            raise ConfigError(f'"{key}" not found in config') from None


configer = Configer()

__all__ = ['configer']
