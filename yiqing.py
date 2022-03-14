# import asyncio
# from pyppeteer import launch
# from pyquery import PyQuery as pq
# import asyncio
# from pyppeteer import launch
# from bs4 import BeautifulSoup
# import os
# # 
# # 
# # async def main():
# #    # browser = await launch()
# #    browser = await launch({'headless': False, 'dumpio': True,  'autoClose': True})
# #    page = await browser.newPage()
# #    await page.goto('http://www.nhc.gov.cn/xcs/yqtb/list_gzbd.shtml')
# #    await page.waitForSelector('.zxxx_list')
# #    doc = pq(await page.content())
# #    names = [item.text() for item in doc('.zxxx_list .li').items()]
# #    print('Names:', names)
# #    await browser.close()
# # asyncio.get_event_loop().run_until_complete(main())
# 
# 
# 
# 
# async def pyppteer_fetchUrl(url):
#     browser = await launch({'headless': False,'dumpio':True, 'autoClose':True})
#     page = await browser.newPage()
# 
#     await page.goto(url)
#     await asyncio.wait([page.waitForNavigation()])
#     str = await page.content()
#     await browser.close()
#     return str
# 
# def fetchUrl(url):
#     return asyncio.get_event_loop().run_until_complete(pyppteer_fetchUrl(url))
# 
# 
# 
# def getPageUrl():
#     for page in range(1,7):
#         if page == 1:
#             yield 'http://www.nhc.gov.cn/xcs/yqtb/list_gzbd.shtml'
#         else:
#             url = 'http://www.nhc.gov.cn/xcs/yqtb/list_gzbd_'+ str(page) +'.shtml'
#             yield url
# 
# 
# def getTitleUrl(html):
# 
#     bsobj = BeautifulSoup(html,'html.parser')
#     titleList = bsobj.find('div', attrs={"class":"list"}).ul.find_all("li")
#     for item in titleList:
#         link = "http://www.nhc.gov.cn" + item.a["href"];
#         title = item.a["title"]
#         date = item.span.text
#         yield title, link, date
# 
# def getContent(html):
#         
#     bsobj = BeautifulSoup(html,'html.parser')
#     cnt = bsobj.find('div', attrs={"id":"xw_box"}).find_all("p")
#     s = ""
#     if cnt:
#         for item in cnt:
#             s += item.text
#         return s
# 
#     return "爬取失败！"
# 
# def saveFile(path, filename, content):
# 
#     if not os.path.exists(path):
#         os.makedirs(path)
#         
#     # 保存文件
#     with open(path + filename + ".txt", 'w', encoding='utf-8') as f:
#         f.write(content)
# 
# if "__main__" == __name__: 
#     for url in getPageUrl():
#         s =fetchUrl(url)
#         for title,link,date in getTitleUrl(s):
#             print(title,link)
#             #如果日期在1月21日之前，则直接退出
#             mon = int(date.split("-")[1])
#             day = int(date.split("-")[2])
#             if mon <= 1 and day < 21:
#                 break;
# 
#             html =fetchUrl(link)
#             content = getContent(html)
#             print(content)
#             saveFile("/Users/jarod/PycharmProjects/疫情数据爬虫/NHC_Data/", title, content)
#             print("-----"*20)




import asyncio
from pyppeteer import launch

url = 'http://www.nhc.gov.cn/xcs/yqtb/list_gzbd.shtml'

async def fetchUrl(url):
    browser = await launch({'headless': False,'dumpio':True, 'autoClose':False})
    page = await browser.newPage()
    await page.evaluateOnNewDocument('() =>{ Object.defineProperties(navigator,'
                      '{ webdriver:{ get: () => false } }) }')
    await page.goto(url)

asyncio.get_event_loop().run_until_complete(fetchUrl(url))


