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



#PYGAME EDITION




def clear(): #clear the screen
    screen.fill((0,0,0))



window=True

def closeable():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

while True:
    clear()
    rep=True
    
    while rep:
        clear()
        closeable()
        sscreen=pg.font.SysFont('courier', 200).render("VWLLSS", True, (255,255,255))
        sscreen_rect=sscreen.get_rect(center=(WX/2,WY/2))
        cont=pg.font.SysFont('courier',25).render("press space to continue", True, (255,255,255))
        cont_rect=cont.get_rect(center=(WX/2, 10))
        screen.blit(cont, cont_rect)
        screen.blit(sscreen, sscreen_rect)
        
        keys = pg.key.get_pressed()
        pg.display.flip()
        if keys[pg.K_SPACE]:
            rep=False

    
    score=0 #overall
    tries=0 #for select stage
    
    correct=''
    inp=''
    
    for i in range(0,N):
        
        clear()
        
        tries=0
        
        inp=levels[i][0] #data that the user is editing
        correct=levels[i][1] #correct answer
        stage=pg.font.SysFont('courier', 200).render("stage "+ str(i+1), True, (255,255,255))
        stage_rect=stage.get_rect(center=(WX/2,WY/2-100))
        screen.blit(stage, stage_rect)
        pg.display.flip()
        pg.time.wait(1000)
        while not inp==correct:
            clear()
            
            pg.display.flip()
            turn=pg.font.SysFont('courier', 200).render('turn '+str(tries+1), True, (255,255,255))
            turn_rect=turn.get_rect(center=(WX/2,WY/2))
            screen.blit(turn, turn_rect)
            pg.display.flip()
            pg.time.wait(1000)
            
            
            clear()
            turnc=pg.font.SysFont('courier',25).render("Overall turns taken: "+str(score+tries),True,(255,255,255))
            screen.blit(turnc, (10,10))
            dis=font.render(inp, True, (255,255,255))
            dis_rect=dis.get_rect(center=(WX/2,WY/2-50))
            screen.blit(dis, dis_rect)
            pg.display.flip()
            
            a=False#attempt input?
            p=False#pos input?
            
            attempt=''
            pos=''
            
            prg=''
            while not a:
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
            turnc=pg.font.SysFont('courier',25).render("Overall turns taken: "+str(score+tries),True,(255,255,255))
            screen.blit(turnc, (10,10))
            dis=font.render(inp, True, (255,255,255))
            dis_rect=dis.get_rect(center=(WX/2,WY/2-50))
            screen.blit(dis, dis_rect)
            prg+=attempt
            sprg=font.render(prg, True, (255,255,255))
            sprg_rect=sprg.get_rect(center=(WX/2,WY/2+50))
            screen.blit(sprg, sprg_rect)
            pg.display.flip()
            

            
            t0,t1,t2,t3,t4,t5,t6,t7,t8,t9,td=0,0,0,0,0,0,0,0,0,0,0
            while not p:
                closeable()
                clear()
                dis=font.render(inp, True, (255,255,255))
                dis_rect=dis.get_rect(center=(WX/2,WY/2-50))
                screen.blit(dis, dis_rect)
                
                
                sprg=font.render(prg+' '+pos, True, (255,255,255))
                sprg_rect=sprg.get_rect(center=(WX/2,WY/2+50))
                screen.blit(sprg, sprg_rect)
                
                turnc=pg.font.SysFont('courier',25).render("Overall turns taken: "+str(score+tries),True,(255,255,255))
                screen.blit(turnc, (10,10))
                
                
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
        
        rep=True
        turnc=pg.font.SysFont('courier',25).render("Overall turns taken: "+str(score+tries),True,(255,255,255))
        screen.blit(turnc, (10,10))
        announce=font.render("Good Job!", True, (255,255,255))
        announce_rect=announce.get_rect(center=(WX/2,WY/2))
        screen.blit(announce, announce_rect)
        pg.display.flip()
        while rep:
            closeable()
            keys = pg.key.get_pressed()
            if keys[pg.K_SPACE]:
                rep=False
        clear()
        turnc=pg.font.SysFont('courier',25).render("Overall turns taken: "+str(score+tries),True,(255,255,255))
        screen.blit(turnc, (10,10))
        pg.time.wait(200)
        turnc=pg.font.SysFont('courier',25).render("Overall turns taken: "+str(score+tries),True,(255,255,255))
        screen.blit(turnc, (10,10))
        turns=font.render('You took '+str(tries)+' turns', True, (255,255,255))
        turns_rect=turns.get_rect(center=(WX/2,WY/2))
        screen.blit(turns, turns_rect)
        pg.display.flip()
        rep=True
        while rep:
            closeable()
            keys = pg.key.get_pressed()
            if keys[pg.K_SPACE]:
                rep=False
        
        score+=tries
    
    clear()
    
    comp=pg.font.SysFont('courier', 150).render("GAME COMPLETE", True, (255,255,255))
    comp_rect=comp.get_rect(center=(WX/2,WY/2-150))
    screen.blit(comp,comp_rect)
    pg.display.flip()
    pg.time.wait(500)
    scores=pg.font.SysFont('courier', 75).render('You took '+str(score)+' turns in total!', True, (255,255,255))
    scores_rect=scores.get_rect(center=(WX/2,WY/2))
    screen.blit(scores,scores_rect)
    pg.display.flip()
    pg.time.wait(500)
    minn=pg.font.SysFont('courier', 75).render('The minimum possible was '+str(min_score)+'!', True, (255,255,255))
    minn_rect=minn.get_rect(center=(WX/2,WY/2+150))
    screen.blit(minn,minn_rect)
    pg.display.flip()
    rep=True
    while rep:
        closeable()
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            rep=False
    
    clear()
    pg.time.wait(200)
    if score==min_score:
        gg=pg.font.SysFont('courier', 200).render("Good Job!", True, (255,255,255))
        gg_rect=gg.get_rect(center=(WX/2,WY/2))
        screen.blit(gg,gg_rect)
        pg.display.flip()
        rep=True
        while rep:
            closeable()
            keys = pg.key.get_pressed()
            if keys[pg.K_SPACE]:
                rep=False
    
