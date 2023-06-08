import time


def is_additive(s: str) -> bool:
    if len(s) < 3:
        return False

    li = [int(x) for x in list(s)]

    if sum(li) == 0:
        return False


    # This is O(n^3) in the worst case which occurs when a number isn't additive.
    # Given that the number of digits in the # of atoms in the universe is ~81
    # and 100-digit numbers take ~200 milliseconds, I think we're fine for now.
    # TODO: Optimize this once we out-scale our current reality.
    for i in range(0, len(li)-2):
        found = inner(li, int(''.join([str(x) for x in li[:i+1]])), i+1)
        if found:
            return True

    return False


def inner(li, sum_so_far, start):
    target = 0
    current_sum = 0
    for j in range(start+1, len(li)):
        if target == 0:
            current_sum = int(''.join([str(x) for x in li[start:j]]))
        else:
            current_sum = current_sum * 10 + li[j-1]

        for k in range(j+1, len(li)+1):
            su = sum_so_far + current_sum
            # ~30% speedup - Break early if it's impossible for target to ever reach what we've already seen
            max_possible = int("9" * (len(li) - j))
            if current_sum > max_possible or sum_so_far > max_possible or su > max_possible:
                return False
            target = int(''.join([str(x) for x in li[j:k]]))

            # increasing k will just increase the sum_so_far further so break
            if su < target:
                break

            if su == target:
                # Explore this possible split point
                res = inner(li, su, j)
                if res or k >= len(li):
                    return True
        # increasing j will just increase current_sum and decrease target so return
        if current_sum > target:
            return False

    return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    assert(is_additive("123143") is True)
    assert(is_additive("123") is True)
    assert(is_additive("1235128") is True)
    assert(is_additive("1235129") is False)
    assert(is_additive("12") is False)
    assert(is_additive("12345168") is True)
    assert(is_additive("1001101") is True)
    assert(is_additive("1003101") is False)
    now = time.time()
    for i in range(20, 30):
        it = time.time()
        v = "1003"*(i+5)
        assert(is_additive(v) is False)
        done = time.time()
        print(f'iter with {len(v)} chars took {done - it}')


