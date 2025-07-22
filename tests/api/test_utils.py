from http import HTTPStatus

def assert_valid_meow_response(response, expected_status=HTTPStatus.OK):
    """Assert common properties of a valid meowfacts API response."""
    assert response.status_code == expected_status, (
        f"Unexpected status code: {response.status_code}"
    )

    data = response.json()
    assert isinstance(data, dict), "Response is not a JSON object"
    assert "data" in data, "Missing 'data' key in response"
    assert isinstance(data["data"], list), "'data' is not a list"

    return data
