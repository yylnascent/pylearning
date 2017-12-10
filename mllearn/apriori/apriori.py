"""
 An Implementation of Apriori Algorithm
"""

def load_dataset():
    return [[1,3,4], [2,3,5], [1,2,3,5], [2,5]]

def create_c1(dataset):
    c1 = []
    for transaction in dataset:
        for item in transaction:
            if [item] not in c1:
                c1.append([item])
    c1.sort()
    return map(frozenset, c1)

def scan_dataset(dataset, ck, min_support):
    sscnt = {}
    for tid in dataset:
        for can in ck:
            if can.issubset(tid):
                sscnt[can] = 1 if can not in sscnt else sscnt[can] + 1

    item_num = float(len(dataset))
    retlist = []
    support_data = {}
    for can, occur_cn in sscnt.items():
        support = occur_cn/item_num
        if support >= min_support:
            retlist.append(can)
        support_data[can] = support
    
    return retlist, support_data
                   
def gen_apriori(lk, k):
    retlist = []
    lk_len = len(lk)
    for i in range(lk_len):
        for j in range(i+1, lk_len):
            l1 = list(lk[i])[:k-2]
            l2 = list(lk[j])[:k-2]
            l1.sort()
            l2.sort()
            if l1 == l2:
                retlist.append(lk[i] | lk[j])

    return retlist

def apriori(data_set, min_support=0.5):
    c1 = create_c1(data_set)
    data = map(set, data_set)
    l1, support_data = scan_dataset(data, c1, min_support)
    l = [l1]
    k = 2
    while (len(l[k-2]) > 0):
        ck = gen_apriori(l[k-2], k)
        lk, supk = scan_dataset(data_set, ck, min_support)
        support_data.update(supk)
        l.append(lk)
        k += 1

    return l, support_data

