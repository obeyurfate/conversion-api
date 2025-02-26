from conversion_worker import usecases
from fastapi import FastAPI
from .v1 import routes
from . import dependancy


def create_app(
    csv_conversion_usecase: usecases.CSVConversionUsecase,
    tsv_conversion_usecase: usecases.TSVConversionUsecase,
) -> FastAPI:
    dependancy.csv_conversion_usecase = csv_conversion_usecase
    dependancy.tsv_conversion_usecase = tsv_conversion_usecase

    app = FastAPI(
        swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"},
    )

    app.include_router(routes.conversion_router)

    return app
