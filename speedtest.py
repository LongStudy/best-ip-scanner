
import requests
import re
import os

china=['中国']
asia=['日本', '韩国', '新加坡', '印度', '澳大利亚']
europe=['德国', '法国', '英国', '俄罗斯', '荷兰']
america=['美国', '加拿大']
google=['Google']
allarea=china+asia+europe+america+google
chinaip=[]
asiaip=[]
europeip=[]
americaip=[]
googleip=[]

urlgit = 'https://github.com/ip-scanner/cloudflare'
url = 'https://raw.githubusercontent.com/ip-scanner/cloudflare/master/'
proxies = {"http": "http://127.0.0.1:7890", "https": "http://127.0.0.1:7890"}
res = requests.get(urlgit, proxies=proxies)
#print(res.text)

matchtxt = re.compile(r'(?<=title=").*.txt(?=" data-pjax)')
matchtxtlist = matchtxt.findall(res.text)
#print(matchtxtlist)


matchremovelist = matchtxtlist + []

for i in matchtxtlist:
    for j in allarea:
        if j in i:
            matchremovelist.remove(i)

print('new area:' + str(matchremovelist))

# china
for i in china:
    for j in matchtxtlist:
        if i in j:
            print('downloading' + j + 'by proxy')
            chinaip.append((requests.get(url+j, proxies=proxies).text))
fo = open("chinaip.txt", "w")
for i in chinaip:
    fo.write(i)
fo.close()
print(chinaip)

# asia
for i in asia:
    for j in matchtxtlist:
        if i in j:
            print(j)
            asiaip.append((requests.get(url+j, proxies=proxies).text))
fo = open("asiaip.txt", "w")
for i in asiaip:
    fo.write(i)
fo.close()
print(asiaip)

# europe
for i in europe:
    for j in matchtxtlist:
        if i in j:
            print(j)
            europeip.append((requests.get(url+j, proxies=proxies).text))
fo = open("europeip.txt", "w")
for i in europeip:
    fo.write(i)
fo.close()
print(europeip)

# america
for i in america:
    for j in matchtxtlist:
        if i in j:
            print(j)
            americaip.append((requests.get(url+j, proxies=proxies).text))
fo = open("americaip.txt", "w")
for i in americaip:
    fo.write(i)
fo.close()
print(americaip)

# google
for i in google:
    for j in matchtxtlist:
        if i in j:
            print(j)
            googleip.append((requests.get(url+j, proxies=proxies).text))
fo = open("googleip.txt", "w")
for i in googleip:
    fo.write(i)
fo.close()
print(googleip)




# not working

# cmdchina = 'CloudflareST.exe -f chinaip.txt'
# outchian = os.popen(cmdchina).readline()
# print(outchian)

# cmdasia = 'CloudflareST.exe -f asiaip.txt'
# outasia = os.popen(cmdasia).read()
# print(outasia.decode('gbk').encode('utf-8'))

# cmdeurope = 'CloudflareST.exe -f europeip.txt'
# outeurope = os.popen(cmdeurope).read()
# print(outeurope.decode('utf-8'))

# cmdamerica = 'CloudflareST.exe -f americaip.txt'
# outamerica = os.popen(cmdamerica).read()
# print(outamerica.decode('utf-8'))

# cmdgoogle = 'CloudflareST.exe -f googleip.txt'
# outgoogle = os.popen(cmdgoogle).read()
# print(outgoogle.decode('gbk').encode('utf-8'))
