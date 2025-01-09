from typing import Optional

from pydantic import BaseModel, model_validator


class TaskSchema(BaseModel):
    id: Optional[int]
    name: Optional[str]
    pomodoro_count: Optional[int]
    category_id: int

    class Config:
        from_attributes = True

    @model_validator(mode='after')
    def check_name_or_pomodoro_count_is_not_none(self):
        if self.name is None or self.pomodoro_count is None:
            raise ValueError('name or pomodoro_count must be provided')
        return self
