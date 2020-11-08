def Container_Webserver():
	import os
	os.system("yum install httpd -y")
	os.system("yum install net-tools -y")
	os.system("cat >>/var/www/html/index.html")
	os.system("/usr/sbin/httpd")
	os.system("ifconfig")


Container_Webserver()
