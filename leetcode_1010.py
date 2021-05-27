def numPairsDivisibleBy60(time):
    print(time)
    d = {}
    cnt = 0
    for tn in time:
        t = tn % 60
        try:
            cnt += d[(60 - t) % 60]
        except KeyError:
            cnt += 0
        if t in d:
            d[t] = d[t] + 1
        else:
            d[t] = 1
        #print(cnt, d)
    return cnt





###Below code in not accepted by leetcode due to "Time limit Exceed", need to reduce the time complexity
    #pair = 0
    #for i in range(len(time)-1):
    #    for j in range(i+1, len(time), 1):
    #        if (time[i] + time[j]) % 60 == 0:
    #            pair += 1
    #            print(time[i], time[j])
    #return pair


def main():
    print("====================================================================")
    inp = input("Enter the array: ")
    arr = []
    for i in inp.split(','):
        arr.append(int(i))
    n = numPairsDivisibleBy60(arr)
    print(f"Number of pair :{n}")


main()
