
#coding: utf-8
#随机生成用户访问网站的数据
#用户行为数据：用户ID 访问频率 访问时间间隔 平均停留时间 平均访问页面数 订单数 客单价
#简化为：user_ID, used_time, page_num

import random
from random import choice

fi = open("web_data.txt","w");

uid = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
fi.write('user_ID')
fi.write(', ')
fi.write('used_time')
fi.write(', ')
fi.write('page_num')
fi.write('\n')
for day in range(1,30):
	fi.write("day")
	fi.write(str(day))
	fi.write('\n')
	for num in range(1,random.randint(20,200)):
		fi.write(choice(uid))
		fi.write(', ')
		fi.write(str(random.randint(1,60*24)))
		fi.write(', ')
		fi.write(str(random.randint(1,50)))
		fi.write('\n')

fi.close()
