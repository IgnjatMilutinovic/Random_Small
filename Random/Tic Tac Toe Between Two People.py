
A1=' '
A2=' '
A3=' ' 
B1=' '
B2=' '
B3=' '
C1=' '
C2=' '
C3=' '
A=[A1,A2,A3]
B=[B1,B2,B3]
C=[C1,C2,C3]
def CallWorld():
    print(A)
    print(B)
    print(C)
print(['A1','A2','A3'])
print(['B1','B2','B3'])
print(['C1','C2','C3'])
FirstMove=input()
if FirstMove=='A1':
    A[0]='X'
    CallWorld()
if FirstMove=='A2':
    A[1]='X'
    CallWorld()
if FirstMove=='A3':
    A[2]='X'
    CallWorld()
if FirstMove=='B1':
    B[0]='X'
    CallWorld()
if FirstMove=='B2':
    B[1]='X'
    CallWorld()
if FirstMove=='B3':
    B[2]='X'
    CallWorld()
if FirstMove=='C1':
    C[0]='X'
    CallWorld()
if FirstMove=='C2':
    C[1]='X'
    CallWorld()
if FirstMove=='C3':
    C[2]='X'
    CallWorld()

SecondMove=input()
if SecondMove=='A1':
    A[0]='O'
    CallWorld()
if SecondMove=='A2':
    A[1]='O'
    CallWorld()
if SecondMove=='A3':
    A[2]='O'
    CallWorld()
if SecondMove=='B1':
    B[0]='O'
    CallWorld()
if SecondMove=='B2':
    B[1]='O'
    CallWorld()
if SecondMove=='B3':
    B[2]='O'
    CallWorld()
if SecondMove=='C1':
    C[0]='O'
    CallWorld()
if SecondMove=='C2':
    C[1]='O'
    CallWorld()
if SecondMove=='C3':
    C[2]='O'
    CallWorld()

ThirdMove=input()
if ThirdMove=='A1':
    A[0]='X'
    CallWorld()
if ThirdMove=='A2':
    A[1]='X'
    CallWorld()
if ThirdMove=='A3':
    A[2]='X'
    CallWorld()
if ThirdMove=='B1':
    B[0]='X'
    CallWorld()
if ThirdMove=='B2':
    B[1]='X'
    CallWorld()
if ThirdMove=='B3':
    B[2]='X'
    CallWorld()
if ThirdMove=='C1':
    C[0]='X'
    CallWorld()
if ThirdMove=='C2':
    C[1]='X'
    CallWorld()
if ThirdMove=='C3':
    C[2]='X'
    CallWorld()

FourthMove=input()
if FourthMove=='A1':
    A[0]='O'
    CallWorld()
if FourthMove=='A2':
    A[1]='O'
    CallWorld()
if FourthMove=='A3':
    A[2]='O'
    CallWorld()
if FourthMove=='B1':
    B[0]='O'
    CallWorld()
if FourthMove=='B2':
    B[1]='O'
    CallWorld()
if FourthMove=='B3':
    B[2]='O'
    CallWorld()
if FourthMove=='C1':
    C[0]='O'
    CallWorld()
if FourthMove=='C2':
    C[1]='O'
    CallWorld()
if FourthMove=='C3':
    C[2]='O'
    CallWorld()

FifthMove=input()
if FifthMove=='A1':
    A[0]='X'
    CallWorld()
if FifthMove=='A2':
    A[1]='X'
    CallWorld()
if FifthMove=='A3':
    A[2]='X'
    CallWorld()
if FifthMove=='B1':
    B[0]='X'
    CallWorld()
if FifthMove=='B2':
    B[1]='X'
    CallWorld()
if FifthMove=='B3':
    B[2]='X'
    CallWorld()
if FifthMove=='C1':
    C[0]='X'
    CallWorld()
if FifthMove=='C2':
    C[1]='X'
    CallWorld()
if FifthMove=='C3':
    C[2]='X'
    CallWorld()
    
if A[0]=='X' and A[1]=='X' and A[2]=='X' or B[0]=='X' and B[1]=='X' and B[2]=='X' or C[0]=='X' and C[1]=='X' and C[2]=='X' or A[0]=='X' and B[0]=='X' and C[0]=='X' or A[1]=='X' and B[1]=='X' and C[1]=='X' or A[2]=='X' and B[2]=='X' and C[2]=='X' or A[0]=='X' and B[1]=='X' and C[2]=='X' or C[0]=='X' and B[1]=='X' and A[2]=='X':
    print('Xs Won, Congratulations!')

SixthMove=input()
if SixthMove=='A1':
    A[0]='O'
    CallWorld()
if SixthMove=='A2':
    A[1]='O'
    CallWorld()
if SixthMove=='A3':
    A[2]='O'
    CallWorld()
if SixthMove=='B1':
    B[0]='O'
    CallWorld()
