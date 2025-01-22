import pytest
import datetime as dt
from app.schema import UserLoginSchema
from app.service.auth import AuthService
from app.settings import Settings
from jose import jwt

pytestmark = pytest.mark.asyncio


async def test_get_google_redirect_url__success(auth_service: AuthService, settings: Settings):
    settings_google_redirect_url = settings.google_redirect_url

    auth_service_google_redirect_url = await auth_service.get_google_redirect_url()

    assert auth_service_google_redirect_url == settings_google_redirect_url


async def test_get_yandex_redirect_url__success(auth_service: AuthService, settings: Settings):
    settings_yandex_redirect_url = settings.yandex_redirect_url
    auth_service_yandex_redirect_url = await auth_service.get_yandex_redirect_url()
    assert settings_yandex_redirect_url == auth_service_yandex_redirect_url


async def test_generate_access_token__success(auth_service: AuthService, settings: Settings):
    user_id = '1'

    access_token = auth_service.generate_access_token(user_id=user_id)
    decoded_access_token = jwt.decode(access_token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ENCODE_ALG])
    decoded_user_id = decoded_access_token.get('user_id')
    decoded_token_expire = dt.datetime.fromtimestamp(decoded_access_token.get('expire'), tz=dt.timezone.utc)

    assert user_id == decoded_user_id
    assert (decoded_token_expire - dt.datetime.now(tz=dt.timezone.utc)) > dt.timedelta(days=6)


async def test_get_user_id_from_access_token__success(auth_service: AuthService):
    user_id = '1'

    access_token = auth_service.generate_access_token(user_id=user_id)
    decoded_user_id = await auth_service.get_user_id_from_access_token(access_token)

    assert decoded_user_id == user_id


async def test_google_auth__success(auth_service: AuthService):
    code = 'fake_code'

    user = await auth_service.google_auth(code=code)
    decoded_user_id = await auth_service.get_user_id_from_access_token(user.access_token)

    assert decoded_user_id == user.user_id
    assert isinstance(user, UserLoginSchema)


async def test_yandex_auth__success(auth_service: AuthService):
    code = 'fake_code'

    user = await auth_service.yandex_auth(code=code)
    decoded_user_id = await auth_service.get_user_id_from_access_token(user.access_token)

    assert decoded_user_id == user.user_id
    assert isinstance(user, UserLoginSchema)