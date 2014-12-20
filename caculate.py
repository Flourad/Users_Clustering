#-*-coding: utf-8 -*-

out = {}
out['xiang'] = [7.58, 30, 10.27, 5.27, 4.5, 3.86, 3.1, 4.41, 1.27, 6.19, 5.66]
out['gong'] = [7.5, 30, 6.55, 2.68, 4.5, 6.25, 3.1, 5.7, 4.69, 3.95]
out['liu'] = [4.89, 30, 3.06, 2.68, 3.25, 6.67, 3.1, 5.7, 3.76, 6.19]
out['zhou'] = [7.32, 30, 5.12, 2.68, 7.23, 3.1, 5.7, 1.99, 7.88]

pay = {}
pay['xiang'] = [27.3, 120, 9, 10.02, 1.27, 16.63]
pay['gong'] = [24.01]
pay['liu'] = [25, 13.31, 3.25, 2.2, 21.52]
pay['zhou'] = [23.71]


out_xiang = sum(out['xiang'])
out_gong = sum(out['gong'])
out_liu = sum(out['liu'])
out_zhou = sum(out['zhou'])

pay_xiang = sum(pay['xiang'])
pay_gong = sum(pay['gong'])
pay_liu = sum(pay['liu'])
pay_zhou = sum(pay['zhou'])

print 'out xiang:', out_xiang
print 'out gong:', out_gong
print 'out liu:', out_liu
print 'out zhou:', out_zhou

print 'pay xiang:', pay_xiang
print 'pay gong:', pay_gong
print 'pay liu:', pay_liu
print 'pay zhou:', pay_zhou

print pay_xiang - out_xiang
print pay_gong - out_gong
print pay_liu - out_liu
print pay_zhou - out_zhou
