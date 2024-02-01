grade = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+":1.5, "D0": 1.0, "F": 0}
total_num = 0
sum_grade = 0

for i in range(20):
    n, g, s = input().split()
    g = float(g)
    if s != "P":
        total_num += g
        sum_grade += grade[s] * g
avg = sum_grade / total_num
print(avg)