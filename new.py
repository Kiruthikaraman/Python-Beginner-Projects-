from bisect import bisect_left
from typing import List, Tuple

# /g:/Python project/new.py

def lis_length_and_sequence(A: List[int]) -> Tuple[int, List[int]]:
    """
    Return (length, one_strictly_increasing_subsequence) of A.
    O(n log n) time, O(n) extra space.
    """
    n = len(A)
    if n == 0:
        return 0, []

    tails: List[int] = []        # values of the current tails
    tails_idx: List[int] = []    # corresponding indices in A
    prev: List[int] = [-1] * n   # previous index in the subsequence

    for i, x in enumerate(A):
        pos = bisect_left(tails, x)  # first index with tails[pos] >= x
        if pos == len(tails):
            tails.append(x)
            tails_idx.append(i)
        else:
            tails[pos] = x
            tails_idx[pos] = i
        if pos > 0:
            prev[i] = tails_idx[pos - 1]

    # Reconstruct one LIS
    k = len(tails)
    seq: List[int] = []
    idx = tails_idx[-1]
    while idx != -1:
        seq.append(A[idx])
        idx = prev[idx]
    seq.reverse()

    return k, seq

if __name__ == "__main__":
    # Example
    A = [10, 9, 2, 5, 3, 7, 101, 18]
    length, sequence = lis_length_and_sequence(A)
    print("LIS length =", length)
    print("One LIS =", sequence)