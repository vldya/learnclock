from dataclasses import dataclass

from database import UserProfile
from exception import UserNotFoundException, UserNotCorrectPasswordException
from repository import UserRepository
from schema import UserLoginSchema


@dataclass
class AuthService:
    user_repository: UserRepository

    def login(self, username: str, password: str) -> UserLoginSchema:
        user = self.user_repository.get_user_by_username(username)
        self._validate_auth_user(self, user, password)
        return UserLoginSchema(user_id=user.id, access_token=user.access_token)

    @staticmethod
    def _validate_auth_user(self, user: UserProfile, password: str):
        if not user:
            raise UserNotFoundException
        if user.password != password:
            raise UserNotCorrectPasswordException



