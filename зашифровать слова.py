
def transform(x):
    lst=[]
    for i in x:
        lst.append(i)
    return lst

def cryptographer(cipher, x):
    new=''
    for symbol in x:
        new +=symbol.replace(symbol, cipher[symbol])
    return new

a= 'abcd'
b= '*d%#'
c= 'abacabadaba'
d= '#*%*d*%'

cipher_in= dict(zip(transform(a), transform(b)))
cipher_out= dict(zip(transform(b), transform(a)))

print(cryptographer(cipher_in, c)+'\n'+cryptographer(cipher_out, d))