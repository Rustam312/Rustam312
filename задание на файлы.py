def number(f, i):
    if f[i].isdigit():
        numb = ''
        while f[i].isdigit():
            if f[i]!=f[-1]:
                numb+= f[i]
                i+=1
            else:
                numb+=f[i]
                break
        return int(numb)



with open('/Users/rustam/Desktop/dataset_3363_2-3.txt', 'r') as file:
    f= file.read()
id= 0
result=''
string=[i for i in f if i.isalpha()]
numb=[]
for j in range(len(f)):
    if f[j].isalpha():
        numb.append(number(f, j+1))
while id != len(string):
    result+=string[id]*numb[id]
    id+=1
with open('/Users/rustam/Desktop/dataset_3363_2-3.txt', 'w') as file:
    f= file.write(result)