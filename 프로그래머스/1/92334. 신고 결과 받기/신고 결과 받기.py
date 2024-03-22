def solution(id_list, report, k):
    n = len(id_list)
    report = list(set(report))
    result = [0]*n
    
    dic = {i:0 for i in id_list}
    
    for rp in report:
        a, b = rp.split()
        dic[b] += 1
    
    for rp in report:
        a, b = rp.split()
        if dic[b] >= k:
            result[id_list.index(a)] += 1
    
    return result