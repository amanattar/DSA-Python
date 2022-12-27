def bubbleSort(arr):
    counter = 0
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                counter += 1
    return arr

if __name__ == "__main__":
    array = []
    no = int(input("Enter no of elements in the array :"))
    for i in range(no):
        array.append(int(input("Enter element :")))
    print("Sorted array is : {} ".format(bubbleSort(array)))


            