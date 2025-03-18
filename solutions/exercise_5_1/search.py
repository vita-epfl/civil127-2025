from enum import Enum


def three_consecutive(s):
    for i in range(len(s)-2):
        if s[i] == s[i+1] and s[i] == s[i+2]:
            return True
    return False


def all_different(s):
    return len(s) == len(set(s))


class NextState(Enum):
    LT = "<"
    GT = ">"


def alternating(s):
    if len(s) < 2:
        # Arbitrary choice to consider 1-digit numbers to not be alternating
        return False

    next_state = None
    if s[0] < s[1]:
        next_state = NextState.GT
    elif s[0] > s[1]:
        next_state = NextState.LT
    else:
        return False

    for i in range(1, len(s)-1):
        match next_state:
            case NextState.GT:
                if s[i] <= s[i+1]:
                    return False
                next_state = NextState.LT
            case NextState.LT:
                if s[i] >= s[i+1]:
                    return False
                next_state = NextState.GT
    return True


def _search(r, filter):
    n = 0
    for i in r:
        if filter(str(i)):
            n += 1
    print(n, "ratio:", round(n/len(r), 3))


def search(r):
    print("3 consecutive: ", end="")
    _search(r, three_consecutive)

    print("all different: ", end="")
    _search(r, all_different)

    print("alternating: ", end="")
    _search(r, alternating)
