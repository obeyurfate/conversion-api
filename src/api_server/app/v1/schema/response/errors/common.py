from typing import Literal

from .base import ErrorResponse, ErrorResult
from pydantic import StrictStr, StrictInt


class InternalUnhandledErrorResponse(ErrorResponse):
    class InternalUnhandledError(ErrorResult):
        code: StrictInt = 500
        message: StrictStr = "Got internal error. Investigation is recommended."

    error: InternalUnhandledError = InternalUnhandledError()


class InvalidFileFormatResponse(ErrorResponse):
    class InvalidFileFormatError(ErrorResult):
        code: StrictInt = 400
        message: StrictStr = "Invalid file format."

    error: InvalidFileFormatError = InvalidFileFormatError()