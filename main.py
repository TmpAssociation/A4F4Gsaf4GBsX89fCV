import requests
from .libs.config import ak


if __name__ == "__main__":
    url = "https://xxxx.intra.weibo.com?ak={}"
    r = requests.get(url=url.format(ak))
    print(r.text)