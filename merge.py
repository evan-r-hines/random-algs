from typing import List
# Pretty bad O(n*nlog(n)) solution but it works. 
def merge(intervals: List[List[int]]) -> List[List[int]]:
    merged = True

    # Ever iteration merges at least one interval so we need to keep going until we don't merge any
    # O(nlog(n)) for the sort and O(n) for the while loop so O(nlog(n) * n)
    while merged:
        merged = False
        intervals = sorted(intervals, key=lambda x: -x[1])
        k = len(intervals) - 1
        i = 0
        while i < k:
            if intervals[i][1] >= intervals[i+1][0] and min(intervals[i][1], intervals[i+1][1]) >= max(intervals[i][0], intervals[i+1][0]):
                merged = True
                intervals[i] = [min(intervals[i][0], intervals[i+1][0]), max(intervals[i+1][1], intervals[i][1])]
                del(intervals[i+1])
                k -= 1

            i += 1
                    
    return intervals

if __name__ == '__main__':
    import timeit

    l = [[1, 3], [2, 6], [8, 10], [15, 18]] * 200

    print(merge(l))
    print(f'{timeit.timeit(lambda: merge(l), number=100) / 100} per iter')
