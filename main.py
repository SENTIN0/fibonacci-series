r=' TEAM '
q='                           '
p=' TOOL BY SENTINO '
o='                        '
n='╚═╝     ╚═╝╚═════╝  ╚════  ╚═╝  ╚══╝╚═╝  ╚═╝ ╚════╝  ╚════╝ ╚═╝'
m='██║     ██║██████╦╝╚█████╔╝██║ ╚███║██║  ██║╚█████╔╝╚█████╔╝██║'
l='██╔══╝  ██║██╔══██╗██║  ██║██║╚████║██╔══██║██║  ██╗██║  ██╗██║'
k='█████╗  ██║██████╦╝██║  ██║██╔██╗██║███████║██║  ╚═╝██║  ╚═╝██║'
j='██╔════╝██║██╔══██╗██╔══██╗████╗ ██║██╔══██╗██╔══██╗██╔══██╗██║'
i='███████╗██╗██████╗  █████╗ ███╗  ██╗ █████╗  █████╗  █████╗ ██╗'
f='_______________________________________________________________'
e='\x1b[0m'
d='\x1b[4m'
c='\x1b[1m'
b='\x1b[47m'
a='\x1b[46m'
Z='\x1b[45m'
Y='\x1b[44m'
X='\x1b[43m'
W='\x1b[42m'
V='\x1b[41m'
U='\x1b[40m'
T='\x1b[37m'
S='\x1b[36m'
R='\x1b[35m'
Q='\x1b[34m'
P='\x1b[33m'
O='\x1b[32m'
N='\x1b[31m'
M='\x1b[30m'
I='r'
H='win'
G=open
J='fibonacci_numbers.txt'
F=int
D=input
B=''
A=print
import os,sys as C,subprocess as K,time as E,requests as g,webbrowser as s
z=J
def t(O0O00O0O00OOOO0O0):
	B=O0O00O0O00OOOO0O0
	if C.platform.startswith(H):s.open(B)
	elif C.platform.startswith('linux'):os.system(f"termux-open-url {B}")
	else:A('Unsupported platform. Unable to open the link.')
def u():
	A='update.py'
	if C.platform.startswith(H):K.run(['python',A],shell=True)
	else:K.run(['python3',A])
def __avalability__():
	A('\x1b[96mChecking the status of the tool\x1b[0m');A(B);A('\x1b[94mCheck availability of tool\x1b[0m');D=g.get('https://ebomb.cyclic.app/fibonacci')
	if D.status_code==200:
		F=D.json()
		if F.get('version')!='1.1':A(B);A('\x1b[41m \x1b[30m Current version is not 1.1  Please update the tool...\x1b[0m');E.sleep(2);u();return
		if F.get('tool')=='enabled':A(B);A('Tool is available ✅️ . Running the tool...');E.sleep(1);__main__()
		else:A('Tool is not enabled. Exiting...Update tool');E.sleep(8);C.exit()
	else:A('Error occurred while requesting status endpoint:',D.status_code)
def v(OO00OOOOOOOOO0000,OOOOOO0OOO0OOOO0O,O0OOOO0OO000O000O):
	B=0;C=[]
	with G(O0OOOO0OO000O000O,I)as D:E=[F(A)for A in D]
	for A in E:
		if A>OO00OOOOOOOOO0000 and A<OOOOOO0OOO0OOOO0O:B+=len(str(A));C.append(A)
	return B,C
def w(O00O0OO0OO0O0O000,OOOO0OO0OO0OOOO0O):
	A=OOOO0OO0OO0OOOO0O;B=[]
	with G(O00O0OO0OO0O0O000,I)as C:
		D=C.readlines()
		for E in D:H=F(E.strip());B.append(H)
	if A>=0 and A<len(B):return F(B[A])
	else:return'Invalid location!'
def x(O0OO000OO0OOOOOOO,O00O0O000OO0OO0O0):
	with G(O0OO000OO0OOOOOOO,I)as B:C=[F(A.strip())for A in B]
	A=None
	for(D,E)in enumerate(C):
		if E==O00O0O000OO0OO0O0:A=D;break
	return A if A is not None else-1
