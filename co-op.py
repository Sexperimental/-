import requests
import random
import string

def randomString(length=64):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

api = "https://gakushoku.coop/api/like"
id = str(input("食品ID: "))
count = int(input("回数: "))

data = {
    "item_code": id,
    "mode": "increment"
}

for i in range(count):
    cookie = randomString()
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"_ga_CYPJTYZ717=GS{i}; likeItems=%7B%22itemCode%22%3A%5B%225137%22%5D%7D; "
                  f"_clck=kr4lcr%7C2%7Cfw0%7C0%7C1964; _clsk=vcbago%7C1747547180140%7C26%7C1%7Cf.clarity.ms%2Fcollect; "
                  f"_ga=GA1.1.1008527694.1747546750; "
                  f"__Host-next-auth.csrf-token={cookie}%7Cotherdata; "
                  f"__Secure-next-auth.callback-url=https%3A%2F%2Fgakushoku.coop"
    }

    with requests.Session() as session:
        response = session.post(api, headers=headers, json=data)
        print(f"{i + 1}: {response.status_code}")