from fastapi import FastAPI

from app.api.router import watcher
from fastapi.exceptions import RequestValidationError
from app.exceptions import input_validation_error_handler

app = FastAPI()

app.include_router(watcher)
app.add_exception_handler(RequestValidationError, input_validation_error_handler)
