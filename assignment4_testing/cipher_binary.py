input_file = open('output1.txt','r')
output_file = open('cipher_in_binary.txt','w')
for line in input_file:
	# print(line)
	for x in line:
		# print(x)
		if(x=='\n'):
			continue
		value = ord(x)-102
		# print(value)
		# print("{0:b}".format(value))
		output_bin = format(value,'04b')
		# print("output_bin ",output_bin)
		# print("len ",len(output_bin))
		# if(len(output_bin)==1):
		output_file.write(output_bin)

	output_file.write('\n')

