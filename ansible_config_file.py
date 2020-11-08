def ansible_config():
	import os
	os.system("rm -rf /etc/ansible/ansible.cfg")
	config_file = open("/etc/ansible/ansible.cfg","w")
	data = '''[defaults]
inventory = /root/inventory_file.txt'''
	config_file.write(data)

ansible_config()
	
