import uvicorn
from starlette.applications import Starlette


def start_api_server(application: Starlette, host: str, port: int) -> None:
    server_config = uvicorn.Config(application, host=host, port=port)
    server = uvicorn.Server(server_config)
    server.run()
