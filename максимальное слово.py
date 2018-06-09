with open('/Users/rustam/Downloads/dataset_3363_3-2.txt', 'r') as file:
    f= file.read()
words= f.lower().split()
set_words=set(words)
numb=[]
d=[]
for i in set_words:
    numb.append(words.count(i))
l= list(set_words)
# l - список слов без повтора
for j in range(len(l)):
    if max(numb) == words.count(l[j]):
        d.append(l[j])
d.sort()
print(d[0], max(numb))
