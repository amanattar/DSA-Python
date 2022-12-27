#code for linear search

def linearSearch(arr, key):
    for item in arr:
        if item == key:
            return True
    return False

if __name__ == "__main__":
    array = []
    no = int(input("Enter no of elements in the array :"))
    for i in range(no):
        array.append(int(input("Enter element :")))
    key = int(input("Enter the key to be searched :"))
    if linearSearch(array, key):
        print("Number {} found in array".format(key))
    else:
        print("Number {} not found in array".format(key))