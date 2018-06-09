import requests


r= 'https://stepic.org/media/attachments/course67/3.6.3/'
file = '699991.txt'
while 'We' not in file:
    l= r+file
    print(requests.get(l).text)
    file= requests.get(l).text