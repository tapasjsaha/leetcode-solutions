def commonChars(words):
    fstr = words.pop()
    common_letters = []
    for ch in fstr:
        common = True
        for st in words:
            if ch not in st:
                common = False
                break
        if common:
            common_letters.append(ch)
            tmp_arr = []
            for st in words:
                tmp_arr.append(st.replace(ch, '', 1))
            words = tmp_arr

    return common_letters




def main():
    st = input("Enter array of strings (comma separated): ")
    in_ar = st.split(',')
    print(f"Input Array: {in_ar}")
    x = commonChars(in_ar)
    print(f"Common Letters: {x}")

main()