if SixthMove=='B2':
    B[1]='O'
    CallWorld()
if SixthMove=='B3':
    B[2]='O'
    CallWorld()
if SixthMove=='C1':
    C[0]='O'
    CallWorld()
if SixthMove=='C2':
    C[1]='O'
    CallWorld()
if SixthMove=='C3':
    C[2]='O'
    CallWorld()
    
if A[0]=='O' and A[1]=='O' and A[2]=='O' or B[0]=='O' and B[1]=='O' and B[2]=='O' or C[0]=='O' and C[1]=='O' and C[2]=='O' or A[0]=='O' and B[0]=='O' and C[0]=='O' or A[1]=='O' and B[1]=='O' and C[1]=='O' or A[2]=='O' and B[2]=='O' and C[2]=='O' or A[0]=='O' and B[1]=='O' and C[2]=='O' or C[0]=='O' and B[1]=='O' and A[2]=='O':
    print('Ox Won, Congratulations!')

SeventhMove=input()
if SeventhMove=='A1':
    A[0]='X'
    CallWorld()
if SeventhMove=='A2':
    A[1]='X'
    CallWorld()
if SeventhMove=='A3':
    A[2]='X'
    CallWorld()
if SeventhMove=='B1':
    B[0]='X'
    CallWorld()
if SeventhMove=='B2':
    B[1]='X'
    CallWorld()
if SeventhMove=='B3':
    B[2]='X'
    CallWorld()
if SeventhMove=='C1':
    C[0]='X'
    CallWorld()
if SeventhMove=='C2':
    C[1]='X'
    CallWorld()
if SeventhMove=='C3':
    C[2]='X'
    CallWorld()
    
if A[0]=='X' and A[1]=='X' and A[2]=='X' or B[0]=='X' and B[1]=='X' and B[2]=='X' or C[0]=='X' and C[1]=='X' and C[2]=='X' or A[0]=='X' and B[0]=='X' and C[0]=='X' or A[1]=='X' and B[1]=='X' and C[1]=='X' or A[2]=='X' and B[2]=='X' and C[2]=='X' or A[0]=='X' and B[1]=='X' and C[2]=='X' or C[0]=='X' and B[1]=='X' and A[2]=='X':
    print('Xs Won, Congratulations!')

EigthMove=input()
if EigthMove=='A1':
    A[0]='O'
    CallWorld()
if EigthMove=='A2':
    A[1]='O'
    CallWorld()
if EigthMove=='A3':
    A[2]='O'
    CallWorld()
if EigthMove=='B1':
    B[0]='O'
    CallWorld()
if EigthMove=='B2':
    B[1]='O'
    CallWorld()
if EigthMove=='B3':
    B[2]='O'
    CallWorld()
if EigthMove=='C1':
    C[0]='O'
    CallWorld()
if EigthMove=='C2':
    C[1]='O'
    CallWorld()
if EigthMove=='C3':
    C[2]='O'
    CallWorld()
    
if A[0]=='O' and A[1]=='O' and A[2]=='O' or B[0]=='O' and B[1]=='O' and B[2]=='O' or C[0]=='O' and C[1]=='O' and C[2]=='O' or A[0]=='O' and B[0]=='O' and C[0]=='O' or A[1]=='O' and B[1]=='O' and C[1]=='O' or A[2]=='O' and B[2]=='O' and C[2]=='O' or A[0]=='O' and B[1]=='O' and C[2]=='O' or C[0]=='O' and B[1]=='O' and A[2]=='O':
    print('Ox Won, Congratulations!')

NinthMove=input()
if NinthMove=='A1':
    A[0]='X'
    CallWorld()
if NinthMove=='A2':
    A[1]='X'
    CallWorld()
if NinthMove=='A3':
    A[2]='X'
    CallWorld()
if NinthMove=='B1':
    B[0]='X'
    CallWorld()
if NinthMove=='B2':
    B[1]='X'
    CallWorld()
if NinthMove=='B3':
    B[2]='X'
    CallWorld()
if NinthMove=='C1':
    C[0]='X'
    CallWorld()
if NinthMove=='C2':
    C[1]='X'
    CallWorld()
if NinthMove=='C3':
    C[2]='X'
    CallWorld()
    
if A[0]=='X' and A[1]=='X' and A[2]=='X' or B[0]=='X' and B[1]=='X' and B[2]=='X' or C[0]=='X' and C[1]=='X' and C[2]=='X' or A[0]=='X' and B[0]=='X' and C[0]=='X' or A[1]=='X' and B[1]=='X' and C[1]=='X' or A[2]=='X' and B[2]=='X' and C[2]=='X' or A[0]=='X' and B[1]=='X' and C[2]=='X' or C[0]=='X' and B[1]=='X' and A[2]=='X':
    print('Xs Won, Congratulations!')
else:
    print("It's A Draw")







