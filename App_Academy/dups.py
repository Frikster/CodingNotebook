 # Write an Array#dups method that will return a hash containing the indices of all
 # duplicate elements. The keys are the duplicate elements; the values are
 # arrays of their indices in ascending order, e.g.
 # [1, 3, 4, 3, 0, 3, 0].dups => { 3 => [1, 3, 5], 0 => [4, 6] }

def dups(arr):
    res = {}
    for idx, el in enumerate(arr):
        if el in res:
            res[el].append(idx)
        else: 
            res[el] = [idx]
    return {k:v for k,v in res.items() if len(v) > 1}

print(dups([1, 3, 4, 3, 0, 3, 0]) == {0: [4, 6], 3: [1, 3, 5]})
