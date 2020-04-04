import random
low = input('請輸入最小值:')
high = input('請輸入最大值:')
low = int(low)
high = int(high)
r = random.randint(low, high)
count = 0

while True:
	count += 1
	num = input('請猜數字:')
	num = int(num)
	if num == r:
		print('恭喜你答對了!')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('比實際數字大')
	elif num < r:
		print('比實際數字小')
	print('這是你猜的第', count, '次')