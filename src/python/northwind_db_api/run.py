from uvicorn import run as uvicorn_run
from northwind_db_api.web_service import web_app


if __name__ == "__main__":
    uvicorn_run(web_app, host='0.0.0.0', port=8888)
