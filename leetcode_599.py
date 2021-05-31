# Minimum Index Sum of Two Lists
import datetime
import time


def findRestaurant(list1, list2):
    d = {}
    maxi = len(list1) + len(list2) + 1
    for s in set(list1).intersection(set(list2)):
        d[s] = list1.index(s) + list2.index(s)
        if maxi > list1.index(s) + list2.index(s):
            maxi = list1.index(s) + list2.index(s)

    res = [r for r in d if d[r] == maxi]
    return res


def main():
    list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
    list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
    print(findRestaurant(list1, list2))


main()