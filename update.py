F='main.py'
A=print
import requests as G,os,subprocess as B,sys
H='https://raw.githubusercontent.com/SENTIN0/fibonacci-serios/main/main.py'
I=F
K='update.py'
C=G.get(H)
L='\x1b[30m'
M='\x1b[31m'
N='\x1b[32m'
O='\x1b[33m'
P='\x1b[34m'
Q='\x1b[35m'
R='\x1b[36m'
S='\x1b[37m'
T='\x1b[40m'
U='\x1b[41m'
V='\x1b[42m'
W='\x1b[43m'
X='\x1b[44m'
Y='\x1b[45m'
Z='\x1b[46m'
a='\x1b[47m'
b='\x1b[1m'
c='\x1b[4m'
d='\x1b[0m'
if C.status_code==200:
	D='temp_main.py'
	with open(D,'w',encoding='utf-8')as J:J.write(C.text)
	os.replace(D,I);A('');A('Update successful!');A('');E=F
	if sys.platform.startswith('win'):B.run(['python',E],shell=True)
	else:B.run(['python3',E])
else:A('Update failed. Please try again later.')