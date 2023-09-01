# #快代理
# import requests
# from lxml.html import etree
#
# url = 'http://www.kuaidaili.com/free/inha/6'#快代理
# data =requests.get(url)
# html = etree.HTML(data.text)
#
# #找xpath
# ip_xpath = '//*[@id="list"]/table/tbody/tr/td[1]/text()'
# port_xpath = '//*[@id="list"]/table/tbody/tr/td[2]/text()'
# http_or_https_xpath ='//*[@id="list"]/table/tbody/tr/td[4]/text()'
#
# #匹配内容
# ip_list = rp_html.xpath(ip_xpath)
# port_list = rp_html.xpath(port_xpath)
# http_or_https_list = rp_html.xpath(http_or_https_xpath)
#
# #进行组合
# list_zip = zip(ip_list,port_list,http_or_https_list)
# proxy_dict= {}
# proxy_list = []
# for ip,port,http_or_https in list_zip:
#     proxy_dict[http_or_https] = f'{ip}:{port}'
#     proxy_list.append(proxy_dict)
#     proxy_dict = {}
#
# #西刺代理
# import re
#
# import requests
# from bs4 import BeautifulSoup
#
# import user
#
# import random
#
#
# def getListProxies():
#     session = requests.session()
#     headers = {'User-Agent': user.getuser()}
#     proxies = random.choice(proxy_list)
#     page = session.get("http://www.xicidaili.com/nn/2", headers = headers,proxies = proxies)#西刺代理
#     soup = BeautifulSoup(page.text, 'lxml')
#
#     proxyList = []
#     taglist = soup.find_all('tr', attrs={'class': re.compile("(odd)|()")})
#     for trtag in taglist:
#         tdlist = trtag.find_all('td')
#         proxy = {'http': tdlist[1].string + ':' + tdlist[2].string}
#
#         proxyList.append(proxy)
#         # 设定代理ip个数
#         if len(proxyList) >= 20:
#             break
#
#     return proxyList
#
#
#

from fake_useragent import UserAgent
import logging
import requests
from bs4 import BeautifulSoup
import time
import random

# 获取网页数据
def get_web_data(url, headers, proxies=[]):
    try:
        data = requests.get(url, proxies=proxies, timeout=3, headers=headers)
    except requests.exceptions.ConnectionError as e:
        logging.error("请求错误，url:", url)
        logging.error("错误详情：", e)
        data = None
    except:
        logging.error("未知错误，url:", url)
        data = None
    return data


# 获取代理数据
def get_proxies(proxy_url, dis_url, page=10):
    proxy_list = []
    for i in range(1, page + 1):
        tmp_ua = UserAgent()
        tmp_headers = {'User-Agent': tmp_ua.random}
        html_str = get_web_data(proxy_url + str(i), tmp_headers)
        soup = BeautifulSoup(html_str.content, "lxml")
        ips = soup.find('tbody').find_all('tr')
        for ip_info in ips:
            tds = ip_info.find_all('td')
            ip = tds[0].get_text()
            port = tds[1].get_text()
            ip_str = ip + ":" + port
            tmp = {"http": "http://" + ip_str}
            if check_proxy(dis_url, tmp):
                logging.info("ip:%s is available", ip_str)
                proxy_list.append(ip_str)
        time.sleep(1)
    return proxy_list


# 检测代理ip是否可用
def check_proxy(url, proxy):
    try:
        tmp_ua = UserAgent()
        tmp_headers = {'User-Agent': tmp_ua.random}
        res = requests.get(url, proxies=proxy, timeout=1, headers=tmp_headers)
    except:
        return False
    else:
        return True


def get_random_ip(ip_list):
    proxy = random.choice(ip_list)
    proxies = {'http': 'http://' + proxy}
    return proxies


