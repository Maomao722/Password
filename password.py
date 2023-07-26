#密碼重試程式
'''
先在程式碼中，設定好密碼 password = 'a123456'
讓使用者(最多輸入3次密碼)
不對的話，就印出"密碼錯誤! 還有_次機會"
對的話，就印出"登入成功!"
'''


x = 3
while True:
	password = input('請輸入密碼: ')

	x = x - 1
	if password == 'a123456':
		print("登入成功")
		break

	if x == 0:
		print("已封鎖")
		break
		
	if password != 'a123456':
		if x == 1:
		    print("你剩餘最後一次機會，再錯將被鎖住")
		else:
			print("密碼錯誤，你還有", x, "次機會")
	    

    
	
	

	

	




