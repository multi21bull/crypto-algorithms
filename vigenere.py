import re
ciphertext = input("enter ciphertext:")
# print(ciphertext)
text = ciphertext.lower()
ciphertext = re.sub(r'[^A-Za-z0-9]+','',ciphertext).lower()
print(ciphertext)

def deviation_english(shift):
	list_occurence = []
	list_english = [8.167,1.492,2.782,4.253,12.702,2.228,2.015,6.094,6.966,0.153,0.773,4.025,2.406,6.749,7.507,1.929,0.095,5.987,
					6.327,9.056,2.758,0.978,2.360,0.150,1.974,0.074]

	for x in range(0,26):
		list_occurence.append(shift.count(chr(x+ord("a"))))
	# print(list_occurence)
	list_occurence = [(x*100)/len(shift) for x in list_occurence]
		# print(list_occurence)
	individual_deviation = [(list_occurence[i]-list_english[i])**2 for i in range(len(list_english))]
	deviation = sum(individual_deviation)


	return deviation

def getstring(ciphertext,y,x):
	return ciphertext[y::x]

def check_key(substring_y):
	deviation = 10000
	key  = "a"
	for shift in range(0,26):
		s = ""
		for l in substring_y:
		    a = (ord(l) - shift - ord("a"))%26 + ord("a")
		    s += chr(a)
		# print("shift by:",shift," ",s)
		value = deviation_english(s)
		# print(value)
		if(value<deviation):
			deviation = value
			key = chr(ord("a")+shift)

	return key


for x in range(2,15):
	print("key length: ",x)
	total_key = ""

	for y in range(0,x):
		# print("y: ",y)
		substring_y = getstring(ciphertext,y,x)
		# print(substring_y)
		key = check_key(substring_y)
		total_key += key
		# print(key)
	print("key: ",total_key)
	count=0
	plaintext = ""
	for letter in text:
		if letter.isalpha():
			num = count%x
			count+=1
			l = total_key[num]
			plaintext += chr((ord(letter) - ord(l))%26 + ord("a"))
		else:
			plaintext += letter

	print(plaintext,"\n\n\n\n")


