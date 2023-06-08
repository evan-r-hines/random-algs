
# O(log(n)) solution for pow(x, n)
def pow(x: float, n: int) -> float:
    if n < 0:
        return 1/pow(x, -n)
    if n == 0:
        return 1
    if n == 1:
        return x

    if n % 2 == 0:
        return pow(x * x, n // 2)
    
    return x * pow(x, n - 1)


if __name__ == '__main__':
    import time
    for i in range(-1000, 1000):
        n = 2 ** i
        now = time.time()
        assert pow(2, i) == n
        done = time.time()
        print(f'pow(2, {i}) took {done - now}')