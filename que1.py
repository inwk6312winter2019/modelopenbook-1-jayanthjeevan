fp = open("running-config.cfg")
readfile=fp.read()


def list_ifname_ip():
	mydict = dict()
	newdict = dict()
	for line in readfile.split():
		word = line.strip()
		if word not in mydict:
			mydict[line]=1
		else:
			mydict[line]+=1
	print(mydict)

	mylist = []
	for key, value in mydict.items():
		if "nameif" in mydict:
			mylist.append((value,key))
	print(mylist)

list_ifname_ip()
