from pydantic import BaseModel
from datetime import datetime

# Вопросы
class QuestionBase(BaseModel):
    text: str

class QuestionCreate(QuestionBase):
    pass

class QuestionRead(QuestionBase):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True

class QuestionDelete(QuestionBase):
    pass

# Ответы
class AnswerBase(BaseModel):
    text: str

class AnswerCreate(AnswerBase):
    user_id: str

class AnswerRead(AnswerBase):
    id: int
    created_at: datetime
    question_id: int
    user_id: str

    class Config:
        from_attributes = True

class AnswerDelete(AnswerBase):
    pass