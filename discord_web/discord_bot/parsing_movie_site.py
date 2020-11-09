from bs4 import BeautifulSoup as bs
import requests

HTTP_HEADERS = {
    'User-Agent': 'Mozilla/5.0 '
                  '(Macintosh; Intel Mac OS X 10_11_5) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/50.0.2661.102 Safari/537.36'}


def _get_url() -> str:
    url = "https://randomfilms.ru"  # 26500 фильмов
    r = requests.get(url, allow_redirects=True, headers=HTTP_HEADERS)
    soup = bs(r.text, "html.parser")
    navigation_class = soup.find(class_="navigation")
    a = navigation_class.find(class_="nav-button")
    href = a.get('href')
    return url + href


def _get_img_url(soup, url: str) -> str:
    r = requests.get(url)
    content_list = []
    bg_img = str(r.content).split(" ")
    for img in bg_img:
        if img.startswith('"/gallery/'):
            content_list.append(img)

    image_url = "https://randomfilms.ru" + content_list[0][1:-4]
    req_img = requests.get(image_url)
    if req_img.status_code == 200:
        return image_url
    else:
        return "https://lh3.googleusercontent.com/proxy/5LPAJo0BNOUjNa5x8hZ5eLWVBqkTL2W-RufoifDHvIZ8MtrrIv5ryHizz2SPaiACOIGpq3ZmXCaQ0MfSlZ3Ydi04X3uEK5WiH8ALLD47-Z2cSIEJFEkdiFvOHZuMmu1-d3gF3RxjPa1TprZS_sf19KyTEmAaXmCCQ2VbtyM6cR0OFaDtqTBeyy2xWfcXsH6gcYMG29BJ1oxJgg7KZtz2EnNYXIHYuMThnxwvHtwOuIRplh0GZwLRny-BmwvcMfomPt7siyRIbzbMBJ006gDlDynWA_1sxfr8pKhaSXxIyr7jTau3033r9ChpfZBQ93qM-5aSHdzD3hKLY7hyUKBS7vlZ-VFz-hfqT6YvZCnlHbwytc-kTLsYL_yva73mKm7IdFKSLLrVXi3MrhKjvdak1w"


def _get_description(soup, url: str) -> str:
    r = requests.get(url)
    parse_list = r.content.decode('utf-8').split("\n")
    return [desc for desc in parse_list if desc.startswith('  <meta property="og:description"')][0][43:-4] + "..."


def get_random_film() -> list:
    url = _get_url()
    r = requests.get(url, allow_redirects=True, headers=HTTP_HEADERS)
    soup = bs(r.text, "html.parser")
    category: list = []
    title: str = "undefined"
    rating: str = 'КиноПоиск0.0'
    description: str = "Описание"

    image = _get_img_url(soup, url)

    description = _get_description(soup, url)

    for header in soup.find(class_="header"):
        """Название фильма"""
        try:
            title = header.contents[0]
            break
        except AttributeError:
            pass

    for a in soup.find(class_="navigation"):
        """Категории фильма"""
        try:
            category.append(a.contents[0])

        except AttributeError:
            pass

    for mb in soup.find_all(class_="margin-bottom--24"):

        try:
            pre_rating = mb.contents[0].replace('\n', '').replace(' ', '').split(",")
            if len(pre_rating) == 2:
                rating = pre_rating[0][9:]

        except Exception:
            pass

    return [title, category, rating, description, image]
