from collections import deque
from typing import Counter, List
import math


def main():
    k = KthLargest(3, [5, -1])
    print(k.add(2))
    print(k.add(1))
    print(k.add(-1))
    print(k.add(3))
    print(k.add(4))


class KthLargest:

    lptr=0
    rptr=0

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.sortedStream = sorted(nums, reverse=True)
        

    def add(self, val: int) -> int:
        if(len(self.sortedStream) < self.k):
            self.left = 0
            self.right = len(self.sortedStream)
            self.binaryInsert(val)
            return self.sortedStream[self.k-1]
        if(val > self.sortedStream[self.k-1]):
            if(val > self.sortedStream[math.floor(self.k/2)]):
                self.left = 0
                self.right = math.floor(self.k/2)
            else:
                self.left = math.floor(self.k/2)
                self.right = self.k
            self.binaryInsert(val)

        return self.sortedStream[self.k-1]

    def binaryInsert(self, val):
        t = math.floor((self.right+self.left)/2)

        if(self.right-self.left < 3):
            for i in range(self.left, self.right+1, 1):
                if(len(self.sortedStream) == i):
                    self.sortedStream.append(val)
                    return
                if(val > self.sortedStream[i]):
                    self.sortedStream.insert(i, val)
                    return

        if(val > self.sortedStream[t]):
            self.right = t
        else:
            self.left = t

        self.binaryInsert(val)

            
        
main()