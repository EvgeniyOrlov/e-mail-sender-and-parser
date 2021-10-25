import requests
from bs4 import BeautifulSoup as BS

persons_url_list = []
persons_mail_list = []

r = requests.get('https://notariatus.ru/moskva')
result = BS(r.content, 'html.parser')

# soup = BeautifulSoup(result, 'lxml')
# persons_urls = soup.find_all(class_='name')

for person in result.select('.grid_out > .notarius_box > .name > a'):
    person_page_url = person.get('href')
    persons_url_list.append(f'https://notariatus.ru{person_page_url}')

for i in persons_url_list:
    q = requests.get(i)
    res = BS(q.content, 'html.parser')
    for el in res.select('.white_block_left > .list_info > .mail'):
        mail = el.text.strip()
        if mail != 'не известно':
            persons_mail_list.append(mail)
        else:
            continue

print(persons_mail_list)

with open('mails.txt', 'a') as file:
    for line in persons_mail_list:
        file.write(f'{line}\n')
