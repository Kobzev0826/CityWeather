import  requests

def get_city_id(name_city):
    app_id = "0be65ff99915191fe542170019157ccc"
    url = f"https://api.openweathermap.org/data/2.5/weather"
    payload = {"q" : name_city, "appid" : app_id}
    response = requests.get(url,params=payload)
    response.raise_for_status()
    try:
        city_id = response.json()["id"]
    except KeyError:
        city_id = None
    return city_id


if __name__ =='__main__':
    city_id = get_city_id("Spitak")
    print(city_id)

