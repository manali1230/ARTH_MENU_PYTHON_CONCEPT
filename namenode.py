def namenode():
	import os
	os.system("espeak-ng 'Give details about namenode' -s 140")
	namenode_ip = input("\t\t\tGive IP of namenode:")
	os.system("espeak-ng 'Give Path for namenode service' -s 140")
	namenode_path = input("\t\t\tGive Path for namenode service:")
	os.system("espeak-ng 'Give Port Number for namenode service' -s 140")
	namenode_port = input("\t\t\tGive Port Number for namenode service:")
	os.system("rm -rf {}".format(namenode_path))	
	os.system("mkdir {}".format(namenode_path))
	file_hdfs = open("/etc/hadoop/hdfs-site.xml","w")
	hdfs_data =  '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
 
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>dfs.name.dir</name>
<value>{}</value>
</property>
</configuration>\n'''.format(namenode_path)
	file_hdfs.write(hdfs_data)

	file_core = open("/etc/hadoop/core-site.xml", "w")
	core_data = '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:{}</value>
</property>
</configuration>\n'''.format(namenode_ip,namenode_port)
	file_core.write(core_data)   




namenode()
