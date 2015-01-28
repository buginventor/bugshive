import sys,os,datetime

def main():
	print("version {}.{}.{}".format(*sys.version_info))
	print(sys.platform)
	print(os.name)
	print(os.getenv("path"))
	print(os.getenv("username"))
	print(os.getcwd())
	now = datetime.datetime.now()
	print(now)
	print(now.year,now.month,now.day)


main()