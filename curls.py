import requests


def main():
    access_token = "<GoogleOAuth2-ACCESS-TOKEN-FROM-CLIENT>"

    url = "http://127.0.0.1/api/register-by-access-token/social/google-oauth2/"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, data={"access_token": access_token})

    print(response.status_code)
    print(response.content)


if __name__ == "__main__":
    main()
