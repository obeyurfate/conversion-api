from pydantic import BaseModel, StrictInt, StrictStr


class ErrorResult(BaseModel):
    message: StrictStr
    code: StrictInt


class ErrorResponse(BaseModel):
    error: ErrorResult
