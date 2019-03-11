import sdk.livescoreapi
import pytest

def test_init_api_key_is_none():
    with pytest.raises(ValueError) as ex:
        sdk.livescoreapi.LivescoresAPI('http://livescore-api.com/api-client/', None, '5555YYYYgggg21aDKKKK2222ssssYYYY', 'en')
    assert 'API Key must be defined!' in str(ex)


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
        sdk.livescoreapi.LivescoresAPI('http://livescore-api.com/api-client/', value, '5555YYYYgggg21aDKKKK2222ssssYYYY', 'en')
    assert 'API Key must be a string' in str(ex)


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
        sdk.livescoreapi.LivescoresAPI('http://livescore-api.com/api-client/', value, '5555YYYYgggg21aDKKKK2222ssssYYYY', 'en')
    assert 'Invalid API Key format!' in str(ex)


def test_init_ok():
    client = sdk.livescoreapi.LivescoresAPI('http://livescore-api.com/api-client/', '5555YYYYgggg21aD', '5555YYYYgggg21aDKKKK2222ssssYYYY', 'ru')
    
    assert client.api_url == 'http://livescore-api.com/api-client/'
    assert client.api_key == '5555YYYYgggg21aD'
    assert client.api_secret == '5555YYYYgggg21aDKKKK2222ssssYYYY'
    assert client.language == 'ru'


@pytest.mark.parametrize("value", [
    "httpww://livescore-api.com/api-client/",
    "http://livescorecom/api-client/",
    "http://livescore-apicom/api-client/",
    "",
])
def test_validate_url(value):
    with pytest.raises(ValueError) as ex:
             sdk.livescoreapi.LivescoresAPI(value, 'this-is-api-key', 'this-is-api-secret', 'en')
    assert 'API URL is not valid' in str(ex)



@pytest.mark.parametrize("value", [
    "bg",
    "es",
    "br",
    "dk",
])
def test_validate_language(value):
    with pytest.raises(ValueError) as ex:
             sdk.livescoreapi.LivescoresAPI('http://livescore-api.com/api-client/', '5555YYYYgggg21aD', '5555YYYYgggg21aDKKKK2222ssssYYYY', value)
    assert 'Language ID is not supported' in str(ex)


#@pytest.fixture
def test_get_all_fixtures_ok():
    client1 = sdk.livescoreapi.LivescoresAPI.get_all_fixtures('1', '2019-03-08', '1')
    assert client1.league_id == '1'
    assert client1.date == '2019-03-08'
    assert client1.page == '1'



@pytest.mark.parametrize("value", [
    "2019-3-8",
    "03-08-2019",
    "08-03-2019",
    "2019-08-03",
    "",
])
def test_get_all_fixtures_validate_date(value):
    with pytest.raises(ValueError) as ex:
             sdk.livescoreapi.LivescoresAPI.get_all_fixtures('league_id', value, 'page')
    assert 'Invalid date format' in str(ex)