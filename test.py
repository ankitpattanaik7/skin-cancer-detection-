import requests

# Define API URL (Update if running on a different host/port)
API_URL = "http://127.0.0.1:8000/predict"

# Path to test image
IMAGE_PATH = "download.jpeg"  # Replace with a valid test image path

def test_upload():
    """Test API with an image upload and check the response."""
    try:
        with open(IMAGE_PATH, "rb") as img:
            files = {"file": img}
            response = requests.post(API_URL, files=files)
        
        # Print response for debugging
        print("Status Code:", response.status_code)
        print("Response JSON:", response.json())

        # Check if the response contains expected keys
        expected_keys = {"id", "key", "confidence", "label", "description", "link"}
        if response.status_code == 200 and expected_keys.issubset(response.json().keys()):
            print("✅ Test Passed: Image was successfully classified.")
        else:
            print("❌ Test Failed: Unexpected response format.")
    
    except Exception as e:
        print(f"❌ Test Failed: {e}")

if __name__ == "__main__":
    test_upload()
    