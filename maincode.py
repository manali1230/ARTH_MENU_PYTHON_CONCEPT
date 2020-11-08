import os
import pyttsx3 as pt
import webbrowser as wp
import time

'''engine = pt.init()  # object creation
voices = engine.getProperty('voices')  # getting details of current voice
#engine.setProperty('voice', voices[0].id)  # changing index, changes voices. 0 for male
engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female
newVoiceRate = 150
engine.setProperty('rate',newVoiceRate)'''
os.system("tput setaf 3")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\t\t\t\t\tWELCOME\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

os.system('espeak-ng "welcome i am grafitti i am especially programmed to perform AWS , Docker ,Linux ,Hadoop , Ansible task" -s 140')

Technology = ["AWS","Docker","Linux","Hadoop","Ansible","Exit"]
os.system("tput setaf 4")
for j in range(0,6):
	print("\t\t\t\t",j+1,". ",Technology[j])
	if j==0:
		os.system("espeak-ng 'press 1 For AWS' -s 150")
	elif j==1:
		os.system("espeak-ng 'press 2 for Docker' -s 150")
	elif j==2:
		os.system("espeak-ng 'press 3 for Linux' -s 150")
	elif j==3:
		os.system("espeak-ng 'press 4 for Hadoop' -s 150")
	elif j==4:
		os.system("espeak-ng 'press 5 for Ansible' -s 150")
	else:
		os.system("espeak-ng 'press 6 to exit'")
		
