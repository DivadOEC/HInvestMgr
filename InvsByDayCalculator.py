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

print 'Ͷ�ʿ�ʼʱ��:', invsDate, ';Ͷ�ʽ���ʱ��:', finiDate, ";�״�����ʱ��:", firstPayDate

totalPayBack = invsFund * invsRatio * invsDays / 365

## �ж��Ƿ�һ������Ϣ
payTimes = (finiDate.year - firstPayDate.year)*12 + finiDate.month - firstPayDate.month + 1
if payTimes == 1:
	#�ṹ��ҵ�����ݺ���������У����ڵ�������
	arrInvsPayBack.append(finiDate)
	arrInvsPayBack.append(invsDays)
	arrInvsPayBack.append(totalPayBack)
	print 'һ������Ϣ,��Ϣ��: ', finiDate, ',��Ϣ����:', invsDays, ',��Ϣ��', totalPayBack
else:
	#print payTimes,'����Գ��翴Ƭȥ��...'
	lastPayDate = invsDate  
	for x in range(payTimes-1):
		# ������Ϣ��&��Ϣ���

		# timedelta���Բ鿴������(days)������ (seconds)
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
		
	# ���һ����Ϣ
	payDays = (finiDate - lastPayDate).days
	payBack = invsFund * invsRatio * payDays / 365
	arrInvsPayBack.append(finiDate)
	arrInvsPayBack.append(payDays)
	arrInvsPayBack.append(payBack)

	len = len(arrInvsPayBack)
	n = 0
	while n<len/3:
		print n, '�����Ϣ,��Ϣ��: ', arrInvsPayBack[3*n], ',��Ϣ����:', arrInvsPayBack[3*n+1], ',��Ϣ��', arrInvsPayBack[3*n+2] 
		n = n + 1
	print 'Ͷ�ʱ���:', invsFund, ';�ۼ�������:',  totalPayBack