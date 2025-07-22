from http import HTTPStatus
import requests
import pytest
from test_utils import assert_valid_meow_response

# Map of ID to expected cat fact(s)
expected_facts_by_id = {
    3: [
        "Mother cats teach their kittens to use the litter box."
    ],
    5: [
        "Contrary to popular belief, the cat is a social animal. A pet cat will respond and answer to speech , and seems to enjoy human companionship."
    ],
    7: [
        "Neutering a cat extends its life span by two or three years."
    ]
}

def test_meowfacts_get():
    """Test basic GET request to root endpoint."""
    url = "https://meowfacts.herokuapp.com/"
    response = requests.get(url)
    assert_valid_meow_response(response)

@pytest.mark.parametrize("count", [0, 1, 3])
def test_meowfacts_count(count):
    """Test the `count` query parameter returns the correct number of facts."""
    url = f"https://meowfacts.herokuapp.com/?count={count}"
    response = requests.get(url)
    data = assert_valid_meow_response(response)

    assert len(data["data"]) == count, f"Expected {count} facts, got {len(data['data'])}"

@pytest.mark.parametrize("fact_id, expected_facts", expected_facts_by_id.items())
def test_meowfacts_by_id(fact_id, expected_facts):
    """Test that a specific ID returns the correct, expected fact."""
    url = f"https://meowfacts.herokuapp.com/?id={fact_id}"
    response = requests.get(url)
    data = assert_valid_meow_response(response)

    assert data["data"] == expected_facts, f"Expected {expected_facts}, got {data['data']}"

@pytest.mark.parametrize("invalid_count", ["abc", -1, -5])
def test_meowfacts_invalid_count(invalid_count):
    """Test invalid values for the count parameter result in a Bad Request.
    The test is failing
    """
    url = f"https://meowfacts.herokuapp.com/?count={invalid_count}"
    response = requests.get(url)

    assert response.status_code == HTTPStatus.BAD_REQUEST, (
        f"Expected 400 Bad Request for count={invalid_count}, got {response.status_code}"
    )

@pytest.mark.parametrize("invalid_id", ["xyz", -3])
def test_meowfacts_invalid_id(invalid_id):
    """Test invalid values for the id parameter result in a Bad Request.
    The test is failing
    """
    url = f"https://meowfacts.herokuapp.com/?id={invalid_id}"
    response = requests.get(url)

    assert response.status_code == HTTPStatus.BAD_REQUEST, (
        f"Expected 400 Bad Request for id={invalid_id}, got {response.status_code}"
    )