def h():
	if C.platform.startswith(H):os.system('cls')
	else:os.system('clear')
def y(OO0000OOOOO00O0O0):
	j='and';I='Press Any key To Main Menu . . . ';E=OO0000OOOOO00O0O0;G=M;o=N;K=O;p=P;q=Q;r=R;s=S;u=T;y=U;z=V;A0=W;A1=X;A2=Y;A3=Z;A4=a;H=b;A5=c;A6=d;C=e
	if E==1:
		L();f=F(D(K+'Enter the location of the Fibonacci number: '+C))
		if f>=1000:A('\n More than 1000 places are not in my database.Sorry for the inconveniece');A(B);A(B);D(H+G+I+C);__main__()
		else:k=w(J,f);A(B);A(f"The Fibonacci number at location {f} is {k}");A(B);A(B);D(H+G+I+C);__main__()
	elif E==2:
		L();A(B);g=F(D(K+'Enter the Fibonacci number: '+C))
		if g>0x14eb22fa5f1a92ba5c694a4fb84cfb88f214d32d10cff2e67f9e9eb767356c85933c369d8cac802f797a3f8e9b7b754ae6682e43b647097b3a9cc2670aee7b1c1939e1ee831c4c8bcd2def142b85d872a7ca8af1d500a2:A(B);A(' Sorry !!!! I have not stored such a large number in my database');A(B);A(B);D(H+G+I+C);__main__()
		else:l=x(J,g);A(B);A(f"The Fibonacci number {g} is at location {l}");A(B);A(B);D(H+G+I+C);__main__()
	elif E==3:L();A(B);h=F(D(K+'Start : '+C));i=F(D(K+'End : '+C));m,n=v(h,i,J);A(B);A(B);A('Number of digits between',h,j,i,':',m);A(B);A(B);A('Digits between',h,j,i,':',n);A(B);D(H+G+I+C);__main__()
	elif E==4:t('https://api.whatsapp.com/send/?phone=94712237369&text&type=phone_number&app_absent=0');A(B)
	elif E==5:A(B)
	else:__main__()
def L():E=M;D=N;L=O;g=P;G=Q;s=R;t=S;u=T;v=U;w=V;x=W;H=X;y=Y;z=Z;I=a;J=b;F=c;K=d;C=e;h();A(B);A(B);A(D+i+C);A(D+j+C);A(D+k+C);A(D+l+C);A(D+m+C);A(D+n+C);A(B);A(o+F+K+H+E+p+C);A(q+F+J+D+' J'+E+'F '+C+B+I+E+r+C);A(B);A(G+f+C);A(B);A(B);A(B);A(B)
def __main__():L=']';K='[';J='           ';g=M;G=N;E=O;H=P;s=Q;A0=R;I=S;A1=T;A2=U;A3=V;A4=W;u=X;A5=Y;A6=Z;v=a;w=b;t=c;x=d;C=e;h();A(B);A(B);A(G+i+C);A(G+j+C);A(G+k+C);A(G+l+C);A(G+m+C);A(G+n+C);A(B);A(o+t+x+u+g+p+C);A(q+t+w+G+' J'+g+'F '+C+B+v+g+r+C);A(B);A(s+f+C);A(B);A(B);A(J+E+K+H+'1'+E+L+I+' Get Fibonacci number by location'+C);A(B);A(J+E+K+H+'2'+E+L+I+' Get location by Fibonacci number'+C);A(B);A(J+E+K+H+'3'+E+L+I+' Fibonacci numbers between two numbers'+C);A(B);A(J+E+K+H+'4'+E+L+I+' REPORT ABOUT BUGS'+C);A(B);A(J+E+K+H+'5'+E+L+G+' EXIT'+C);A(B);A(s+f+C);A(B);A(B);z=F(D(I+'Enter your choice (1-5) : '+C));y(z)
__avalability__()