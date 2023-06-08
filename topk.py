from typing import List

# O(n) + O(u*log(u)) where n is the number of elements in nums and u is the number of unique elements in nums
def topk(nums: List[int], k: int) -> List[int]:

    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    return [x[0] for x in sorted(freq.items(), key=lambda x: -x[1])][:k]




if __name__ == '__main__':
    import timeit
    import random

    l = [random.randrange(1, 1000, 1) for _ in range(0, 1000000)]

    for i in range(0, 10):
        print(topk(l, i+1))
        print(f'{i}: {timeit.timeit("".join(map(str, topk(l, i+1))), number=100000)}')
