def bubleSort(arr):
	n = len(arr)
	#Цикл для прохождения через массив
	for i in range(n):
		swapped = False
		for j in range(0, n-i-1):
			#если текущий элемент больше следующего -> меняем местами
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = True
		if swapped == False:
			break
arr = [64, 32, 128, 54, 31, 12, 10, 1, 2, 5]
print("Список до сортировки: ", arr)
bubleSort(arr)
print("Новый список: ", arr)
