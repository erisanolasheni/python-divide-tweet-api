def binarySearch(alist, item):

    # sort list first
    alist = sorted(alist)
    first = 0
    last = len(alist)-1
    found = False
    while first <= last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True, item, midpoint
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    return found


def binarySearchQuot(numerator, denominator):
    # is_TotalAbs = False if numerator > 0 and denominator > 0 else True
    prime_numerator = numerator
    prime_denominator = denominator
    if numerator < 0 and denominator < 0:
        numerator = abs(numerator)
        denominator = abs(denominator)

    quotient_lists = ngcd(numerator, denominator)[1]
    first = 0
    last = len(quotient_lists)-1
    found = False
    while first <= last and not found:
        midpoint = round((first + last)*0.5)
        if quotient_lists[midpoint] * denominator == numerator:
            found = [quotient_lists[midpoint], 0]
        else:
            if numerator > quotient_lists[midpoint] * denominator:
                if (numerator - quotient_lists[midpoint] * denominator) < denominator:
                    found = [quotient_lists[midpoint], prime_numerator -
                             quotient_lists[midpoint] * prime_denominator]
                else:
                    first = midpoint+1
            elif numerator < quotient_lists[midpoint] * denominator:
                last = midpoint-1

        # return found

    return found


def ngcd(numerator, denominator):
    lst = []
    maxn = max(numerator, denominator)
    minn = min(numerator, denominator)

    start = min(1, minn)
    i = start
    while(i <= maxn):
        if(numerator % i == 0 or denominator % i == 0):
            gcd = i
            lst.append(i)
        i += 1
        if i == 0:
            i = 1
    # get range between lowest and highest factors
    print(lst)
    start = lst[0]
    end = lst[len(lst)-1]
    range_list = []
    while start <= end:
        range_list.append(start)
        start += 1
        if start == 0:
            start = 1
    print(range_list)
    return gcd, range_list


print(binarySearchQuot(61, 5))
