def numberOfMatches(n):
    total_matches = 0
    while n != 1:
        total_matches += n // 2
        if n % 2 == 0:
            n = n // 2
        else:
            n = ((n - 1) / 2) + 1
    return int(total_matches)


def main():
    team = input("Enter number of teams :")
    team_num = int(team)

    print(f"Teams played :", team_num)
    print(f"Total Matches :", numberOfMatches(team_num))


main()
