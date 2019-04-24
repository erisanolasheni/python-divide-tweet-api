# Task write a task that get the quotient of a dividend and a divisor with using the '/' operator


def binarySearchQuot(numerator, denominator):
    prime_numerator = numerator
    prime_denominator = denominator

    # Throw error if the denominator is zero
    if denominator == 0:
        raise ZeroDivisionError('Division by Zero not allowed.')

    # numerator and denominator are both negative integers, then absolute them
    if numerator < 0 and denominator < 0:
        numerator = abs(numerator)
        denominator = abs(denominator)

    quotient_lists = get_range(numerator, denominator)

    """ 
        For faster approach to answer, use the binary search algorithm 
        To search for the possible quotient
        Since no division operator should to be used
         * 0.5 is used in place of /2 to get the
        midpoint of the range
    """

    first = 0
    last = len(quotient_lists)-1
    found = False
    while first <= last and not found:
        midpoint = round((first + last)*0.5)

        # if the product of quotient and denominator arrives exactly
        # the numerator, then we got the answer!
        if quotient_lists[midpoint] * denominator == numerator:
            found = [quotient_lists[midpoint], 0]
        else:
            # else if the numerator is greater than the product,
            # and we the difference between the numerator
            # and the product les than the denominator,
            # then we found it with remainder also!
            if numerator > quotient_lists[midpoint] * denominator:
                if (numerator - quotient_lists[midpoint] * denominator) < denominator:
                    found = [quotient_lists[midpoint], prime_numerator -
                             quotient_lists[midpoint] * prime_denominator]
                else:
                    # else we have to move the start index further the range of quotients
                    first = midpoint+1
            # else if the numerator is then less than the product of
            # the quotient and the denominator,

            # then we have to move the last index more closer
            elif numerator < quotient_lists[midpoint] * denominator:
                last = midpoint-1

        # return found

    return found

# create a function to get range (bracket) of possible quotients


def get_range(numerator, denominator):
    lst = []
    maxn = max(numerator, denominator)
    minn = min(numerator, denominator)

    start = min(1, minn)
    end = maxn

    range_list = []
    while start <= end:
        range_list.append(start)
        start += 1
        if start == 0:
            start = 1
    
    return range_list


print(binarySearchQuot(-61, 5))
