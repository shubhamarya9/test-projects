def binary_search(list, target):
    first = 0
    last = len(list - 1)

    while first <=last:
        midpoint = (first + last)//2
        if midpoint == target:
            return midpoint
        elif midpoint < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    else return None
    