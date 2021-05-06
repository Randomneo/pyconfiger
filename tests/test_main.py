import pytest


def test_configer(monkeypatch):
    from pyconfiger import Configer
    from pyconfiger import ConfigError
    configer = Configer()

    monkeypatch.setenv('TEST_ENV', 'TEST_ENV_VALUE')
    assert configer.get('TEST_ENV') == 'TEST_ENV_VALUE'
    with pytest.raises(ConfigError):
        configer.get('TEST_ENV_NOT_EXIST')
    assert configer.get('TEST_ENV_NOT_EXIST', 'default_value') == 'default_value'


def test_keybuilder(monkeypatch):
    from pyconfiger import Configer
    from pyconfiger import key_builder
    configer = Configer()

    @key_builder(use=(
        'KEY1',
        'KEY2',
    ))
    def built_key(key1, key2):
        return f'{key1}+{key2}'

    monkeypatch.setenv('KEY1', 'VALUE1')
    monkeypatch.setenv('KEY2', 'VALUE2')

    configer.built_keys['BUILT_KEY'] = built_key
    assert configer.get('BUILT_KEY') == 'VALUE1+VALUE2'


def test_broken_keybuilder():
    from pyconfiger import Configer
    from pyconfiger import ConfigError
    from pyconfiger import key_builder

    # empty key in use
    configer = Configer()
    @key_builder(use=(
        'KEY1',
        'KEY2',
    ))
    def built_key(key1, key2):
        return f'{key1}+{key2}'
    configer.built_keys['BUILT_KEY'] = built_key
    with pytest.raises(ConfigError):
        configer.get('HOME')

    #borken use
    configer = Configer()
    with pytest.raises(ValueError):
        @key_builder(use=1)
        def built_key(key1):
            return f'{key1}'


def test_required():
    from pyconfiger import Configer
    from pyconfiger import ConfigError
    configer = Configer()

    configer.required_keys = ('KEY',)
    with pytest.raises(ConfigError):
        configer.get('KEY')
