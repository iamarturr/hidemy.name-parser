import requests
from bs4 import BeautifulSoup


def main(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.find("div", class_="table_block")

    """
        Speed_col - this is unnecessary information for parsing, i removed it
    """

    for item in items.find_all("tr"):
        if "speed_col" in str(item):
            pass
        else:
            i = item.find_all("td")
            result.append({
                "ip": f"{i[0].text}:{i[1].text}",
                "country": i[2].text,
                "ping": i[3].text,
                "type": i[4].text,
                "anonimus": i[5].text,
                "last_checked": i[6].text
            })


if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) like Gecko"
    }

    """
        max_ping - max speed of proxy (default 300)
        type_proxy - type of proxy:
            h = http only
            s = https only
            4 = socks 4 only
            5 = socks 5 only
        Example: &type=hs
        PS: if u want search all, type should be empty
    """

    max_ping = 300
    type_proxy = ""
    link = f"https://hidemy.name/ru/proxy-list/?maxtime={max_ping}{type_proxy}"
    result = []

    main(link)
    print(result)
