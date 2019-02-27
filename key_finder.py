def expansion():
	input_file = open('output_xor.txt','r')
	text = input_file.readlines()
	output_file = open('expansion_xor.txt','w')
	ex = [
  	 32, 1, 2, 3, 4, 5,
  	 4, 5,6, 7, 8, 9,
  	 8, 9, 10, 11, 12, 13,
  	 12, 13, 14, 15, 16, 17,
  	 16, 17, 18, 19, 20, 21,
  	 20, 21, 22, 23, 24, 25,
  	 24, 25, 26, 27, 28, 29,
  	 28, 29, 30, 31, 32, 1
	]
	count=0
	for input_bits in text:
		output_bits = ''
		for x in ex:
			# print(x)
			# print(len(input_bits))
			output_bits = output_bits + (input_bits[x-1])
			# print(len(output_bits))
			# output_file.write(output_bits+'\n')
			count = count + 1 
			print(count)
		output_file.write(output_bits+'\n')
	# print(output_bits)

def inverse_permutation():
	input_file = open('output_xor.txt')
	text = input_file.readlines()
	left = '00000100000000000000000000000000'
	left = int(left,2)
	invp = [
     9, 17, 23, 31,
	 13, 28, 2, 18,
	 24, 16, 30, 6,
	 26, 20, 10, 1,
	 8, 14, 25, 3,
	 4, 29, 11, 19,
	 32, 12, 22, 7,
	 5, 27, 15, 21]
	output_file = open('after_sbox_xor.txt','w')
	count=0
	for input_bit in text:

		right = input_bit[32:64]
		right = int(right,2)
		# print(right)
		output_xor = right ^ left
		# print(output_xor)
		output_xor = format(output_xor,'032b')
		output_bits = ''
		for x in invp:
			# print(count)
			# count = count + 1
			output_bits = output_bits + (output_xor[x-1])
		
		# print(output_bits)
		output_file.write(output_bits+'\n')
		
def total_before_sbox():
	input_file = open('l6_r6.txt','r')
	text = input_file.readlines()
	output_file = open('total_before_sbox.txt','w')
	ex = [
  	 32, 1, 2, 3, 4, 5,
  	 4, 5,6, 7, 8, 9,
  	 8, 9, 10, 11, 12, 13,
  	 12, 13, 14, 15, 16, 17,
  	 16, 17, 18, 19, 20, 21,
  	 20, 21, 22, 23, 24, 25,
  	 24, 25, 26, 27, 28, 29,
  	 28, 29, 30, 31, 32, 1
	]
	count=0
	for input_bits in text:
		output_bits = ''
		for x in ex:
			# print(x)
			# print(len(input_bits))
			output_bits = output_bits + (input_bits[x-1])
			# print(len(output_bits))
			# output_file.write(output_bits+'\n')
			count = count + 1 
			print(count)
		output_file.write(output_bits+'\n')

# input_bit = '11001110000101110111110111110011'
# expansion()
inverse_permutation()
# total_before_sbox()