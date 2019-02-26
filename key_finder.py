def expansion(input_bits):
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
	output_bits = ''
	for x in ex:
		print(x)
		print(len(input_bits))
		output_bits = output_bits + (input_bits[x-1])
		print(len(output_bits))
	print(output_bits)

input_bit = '11001110000101110111110111110011'
expansion(input_bit)
