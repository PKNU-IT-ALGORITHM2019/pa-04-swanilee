import sys
import random
import time


def mkarray(n):

    array = []
    rev_array = []
    # 천
    for j in range(0,10):
        first_ran, first_rev = [],[]
        for i in range(0, n):
            num = random.randrange(1, n+1)
            first_ran.append(num)
            first_rev.append(i + 1)

        first_rev.reverse()

        array.append(first_ran)
        rev_array.append(first_rev)

    return array,rev_array


def MAX_HEAPIFY(list, num, i):
    max_num = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < num and list[i] < list[l]:
        max_num = l

    if r < num and list[max_num] < list[r]:
        max_num = r

    if max_num != i:
        list[i], list[max_num] = list[max_num], list[i]
        MAX_HEAPIFY(list, num, max_num)


def BUILD_MAX_HEAP(list):
    num = len(list)

    for i in range(num, -1, -1):
        MAX_HEAPIFY(list, num, i)

    for i in range(num-1, 0, -1):
        list[i], list[0] = list[0], list[i]
        MAX_HEAPIFY(list, i, 0)

    return list


def main():

    A,R = mkarray(1000)
    AA,RR = mkarray(10000)
    AAA,RRR = mkarray(100000)
    # for i in A:
    # print(i)
    # for i in R:
    #    print(i)
    #
    # t = 0
    # for i in R:
    #     t += BUILD_MAX_HEAP(i)
    timee = time.time()
    list = BUILD_MAX_HEAP(A)
    #print(list)
    tmp_timee = time.time() - timee
    print("Random1000 : " + "%0.9f" % tmp_timee)

    timee = time.time()
    list = BUILD_MAX_HEAP(R)
    #print(list)
    tmp_timee = time.time() - timee
    print("Reverse1000 : " + "%0.9f" % tmp_timee)

    timee = time.time()
    list = BUILD_MAX_HEAP(AA)
    #print(list)
    tmp_timee = time.time() - timee
    print("Random10000 : " + "%0.9f" % tmp_timee)

    timee = time.time()
    list = BUILD_MAX_HEAP(RR)
    #print(list)
    tmp_timee = time.time() - timee
    print("Reverse10000 : " + "%0.9f" % tmp_timee)

    timee = time.time()
    list = BUILD_MAX_HEAP(AAA)
    #print(list)
    tmp_timee = time.time() - timee
    print("Random100000 : " + "%0.9f" % tmp_timee)

    timee = time.time()
    list = BUILD_MAX_HEAP(RRR)
    #print(list)
    tmp_timee = time.time() - timee
    print("Reverse100000 : " + "%0.9f" % tmp_timee)


    # print("--------Random1000-------Reverse1000------Random10000----Reverse10000-----Random100000------Reverse100000---")
    # print("Heap")
    # print(howlongA)
    # print(howlongR)
    # print(howlongAA)
    # print(howlongRR)
    # print(howlongAAA)
    # print(howlongRRR)
main()