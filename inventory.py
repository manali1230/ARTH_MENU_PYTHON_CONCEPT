def inventory():
	import os
	os.system("espeak-ng 'How many target nodes you want to configure ' -s 140")
	count = int(input("How many target nodes you want to configure? "))
	for i in range(0,count):
		inventory_data = open("/root/inventory_file.txt","a")
		os.system("espeak-ng 'Enter The Target Node IP' -s 140")
		ip = input("Enter The Target Node IP : ")
		os.system("espeak-ng 'Enter The Target Node username' -s 140")
		username = input("Enter The Target Node username : ")
		os.system("espeak-ng 'Enter The Target Node password' -s 140")
		password = input("Enter The Target Node password : ")
		os.system("espeak-ng 'Enter The connection protocol' -s 140")
		protocol = input("Enter The connection protocol : ")
		data = '''{} ansible_user={} ansible_ssh_pass={} ansible_connection={}'''.format(ip,username,password,protocol)
		inventory_data.write(data)

inventory()
	
