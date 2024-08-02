#!/usr/bin/env python

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from .boilerplate import Boilerplate

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

    Returns:
        RedirectResponse: Redirect to API documentation.

    """
    return RedirectResponse("/docs")


@app.get("/hello")
async def hello() -> str:
    """Show a simple hello world message.

    Returns:
        str: String response.
    """
    return "Hello World!"


@app.get("/add/{x}/{y}")
async def add(x: int, y: int) -> int:
    """Add two numbers together.

    Args:
        x (int): The first number.
        y (int): The second number.

    Returns:
        int: The sum of the two numbers.
    """
    return Boilerplate(x, y).add()


@app.get("/subtract/{x}/{y}")
async def subtract(x: int, y: int) -> int:
    """Subtract two numbers.

    Args:
        x (int): The first number.
        y (int): The second number.

    Returns:
        int: The difference of the two numbers.
    """
    return Boilerplate(x, y).subtract()


@app.get("/multiply/{x}/{y}")
async def multiply(x: int, y: int) -> int:
    """Multiply two numbers.

    Args:
        x (int): The first number.
        y (int): The second number.

    Returns:
        int: The product of the two numbers.
    """
    return Boilerplate(x, y).multiply()


@app.get("/divide/{x}/{y}")
async def divide(x: int, y: int) -> float:
    """Divide two numbers.

    Args:
        x (int): The first number.
        y (int): The second number.

    Returns:
        float: The quotient of the two numbers.
    """
    return Boilerplate(x, y).divide()
