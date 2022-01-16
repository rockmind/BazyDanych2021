from web_service import web_app
from uvicorn import run as uvicorn_run


if __name__ == "__main__":
    uvicorn_run(web_app, host='0.0.0.0', port=8000, log_level='info')
