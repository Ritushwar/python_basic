NUMBER_OF_DISK = 4
A = list(range(NUMBER_OF_DISK,0,-1)) #source
B = []                               #Aux
C = []                               #Destination
def move(n,source,auxiliary,target):
    if n<=0:
        return
    move(n-1,source,target,auxiliary)
    target.append(source.pop())
    print(A,B,C,"\n")
    move(n-1,auxiliary,source,target)

move(NUMBER_OF_DISK,A,B,C)