import uvicorn
from fastapi import FastAPI
from routes import slots, suggest, book, calendar
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(slots.router)
app.include_router(suggest.router)
app.include_router(book.router)
app.include_router(calendar.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)