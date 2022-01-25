import requests
from bs4 import BeautifulSoup


def getLandL(address):

    url = f"https://www.google.com/maps/place?q={address}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    text = soup.prettify()
    initial_pos = text.find(";window.APP_INITIALIZATION_STATE")
    data = text[initial_pos + 36:initial_pos + 85]
    data = data.split(',')

    lo = data[1]
    la = data[2]

    return lo, la
