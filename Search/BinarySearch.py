# Binary Search

def binarySearch(arr, key):
    low = 0
    high = len(arr) - 1

    arr.sort()

    while low <= high:
        mid = (low + high)//2
        if arr[mid] == key:
            return True
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return False

if __name__ == "__main__":
    array = []
    no = int(input("Enter no of elements in the array :"))
    for i in range(no):
        array.append(int(input("Enter element :")))
    key = int(input("Enter the key to be searched :"))
    if binarySearch(array, key):
        print("Number {} found in array".format(key))
    else:
        print("Number {} not found in array".format(key))