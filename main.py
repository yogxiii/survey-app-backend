from fastapi import FastAPI
from tags.user.route import user_router
from tags.surveys.route import survey_route
from tags.questions.route import question_route
from tags.answers.route import answer_route
from tags.create_thumbnail.route import image_route

app = FastAPI()

# root routes
@app.get("/")
async def health():
    return {"message":"green"}

# including routers
app.include_router(user_router)
app.include_router(survey_route)
app.include_router(question_route)
app.include_router(answer_route)
app.include_router(image_route)