from fastapi import FastAPI

app = FastAPI()  

# Вопросы
@app.get("/questions")
def get_questions():
    pass

@app.post("/questions")
def post_questions():
    pass

@app.get("/questions/{id}")
def get_question_by_id(id: int):
    pass

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