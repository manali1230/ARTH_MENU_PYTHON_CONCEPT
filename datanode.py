def datanode():
	import os
	os.system("espeak-ng 'Path for datanode' -s 140")
	datanode_path = input("\t\t\tPath for datanode:")
	os.system("rm -rf {}".format(datanode_path))
	os.system("mkdir {}".format(datanode_path))
	os.system("espeak-ng 'Enter namenode IP' -s 140")
	namenode_IP = input("\t\t\tEnter namenode IP: ")
	os.system("espeak-ng 'Enter port number of namenode' -s 140")
	namenode_port = input("\t\t\tEnter port number of namenode: ")
	file_hdfs = open("/etc/hadoop/hdfs-site.xml","w")
	hdfs_data =  '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
 
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>dfs.data.dir</name>
<value>{}</value>
</property>
</configuration>\n'''.format(datanode_path)
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
</configuration>\n'''.format(namenode_IP,namenode_port)
	file_core.write(core_data)   
	  


datanode()
