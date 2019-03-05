import sdk.livescoreapi
import pytest


def test_init_api_key_is_none():
    with pytest.raises(ValueError) as ex:
        sdk.livescoreapi.Livescores('http://example.com', None, 'this-is-api-secret', 'en')
    assert 'Api key cannot be None' in str(ex)


@pytest.mark.parametrize("value", [
    8,
    True,
    False,
    {},
    [],
    8.90,
])
def test_init_api_key_is_not_string(value):
    with pytest.raises(ValueError) as ex:
        sdk.livescoreapi.Livescores('http://example.com', value, 'this-is-api-secret', 'en')
    assert 'Api key must be a string' in str(ex)


@pytest.mark.parametrize("value", [
    "1",
    "1234567890",
    "123456789012345",
    "12345678901234567",
    "12345_-7890123*5(",
    "",
])
def test_init_api_key_is_not_16_characters(value):
    with pytest.raises(ValueError) as ex:
        sdk.livescoreapi.Livescores('http://example.com', value, 'this-is-api-secret', 'en')
    assert 'Api key has invalid format' in str(ex)


def test_init_ok():
    client = sdk.livescoreapi.Livescores('http://example.com', '0123456789123456', '01234567891234560123456789123456', 'en')
    assert client.api_key == '0123456789123456'
