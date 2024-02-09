import requests



AMOUNT=10
TYPE="boolean"

parameters={
    "amount":10,
    "type":"boolean"
}
url = 'https://opentdb.com/api.php'

try:
    for _ in range(3):  # Try making the request 3 times before giving up
        response = requests.get(url=url, params=parameters)
        if response.status_code == 200:
            break  # If the request is successful, exit the loop
        elif response.status_code == 429:
            # If rate limited, wait for a while before retrying
            retry_after = int(response.headers.get('Retry-After', 10))  # Default to wait for 10 seconds
            time.sleep(retry_after)
    else:
        # If all retries fail, raise an error
        response.raise_for_status()

    data = response.json()
    question_data = data["results"]

except Exception as e:
    print("An error occurred:", e)





