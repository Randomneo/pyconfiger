import pytest


def test_configer(monkeypatch):
    from pyconfiger import ConfigError
    from pyconfiger import configer

    monkeypatch.setenv('TEST_ENV', 'TEST_ENV_VALUE')
    assert configer.get('TEST_ENV') == 'TEST_ENV_VALUE'
    with pytest.raises(ConfigError):
        configer.get('TEST_ENV_NOT_EXIST')


def test_configer_context():
    from pyconfiger import configer
    assert configer.get('TEST_ENV') == 'TEST_ENV_VALUE'
