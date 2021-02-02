liplan_work




def linkedListMerge(ls):
    nls = []
    for l in ls:
        nls.extend(l)
        rmd = set(nls)
        l_rmd = list(rmd)

    return l_rmd


if __name__ == "__main__":
    a = [[2, 4, 9, 2, 1, 6], [9, 5, 22, 1, 0, 56, 8, 5]]

    print(linkedListMerge(a))

import ctypes
import gc


from question2 import DynamicArray, ArrayClass


class MoreF(DynamicArray, ArrayClass):

    def __init__(self, array):
        DynamicArray.__init__(self, array)    
        ArrayClass.__init__(self, array)
        self.array = array

    def contains(self, val):
        exist = val in self.array
        return exist
        
    def reverse(self):
        rev_arr = self.array[::-1]
        return rev_arr

    def insert(self, val, i):
        return self.array[:i] + [val] + self.array[i:]



    # Time Complexity: O(1)
    # Space Complexity: O(1)
