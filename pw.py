password = 'a123456'
i = 3 #剩余机会
while True:
	pwd = input('请输入你的密码：')
	if pwd == password:
		print('登陆成功!')
		break
	else:
		i = i - 1
		print('密码错误！还有' , i ,'次机会')
		if i == 0:
			break


