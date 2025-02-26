from conversion_worker import usecases
import api_server
from utils import environment as env


def main():
    app = api_server.create_app(
        csv_conversion_usecase=usecases.CSVConversionUsecase(),
        tsv_conversion_usecase=usecases.TSVConversionUsecase(),
    )

    try:
        api_server.start_api_server(app, host="0.0.0.0", port=env.SERVE_PORT)
    except Exception:
        msg_crit = "Critical error during service's work."
        print(msg_crit)
        return 1


if __name__ == "__main__":
    main()
