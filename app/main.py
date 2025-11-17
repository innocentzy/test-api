from fastapi import FastAPI, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy import and_
from sqlalchemy.orm import Session
from . import models, schemas, database

app = FastAPI()  

# Вопросы
@app.get("/questions", response_model=list[schemas.QuestionRead])
def get_questions(db: Session = Depends(database.get_db)):
    return db.query(models.Question).all()

@app.post("/questions", response_model=schemas.QuestionRead)
def post_questions(question: schemas.QuestionCreate, db: Session = Depends(database.get_db)):
    question_from_db = db.query(models.Question).filter(models.Question.text == question.text).first()

    if question_from_db:
        raise HTTPException(status_code=400, detail="Question already exists")
    else:
        question_from_db = models.Question(text=question.text)
        db.add(question_from_db)
        db.commit()
        db.refresh(question_from_db)
        return question_from_db

@app.get("/questions/{id}", response_model=schemas.QuestionRead)
def get_question_by_id(id: int, db: Session = Depends(database.get_db)):
    question_from_db = db.query(models.Question).filter(models.Question.id == id).first()

    if question_from_db is None:
        raise HTTPException(status_code=404, detail="Question not found")
    else:
        return question_from_db

@app.delete("/questions/{id}", response_model=schemas.QuestionDelete)
def delete_question_by_id(id: int, db: Session = Depends(database.get_db)):
    question_from_db = db.query(models.Question).filter(models.Question.id == id).first()

    if question_from_db is None:                                                              # Если day не найден
        raise HTTPException(status_code=404, detail="Question not found")
    else:
        db.delete(question_from_db)

    db.commit()
    return question_from_db

# Ответы
@app.post("/questions/{id}/answers", response_model=schemas.AnswerRead)
def post_answer(id: str, answer: schemas.AnswerCreate, db: Session = Depends(database.get_db)):
    answer_from_db = db.query(models.Answer).filter(and_(models.Answer.question_id == id, models.Answer.text == answer.text)).first()
    
    if answer_from_db:
        raise HTTPException(status_code=400, detail="This answer already exists")
    else:
        answer_from_db = models.Answer(question_id=id, user_id=answer.user_id, text=answer.text)
        db.add(answer_from_db)
        db.commit()
        db.refresh(answer_from_db)
        return answer_from_db

@app.get("/answers/{id}", response_model=schemas.AnswerRead)
def get_answer_by_id(id: int, db: Session = Depends(database.get_db)):
    answer_from_db = db.query(models.Answer).filter(models.Answer.id == id).first()

    if answer_from_db is None:
        raise HTTPException(status_code=404, detail="This answer does not exist")
    else:
        return answer_from_db

@app.delete("/answers/{id}")
def delete_answer_by_id(id: int):
    pass