from dataclasses import dataclass
import requests

from schema import YandexUserData
from settings import Settings


@dataclass
class YandexClient:
    settings: Settings

    def get_user_info(self, code: str):
        access_token = self._get_user_access_token(code=code)
        user_info = requests.get('https://login.yandex.ru/info?format=json',
                                 headers={'Authorization': f'OAuth {access_token}'})
        return YandexUserData(**user_info.json(), access_token=access_token)

    def _get_user_access_token(self, code: str) -> str:
        data = {
            'code': code,
            'client_id': self.settings.YANDEX_CLIENT_ID,
            'client_secret': self.settings.YANDEX_SECRET_KEY,
            'redirect_uri': self.settings.YANDEX_REDIRECT_URI,
            'grant_type': "authorization_code",
        }
        response = requests.post(
            self.settings.YANDEX_TOKEN_URL,
            data=data,
            headers={
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        )
        return response.json()['access_token']
