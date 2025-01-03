def is_valid(isbn):
    listisbn = list(''.join(filter(str.isalnum, isbn)))
    if len(listisbn) != 10:
        return False
    else:
        try:
            numlist = [int(i) for i in listisbn[:-1]]
            result = sum([numlist[x] * (10-x) for x in range(0,9)])
            result = result + 10 if isbn[-1] == "X" else result + int(isbn[-1]) if int(isbn[-1]) > 0 else -1
            return result % 11 == 0
        except:
            return False


print(is_valid("3-598-21507-X"))

