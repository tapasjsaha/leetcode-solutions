#Find Lucky Integer in an Array

def findLucky(arr):
    d = {}
    for n in arr:
        if n in d:
            d[n] += 1
        else:
            d[n] = 1

    for n in sorted(set(arr), reverse = True):
        if d[n] == n:
            return n
    else:
        return -1

def main():
    arr = [1] #[3,3,3] #[5] #[2,2,2,3,3] #[2,2,3,4] #[1,2,2,3,3,3]
    print(findLucky(arr))


main()

