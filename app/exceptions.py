from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError


ERROR_MESSAGES = {
    "int_parsing": "{parameter_name} должен быть числом",
    "greater_than_equal": "{parameter_name} должен быть больше нуля",
    "unknown": "Неизвестная ошибка",
}


def input_validation_error_handler(request: Request, exc: RequestValidationError):
    errors = list()
    for error in exc.errors():
        if custom_message := ERROR_MESSAGES.get(error["type"]):
            error = custom_message.format(parameter_name=error["loc"][1])
        errors.append(error)
    return JSONResponse(
        status_code=status.HTTP_403_FORBIDDEN, content={"status": errors}
    )
