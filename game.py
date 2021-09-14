nmbr1= int(input("write number of rows: "))
num2 = int(input("select 0 or 1: "))
val = bool(num2)
if val == True:
    for i in range(nmbr1+1):
        print(i*'* ')
        i =+1
if val == False:
    for j in range(nmbr1+1):
        print((nmbr1-j)*'* ')
        j =+ 1







