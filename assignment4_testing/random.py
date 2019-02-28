import random
output_file = open('random.txt','w+')
i=0
start = 0
end = 1
for i in range(0,100000):
  j = 0
  number = ''
  for j in range(0,64):
    number = number + str(random.randint(start, end))
  # print(number)
  output_file.write(number)
  output_file.write("\n")