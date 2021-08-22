# Python modules.
import multiprocessing

# FastAPI modules.
from fastapi import FastAPI

# Uvicorn modules.
import uvicorn


application = FastAPI()


@application.get("/")
async def root():
    return {
        "message": "Hello World"
    }

if __name__ == "__main__":
    multiprocessing.freeze_support()
    uvicorn.run(
        "manage:application",
        host="0.0.0.0",
        port=8000,
        reload=False,
        log_level="debug"
    )
