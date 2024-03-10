def solution(today, terms, privacies):
        
    answer = []
    t_y, t_m, t_d = map(int, today.split("."))
    idx = 1
    for priv in privacies:
        date, typ = map(str, priv.split())
        y, m, d = map(int, date.split("."))
        for i in terms:
            a, b = map(str, i.split())
            if typ == a:
                m += int(b)
        y += m//12
        m = m%12

        res = ((t_y-y)*12 + t_m-m)*30 + (t_d-d)
        if res >= 0:
            answer.append(idx)
        idx += 1
        
    return answer