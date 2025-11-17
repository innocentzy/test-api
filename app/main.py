from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas, database

app = FastAPI()  

# Вопросы
@app.get("/questions", response_model=list[schemas.QuestionRead])
def get_questions(db: Session = Depends(database.get_db)):
    return db.query(models.Question).all()

@app.post("/questions", response_model=schemas.QuestionRead | None)
def post_questions(question: schemas.QuestionCreate, db: Session = Depends(database.get_db)):
    question_from_db = db.query(models.Question).filter(models.Question.text == question.text).first()

    if question_from_db:
        return None
    else:
        question_from_db = models.Question(text=question.text)
        db.add(question_from_db)
        db.commit()
        db.refresh(question_from_db)
        return question_from_db

@app.get("/questions/{id}", response_model=schemas.QuestionRead)
def get_question_by_id(id: int, db: Session = Depends(database.get_db)):
    return db.query(models.Question).filter(models.Question.id == id).first()

@app.delete("/questions/{id}")
def delete_question_by_id(id: int):
    pass

# Ответы
@app.post("/questions/{id}/answers")
def post_answer(id: int):
    pass

@app.get("/answers/{id}")
def get_answer_by_id(id: int):
    pass

@app.delete("/answers/{id}")
def delete_answer_by_id(id: int):
    pass