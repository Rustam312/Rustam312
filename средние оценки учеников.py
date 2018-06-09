
stud = []
m, p, r= 0, 0, 0
with open('/Users/rustam/Downloads/dataset_3363_4-2.txt', 'r') as file:
    for line in file:
        stud.append(line.strip().split(';'))
for surname, math, physics, russian in stud:
    print((int(math) +int(physics)+ int(russian))/3)
for el in stud:
    m+=int(el[1])
    p+=int(el[2])
    r+=int(el[3])
print((m/len(stud)), (p/len(stud)), (r/len(stud)))