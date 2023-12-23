from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError


ERROR_MESSAGES = {
    "int_parsing": "{parameter_name} должен быть числом. Неверный ввод: {parameter_value}",
    "greater_than_equal": "{parameter_name} должен быть больше нуля. Неверный ввод: {parameter_value}",
    "url_type": "{parameter_name} должен содержать HTTP или HTTPS ссылки. Неверный ввод: {parameter_value}"
}


def input_validation_error_handler(_: Request, exc: RequestValidationError):
    errors = list()
    for error in exc.errors():
        if custom_message := ERROR_MESSAGES.get(error["type"]):
            error = custom_message.format(parameter_name=error["loc"][1], 
                                          parameter_value=error['input'])
        errors.append(error)
    return JSONResponse(
        status_code=status.HTTP_403_FORBIDDEN, content={"status": errors}
    )
