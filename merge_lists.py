def merge(a, b):
    if a == [] or b == []:
        return []

    def m(l1, l2):
        li = []
        for index, number in enumerate(l1):
            if index + 1 > len(l2):
                index = -1
            li.append((number, l2[index]))
        return li
    if len(a) < len(b):
        return [tup[::-1] for tup in m(b, a)]
    else:
        return m(a, b)
