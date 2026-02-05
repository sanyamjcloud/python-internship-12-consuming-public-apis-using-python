import requests
import json

API_URL = "https://randomuser.me/api/"

def fetch_user_data():
    try:
        response = requests.get(API_URL, timeout=10)

        # 4. Check response status code
        if response.status_code != 200:
            print(f"Failed to fetch data. Status Code: {response.status_code}")
            return

        # 5. Parse JSON response
        data = response.json()

        # 6. Extract nested fields
        user = data["results"][0]

        extracted_data = {
            "full_name": f"{user['name']['first']} {user['name']['last']}",
            "gender": user["gender"],
            "email": user["email"],
            "country": user["location"]["country"],
            "city": user["location"]["city"]
        }

        # 8. Display clean output
        print("\nUser Data Fetched Successfully\n")
        for key, value in extracted_data.items():
            print(f"{key.capitalize().replace('_', ' ')}: {value}")

        # 9. Store data locally
        with open("data.json", "w") as file:
            json.dump(extracted_data, file, indent=4)

        print("\nData saved to data.json")

    # 7. Handle API errors gracefully
    except requests.exceptions.Timeout:
        print("⏳Request timed out.")
    except requests.exceptions.ConnectionError:
        print("Network connection error.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except KeyError:
        print("Unexpected response structure.")

if __name__ == "__main__":
    fetch_user_data()
