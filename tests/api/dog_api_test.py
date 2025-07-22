from http import HTTPStatus
import requests

DOG_API_URL = "https://dog.ceo/api/breeds/image/random"

def validate_image_url(url):
    """Helper function to validate that the image URL is reachable and it returns image content."""
    response = requests.get(url)
    
    assert response.status_code == HTTPStatus.OK, f"Image URL did not return 200 OK: {url}"
    content_type = response.headers.get("Content-Type", "")
    assert content_type.startswith("image/"), f"Unexpected content type: {content_type}"

def test_dog_ceo_random_image():
    """Tests the Dog CEO API endpoint for retrieving a random dog image by validating response content and image validation."""
    response = requests.get(DOG_API_URL)

    assert response.status_code == HTTPStatus.OK, f"Expected {HTTPStatus.OK}, got {response.status_code}"

    data = response.json()
    assert "message" in data, "'message' key not in response"
    assert "status" in data, "'status' key not in response"
    assert data["status"] == "success", f"Expected status 'success', got {data['status']}"

    # Validate the returned image URL
    image_url = data["message"]
    validate_image_url(image_url)
