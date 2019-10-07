# check whether `pwd` is a valid password
if len(pwd) >= 8 and len(pwd) <= 16:    
    sonder = []
    gross = []
    klein = []
    num = []
    for p in pwd:
        if p in "+-*/":
            sonder.append(p)
        elif p.isdigit():
            num.append(p)
        elif p.isupper() and p.isalpha():
            gross.append(p)
        else:
            klein.append(p)

    if len(klein) > 1 and len(gross) > 1 and len(sonder) > 1 and len(num) > 1:
        is_valid = True
    else:
        is_valid = False
    print(is_valid)
