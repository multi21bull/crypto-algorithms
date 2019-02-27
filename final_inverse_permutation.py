def final_inverse():
	invrfp = [
	 57,49,41,33,25,17,9,1,
	 59,51,43,35,27,19,11,3,
	 61,53,45,37,29,21,13,5,
	 63,55,47,39,31,23,15,7,
	 58,50,42,34,26,18,10,2,
	 60,52,44,36,28,20,12,4,
	 62,54,46,38,30,22,14,6,
	 64,56,48,40,32,24,16,8
	]
	input_file = open('cipher_in_binary.txt','r')
	output_file = open('l6_r6.txt','w')
	text = input_file.readlines()
	for line in text:
		for x in invrfp:
			# print(x)
			output_file.write(line[x-1])
		output_file.write('\n')

def output_xor():
	input_file = open('l6_r6.txt','r')
	text = input_file.readlines()
	output_file = open('output_xor.txt','w')
	count = 0
	for line in text:
		if(count%2==0):
			first = line
		else:
			second = line
			first = int(first, 2)
			second = int(second, 2)
			xor = first ^ second
			# print(xor)
			xor = format(xor,'064b')
			# print(xor)
			output_file.write(xor)
			output_file.write('\n')
		count = count + 1


def input_xor():
	input_file = open('output_xor.txt','r')
	first = '00000100000000000000000000000000'
	# print(len(first))
	output_file = open('l5_r5.txt','w')
	text = input_file.readlines()
	for line in text:
		second = line[0:32]
		# print(second)
		# print(len(second))
		total = first + second
		output_file.write(total+'\n')
final_inverse()
output_xor()
def key_schedule():
	invrfp = [24 ,27 ,21 ,6 ,11 ,15 ,13 ,10 ,25 ,16 ,3 ,20,
	 5 ,1 ,22 ,14 ,8 ,18 ,26 ,17 ,9 ,2 ,23 ,12 ,51 ,34 ,41,
	 47 ,29 ,37 ,40 ,50 ,33 ,55 ,43 ,30 ,54 ,31 ,49 ,38 ,44,
	 35 ,56 ,52 ,32 ,46 ,39 ,42 
	]
	input_xor = ''
	count = 0
	for x in input_xor:
		# print(x)
		output_xor[invrp[count]] = x
		count = count + 1


# key_schedule()
input_xor()