# -*- coding: utf-8 -*- 

import KMean
from Point import Point
import math

#读取文件中的数据
def read_file():
	dic_rflie = {} 	#存储从文件中读取出的每一行，key：UID，value：嵌套的列表，列表的每一项为[stayTime,PageNums
	rfi = open("web_data.txt","r")
	try:
		for line in rfi.readlines():    #依次读取每一行
			line.strip()				#去掉每行头尾空行
			if line.find("day") != -1 or line.find("user") != -1:	#跳过包含不是用户记录的行，即包含day和user的行（==-1表示没找到）
				continue
			tmp = []		
			tmp = line.split(',')		#用逗号来分割每行中的字符串，分割后返回列表
			uid = tmp[0]
			if uid not in dic_rflie:	#初始化字典的value对应的列表
				dic_rflie[uid] = []
			dic_rflie[uid].append([tmp[1],tmp[2]]) #将每一行中UID对应的st和pn作为列表追加到字典中
	finally:
		rfi.close()
	return dic_rflie

#统计从文件中读取的数据，求均值
def sum(dic_rflie):
	dic_sum = {} 	#存储每一个UID对应的ST和PN的累加和，key：UID，value：列表，[sum_st,sum_pn]
	for u,v in dic_rflie.items():
		st = 0	#记录每个用户的页面停留时间
		pn = 0	#记录每个用户浏览的总得页面数
		for s in v:
			st += int(s[0])
			pn += int(s[1])
		st = st/30
		pn = pn/30
		dic_sum[u] = '&'.join([str(st),str(pn)])

	for u,v in dic_sum.items():
		print u,v

	return dic_sum


def main():

    kmean = KMean.KMean()

    def distance(p1,p2):
        #return float(abs(p1.x - p2.x))
    	return float(math.sqrt(math.pow(float(p1.x-p2.x),2)+math.pow(float(p1.y-p2.y),2)))

    def center(points):
    	center_point = Point(0,0,0)
    	for point in points:
    		center_point.x += point.x
    		center_point.y += point.y
    	center_point.x = center_point.x/float(len(points))
    	center_point.y = center_point.y/float(len(points))	
        return center_point

    kmean.distance = distance
    kmean.center = center

    dic_rflie = read_file()
    dic_sum = sum(dic_rflie)
    point_list = []
    for i,p in dic_sum.items():
		data = p.split("&")
		point_list.append(Point(i,float(data[0]),float(data[1])))

    groups = kmean.run(point_list,4,[point_list[0],point_list[1],point_list[2],point_list[3]])
    for group in groups:
    	for point in group:
    		print '(',point.id, point.x, ',', point.y, '),'
    	print '\n'


if __name__ == "__main__":
    main()
