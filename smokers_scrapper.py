import os
import json

import requests
from dotenv import dotenv_values

def get_smokers_json(api_key: str, page=1) -> None:
    url = "https://www.searchapi.io/api/v1/search"
    params = {
    "engine": "google_images",
    "q": "smoking+man+model",
    "api_key": api_key,
    "page": str(page)
    }

    try:
        response = requests.api.get(url, params=params)

        if response.status_code == 200:
            with open('smokers_scheme.json', 'w') as file:
                json.dump(response.json(), file, indent=4, ensure_ascii=False)

            print('Get smokers json successfully!')
        
        else:
            print("Failed to get smokers json. Status code:", response.
            status_code)

    except requests.exceptions.RequestException as e:
        print("An error occurred due to get smokers json file:", e)

def get_people_json(api_key: str, page=1) -> None:
    url = "https://www.searchapi.io/api/v1/search"
    params = {
    "engine": "google_images",
    "q": "man+phone+talking",
    "api_key": api_key,
    "page": str(page)
    }

    try:
        response = requests.api.get(url, params=params)

        if response.status_code == 200:
            with open('people_scheme.json', 'w') as file:
                json.dump(response.json(), file, indent=4, ensure_ascii=False)

            print('Get people json successfully!')
        
        else:
            print("Failed to get people json. Status code:", response.
            status_code)

    except requests.exceptions.RequestException as e:
        print("An error occurred due to get people json file:", e)

def download_image(url, file_path, number, headers) -> None:
    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                file.write(response.content)

            print(f"Image {number} downloaded successfully!")

        else:
            print(f"Failed to download image {number}. Status code:", response.status_code)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred due to image {number} downloading:", e)

if __name__ == '__main__':
    api_key = dotenv_values('.env')['api_key']
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)\
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaBrowser/22.7.3.799 Yowser/2.5 Safari/537.36"
    }
    page = 8
    # get_smokers_json(api_key, 4)
    get_people_json(api_key)

    # with open('smokers_scheme.json') as file:
    #     smokers = json.load(file)

    # if not os.path.exists("smokers"):
    #     os.mkdir("smokers")
    
    # for smoker in smokers["images"]:
    #     download_image(smoker["original"]["link"], f"smokers/{page}/" + f"{smoker["position"]}_{page}" + ".jpg", f"{smoker["position"]}_{page}", headers)

    with open('people_scheme.json') as file:
        peoples = json.load(file)

    if not os.path.exists("people"):
        os.mkdir("people")
    
    if page is not None:
        for people in peoples["images"]:
            download_image(people["original"]["link"], f"people/{page}/" + f"{people["position"]}_{page}" + ".jpg", f"{people["position"]}_{page}", headers)
