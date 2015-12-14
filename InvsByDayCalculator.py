import datetime,time;

year=2015
month=6
day=22
invsDays=64
invsRatio=0.096
invsFund = 2000

arrInvsPayBack = []

#array arrInvsPayPlan={}

invsDate = datetime.date(year,month,day)
finiDate = invsDate + datetime.timedelta(invsDays)
firstPayDate = datetime.date(year,month+1,20)

print '投资开始时间:', invsDate, ';投资结束时间:', finiDate, ";首次收益时间:", firstPayDate

totalPayBack = invsFund * invsRatio * invsDays / 365

## 判断是否一次性派息
payTimes = (finiDate.year - firstPayDate.year)*12 + finiDate.month - firstPayDate.month + 1
if payTimes == 1:
	#结构化业务数据后放入容器中，便于迭代遍历
	arrInvsPayBack.append(finiDate)
	arrInvsPayBack.append(invsDays)
	arrInvsPayBack.append(totalPayBack)
	print '一次性派息,派息日: ', finiDate, ',计息天数:', invsDays, ',利息：', totalPayBack
else:
	#print payTimes,'程序猿哥哥看片去了...'
	lastPayDate = invsDate  
	for x in range(payTimes-1):
		# 计算派息日&派息金额

		# timedelta可以查看：天数(days)，秒数 (seconds)
		#payDate = firstPayDate + datetime.timedelta(months=x)
		if firstPayDate.month+x <=12:
			payDate = datetime.date(firstPayDate.year,firstPayDate.month+x,20)
		else:
			payDate = datetime.date(firstPayDate.year+1,firstPayDate.month+x-12,20)
		payDays = (payDate - lastPayDate).days
		payBack = invsFund * invsRatio * payDays / 365
		arrInvsPayBack.append(payDate)
		arrInvsPayBack.append(payDays)
		arrInvsPayBack.append(payBack)
		#print x, payDate, payBack
		lastPayDate = payDate
		
	# 最后一期派息
	payDays = (finiDate - lastPayDate).days
	payBack = invsFund * invsRatio * payDays / 365
	arrInvsPayBack.append(finiDate)
	arrInvsPayBack.append(payDays)
	arrInvsPayBack.append(payBack)

	len = len(arrInvsPayBack)
	n = 0
	while n<len/3:
		print n, '多次派息,派息日: ', arrInvsPayBack[3*n], ',计息天数:', arrInvsPayBack[3*n+1], ',利息：', arrInvsPayBack[3*n+2] 
		n = n + 1
	print '投资本金:', invsFund, ';累计总收益:',  totalPayBack