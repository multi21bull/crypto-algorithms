import requests as r
import multiprocessing.dummy
import time
pool = multiprocessing.dummy.Pool(processes=10)
import sys
r.packages.urllib3.disable_warnings()
url = 'https://172.27.26.163:9999/des'
defbody = {'teamname': 'codebreakers', 'password': '141798618b83828d42ab9619284fb5de', 'plaintext':'ci'}
#md5 = 141798618b83828d42ab9619284fb5de
#fbf32niwgh
resp = r.post(url,json = defbody, verify=False)
print(resp.text)


file = open('input_random.txt','r+')
text = file.readlines()
output_file = open('output1.txt','a')
count = 0
line_start = sys.argv[1]
for line in text:
	if(count<int(line_start)):
		count = count + 1
		print(count)
	else:
		print("input ",line)
		line = line.split()
		# print("after split" ,line[0])
		defbody['plaintext'] = line[0]
		resp = r.post(url,json = defbody, verify=False)
		# print(type(resp.text))
		arr = resp.text.split()
		print("output",arr[1][1:-2])
		cipher = arr[1][1:-2]+'\n'
		count = count + 1
		output_file.write(cipher)
		print(count)
		# time.sleep(.5)





# file = open("input_random.txt",'r+')
# for i in range(0,200001):
#   print(file.readline())
  
