# import requests
# import scrapy
# from bs4 import BeautifulSoup

# def __main__():

#     URL = 'https://stockx.com/sneakers'
#     #headers = {"User-Agent": "soled-bot"}
#     headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
#     page = requests.get(URL, headers=headers)
    
#     soup = BeautifulSoup(page.content, 'html.parser')
#     # scripts = soup.find_all("script", attrs={"type": "application/ld+json"})
#     # items_string = scripts[-1].string
#     # start = items_string.find('[')
#     # items_string = items_string[start::]
#     # items_string = items_string.split("}}}")

#     # keys = [
#     #     "name",
#     #     "description",
#     #     "lowPrice",
#     #     "highPrice",
#     #     "url"
#     # ]

#     # items = list()

#     # for item_string in items_string:
#     #     item = dict()
#     #     for key in keys:
#     #         data = item_string
#     #         data = data[data.find(key)::]
#     #         data = data[data.find(':')+1::]
#     #         data = data[:data.find(",\"")]
#     #         item[key] = data
#     #     items.append(item)

#     fw = open("../data/stockx-data.txt", "w")
#     # for item in items:
#     #     for k,v in item.items():
#     #         fw.write(k + ":" + v + ", ")
#     #     fw.write("\n")
#     fw.write(soup.text)
#     fw.close()

# __main__()