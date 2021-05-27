def largestAltitude(gain):
#    curr_alt = 0
#    max_alt = 0
#    for alt in gain:
#        curr_alt += alt
#        if curr_alt > max_alt:
#            max_alt = curr_alt
#    return max_alt
    altitude = [0]
    for i in range(len(gain)):
        altitude.append(altitude[i] + gain[i])
    return max(altitude)



def main():
    g = input("Please enter list of gain (comma separated):")
    gain = []
    for i in g.split(','):
        gain.append(int(i))
    max_alt = largestAltitude(gain)
    print(f"Maximum altitude is : {max_alt}")


main()

