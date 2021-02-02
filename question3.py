

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

# time complexity - O(N)
# space complexity - O(1)