while True:
	os.system("tput setaf 6")
	os.system("espeak-ng 'Enter Your Technology' -s 150")
	select_tech=int(input("Enter Your Technology : "))
	if select_tech == 1:
		flag=0
		os.system('espeak-ng "welcome to AWS Technology" -s 140')
		os.system("clear")
		print("\n\n\n\n\n\n\n")
		tasks=["Configure AWS","Create a Key","Create a Security Group","Launch an Instance","Login Into The Instance","Terminate the Instance","Delete a Security Group","Delete the Key Pair","Create EBS Volume","Attach EBS Volume to EC2 Instance","Delete a Volume","Create S3 Bucket","Upload a Picture on S3","Create CloudFront","Create a Snapshot","Delete The Snapshots","Exit"]
		for i in range(0,len(tasks)):
			print("\t\t\t\t",i+1,". ",tasks[i])
			if i==0:
				os.system("espeak-ng 'press 1 to configure AWS' -s 150")
			elif i==1:
				os.system("espeak-ng 'press 2 to create a key' -s 150")
			elif i==2:
				os.system("espeak-ng 'press 3 to create a Security Group' -s 150")
			elif i==3:
				os.system("espeak-ng 'press 4 to Launch an Instance' -s 150")
			elif i==4:
				os.system("espeak-ng 'press 5 to Login Into The Instance' -s 150")
			elif i==5:
				os.system("espeak-ng 'press 6 to Terminate the Instance' -s 150")
			elif i==6:
				os.system("espeak-ng 'press 7 to Delete a Security Group' -s 150")
			elif i==7:
				os.system("espeak-ng 'press 8 to Delete the Key Pair' -s 150")
			elif i==8:
				os.system("espeak-ng 'press 9 to Create EBS Volume' -s 150")
			elif i==9:
				os.system("espeak-ng 'press 10 to Attach EBS Volume to EC2 Instance' -s 150")
			elif i==10:
				os.system("espeak-ng 'press 11 to Delete a Volume' -s 150")
			elif i==11:
				os.system("espeak-ng 'press 12 to Create S3 Bucket' -s 150")
			elif i==12:
				os.system("espeak-ng 'press 13 to Upload a Picture on S3' -s 150")
			elif i==13:
				os.system("espeak-ng 'press 14 to Create CloudFront' -s 150")
			elif i==14:
				os.system("espeak-ng 'press 15 to Create a Snapshot'")
			elif i==15:
				os.system("espeak-ng 'press 16 to Delete The Snapshot'")
			elif i==16:
				os.system("espeak-ng 'press 17 to Exit'")
		    #espeak-ng("press {} for {}".format(i+1,tasks[i]))
		    
		while True:
			os.system("tput setaf 3")
			if flag==1:
				for i in range(0,len(tasks)):
					print("\t\t\t\t",i+1,". ",tasks[i])
			os.system("espeak-ng 'press a number'")
			n = int(input("press a number : "))
			if n==1:
				os.system("aws configure")
				os.system("espeak-ng 'AWS configured'")
				wp.open("https://ap-south-1.console.aws.amazon.com/console/home?region=ap-south-1")
				flag=1
				time.sleep(5)
			elif n==2:
				os.system("espeak-ng 'Enter Your Key Name'")
				key = input("Enter Your Key Name : ")
				os.system('aws ec2 create-key-pair --key-name {} --query "KeyMaterial" --output text > {}.pem'.format(key,key))
				os.system("espeak-ng 'Your Key is successfully created'")
				wp.open("https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#KeyPairs:")
				flag=1
				time.sleep(10)
			elif n==3:
				os.system("espeak-ng 'Enter Your Security Group Name'")
				sg_name = input("Enter Your Security Group Name: ")
				os.system("espeak-ng 'Enter Your description'")
				description = input("Enter Your description : ")
				os.system("espeak-ng 'Enter Your VPC'")
				vpc_name = input("Enter Your VPC Name : ")
				os.system("espeak-ng 'Enter Your Inbound rule protocol'")
				protocol = input("Enter Your Inbound Rule Protocol : ")
				os.system("espeak-ng 'Enter Your port'")
				port = input("Enter Your Port : ")
				os.system("espeak-ng 'Enter Your CIDR'")
				cidr = input("Enter Your CIDR : ")
				os.system('aws ec2 create-security-group --group-name {} --description "{}" --vpc-id {}'.format(sg_name,description,vpc_name))
				os.system("aws ec2 authorize-security-group-ingress --group-name {}  --protocol {} --port {} --cidr {}".format(sg_name,protocol,port,cidr))
				os.system("espeak-ng 'Your Security Group is successfully created'")
				wp.open("https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#SecurityGroups:")
				flag=1
				time.sleep(10)
			elif n==4:
				os.system("espeak-ng 'Enter Your Amazon Machine Image ID'")
				ami = input("Enter Your AMI ID: ")
				os.system("espeak-ng 'Enter the number of instance you want to launch'")
				count = int(input("Enter the number of instance you want to launch : "))
				os.system("espeak-ng 'Enter Your Instance Type'")
				instance_type = input("Enter Your instance type : ")
				os.system("espeak-ng 'Enter Your Key Name'")
				key = input("Enter Your Key Name : ")
				os.system("espeak-ng 'Enter Your Security Group ID'")
				sg_id = input("Enter Your Security Group ID : ")
				os.system("espeak-ng 'Enter Your Subnet ID'")
				subnet_id = input("Enter Your Subnet ID : ")
				os.system('aws ec2 run-instances --image-id {} --count {} --instance-type {} --key-name {} --security-group-ids {} --subnet-id {}'.format(ami,count,instance_type,key,sg_id,subnet_id))
				os.system("espeak-ng 'Your instance is succesfuuly launched'")
				wp.open("https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#Instances:")
				flag=1
				time.sleep(10)
			elif n==5:
				os.system("espeak-ng 'Enter Your user name'")
				username = input("Enter Your User Name : ")
				os.system("espeak-ng 'Enter Your Key name'")
				key = input("Enter Your Key Name : ")
				os.system("espeak-ng 'Enter Your Instance IP'")
				instance_ip = input("Enter Your Instance IP: ")
				os.system("espeak-ng 'Welcome to Your Instance'")
				os.system("ssh -l {} -i {}.pem {}".format(username,key,instance_ip))
				flag=1
				time.sleep(3)
			elif n==6:
				os.system("espeak-ng 'Enter Your instance ID'")
				instance_id = input("Enter Your Instance ID : ")
				os.system("aws ec2 terminate-instances --instance-ids {}".format(instance_id))
				os.system("espeak-ng 'Your instance is succesfully Terminated'")
				wp.open("https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#Instances:")
				flag=1
				time.sleep(10)
			elif n==7:
				os.system("espeak-ng 'Enter Your Security Group name'")
				sg_name = input("Enter Your Security Group name : ")
				os.system("aws ec2 delete-security-group --group-name {}".format(sg_name))
				os.system("espeak-ng 'Your Security Group is successfully deleted'")
				wp.open("https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#SecurityGroups:")
				flag=1
				time.sleep(10)
			elif n==8:
				os.system("espeak-ng 'Enter Your Key Name'")
				key = input("Enter Your Key Name : ")
				os.system("aws ec2 delete-key-pair --key-name {}".format(key))
				os.system("rm {}.pem".format(key))
				os.system("espeak-ng 'Your Key is successfully Deleted'")
				wp.open("https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#KeyPairs:")
				flag=1
				time.sleep(10)
			elif n==9:
				os.system("espeak-ng 'Enter Your Availability Zone'")
				az = input("Enter Your Availability Zone : ")
				os.system("espeak-ng 'Enter Your Volume Type'")
				volume_type = input("Enter Your Volume Type : ")
				os.system("espeak-ng 'Enter Your Size'")
				size = input("Enter Your Size : ")
				os.system("aws ec2 create-volume --availability-zone {}  --volume-type {}  --size {}".format(az,volume_type,size))
				wp.open("https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#Volumes:")
				time.sleep(10)
				flag=1
			elif n==10:
				os.system("espeak-ng 'Enter Your Volume ID'")
				volume_id = input("Enter Your Volume ID : ")
				os.system("espeak-ng 'Enter Your Instance ID'")
				instance_id = input("Enter Your Instance ID : ")
				os.system("espeak-ng 'Enter Your Device'")
				device = input("Enter Your Device : ")
				os.system("aws ec2 attach-volume --volume-id {} --instance-id {} --device {}".format(volume_id,instance_id,device))
				#aws ec2 attach-volume --volume-id vol-0509b3cb61afb5f42 --instance-id i-071d7b410c0f5a9d6 --device /dev/sdf
				wp.open("https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#Volumes:")
				flag=1
				os.system("espeak-ng 'Your Volume is succesfully Attached'")
				time.sleep(10)
			elif n==11:
				os.system("espeak-ng 'Enter Your Volume ID'")
				volume_id = input("Enter Your Volume ID : ")
				os.system("aws ec2 detach-volume --volume-id {}".format(volume_id))
				time.sleep(5)
				os.system("aws ec2 delete-volume --volume-id {}".format(volume_id))
				wp.open("https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#Volumes:")
				flag=1
				os.system("espeak-ng 'Your Volume is succesfully Deleted'")
				time.sleep(10)
			elif n==12:
				os.system("espeak-ng 'Enter Your Unique Bucket Name'")
				bucket = input("Enter Your Unique Bucket Name : ")
				os.system("espeak-ng 'Enter Your Region'")
				region = input("Enter Your Unique Region : ")
				os.system("espeak-ng 'Enter Your Location Constraint'")
				location_constraint = input("Enter Your Unique Location Constraint : ")
				os.system("aws s3api create-bucket --bucket {} --region {} --create-bucket-configuration LocationConstraint={}".format(bucket,region,location_constraint))
				# aws s3api create-bucket --bucket manalibucket --region ap-south-1 --create-bucket-configuration LocationConstraint=ap-south-1
				wp.open("https://s3.console.aws.amazon.com/s3/home?region=ap-south-1#")
				flag=1
				os.system("espeak-ng 'Your Bucket is succesfully created'")
				time.sleep(10)
			elif n==13:
				os.system("espeak-ng 'Enter Your Unique Bucket Name'")
				bucket = input("Enter Your Unique Bucket Name : ")
				os.system("espeak-ng 'Enter Your Key'")
				key = input("Enter Your Unique Key : ")
				os.system("aws s3 sync '/root/AWS' s3://{}".format(bucket))
				os.system("aws s3api put-object-acl --bucket {} --key {} --acl public-read".format(bucket,key))
				flag=1
				time.sleep(10)
			elif n==14:
				os.system("espeak-ng 'Enter Your Unique Bucket Name'")
				bucket = input("Enter Your Unique Bucket Name : ")
				os.system("espeak-ng 'Enter Your Default root object'")
				root_object = input("Enter Your Default root object : ")
				os.system("aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com --default-root-object {}".format(bucket,root_object))
				wp.open("https://console.aws.amazon.com/cloudfront/home?region=ap-south-1#")
				flag=1
				os.system("espeak-ng 'Your CloudFront is succesfully created'")
				time.sleep(10)
			elif n==15:
				os.system("espeak-ng 'Enter Your Volume ID'")
				volume_id = input("Enter Your Volume ID : ")
				os.system("espeak-ng 'Enter Your Description'")
				description = input("Enter Your Description : ")
				os.system('aws ec2 create-snapshot --volume-id {} --description "{}"'.format(volume_id,description))
				wp.open("https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#Snapshots:sort=snapshotId")
				flag=1
				os.system("espeak-ng 'Your snapshot is succesfully created'")
				time.sleep(10)
			elif n==16:
				os.system("espeak-ng 'Enter Your Snapshot ID'")
				snapshot_id = input("Enter Your Snapshot ID : ")
				os.system('aws ec2 delete-snapshot --snapshot-id {}'.format(snapshot_id))
				wp.open("https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#Snapshots:sort=snapshotId")
				flag=1
				os.system("espeak-ng 'Your snapshot is succesfully Deleted'")
				time.sleep(10)
			elif n==17:
				os.system("espeak-ng 'Thank You See You Soon'")
				os.system("clear")
				print("\n\n\n\n\n\n\n\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\t\t\t\t\tSAYONARA\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
				flag=0
				time.sleep(4)
				break
			else:
				os.system("tput setaf 1")
				os.system("espeak-ng 'Enter Correct number'")
	elif select_tech == 2:
			flag=0
			os.system("tput setaf 2")
			os.system('espeak-ng "welcome to Docker Technology" -s 140')
			os.system("clear")
			print("\n\n\n\n\n\n\n")
			tasks=["Start docker","Status of docker","Install an OS through docker image","Start Docker Container","Stop Docker Container","Copy file on docker container","Copy files from docker container","check docker logs of particular container","Execute the container OS","Remove the container","Remove all the containers","show all images present on the system","Exit"]
			for i in range(0,len(tasks)):
				print("\t\t\t\t",i+1,". ",tasks[i])
				if i==0:
					os.system("espeak-ng 'press 1 to Start docker' -s 150")
				elif i==1:
					os.system("espeak-ng 'press 2 to Status of docker' -s 150")
				elif i==2:
					os.system("espeak-ng 'press 3 to Install an OS through docker image' -s 150")
				elif i==3:
					os.system("espeak-ng 'press 4 to Start Docker Container' -s 150")
				elif i==4:
					os.system("espeak-ng 'press 5 to  Stop Docker Container' -s 150")
				elif i==5:
					os.system("espeak-ng 'press 6 to Copy file on docker container' -s 150")
				elif i==6:
					os.system("espeak-ng 'press 7 to Copy file from docker container' -s 150")
				elif i==7:
					os.system("espeak-ng 'press 8 to check docker logs of particular container' -s 150")
				elif i==8:
					os.system("espeak-ng 'press 9 to Execute the container OS' -s 140")
				elif i==9:
					os.system("espeak-ng 'press 10 to Remove the container '  -s 140")
				elif i==10:
					os.system("espeak-ng 'press 11 to Remove all the containers'  -s 140")
				elif i==11:
					os.system("espeak-ng 'press 12 to show all the images'  -s 140")
				elif i==12:
					os.system("espeak-ng 'press 13 to Exit'")
			
			while True:
				os.system("tput setaf 4")
				os.system("espeak-ng 'want to work on local system or remote PC or want to exit' -s 150")
				choice = input("want to work on local system or remote PC or want to exit : ")
			
				if choice == "local":
					while True :
						if flag ==1:
							for i in range(0,len(tasks)):
								print("\t\t\t\t",i+1,". ",tasks[i])
						os.system("espeak-ng 'Enter Your Choice' -s 150")
						docker = int(input("Enter your Choice : "))
						if docker==1:
							os.system("setenforce 0")
							os.system("systemctl start docker")
							os.system("espeak-ng 'docker Started' -s 150")
							flag=1
							time.sleep(5)
						elif docker ==2:
							os.system("setenforce 0")
							os.system("systemctl status docker")
							os.system("espeak-ng 'docker status shown' -s 150")
							flag=1
							time.sleep(5)
						elif docker ==3:
							os.system("espeak-ng 'Enter the Container Name' -s 150")
							name = input("Enter the Container Name : ")
							os.system("espeak-ng 'Enter the OS you want to install' -s 150")
							os_container = input("Enter the OS you want to install : ")
							os.system("espeak-ng 'Enter the version of OS ' -s 150")
							version = input("Enter the version of OS : ")
							os.system("setenforce 0")
							os.system("docker run -it --name {} {}:{}".format(name,os_container,version))
							flag=1
							time.sleep(5)
						elif docker ==4:
							os.system("espeak-ng 'Enter the Container Name' -s 150")
							name = input("Enter the Container Name : ")
							os.system("setenforce 0")
							os.system("docker start {}".format(name))
							os.system("docker ps")
							flag=1
							time.sleep(5)
						elif docker ==5:
							os.system("espeak-ng 'Enter the Container Name' -s 150")
							name = input("Enter the Container Name : ")
							os.system("docker stop {}".format(name))
							os.system("docker ps")
							flag=1
							time.sleep(5)
						elif docker ==6:
							os.system("espeak-ng 'Enter the file Path' -s 150")
							local_path = input("Enter the file path: ")
							os.system("espeak-ng 'Enter the Container Name' -s 150")
							name = input("Enter the Container name : ")
							os.system("espeak-ng 'Enter the Container path' -s 150")
							container_path = input("Enter the Container Name : ")
							os.system("docker cp {} {}:/{}".format(local_path,name,container_path))
							flag=1
							time.sleep(5)
						elif docker ==7:
							os.system("espeak-ng 'Enter the file Path' -s 150")
							local_path = input("Enter the file path: ")
							os.system("espeak-ng 'Enter the Container Name' -s 150")
							name = input("Enter the Container name : ")
							os.system("espeak-ng 'Enter the Container path' -s 150")
							container_path = input("Enter the Container path : ")
							os.system("docker cp {}:/{} /{}".format(name,container_path,local_path))
							flag=1
							time.sleep(5)
						elif docker ==8:
							os.system("espeak-ng 'Enter the Container Name' -s 150")
							name = input("Enter the Container Name : ")
							os.system("setenforce 0")
							os.system("docker logs {}".format(name))
							flag=1
							time.sleep(5)
						elif docker ==9 : 
							os.system("espeak-ng 'Enter the Container Name' -s 150")
							name = input("Enter the Container Name : ")
							os.system("setenforce 0")
							os.system("docker exec -it {} bash".format(name))
							flag=1
							time.sleep(5)
						elif docker ==10 : 
							os.system("espeak-ng 'Enter the Container Name' -s 150")
							name = input("Enter the Container Name : ")
							os.system("setenforce 0")
							os.system("docker stop {}".format(name))
							os.system("docker rm {}".format(name))
							os.system("docker ps")
							flag=1
							time.sleep(5)
						elif docker ==11 : 
							os.system("setenforce 0")
							os.system("docker rm `docker ps -q -a`")
							os.system("docker ps")
							os.system("espeak-ng 'Successfully removed' -s 150")
							flag=1
							time.sleep(5)
						elif docker ==12 : 
							os.system("setenforce 0")
							os.system("docker images")
							os.system("espeak-ng 'See the images' -s 150")
							flag=1
							time.sleep(5)
						elif docker==13:
							os.system("espeak-ng 'Thank You See You Soon' -s 140 ")
							os.system("clear")
							print("\n\n\n\n\n\n\n\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\t\t\t\t\tSAYONARA\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
							flag=0
							time.sleep(5)
							break
				elif choice =="remote":
					os.system("tput setaf 6")
					os.system("espeak-ng 'Enter Your IP of remote system' -s 150")
					ip = input("Enter your IP remote system : ")
					os.system("ssh {} setenforce 0".format(ip))
					while True :
						if flag ==1:
							for i in range(0,len(tasks)):
								print("\t\t\t\t",i+1,". ",tasks[i])
						os.system("espeak-ng 'Enter Your Choice' -s 150")
						docker = int(input("Enter your Choice : "))
						if docker==1:
							os.system("ssh {} systemctl start docker".format(ip))
							os.system("espeak-ng 'docker Started' -s 150")
							flag=1
							time.sleep(5)
						elif docker ==2:
							os.system("ssh {} systemctl status docker".format(ip))
							os.system("espeak-ng 'docker status shown' -s 150")
							flag=1
							time.sleep(5)
						elif docker ==3:
							os.system("espeak-ng 'Enter the Container Name' -s 150")
							name = input("Enter the Container Name : ")
							os.system("espeak-ng 'Enter the OS you want to install' -s 150")
							os_container = input("Enter the OS you want to install : ")
							os.system("espeak-ng 'Enter the version of OS ' -s 150")
							version = input("Enter the version of OS : ")
							os.system("ssh {} docker run -i --name {} {}:{}".format(ip,name,os_container,version))
							flag=1
							time.sleep(5)
						elif docker ==4:
							os.system("espeak-ng 'Enter the Container Name' -s 150")
							name = input("Enter the Container Name : ")
							os.system("ssh {} docker start {}".format(ip,name))
							os.system("ssh {} docker ps".format(ip))
							flag=1
							time.sleep(5)
						elif docker ==5:
							os.system("espeak-ng 'Enter the Container Name' -s 150")
							name = input("Enter the Container Name : ")
							os.system("ssh {} docker stop {}".format(ip,name))
							os.system("ssh {} docker ps".format(ip))
							flag=1
							time.sleep(5)
						elif docker ==6:
							os.system("espeak-ng 'Enter the file Path' -s 150")
							local_path = input("Enter the file path: ")
							os.system("espeak-ng 'Enter the Container Name' -s 150")
							name = input("Enter the Container name : ")
							os.system("espeak-ng 'Enter the Container path' -s 150")
							container_path = input("Enter the Container path : ")
							os.system("ssh {} docker cp {} {}:/{}".format(ip,local_path,name,container_path))
							flag=1
							time.sleep(5)
						elif docker ==7:
							os.system("espeak-ng 'Enter the file Path' -s 150")
							local_path = input("Enter the file path: ")
							os.system("espeak-ng 'Enter the Container Name' -s 150")
							name = input("Enter the Container path : ")
							os.system("espeak-ng 'Enter the Container path' -s 150")
							container_path = input("Enter the Container Name : ")
							os.system("ssh {} docker cp {}:/{} /{}".format(ip,name,container_path,local_path))
							flag=1
							time.sleep(5)
						elif docker ==8:
							os.system("espeak-ng 'Enter the Container Name' -s 150")
							name = input("Enter the Container Name : ")
							os.system("ssh {} docker logs {}".format(ip,name))
							flag=1
							time.sleep(5)
						elif docker ==9 : 
							os.system("espeak-ng 'Enter the Container Name' -s 150")
							name = input("Enter the Container Name : ")
							os.system("ssh {} docker exec -i {} bash".format(ip,name))
							flag=1
							time.sleep(5)
						elif docker ==10 : 
							os.system("espeak-ng 'Enter the Container Name' -s 150")
							name = input("Enter the Container Name : ")
							os.system("ssh {} docker stop {}".format(ip,name))
							os.system("ssh {} docker rm {}".format(ip,name))
							os.system("ssh {} docker ps".format(ip))
							flag=1
							time.sleep(5)
						elif docker ==11 : 
							os.system("ssh {} docker rm `docker ps -q -a`".format(ip))
							os.system("ssh {} docker ps".format(ip))
							os.system("espeak-ng 'Successfully removed' -s 150")
							flag=1
							time.sleep(5)
						elif docker ==12 : 
							os.system("ssh {} docker images".format(ip))
							os.system("espeak-ng 'See all the images' -s 150")
							flag=1
							time.sleep(5)
						elif docker==13:
							os.system("espeak-ng 'Thank You See You Soon' -s 140 ")
							os.system("clear")
							print("\n\n\n\n\n\n\n\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\t\t\t\t\tSAYONARA\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
							flag=0
							time.sleep(5)
							break
				else:
					os.system("tput setaf 3")
					os.system("espeak-ng 'Thank You See You Soon' -s 140 ")
					os.system("clear")
					print("\n\n\n\n\n\n\n\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\t\t\t\t\tSAYONARA\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
					break

	elif select_tech == 3:
			os.system("tput setaf 2")
			os.system('espeak-ng "welcome to Linux Technology" -s 140')
			os.system("clear")
			print("\n\n\n\n\n\n\n")
			while True:
				flag=0
				os.system("espeak-ng 'want to work on local or remote desktop or exit' -s 150")
				wish = input("want to work on local or remote desktop or exit: ")
				if wish == "local":
					tasks = ["run date command","run cal command","run python","install a service","start a service","status of a service","Configure Webserver","create LVM","rpm query command","yum whatprovides command","Exit"]
					for i in range(0,len(tasks)):
						print("\t\t\t\t",i+1,". ",tasks[i])
						if i==0:
							os.system("espeak-ng 'press 1 to run date command' -s 150")
						elif i==1:
							os.system("espeak-ng 'press 2 to run cal command' -s 150")
						elif i==2:
							os.system("espeak-ng 'press 3 to run python' -s 150")
						elif i==3:
							os.system("espeak-ng 'press 4 to install a service' -s 150")
						elif i==4:
							os.system("espeak-ng 'press 5 to start a service' -s 150")
						elif i==5:
							os.system("espeak-ng 'press 6 to status of a service' -s 150")
						elif i==6:
							os.system("espeak-ng 'press 7 to Configure Webserver' -s 150")
						elif i==7:
							os.system("espeak-ng 'press 8 to create LVM' -s 150")
						elif i==8:
							os.system("espeak-ng 'press 9 to rpm query command' -s 140 ")
						elif i==9:
							os.system("espeak-ng 'press 10 to yum whatprovides command' -s 140 ")
						elif i==10:
							os.system("espeak-ng 'press 11 to Exit'")
					while True:
						os.system("tput setaf 4")
						if flag==1:
							for i in range(0,len(tasks)):
								print("\t\t\t\t",i+1,". ",tasks[i])
						os.system("espeak-ng 'enter your  Choice' -s 140 ")
						linux=int(input("Enter Your Choice : "))
						if linux==1:
							os.system("espeak-ng `date` -s 150")
							os.system("date")
							flag=1
							time.sleep(5)
						elif linux==2:
							os.system("espeak-ng `cal` -s 140 ")
							os.system("cal")
							flag=1
							time.sleep(5)
						elif linux==3:
							os.system("espeak-ng 'entered python 3 ' -s 140 ")
							os.system("python3")
							os.system("espeak-ng 'closed python 3 ' -s 140 ")
							flag=1
							time.sleep(5)
						elif linux==4:
							os.system("espeak-ng 'enter your service name' -s 140 ")
							service=input("Enter Your service name : ")
							os.system("yum install {} -y".format(service))
							os.system("{} installed".format(service))
							flag=1
							time.sleep(5)
						elif linux==5:
							os.system("espeak-ng 'enter your service name' -s 140 ")
							service=input("Enter Your service name : ")
							os.system("systemctl start {}".format(service))
							os.system("{} started".format(service))
							flag=1
							time.sleep(5)
						elif linux==6:
							os.system("espeak-ng 'enter your service name' -s 140 ")
							service=input("Enter Your service name : ")
							os.system("systemctl status {}".format(service))
							os.system("{} status".format(service))
							flag=1
							time.sleep(5)
						elif linux==7:
							os.system("yum install httpd -y")
							os.system("systemctl start httpd")
							os.system("espeak-ng 'enter your file name' -s 140 ")
							file_name=input("Enter Your file name : ")
							os.system("cat > /var/www/html/{}.html".format(file_name))
							os.system("setenforce 0")
							os.system("systemctl stop firewalld")
							os.system("ifconfig")
							flag=1
							time.sleep(5)
						elif linux==8:
							os.system("espeak-ng 'how many Physical Volume you want to create' -s 140  ")
							count = int(input("how many Physical Volume you want to create :"))
							os.system("fdisk -l")
							for i in range(0,count):
								os.system("espeak-ng 'enter your device name'")
								device=input("Enter Your device name : ")
								os.system("pvcreate {}".format(device))
								os.system("pvdisplay {}".format(device))
							os.system("espeak-ng 'Now i will create volume group' -s 140  ")
							os.system("espeak-ng 'Enter the group name' -s 140  ")
							group = input("Enter the group name :")
							os.system("espeak-ng 'Enter the device name with spaces' -s 140 ")
							device = input("Enter the device name with spaces :")
							os.system("vgcreate {} {}".format(group,device))
							os.system("vgdisplay {}".format(group))
							os.system("espeak-ng 'Now i will create logical volume' -s 140  ")
							os.system("espeak-ng 'Enter the size' -s 140  ")
							size = input("Enter the size :")
							os.system("espeak-ng 'Enter the logical volume name' -s 140  ")
							lv_name = input("Enter the logical volume name :")
							os.system("espeak-ng 'Enter the volume group name' -s 140  ")
							vg_name = input("Enter the volume group name:")
							os.system("lvcreate --size {} --name {} {}".format(size,lv_name,vg_name))
							os.system('espeak-ng  "Partition Created"  -s 140')
							os.system("mkfs.ext4 /dev/{}/{}".format(vg_name,lv_name))
							path = input("enter the path where you want to mount it :")
							os.system("mkdir /{}".format(path))
							os.system("mount /dev/{}/{} /{}".format(vg_name,lv_name,path))
							os.system("df -h")
							flag=1
							time.sleep(5)
						elif linux==9:
							os.system("espeak-ng 'query for a software' -s 140  ")
							service = input("query for a software :")
							os.system("rpm -q {}".format(service))
							flag=1
						elif linux==10:
							os.system("espeak-ng 'let us ask yum' -s 140 ")
							service = input("enter your hint :")
							os.system("yum whatprovides {}".format(service))
							flag=1
							time.sleep(5)
						elif linux==11:
							os.system("espeak-ng 'Thank You See You Soon' -s 140 ")
							os.system("clear")
							print("\n\n\n\n\n\n\n\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\t\t\t\t\tSAYONARA\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
							flag=0
							time.sleep(5)
							break

				elif wish == "remote":
					os.system("tput setaf 6")
					flag = 0
					os.system("espeak-ng 'Enter the IP of Remote OS' -s 150")
					ip=input("Enter the IP of Remote OS : ")
					tasks = ["run date command remotely","run cal command remotely","run python remotely","install a service remotely","start a service remotely","status of a service remotely","Configure Webserver remotely","create LVM remotely","rpm query command remotely","yum whatprovides command remotely","Exit"]
					for i in range(0,len(tasks)):
						print("\t\t\t\t",i+1,". ",tasks[i])
						if i==0:
							os.system("espeak-ng 'press 1 to run date command remotely' -s 150")
						elif i==1:
							os.system("espeak-ng 'press 2 to run cal command remotely' -s 150")
						elif i==2:
							os.system("espeak-ng 'press 3 to run python remotely' -s 150")
						elif i==3:
							os.system("espeak-ng 'press 4 to install a service remotely' -s 150")
						elif i==4:
							os.system("espeak-ng 'press 5 to start a service remotely' -s 150")
						elif i==5:
							os.system("espeak-ng 'press 6 to status of a service remotely' -s 150")
						elif i==6:
							os.system("espeak-ng 'press 7 to Configure Webserver remotely' -s 150")
						elif i==7:
							os.system("espeak-ng 'press 8 to create LVM remotely' -s 150")
						elif i==8:
							os.system("espeak-ng 'press 9 to rpm query command remotely' -s 140 ")
						elif i==9:
							os.system("espeak-ng 'press 10 to yum whatprovides command remotely' -s 140 ")
						elif i==10:
							os.system("espeak-ng 'press 11 to Exit'")
					while True:
						if flag == 1:
							for i in range(0,len(tasks)):
								print("\t\t\t\t",i+1,". ",tasks[i])
						os.system("espeak-ng 'enter your  Choice' -s 140 ")
						linux=int(input("Enter Your Choice : "))
						if linux==1:
							os.system("espeak-ng `date` -s 150")
							os.system("ssh {} date".format(ip))
							flag=1
							time.sleep(5)
						elif linux==2:
							os.system("espeak-ng `cal` -s 140 ")
							os.system("ssh {} cal".format(ip))
							flag=1
							time.sleep(5)
						elif linux==3:
							os.system("espeak-ng 'entered python 3 ' -s 140 ")
							os.system(" ssh {} python3".format(ip))
							os.system("espeak-ng 'closed python 3 ' -s 140 ")
							flag=1
							time.sleep(5)
						elif linux==4:
							os.system("espeak-ng 'enter your service name' -s 140 ")
							service=input("Enter Your service name : ")
							os.system("ssh {} yum install {} -y".format(ip,service))
							os.system("{} installed".format(service))
							flag=1
							time.sleep(5)
						elif linux==5:
							os.system("espeak-ng 'enter your service name' -s 140 ")
							service=input("Enter Your service name : ")
							os.system("ssh {} systemctl start {}".format(ip,service))
							os.system("{} started".format(service))
							flag=1
							time.sleep(5)
						elif linux==6:
							os.system("espeak-ng 'enter your service name' -s 140 ")
							service=input("Enter Your service name : ")
							os.system("ssh {} systemctl status {}".format(ip,service))
							os.system("{} status".format(service))
							flag=1
							time.sleep(5)
						elif linux==7:
							os.system("ssh {} yum install httpd -y".format(ip))
							os.system("ssh {} systemctl start httpd".format(ip))
							os.system("espeak-ng 'enter your file name' -s 140 ")
							file_name=input("Enter Your file name : ")
							os.system("ssh {} cat > /var/www/html/{}.html".format(ip,file_name))
							os.system("ssh {} setenforce 0".format(ip))
							os.system("ssh {} systemctl stop firewalld".format(ip))
							os.system("ssh {} ifconfig".format(ip))
							flag=1
							time.sleep(5)
						elif linux==8:
							os.system("espeak-ng 'how many Physical Volume you want to create' -s 140  ")
							count = int(input("how many Physical Volume you want to create :"))
							os.system("ssh {} fdisk -l".format(ip))
							for i in range(0,count):
								os.system("espeak-ng 'enter your device name")
								device=input("Enter Your device name : ")
								os.system("ssh {} pvcreate {}".format(ip,device))
								os.system("ssh {} pvdisplay {}".format(ip,device))
							os.system("espeak-ng 'Now i will create volume group' -s 140  ")
							os.system("espeak-ng 'Enter the group name' -s 140  ")
							group = input("Enter the group name :")
							os.system("espeak-ng 'Enter the device name with spaces' -s 140 ")
							device = input("Enter the device name with spaces :")
							os.system("ssh {} vgcreate {} {}".format(ip,group,device))
							os.system("ssh {} vgdisplay {}".format(ip,group))
							os.system("espeak-ng 'Now i will create logical volume' -s 140  ")
							os.system("espeak-ng 'Enter the size' -s 140  ")
							size = input("Enter the size :")
							os.system("espeak-ng 'Enter the logical volume name' -s 140  ")
							lv_name = input("Enter the logical volume name :")
							os.system("espeak-ng 'Enter the volume group name' -s 140  ")
							vg_name = input("Enter the volume group name:")
							os.system("ssh {} lvcreate --size {} --name {} {}".format(ip,size,lv_name,vg_name))
							os.system('espeak-ng  "Partition Created"  -s 140')
							os.system("ssh {} mkfs.ext4 /dev/{}/{}".format(ip,vg_name,lv_name))
							path = input("enter the path where you want to mount it :")
							os.system("ssh {} mkdir /{}".format(ip,path))
							os.system("ssh {} mount /dev/{}/{} /{}".format(ip,vg_name,lv_name,path))
							os.system("ssh {} df -h".format(ip))
							flag=1
							time.sleep(5)
						elif linux==9:
							os.system("espeak-ng 'query for a software' -s 140  ")
							service = input("query for a software :")
							os.system("ssh {} rpm -q {}".format(ip,service))
							flag=1
							time.sleep(5)
						elif linux==10:
							os.system("espeak-ng 'let us ask yum' -s 140 ")
							service = input("enter your hint :")
							os.system("ssh {} yum whatprovides {}".format(ip,service))
							flag=1
							time.sleep(5)
						elif linux==11:
							os.system("espeak-ng 'Thank You See You Soon' -s 140 ")
							os.system("clear")
							print("\n\n\n\n\n\n\n\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\t\t\t\t\tSAYONARA\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
							flag=0
							time.sleep(5)
							break
				elif wish =="exit":
					os.system("espeak-ng 'Thank You See You Soon' -s 140 ")
					os.system("clear")
					print("\n\n\n\n\n\n\n\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\t\t\t\t\tSAYONARA\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
					time.sleep(5)
					break
					
	elif select_tech == 4:
			os.system("tput setaf 3")
			flag=0
			os.system('espeak-ng "welcome to Hadoop Technology" -s 140')
			os.system("clear")
			print("\n\n\n\n\n\n\n")
			tasks=["Install Java JDK","Install Hadoop","Configure NameNode","Configure Datanode","Open NameNode on Browser","Login to NameNode","Login to Datanode","Configure Client Node","Exit"]
			for i in range(0,len(tasks)):
				print("\t\t\t\t",i+1,". ",tasks[i])
				if i==0:
					os.system("espeak-ng 'press 1 to Install Java JDK' -s 150")
				elif i==1:
					os.system("espeak-ng 'press 2 to Install Hadoop' -s 150")
				elif i==2:
					os.system("espeak-ng 'press 3 to Configure NameNode' -s 150")
				elif i==3:
					os.system("espeak-ng 'press 4 to Configure Datanode' -s 150")
				elif i==4:
					os.system("espeak-ng 'press 5 to Open NameNode on Browser' -s 150")
				elif i==5:
					os.system("espeak-ng 'press 6 to Login to NameNode' -s 150")
				elif i==6:
					os.system("espeak-ng 'press 7 to Login to Datanode' -s 150")
				elif i==7:
					os.system("espeak-ng 'press 8 to Configure Client Node'")
				elif i==8:
					os.system("espeak-ng 'press 9 to Exit'")
			while True:
				os.system("tput setaf 2")
				if flag ==1:
					for i in range(0,len(tasks)):
						print("\t\t\t\t",i+1,". ",tasks[i])
				os.system("espeak-ng 'press a hadoop technology number'")
				hadoop = int(input("press a number :"))
				if hadoop==1:
					os.system("rpm -i jdk-8u171-linux-x64.rpm")
					os.system("java -version")
					os.system("espeak-ng 'Java JDK installed' -s 150")
					flag=1
					time.sleep(5)
				elif hadoop==2:
					os.system("rpm -i hadoop-1.2.1-1.x86_64.rpm")
					os.system("hadoop version")
					os.system("espeak-ng 'Hadoop installed' -s 150")
					flag=1
					time.sleep(5)
				elif hadoop == 3:
					os.system("espeak-ng 'Enter master node IP' -s 140")
					ip = input("Enter the Master node IP : ")
					os.system("scp namenode.py root@{}:/root/".format(ip))
					#install python3 on the instance
					os.system("ssh root@{} yum install python3 -y".format(ip))
					#setup namenode core-site.xml and hdfs-site.xml
					os.system("ssh root@{} python3 namenode.py".format(ip))
					os.system("ssh {} hadoop namenode -format".format(ip))
					os.system("ssh {} hadoop-daemon.sh start namenode".format(ip))
					os.system("ssh {} jps".format(ip))
					os.system("ssh {} hadoop dfsadmin -report".format(ip))
					os.system("firefox {}:50070".format(ip))
					os.system("espeak-ng 'Hadoop namenode configured' -s 150")
					flag=1
					time.sleep(5)
				elif hadoop == 4:
					os.system("espeak-ng 'enter the total number of datanodes you want to configure ' -s 140")
					count = int(input("Enter the total number of datanodes you want to configure : "))
					for i in range(0,count):
						os.system("espeak-ng 'Enter data node IP' -s 140")
						ip = input("Enter the Data node IP : ")
						os.system("scp datanode.py root@{}:/root/".format(ip))
						#install python3 on the instance
						os.system("ssh root@{} yum install python3 -y".format(ip))
						#setup datanode core-site.xml and hdfs-site.xml
						os.system("ssh root@{} python3 datanode.py".format(ip))
						os.system("ssh {} hadoop-daemon.sh start datanode".format(ip))
						os.system("ssh {} jps".format(ip))
					os.system("espeak-ng 'Hadoop datanode configured' -s 150")
					flag=1
					time.sleep(5)
				elif hadoop==5:
					os.system("espeak-ng 'Enter master node IP' -s 140")
					ip = input("Enter the master node IP :")
					os.system("firefox {}:50070".format(ip))
					flag=1
					time.sleep(5)
				elif hadoop==6:
					os.system("espeak-ng 'Enter master node IP' -s 140")
					ip = input("Enter the master node IP :")
					os.system("ssh {}".format(ip))
					flag=1
					time.sleep(5)
				elif hadoop==7:
					os.system("espeak-ng 'Enter data node IP' -s 140")
					ip = input("Enter the data node IP :")
					os.system("ssh {}".format(ip))
					flag=1
					time.sleep(5)
				elif hadoop==8:
					os.system("espeak-ng 'enter the total number of client you want to configure ' -s 140")
					count = int(input("Enter the total number of client you want to configure : "))
					for i in range(0,count):
						os.system("espeak-ng 'Enter client node IP' -s 140")
						ip = input("Enter the Client node IP : ")
						os.system("scp client.py root@{}:/root/".format(ip))
						#install python3 on the instance
						os.system("ssh root@{} yum install python3 -y".format(ip))
						#setup datanode core-site.xml and hdfs-site.xml
						os.system("ssh root@{} python3 client.py".format(ip))
					os.system("espeak-ng 'Hadoop client configured' -s 150")
					flag=1
					time.sleep(5)
				elif hadoop==9:
					os.system("espeak-ng 'Thank You See You Soon' -s 140 ")
					os.system("clear")
					print("\n\n\n\n\n\n\n\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\t\t\t\t\tSAYONARA\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
					flag=0
					time.sleep(5)
					break
	elif select_tech == 5:
		os.system("tput setaf 4")
		flag=0
		tasks = ["install Ansible","Check Ansible Version","Create inventory file ","create ansible config file","See the Hosts","start apache server on target Node","Exit"]
		for i in range(0,len(tasks)):
			print("\t\t\t\t",i+1,". ",tasks[i])
			if i==0:
				os.system("espeak-ng 'press 1 to Install Ansible' -s 150")
			elif i==1:
				os.system("espeak-ng 'press 2 to Check Ansible Version' -s 150")
			elif i==2:
				os.system("espeak-ng 'press 3 to Create inventory file ' -s 150")
			elif i==3:
				os.system("espeak-ng 'press 4 to create ansible config file' -s 150")
			elif i==4:
				os.system("espeak-ng 'press 5 to see the hosts' -s 150")
			elif i==5:
				os.system("espeak-ng 'press 6 to start apache server on target Node' -s 150")
			elif i==6:
				os.system("espeak-ng 'press 7 to Exit'")
		while True :
			os.system("tput setaf 6")
			if flag ==1:
				os.system("clear")
				for i in range(0,len(tasks)):
					print("\t\t\t\t",i+1,". ",tasks[i])
			os.system("espeak-ng 'Enter Your Wish' -s 150")
			ansible = int(input("Enter Your Wish :"))
			if ansible == 1:
				os.system("pip3 install ansible") 
				os.system("espeak-ng 'Ansible Installed' -s 150")
				time.sleep(4)
				flag=1
			elif ansible == 2:
				os.system("ansible --version") 
				os.system("espeak-ng 'Ansible version' -s 150")
				time.sleep(4)
				flag=1
			elif ansible == 3:
				os.system("espeak-ng 'Enter your controller node IP' -s 140")
				ip = input("Enter your controller node  IP : ") 
				os.system("scp inventory.py root@{}:/root/".format(ip))
				os.system("ssh root@{} yum install python3 -y".format(ip))
				os.system("ssh root@{} python3 inventory.py".format(ip))
				os.system("espeak-ng 'inventory file created' -s 150")
				time.sleep(4)
				flag=1
			elif ansible == 4:
				os.system("espeak-ng 'Enter your controller node IP' -s 140")
				ip = input("Enter your controller node  IP : ") 
				os.system("scp ansible_config_file.py root@{}:/root/".format(ip))
				os.system("ssh root@{} python3 ansible_config_file.py".format(ip))
				os.system("espeak-ng 'config file created' -s 150")
				time.sleep(4)
				flag=1
			elif ansible == 5:
				os.system("espeak-ng 'Enter your controller node IP' -s 140")
				ip = input("Enter your controller node  IP : ")
				os.system("ssh {} ansible all --list-hosts".format(ip)) 
				os.system("espeak-ng 'All Hosts' -s 150")
				time.sleep(4)
				flag=1
			elif ansible == 6:
				os.system("ansible all -m service -a 'name=httpd state=started'") 
				os.system("espeak-ng 'service started' -s 150")
				time.sleep(4)
				flag=1
			elif ansible ==	7:
				os.system("espeak-ng 'Thank You For using ansible come back soon' -s 140 ")
				os.system("clear")
				print("\n\n\n\n\n\n\n\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\t\t\t\t\tBye Bye Ansible\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
				flag=0
				break
	
	else:
		os.system("tput setaf 3")
		os.system("espeak-ng 'Thank You See You Soon'")
		os.system("clear")
		print("\n\n\n\n\n\n\n\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\t\t\t\t\tSAYONARA\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
		break
