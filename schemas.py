from pydantic import BaseModel
from datetime import datetime

# Вопросы
class QuestionBase(BaseModel):
    text: str
    created_at: datetime

class QuestionCreate(QuestionBase):
    pass

class QuestionRead(QuestionBase):
    id: int

    class Config:
        from_attributes = True

class QuestionDelete(QuestionBase):
    pass

# Ответы
class AnswerBase(BaseModel):
    text: str
    created_at: datetime

class AnswerCreate(AnswerBase):
    question_id: int
    user_id: str

class AnswerRead(AnswerBase):
    id: int

    class Config:
        from_attributes = True

class AnswerDelete(AnswerBase):
    pass