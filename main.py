import pygame as pg

pg.init()

WX=1280
WY=720
DELAY=200
screen =  pg.display.set_mode((WX,WY))
pg.display.set_caption("VWLLSS")
font = pg.font.SysFont('courier', 100)


clock = pg.time.Clock()
clock.tick(30)

data=open('vwllss.txt')

levels = []

N,min_score=data.readline().split()


N=int(N)

min_score=int(min_score)
for i in range(0,N):
    levels.append(data.readline().split())





def ins(str, ch, pos): #insert character into string at position pos
    
    if not (ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
        print('This character is not a vowel!')
        return(str+' 0')
    
    a=[]
    
    for i in range(0,len(str)):
        
        if i==pos:
            
            a.append(ch)
            
        a.append(str[i])
    
    if pos==len(str): a.append(ch)
    
    return(''.join(a)+' 1')

def det(str, pos): #remove character as position pos in string str
    
    ch=str[pos]
    
    if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
        
        a=''
        
        for i in range(0,len(str)):
            
            if i!=pos:
                
                a+=str[i]
                
        return(a+' 1')
    
    else: 
        
        print('The character at the place you selected was not a vowel!')
        return(str+' 0')

def spacer(): #wait until space pressed
    rep=True
    while rep:
        closeable()
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            rep=False

def overall(x): #display text
    txtout=pg.font.SysFont('courier',25).render('Overall turns taken: '+str(x), True, (255,255,255))
    screen.blit(txtout,(10,10))

def sout(txt,size,loc): #display text
    txtout=pg.font.SysFont('courier', size).render(txt, True, (255,255,255))
    txtout_rect=txtout.get_rect(center=loc)
    screen.blit(txtout,txtout_rect)
#PYGAME EDITION




def clear(): #clear the screen
    screen.fill((0,0,0))



window=True

def closeable():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

clear()
rep=True

sout("VWLLSS",200,(WX/2,WY/2))
sout("press space to continue",25,(WX/2,10))
pg.display.flip()
spacer()


score=0 #overall
tries=0 #for select stage

correct=''
inp=''

for i in range(0,N):
    
    clear()
    
    tries=0
    
    inp=levels[i][0] #data that the user is editing
    correct=levels[i][1] #correct answer
    sout("stage "+str(i+1),200,(WX/2,WY/2))
    pg.display.flip()
    pg.time.wait(1000)
    while not inp==correct:
        clear()
        
        pg.display.flip()
        sout('turn '+str(tries+1), 200, (WX/2,WY/2))
        pg.display.flip()
        pg.time.wait(1000)
        
        
        clear()
        overall((score+tries))
        sout(inp,100,(WX/2,WY/2-50))
        pg.display.flip()
        
        a=False#attempt input?
        p=False#pos input?
        
        attempt=''
        pos=''
        
        prg=''
        while not a:#get edit typep
            closeable()
            keys = pg.key.get_pressed()
            if keys[pg.K_a]:
                attempt='a'
                a=True
            if keys[pg.K_e]:
                attempt='e'
                a=True
            if keys[pg.K_i]:
                attempt='i'
                a=True
            if keys[pg.K_o]:
                attempt='o'
                a=True
            if keys[pg.K_u]:
                attempt='u'
                a=True
            if keys[pg.K_MINUS]:
                attempt='-'
                a=True
        clear()
        overall((score+tries))
        sout(inp,100,(WX/2,WY/2-50))
        prg+=attempt
        sout(prg,100,(WX/2,WY/2+50))
        pg.display.flip()
        

        
        t0,t1,t2,t3,t4,t5,t6,t7,t8,t9,td=0,0,0,0,0,0,0,0,0,0,0
        while not p:#get edit pos
            closeable()
            clear()
            
            sout(inp,100,(WX/2,WY/2-50))
            sout(prg+' '+pos,100,(WX/2,WY/2+50))
            
            overall(score+tries)
            
            pg.display.flip()
            
            keys = pg.key.get_pressed()
            curt=pg.time.get_ticks()
            if keys[pg.K_0] and curt>(t0+DELAY):
                if pos!='':
                    pos+='0'
                    t0=curt
            elif curt>(t1+DELAY) and keys[pg.K_1]:
                pos+='1'
                t1=curt
            elif curt>(t2+DELAY) and keys[pg.K_2]:
                pos+='2'
                t2=curt
            elif curt>(t3+DELAY) and keys[pg.K_3]:
                pos+='3'
                t3=curt
            elif curt>(t4+DELAY) and keys[pg.K_4]:
                pos+='4'
                t4=curt
            elif curt>(t5+DELAY) and keys[pg.K_5]:
                pos+='5'
                t5=curt
            elif curt>(t6+DELAY) and keys[pg.K_6]:
                pos+='6'
                t6=curt
            elif curt>(t7+DELAY) and keys[pg.K_7]:
                pos+='7'
                t7=curt
            elif curt>(t8+DELAY) and keys[pg.K_8]:
                pos+='8'
                t8=curt
            elif curt>(t9+DELAY) and keys[pg.K_9]:
                pos+='9'
                t9=curt
            elif curt>(td+DELAY) and keys[pg.K_BACKSPACE]:
                a=pos[0:len(pos)-1]
                pos=a
                td=curt
            elif keys[pg.K_RETURN]:
                p=True
        prg+=' '+pos
        
        
        pos=int(pos)
        pos=max(1,min(int(len(inp)+1),pos))
        tr=0
        
        clear()
        pos-=1
        if attempt=='-':
            inp,tr=det(inp, pos).split()
        else:
            inp,tr=ins(inp,attempt,pos).split()
            
        tr=int(tr)
        tries+=tr
        
    
    clear()
    
    
    
    overall(score+tries)
    sout("Good Job!", 100, (WX/2,WY/2))
    pg.display.flip()
    
    spacer()
    clear()
    
    
    pg.time.wait(200)
    
    overall(score+tries)
    sout('You took '+str(tries)+' turns', 100, (WX/2,WY/2))
    pg.display.flip()
    spacer()
    
    score+=tries

clear()

comp=pg.font.SysFont('courier', 150).render("GAME COMPLETE", True, (255,255,255))
comp_rect=comp.get_rect(center=(WX/2,WY/2-150))
screen.blit(comp,comp_rect)
sout("GAME COMPLETE", 150, (WX/2,WY/2-150))
pg.display.flip()
pg.time.wait(500)
sout('You took '+str(score)+' turns in total!', 75, (WX/2,WY/2))
pg.display.flip()
pg.time.wait(500)
sout('The minimum possible was '+str(min_score)+'!', 75, (WX/2,WY/2+150))
pg.display.flip()

spacer()

clear()
pg.time.wait(200)
if score==min_score:
    sout("Good Job!", 200, (WX/2,WY/2))
    pg.display.flip()
    spacer()
pg.quit()
    
