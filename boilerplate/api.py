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
async def add(x: float, y: float) -> float:
    """Add two numbers together.

    Args:
        x (float): The first number.
        y (float): The second number.

    Returns:
        float: The sum of the two numbers.
    """
    return Boilerplate(x, y).add()


@app.get("/subtract/{x}/{y}")
async def subtract(x: float, y: float) -> float:
    """Subtract two numbers.

    Args:
        x (float): The first number.
        y (float): The second number.

    Returns:
        float: The difference of the two numbers.
    """
    return Boilerplate(x, y).subtract()


@app.get("/multiply/{x}/{y}")
async def multiply(x: float, y: float) -> float:
    """Multiply two numbers.

    Args:
        x (float): The first number.
        y (float): The second number.

    Returns:
        float: The product of the two numbers.
    """
    return Boilerplate(x, y).multiply()


@app.get("/divide/{x}/{y}")
async def divide(x: float, y: float) -> float | str:
    """Divide two numbers.

    Args:
        x (float): The first number.
        y (float): The second number.

    Returns:
        float | str: The quotient of the two numbers. If the second number is zero, return a string indicating that division by zero is not allowed.
    """  # noqa: E501
    return Boilerplate(x, y).divide()
