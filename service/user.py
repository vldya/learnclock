import string
from dataclasses import dataclass
from random import choice

from schema import UserLoginSchema
from repository import UserRepository


@dataclass
class UserService:
    user_repository: UserRepository

    def create_user(self, username: str, password: str) -> UserLoginSchema:
        token = self._generate_access_token(self)
        user = self.user_repository.create_user(username, password, token)
        return UserLoginSchema(user_id=user.id, access_token=user.access_token)

    @staticmethod
    def _generate_access_token(self) -> str:
        return ''.join(choice(string.ascii_uppercase + string.digits) for _ in range(10))



