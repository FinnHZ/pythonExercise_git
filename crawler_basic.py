from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup as bf   #pip install beautifulsoup4



html_ori =  urlopen("https://www.baidu.com/")  #https://www.baidu.com/    https://google.com/

#1) print all html information of the url---------------------------------------------------------
# html_txt = bytes.decode(html_ori.read())
# print(html_txt)


#2) print the title of the url---------------------------------------------------------
# obj = bf(html_ori.read(), 'html.parser')
# title = obj.head.title
# print(title)


#3) print the html code of image---------------------------------------------------------
# obj = bf(html_ori.read(), 'html.parser')
# img_html = obj.find_all('img')
# for item in img_html:
#     print(item)

#4) print the html url of image---------------------------------------------------------
# obj = bf(html_ori.read(), 'html.parser')
# img_html = obj.find_all('img', class_ = "index-logo-src")  #if id, we write 'id' directly, if class, we write 'class_'
# img_url = "https:" + img_html[0]['src']
# print(img_url)


#4) download a picture based on the url---------------------------------------------------------
obj = bf(html_ori.read(), 'html.parser')
img_html = obj.find_all('img', class_ = "index-logo-src")  #if id, we write 'id' directly, if class, we write 'class_'
img_url = "https:" + img_html[0]['src']
urlretrieve(img_url, filename = './img/logo.png')