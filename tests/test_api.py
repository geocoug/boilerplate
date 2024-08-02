from __future__ import annotations

from fastapi.testclient import TestClient

from boilerplate.api import app

client = TestClient(app)


class TestAPI:
    """Base API test class."""

    def test_read_root(self: TestAPI) -> None:
        """Check that the response returns a 200 status message.

        Args:
            self (TestAPI): Base API test class.

        """
        response = client.get("/")
        assert response.status_code == 200

    def test_read_hello(self: TestAPI) -> None:
        """Check that the response returns a 200 status message.

        Args:
            self (TestAPI): Base API test class.

        """
        response = client.get("/hello")
        assert response.status_code == 200
        assert "Hello World!" in response.text

    def test_add(self: TestAPI) -> None:
        """Test the add endpoint.

        Args:
            self (TestAPI): Base API test class.
        """
        response = client.get("/add/2/2")
        assert response.status_code == 200
        assert response.json() == 4

    def test_subtract(self: TestAPI) -> None:
        """Test the subtract endpoint.

        Args:
            self (TestAPI): Base API test class.
        """
        response = client.get("/subtract/2/2")
        assert response.status_code == 200
        assert response.json() == 0

    def test_multiply(self: TestAPI) -> None:
        """Test the multiply endpoint.

        Args:
            self (TestAPI): Base API test class.
        """
        response = client.get("/multiply/2/2")
        assert response.status_code == 200
        assert response.json() == 4

    def test_divide(self: TestAPI) -> None:
        """Test the divide endpoint.

        Args:
            self (TestAPI): Base API test class.
        """
        response = client.get("/divide/2/2")
        assert response.status_code == 200
        assert response.json() == 1.0
