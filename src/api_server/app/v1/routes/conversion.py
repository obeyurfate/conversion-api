import json

from fastapi import APIRouter, status, UploadFile, File, Response
from conversion_worker import conversion_errors
from api_server.app.v1 import schema
from ... import dependancy


conversion_router = APIRouter(
    prefix="/api/v1/conversion",
    tags=["CONVERSION"],
)


@conversion_router.post(
    "/convert/tsv",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {
            "model": dict
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": schema.response.InvalidFileFormatResponse
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "model": schema.response.InternalUnhandledErrorResponse
        }
    },
    description="Upload a TSV file for conversion.",
)
async def upload_tsv_file(  # noqa: ANN201
    response: Response, file: UploadFile = File(...),
):
    try:
        converted_text = await dependancy.tsv_conversion_usecase.execute(file.file.read())
    except conversion_errors.InvalidFileFormatError:
        response.status_code = schema.response.InvalidFileFormatResponse().error.code
        return schema.response.InvalidFileFormatResponse()
    except Exception as exc:
        print(exc)
        response.status_code = schema.response.InternalUnhandledErrorResponse().error.code
        return schema.response.InternalUnhandledErrorResponse()
    return json.loads(converted_text)


@conversion_router.post(
    "/convert/csv",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {
            "model": dict
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": schema.response.InvalidFileFormatResponse
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "model": schema.response.InternalUnhandledErrorResponse
        }
    },
    description="Upload a CSV file for conversion.",
)
async def upload_csv_file(  # noqa: ANN201
    response: Response, file: UploadFile = File(...),
):
    try:
        converted_text = await dependancy.csv_conversion_usecase.execute(file.file.read())
    except conversion_errors.InvalidFileFormatError:
        response.status_code = schema.response.InvalidFileFormatResponse().error.code
        return schema.response.InvalidFileFormatResponse()
    except Exception as exc:
        print(exc)
        response.status_code = schema.response.InternalUnhandledErrorResponse().error.code
        return schema.response.InternalUnhandledErrorResponse()
    return json.loads(converted_text)
