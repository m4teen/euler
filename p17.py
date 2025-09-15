def o(m):
    """
    Decompose integer m into its thousands, hundreds, tens, and units digits.
    Returns (string form, unit, ten, hundred, thousand).
    """
    m = str(m).zfill(4)  
    thou = int(m[0])
    hund = int(m[1])
    ten  = int(m[2])
    unit = int(m[3])
    return m, unit, ten, hund, thou


def p(n):
    """
    Map an integer n (1–19, 20,30,...,90) to its English word form.
    Returns empty string if n not in the mapping.
    """
    mapping = {
        1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
        11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
        15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
        19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty",
        50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty",
        90: "ninety"
    }
    return mapping.get(n, "")


def count(m, unit, ten, hund, thou):
    """
    Compute the letter count of the English word form of a number
    given its digits (unit, ten, hundred, thousand).
    British usage: includes 'and' after hundreds where appropriate.
    """
    if thou != 0:
        counter = 11
    else:
        if hund != 0:
            counter = len(p(hund)) + len('hundred')
            tenu = ten * 10 + unit
            if tenu == 0:
                pass
            elif ten == 0:
                counter += len(p(unit)) + len('and')
            elif tenu < 20:
                counter += len(p(tenu)) + len('and')
            else:
                counter += len(p(ten * 10)) + len(p(unit)) + len('and')
        else:
            counter = 0
            tenu = ten * 10 + unit
            if tenu == 0:
                counter = 4  
            elif ten == 0:
                counter += len(p(unit))
            elif tenu < 20:
                counter += len(p(tenu))
            else:
                counter += len(p(ten * 10)) + len(p(unit))
    return counter


def f(n):
    """
    Compute the total letter count of English word forms
    for all integers from 1 to n inclusive.
    """
    total = 0
    for i in range(1, n + 1):
        m, unit, ten, hund, thou = o(i)
        total += count(m, unit, ten, hund, thou)
    return total