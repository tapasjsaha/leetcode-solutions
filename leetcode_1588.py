def sumOddLengthSubarrays(arr):
    total = sum(arr)  # taking care of 1st iteration of single elements
    l = len(arr)
    for j in range(3, l + 1, 2):
        for i in range(0, (l + 1) - j, 1):
            total += sum(arr[i:i + j])
    return total


def toInt(lst):
    out = []
    for l in lst:
        out.append(int(l))
    return out

def main():
    st = input("Enter array of numbers (comma separated): ")
    ar = st.split(',')
    in_ar = toInt(ar)
    print(f"Input Array: {in_ar}")
    sum_odd = sumOddLengthSubarrays(in_ar)
    print(f"Sum of all possible odd length sub array: {sum_odd}")

main()

