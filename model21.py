j=[]
def opening_file(filename):
	fout=open(filename)
	for line in fout:
		f=tuple()
		line=line.split(",")
		str_name=line[2]
		full_name=line[4]
		from_str=line[6]
		to_str=line[7]
		f=(str_name,full_name,from_str,to_str)
		j.append(f)
	return j
print(opening_file("Street_Centrelines.csv"))
