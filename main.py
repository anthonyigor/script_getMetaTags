import requests
from bs4 import BeautifulSoup
import json

list_metas = []
final_list_metas = []
dict = {}


def getMetas(url):
    #faz a requisição da url
    html = requests.get(url)
    if html.status_code != 200:
        print('Falha na requisição')
    else:
        html_content = html.content

    soup = BeautifulSoup(html_content, 'html.parser')
    for tag in soup.find_all('meta'):
        list_metas.append(str(tag))

    # salva os dados em um dicionário
    for i in range(0, len(list_metas) - 1):
        final_list_metas.insert(i, list_metas[i])
    dict.update({'Metas': final_list_metas})

    #transforma o dicionário em json
    json_file = json.dumps(dict, indent=4)
    with open("metas.json", "w") as outfile:
        outfile.write(json_file)
    print("Meta tags salvas no arquivo 'metas.json'")


url = input('Informe URL para extração das meta tags: ')
getMetas(url)
