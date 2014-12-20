#coding: utf-8
#统计用户的平均停留时间和平均停留页面数

#构造数据结构用于存储从文件中读取出来的数据

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

	#sorted(dic_sum.items(),key = lambda dic_sum:dic_sum[0])
	for u,v in dic_sum.items():
		print u,v

	return dic_sum

if __name__ == "__main__":
	dic_rflie = {}
	dic_rflie = read_file()
	sum(dic_rflie)




