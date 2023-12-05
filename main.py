import pygame as pg

def ins(str, ch, pos):
    
    if not (ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
        print('This character is not a vowel!')
        input()
        return(str+' 0')
    
    a=[]
    
    for i in range(0,len(str)):
        
        if i==pos:
            
            a.append(ch)
            
        a.append(str[i])
    
    if pos==len(str): a.append(ch)
    
    return(''.join(a)+' 1')

def det(str, pos):
    
    ch=str[pos]
    
    if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
        
        a=''
        
        for i in range(0,len(str)):
            
            if i!=pos:
                
                a+=str[i]
                
        return(a+' 1')
    
    else: 
        
        print('The character at the place you selected was not a vowel!')
        input()
        return(str+' 0')


def clear():
    
    for i in range(0,100): print('\n')


data=open('vwllss.txt')

levels = []

N,min_score=data.readline().split()


N=int(N)

min_score=int(min_score)
for i in range(0,N):
    levels.append(data.readline().split())

input("Welcome to VWLLSS!")

clear()

score=0 #overall
tries=0 #for select stage

correct=''
inp=''

for i in range(0,N):
    
    clear()
    
    tries=0
    
    inp=levels[i][0]
    correct=levels[i][1]
    
    while not inp==correct:
        clear()
        print("STAGE "+ str(i+1))
        print('Turn '+str(tries+1))
        print('Word Progress: '+inp)
        
        attempt,pos=input().split()
        pos=int(pos)
        pos=max(0,min(int(len(inp)),pos))
        tr=0
        clear()
        if attempt=='-':
            
            pos=max(pos,1)
            pos -= 1
            
            inp,tr=det(inp, pos).split()
            
        else:
            
            inp,tr=ins(inp,attempt,pos).split()
            
        tr=int(tr)
        
        tries+=tr
        
    
    clear()
    
    print('Good job!')
    print('You took '+str(tries)+' turns to complete this word')
    
    score+=tries
    input()

clear()

print('Game Complete!')

print('You took '+str(score)+' turns to complete this game!')
print('The minimum possible was '+str(min_score)+'!')

if score==min_score:
    print('Good job!')

            
        
        
        

