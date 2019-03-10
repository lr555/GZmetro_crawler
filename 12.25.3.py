# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 12:22:29 2017

@author: Dell
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 10:40:43 2017

@author: Dell
"""

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
#去掉了龙溪
#去掉了龙溪
#去掉了龙溪
table=['金融高新区',
'千灯湖',
'礌岗',
'南桂路',
'桂城',
'朝安',
'普君北路',
'祖庙',
'同济路',
'季华园',
'魁奇路',
'澜石',
'世纪莲',
'东平',
'新城东',
'广州东站',
'体育中心',
'体育西路',
'杨箕',
'东山口',
'烈士陵园',
'农讲所',
'公园前',
'西门口',
'陈家祠',
'长寿路',
'黄沙',
'芳村',
'花地湾',
'坑口',
'西朗',
'嘉禾望岗',
'黄边',
'江夏',
'萧岗',
'白云文化广场',
'白云公园',
'飞翔公园',
'三元里',
'广州火车站',
'越秀公园',
'纪念堂',
'海珠广场',
'市二宫',
'江南西',
'昌岗',
'江泰路',
'东晓南',
'南洲',
'洛溪',
'南浦',
'会江',
'石壁',
'广州南站',
'番禺广场',
'市桥',
'汉溪长隆',
'大石',
'厦滘',
'沥滘',
'大塘',
'客村',
'广州塔',
'珠江新城',
'石牌桥',
'岗顶',
'华师',
'五山',
'天河客运站',
'林和西',
'燕塘',
'梅花园',
'京溪南方医院',
'同和',
'永泰',
'白云大道北',
'龙归',
'人和',
'机场南',
'黄村',
'车陂',
'车陂南',
'万胜围',
'官洲',
'大学城北',
'大学城南',
'新造',
'石碁',
'海傍',
'低涌',
'东涌',
'黄阁汽车城',
'黄阁',
'蕉门',
'金洲',
'文冲',
'大沙东',
'大沙地',
'鱼珠',
'三溪',
'东圃',
'科韵路',
'员村',
'潭村',
'猎德',
'五羊邨',
'动物园',
'区庄',
'淘金',
'小北',
'西村',
'西场',
'中山八',
'坦尾',
'滘口',
'浔峰岗',
'横沙',
'沙贝',
'河沙',
'如意坊',
'文化公园',
'一德路',
'北京路',
'团一大广场',
'东湖',
'黄花岗',
'沙河顶',
'天平架',
'长湴',
'植物园',
'龙洞',
'柯木塱',
'高塘石',
'黄陂',
'金峰',
'暹岗',
'苏元',
'萝岗',
'香雪',
'板桥',
'员岗',
'南村万博',
'钟村',
'谢村',
'凤凰新村',
'沙园',
'宝岗大道',
'晓港',
'中大',
'鹭江',
'赤岗',
'磨碟沙',
'新港东',
'琶洲',
'燕岗',
'沙涌',
'鹤洞',
'菊树',
'体育中心南',
'天河南',
'黄埔大道',
'妇儿中心',
'花城大道',
'大剧院',
'海心沙',
       ]



SERVICE_ARGS=['--load-images=false','--disk-cache=true']
browser= webdriver.PhantomJS(service_args=SERVICE_ARGS)
browser.set_window_size(1400,900)
wait=WebDriverWait(browser, 10)
browser.get('http://ditie.114huoche.com/GuangZhou/')
def search(start,end):
    try:
        input1=wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#f"))
        )
        input1.clear()
        input1.send_keys(start)
        input2=wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#d"))
        )
        input2.clear()
        input2.send_keys(end)
        submit=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#chaxun_left > ul.kuang > form > input.submit_chaxun')))
        submit.click()
        time.sleep(5)   
        content=wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#zz > div > div"))
        )
        print (content.text)
        detail=content.text;
        loc1=detail.find('价')
        loc2=detail.find('元')
        if loc1==-1 or loc2==-1:
            return search(start,end)
        with open("stations_cost.txt","a") as f:
            f.write(start)
            f.write(' ')
            f.write(end)
            f.write(' ')
            f.write(detail[loc1+1:loc2])
            f.write('\n')
    except TimeoutException:
        return search(start,end)

def main():
    count=0
    for i in range(7):
        for j in range(15,165):
            if i==0 and j<51:
                continue
            count+=1
            print ("subway",i,j,count)
            search(table[i],table[j])

if __name__=='__main__':
    main()   










