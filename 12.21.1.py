# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 22:17:26 2017

@author: Dell
"""

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup

table=[
['广州东站','体育中心'],
['广州东站','林和西'],
['广州东站','燕塘'],
['体育中心','体育西路'],
['体育西路','杨箕'],
['体育西路','珠江新城'],
['体育西路','石牌桥'],
['体育西路','林和西'],
['杨箕','东山口'],
['杨箕','五羊邨'],
['杨箕','动物园'],
['东山口','烈士陵园'],
['东山口','区庄'],
['东山口','东湖'],
['烈士陵园','农讲所'],
['农讲所','公园前'],
['公园前','西门口'],
['公园前','纪念堂'],
['公园前','海珠广场'],
['西门口','陈家祠'],
['陈家祠','长寿路'],
['长寿路','黄沙'],
['黄沙','芳村'],
['黄沙','如意坊'],
['黄沙','文化公园'],
['芳村','花地湾'],
['花地湾','坑口'],
['坑口','西朗'],
['西朗','鹤洞'],
['西朗','菊树'],
['嘉禾望岗','黄边'],
['嘉禾望岗','白云大道北'],
['嘉禾望岗','龙归'],
['黄边','江夏'],
['江夏','萧岗'],
['萧岗','白云文化广场'],
['白云文化广场','白云公园'],
['白云公园','飞翔公园'],
['飞翔公园','三元里'],
['三元里','广州火车站'],
['广州火车站','越秀公园'],
['广州火车站','小北'],
['广州火车站','西村'],
['越秀公园','纪念堂'],
['海珠广场','市二宫'],
['海珠广场','一德路'],
['海珠广场','北京路'],
['市二宫','江南西'],
['江南西','昌岗'],
['昌岗','江泰路'],
['昌岗','宝岗大道'],
['昌岗','晓港'],
['江泰路','东晓南'],
['东晓南','南洲'],
['南洲','洛溪'],
['洛溪','南浦'],
['南浦','会江'],
['会江','石壁'],
['石壁','广州南站'],
['石壁','谢村'],
['番禺广场','市桥'],
['市桥','汉溪长隆'],
['汉溪长隆','大石'],
['汉溪长隆','南村万博'],
['汉溪长隆','钟村'],
['大石','厦滘'],
['厦滘','沥滘'],
['沥滘','大塘'],
['大塘','客村'],
['客村','广州塔'],
['客村','鹭江'],
['客村','赤岗'],
['广州塔','珠江新城'],
['广州塔','海心沙'],
['珠江新城','猎德'],
['珠江新城','五羊邨'],
['石牌桥','岗顶'],
['岗顶','华师'],
['华师','五山'],
['五山','天河客运站'],
['天河客运站','燕塘'],
['天河客运站','长湴'],
['林和西','体育中心南'],
['燕塘','梅花园'],
['燕塘','天平架'],
['梅花园','京溪南方医院'],
['京溪南方医院','同和'],
['同和','永泰'],
['永泰','白云大道北'],
['龙归','人和'],
['人和','机场南'],
['黄村','车陂'],
['车陂','车陂南'],
['车陂南','万胜围'],
['车陂南','东圃'],
['车陂南','科韵路'],
['万胜围','官洲'],
['万胜围','琶洲'],
['官洲','大学城北'],
['大学城北','大学城南'],
['大学城南','新造'],
['大学城南','板桥'],
['新造','石碁'],
['石碁','海傍'],
['海傍','低涌'],
['低涌','东涌'],
['东涌','黄阁汽车城'],
['黄阁汽车城','黄阁'],
['黄阁','蕉门'],
['蕉门','金洲'],
['文冲','大沙东'],
['大沙东','大沙地'],
['大沙地','鱼珠'],
['鱼珠','三溪'],
['三溪','东圃'],
['科韵路','员村'],
['员村','潭村'],
['潭村','猎德'],
['动物园','区庄'],
['区庄','淘金'],
['区庄','黄花岗'],
['淘金','小北'],
['西村','西场'],
['西场','中山八'],
['中山八','坦尾'],
['坦尾','滘口'],
['坦尾','河沙'],
['坦尾','如意坊'],
['浔峰岗','横沙'],
['横沙','沙贝'],
['沙贝','河沙'],
['文化公园','一德路'],
['北京路','团一大广场'],
['团一大广场','东湖'],
['黄花岗','沙河顶'],
['沙河顶','天平架'],
['长湴','植物园'],
['植物园','龙洞'],
['植物园','柯木塱'],
['高塘石','黄陂'],
['黄陂','金峰'],
['金峰','暹岗'],
['暹岗','苏元'],
['苏元','萝岗'],
['萝岗','香雪'],
['板桥','员岗'],
['员岗','南村万博'],
['钟村','谢村'],
['凤凰新村','沙园'],
['沙园','宝岗大道'],
['沙园','燕岗'],
['沙园','沙涌'],
['晓港','中大'],
['中大','鹭江'],
['赤岗','磨碟沙'],
['磨碟沙','新港东'],
['新港东','琶洲'],
['沙涌','鹤洞'],
['菊树','龙溪'],
['体育中心南','天河南'],
['天河南','黄埔大道'],
['黄埔大道','妇儿中心'],
['妇儿中心','花城大道'],
['花城大道','大剧院'],
['大剧院','海心沙'],
['金融高新区','千灯湖'],
['金融高新区','龙溪'],
['千灯湖','礌岗'],
['礌岗','南桂路'],
['南桂路','桂城'],
['桂城','朝安'],
['朝安','普君北路'],
['普君北路','祖庙'],
['祖庙','同济路'],
['同济路','季华园'],
['季华园','魁奇路'],
['魁奇路','澜石'],
['澜石','世纪莲'],
['世纪莲','东平'],
['东平','新城东'],
    ]

SERVICE_ARGS=['--load-images=false','--disk-cache=true']
browser= webdriver.PhantomJS(service_args=SERVICE_ARGS)
browser.set_window_size(1400,900)
wait=WebDriverWait(browser, 10)
browser.get('http://www.gpsspg.com/distance.htm')
last_dis='+'
def search(start,end):
    global last_dis
    try:
        submit5=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#u_btn3')))
        submit5.click()
        time.sleep(5) 
        input1=wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#s_t"))
        )
        input1.clear()
        start1='广州市'+start+'地铁站'
        input1.send_keys(start1)
        submit1=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#s_btn')))
        submit1.click()
        time.sleep(5) 
        submit2=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#u_btn1')))
        submit2.click()
        time.sleep(5) 
        
        input2=wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#s_t"))
        )
        input2.clear()
        end1='广州市'+end+'地铁站'
        input2.send_keys(end1)
        submit3=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#s_btn')))
        submit3.click()
        time.sleep(5) 
        submit4=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#u_btn1')))
        submit4.click()
        time.sleep(5) 
        dis=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#r_distances')))
        print (start,end,dis.text)
        if dis.text=='0.00' or dis.text=='0':
            return search(start,end)
        if dis.text==last_dis:
            return search(start,end)
        last_dis=dis.text;
        print (last_dis)
        with open("station_dis.txt","a") as f:
            f.write(start)
            f.write(' ')
            f.write(end)
            f.write(' ')
            f.write(dis.text)
            f.write('\n')
    except TimeoutException:
        return search(start,end)


def main():
    for i in table:
        search(i[0],i[1])
        

if __name__=='__main__':
    main()   