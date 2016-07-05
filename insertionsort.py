import random
import datetime

test = []
for x in range(1,101):
	test.append(random.randint(0, 10000))

start = datetime.datetime.now()
def insertionSort(list):
	result = []
	for i in range(0, len(list)):
		for j in range(0, len(result)):
			if list[i] <= result[j]:
				result.insert(j, list[i])
				break
		else:
			result.append(list[i])
			

	return result
print insertionSort(test)

print datetime.datetime.now() - start