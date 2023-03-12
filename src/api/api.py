#!/usr/bin/env python

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

app = FastAPI(title="Boilerplate API")

# allow any origin
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root() -> RedirectResponse:
    """Entrypoint that redirects to documentation.

    Returns
    -------
        RedirectResponse: Redirect to API documentation.
    """
    return RedirectResponse("/docs")


@app.get("/hello")
async def hello() -> str:
    """Show a simple hello world message.

    Returns
    -------
        str: String response.
    """
    return "Hello World!"
