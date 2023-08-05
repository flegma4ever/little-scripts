from bs4 import BeautifulSoup
from requests import request
# from datetime import date


def univ_site_parse(url):
    html = request('GET', url).content
    doc = BeautifulSoup(html, 'html.parser')
    return doc

class UniversityOpenings:
    def __init__(self, univ, dep, addr, date, ct):
        self.name = dep
        self.university = univ
        self.address = addr
        self.date = date
        self.city = ct

    def __repr__(self):
        return f'ВУЗ: {self.university}, {self.name} по адресу г.{self.city},{self.address} {self.date}'

    @classmethod
    def generate(cls, univ, dep, addr, date, ct):
        return cls(univ, dep, addr, date, ct)


# -----------------------------МИРЭА------------------------>

doc = univ_site_parse('https://priem.mirea.ru/open-doors/#online_dod_section_2023')
divs = doc.findAll('div', class_='bottomContent')[1:8]
lst = []
for i in divs:
    a = 1
    nm = i.find('p', class_='title').text
    dt = i.find('p', class_='date').text
    ad = i.find('p', class_='location').text
    lst.append(UniversityOpenings.generate('МИРЭА', nm, ad, dt, 'Москва'))

# -----------------------------МИЭТ----------------------->

doc = univ_site_parse('https://www.abiturient.ru/news/')
divs = doc.findAll('div', class_='news-list')
# print(univ_site_parse('https://www.abiturient.ru/news/'))

# -----------------------------МГУ----------------------->

# print(univ_site_parse('https://openday.msu.ru/')) # 403 forbidden

# -----------------------------МЭИ----------------------->

doc = univ_site_parse('https://abitur-mpei.ru/open-day')
h2 = doc.find('h2').text
tm = doc.find('span', itemprop='startDate').contents[5].text
mei = UniversityOpenings('МЭИ', 'МЭИ', 'Энергетическая улица, 8 к2', f'{h2} {tm}', 'Москва')
lst.append(mei)

