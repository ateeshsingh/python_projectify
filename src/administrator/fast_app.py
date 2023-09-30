import logging
from fastapi import FastAPI, Header, Depends, HTTPException
from .api_logs import RouterLoggingMiddleware
from ..administrator.api_routes import ApiRoutes
from starlette.middleware.cors import CORSMiddleware


def verify_auth(header=Header("At")):
    if header != "At":
        raise HTTPException(status_code=401, detail={"response": "UnAuthorized"})


def create_app():
    app = FastAPI(
        title="Project Gallery",
        description="Documentation for Project Gallery package Api's ",
        dependencies=[Depends(verify_auth)],
        contact={
            "name": "Ateesh Chauhan",
            "email": "ateeshchauhan4023@gmail.com"
        }

    )
    ApiRoutes(app)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    # app.add_middleware(BeforeRequest)
    app.add_middleware(RouterLoggingMiddleware, logger=logging.getLogger(__name__))
    return app






