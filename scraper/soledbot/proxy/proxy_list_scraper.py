import requests
import scrapy
from bs4 import BeautifulSoup

def __main__():

    fr = open("proxy_list.txt", "r")
    lines = fr.readlines()
    print(lines)
    fw = open("proxy_list.txt", "w")
    for line in lines:
        print(line)
        fw.write("http://" + line)

    fw.close()
    fr.close()

    # URL = 'https://free-proxy-list.net/'
    # #headers = {"User-Agent": "soled-bot"}
    # headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
    # page = requests.get(URL, headers=headers)
    # soup = BeautifulSoup(page.content, 'html.parser')

    # proxy = list()
    # table = soup.find('table', attrs={'class':'table table-striped table-bordered dataTable'})
    # print(table)
    # # table_body = table.find('tbody')
    # # rows = table_body.find_all('tr')

    # # fw = open("proxy_list.txt", "w")
    # # for row in rows:
    # #     cols = row.find_all('td')
    # #     fw.write(cols[0].text.strip() + ':' + cols[1].text.strip())
    # # fw.close()

__main__()