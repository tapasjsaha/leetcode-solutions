def uniqueOccurrences(arr):
    d = {}
    for a in arr:
        if a in d:
            d[a] += 1
        else:
            d[a] = 1
    # lst = list(d.values())
    # s = set(lst)
    if len(list(d.values())) == len(set(list(d.values()))):
        return True
    else:
        return False


def main():
    print("====================================================================")
    lst = input("Enter the array(comma separated): ")
    arr = []
    for i in lst.split(','):
        arr.append(int(i))
#    print(arr)
#    d = numberOfOcc(arr)
#    print(f"Count of occurrence is :{d}")
    if_unique = uniqueOccurrences(arr)
    if if_unique:
        print(f"YES- All the occurrence of numbers present in {lst} is unique")
    else:
        print(f"NO- All the occurrence of numbers present in {lst} is not unique")


main()