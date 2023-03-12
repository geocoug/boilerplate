from api.api import app
from fastapi.testclient import TestClient

client = TestClient(app)


class TestAPI:
    """Base API test class."""

    def test_read_root(self: "TestAPI") -> None:
        """Check that the response returns a 200 status message.

        Args:
        ----
            self (TestAPI): Base API test class.
        """
        response = client.get("/")
        assert response.status_code == 200

    def test_read_hello(self: "TestAPI") -> None:
        """Check that the response returns a 200 status message.

        Args:
        ----
            self (TestAPI): Base API test class.
        """
        response = client.get("/hello")
        assert response.status_code == 200
        assert "Hello World!" in response.text
