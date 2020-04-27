def insertionSort(array):
	for index in range(1, len(array)):
		currentValue = array[index]
		currentPosition = index

		while currentPosition > 0 and array[currentPosition - 1] > currentValue:
			array[currentPosition] = array[currentPosition -1]
			currentPosition = currentPosition - 1

		array[currentPosition] = currentValue
	return array

def binarySearch(sortedArray, first, last, key):
	if last >= first:
		mid = first +(last - first)//2

		if sortedArray[mid] == key:
			return mid
		elif sortedArray[mid] > key:
			return binarySearch(sortedArray, first, mid-1, key)
		else:
			return binarySearch(sortedArray, mid+1, last, key)
	else:
		return -1

def main():
	array = []
	number = int(input("How many names would you like to enter?: "))

	for i in range(number):
		n = input("Name: ")
		array.append(n)

	print(array)
	sortedArray = insertionSort(array)
	print(sortedArray)

	key = input("Enter the name you'd like to search for: ")

	index = binarySearch(sortedArray, 0, len(sortedArray), key)
	if index != -1:
		print(key, "was found.")
	else:
		print(key, "was not found.")

main()
