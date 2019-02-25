import requests as r
import multiprocessing.dummy

pool = multiprocessing.dummy.Pool(processes=10)



r.packages.urllib3.disable_warnings()
url = 'https://172.27.26.163:9999/des'
defbody = {'teamname': 'codebreakers', 'password': '141798618b83828d42ab9619284fb5de', 'plaintext':'ci'}

resp = r.post(url,json = defbody, verify=False)
print(resp.text)


file = open('input_random.txt','r+')
output_file = open('output1.txt','w+')
count = 0
for line in file:
	if(count>5):
		break
	print(line)
	line = line.split()
	print("after split" ,line[0])
	defbody['plaintext'] = line[0]
	resp = r.post(url,json = defbody, verify=False)
	print(resp.text)
	count = count + 1
	output_file.write(resp.text['ciphertext'])





# file = open("input_random.txt",'r+')
# for i in range(0,200001):
#   print(file.readline())
  
