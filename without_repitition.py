import random
import math



data = []
upto=pow(2,10)
numbers=pow(2,3)

def unique_rand(inicial, limit, total):

        data = []

        i = 0

        while i < total:
            number = random.randint(inicial, limit)
            if number not in data:
                data.append(number)
                i += 1

        return data


data = unique_rand(0,upto , numbers)

print(data)

for i in range(len(data)):
	
	print(format(data[i],'010b'))




