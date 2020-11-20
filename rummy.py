import pygame
import copy
import numpy
import random
pygame.init()
#create screen
screen=pygame.display.set_mode((800,600))
#title and icon
pygame.display.set_caption("INDIAN RUMMY")
icon =pygame.image.load("poker.png")
pygame.display.set_icon(icon)

def displaycard(img,x,y):
    pimage=pygame.image.load(img+".png")
    screen.blit(pimage,(x,y))

#function to extract num
def numb(x):
    i=x.find("_")
    num=int(x[:i])
    return num
def ty(x):
    i=x.find("_")
    t=x[i+1:]
    return t
deck=[]
suit=["H","S","C","D"]
for i in range(1,14):
    for j in range(0,4):
        c=str(i)+"_"+suit[j]
        deck.append(c)

""" making three lists com, player , faceup , facedown  """
#copy oof deck
faceup=[]
com=[]
player=[]
copydeck=copy.deepcopy(deck)
numpy.random.shuffle(copydeck)
""" assigining cards to player com and face down cards """
for i in range(13):
    player.append(copydeck[i])
for i in range(13):
    com.append(copydeck[i+13])
facedown=copy.deepcopy(copydeck[26:])

com.sort(key=lambda x: x[-1:])
com.sort(key=lambda x: x[:2])
comnum=[0]*13
comtype=[0]*13
for i in range(13):
    ind=com[i].find("_")
    comnum[i]=int(com[i][:ind])
    comtype[i]=com[i][ind+1:]
print(com)
print(comnum)
print(comtype)
comcard1={"name":com[0]}
comcard2={"name":com[1]}
comcard3={"name":com[2]}
comcard4={"name":com[3]}
comcard5={"name":com[4]}
comcard6={"name":com[5]}
comcard7={"name":com[6]}
comcard8={"name":com[7]}
comcard9={"name":com[8]}
comcard10={"name":com[9]}
comcard11={"name":com[10]}
comcard12={"name":com[11]}
comcard13={"name":com[12]}
comdic=[comcard1,comcard2,comcard3,comcard4,comcard5,comcard6,comcard7,comcard8,comcard9,comcard10,comcard11,comcard12,comcard13]
print(comdic)

    
"""  algorithm to divide sorted com cards """
"""colorss """
red=(120,0,0)
blue=(0,0,120)
white=(255,255,255)
black=(0,0,0)

""" text to display"""
font=pygame.font.Font("freesansbold.ttf",16)
font2=pygame.font.Font("freesansbold.ttf",45)
win=font2.render("YOU WON !",True,white,black)
lost=font2.render("YOU LOST !",True,white,black)
reset=font2.render("Reseting Deck",True,white,blue)
winrect=win.get_rect()
lostrect=lost.get_rect()
winrect.center=(400,300)
lostrect.center=(400,300)
resetrect=reset.get_rect()
resetrect.center=(400,300)

text1=font.render("SET 1 COMPLETE",True,white,blue)
text1rect=text1.get_rect()
text1rect.center=(88,520)

text2=font.render("SET 2 COMPLETE",True,white,blue)
text2rect=text2.get_rect()
text2rect.center=(280,520)

text3=font.render("SET 3 COMPLETE",True,white,blue)
text3rect=text3.get_rect()
text3rect.center=(472,520)

text4=font.render("SET 4 COMPLETE",True,white,blue)
text4rect=text4.get_rect()
text4rect.center=(682,520)


card1={"name":player[0],"x":10,"y":400}
card2={"name":player[1],"x":60,"y":400}
card3={"name":player[2],"x":110,"y":400}
card4={"name":player[3],"x":200,"y":400}
card5={"name":player[4],"x":250,"y":400}
card6={"name":player[5],"x":300,"y":400}
card7={"name":player[6],"x":390,"y":400}
card8={"name":player[7],"x":440,"y":400}
card9={"name":player[8],"x":490,"y":400}
card10={"name":player[9],"x":580,"y":400}
card11={"name":player[10],"x":630,"y":400}
card12={"name":player[11],"x":680,"y":400}
card13={"name":player[12],"x":730,"y":400}
ini=0
upcard={"name":facedown[ini],"x":300,"y":200}

downcard={"name":facedown[ini+1],"x":500,"y":200}





swapcard1=[]
swapcard2=[]
temp1=False
temp2=False
flag4=False
flag1=False
flag2=False
flag3=False
flag1a=False
flag2a=False
flag3a=False
flag4a=False
comturn=0
downclick=0
diff=0
#gamelooop
running=True
startt=True
animation=True
difficulty=True



"""START MENU GUIII """
while startt:
    displaycard("start",0,0)
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    displaycard("play1",320,500)
    mx=mouse[0]
    my=mouse[1]
    if 320<mx<470 and 520<my<552:
        displaycard("play2",320,500)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            startt=False
            running=False
            animation=False
            difficulty=False
        
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                if 320<mx<470 and 520<my<552:
                    startt=False


    pygame.display.update()

"""START MENU GUI ENDS HERE
difficulty gui starts here """

while difficulty:
    displaycard("diff",0,0)
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    mx=mouse[0]
    my=mouse[1]
    displaycard("easy1",50,200)
    displaycard("fair1",50,300)
    displaycard("hard1",50,400)
    if 50<mx<195:
        if 200<my<255:
            displaycard("easy2",50,200)
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    diff=50
                    difficulty=False
        elif 300<my<355:
            displaycard("fair2",50,300)
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    diff=25
                    difficulty=False
        elif 400<my<455:
            displaycard("hard2",50,400)
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    diff=15
                    difficulty=False

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            difficulty=False
            running=False
            animation=False

    pygame.display.update()













"""animation starts here"""

while animation:
    screen.fill((25,100,25))
    displaycard("bg",0,0)
    if diff==25:
        displaycard("bg3",0,0)
    if diff==15:
        displaycard("bg4",0,0)
    displaycard("back",360,250)
    ag=0
    bg=0
    pygame.display.update()
    for i in range(13):
        displaycard("back",50+ag,50)
        ag+=50
        pygame.display.update()
        pygame.time.delay(100)
    for i in range(3):
        displaycard("back",10+bg,400)
        bg+=50
        pygame.display.update()
        pygame.time.delay(100)

    bg=200

    for i in range(3):
        displaycard("back",bg,400)
        bg+=50
        pygame.display.update()
        pygame.time.delay(100)
    
    bg=390

    for i in range(3):
        displaycard("back",bg,400)
        bg+=50
        pygame.display.update()
        pygame.time.delay(100)
    
    bg=580
    for i in range(4):
        displaycard("back",bg,400)
        bg+=50
        pygame.display.update()
        pygame.time.delay(100)
    pygame.display.update()
    displaycard("back",250,200)
    pygame.display.update()

    displaycard("back",500,200)


    pygame.display.update()
    
    animation=False







"""GAME LOOP STARTS HERE """

while running:
    screen.fill((25,100,25))
    displaycard("bg",0,0)
    if diff==25:
        displaycard("bg3",0,0)
    if diff==15:
        displaycard("bg4",0,0)
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    mx=mouse[0]
    my=mouse[1]
    
    

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        """ to swap cards amonghst themselves and other cards"""
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                if my>390:
                    if card1["x"]<mx<card2["x"]:
                        pygame.draw.rect(screen,red,(card1["x"]-10,card1["y"]-10,70,100))
                        
                        swapcard1.append(card1)
                    if card2["x"]<mx<card3["x"]:
                        pygame.draw.rect(screen,red,(card2["x"]-10,card1["y"]-10,70,100))
                        swapcard1.append(card2)
                    if card3["x"]<mx<card4["x"]:
                        pygame.draw.rect(screen,red,(card3["x"]-10,card1["y"]-10,70,100))
                        swapcard1.append(card3)
                    if card4["x"]<mx<card5["x"]:
                        pygame.draw.rect(screen,red,(card4["x"]-10,card1["y"]-10,70,100))
                        swapcard1.append(card4)
                    if card5["x"]<mx<card6["x"]:
                        pygame.draw.rect(screen,red,(card5["x"]-10,card1["y"]-10,70,100))
                        swapcard1.append(card5)
                    if card6["x"]<mx<card7["x"]:
                        pygame.draw.rect(screen,red,(card6["x"]-10,card1["y"]-10,70,100))
                        swapcard1.append(card6)
                    if card7["x"]<mx<card8["x"]:
                        pygame.draw.rect(screen,red,(card7["x"]-10,card1["y"]-10,70,100))
                        swapcard1.append(card7)
                    if card8["x"]<mx<card9["x"]:
                        pygame.draw.rect(screen,red,(card8["x"]-10,card1["y"]-10,70,100))
                        swapcard1.append(card8)
                    if card9["x"]<mx<card10["x"]:
                        pygame.draw.rect(screen,red,(card9["x"]-10,card1["y"]-10,70,100))
                        swapcard1.append(card9)
                    if card10["x"]<mx<card11["x"]:
                        pygame.draw.rect(screen,red,(card10["x"]-10,card1["y"]-10,70,100))
                        swapcard1.append(card10)
                    if card11["x"]<mx<card12["x"]:
                        pygame.draw.rect(screen,red,(card11["x"]-10,card1["y"]-10,70,100))
                        swapcard1.append(card11)
                    if card12["x"]<mx<card13["x"]:
                        pygame.draw.rect(screen,red,(card12["x"]-10,card1["y"]-10,70,100))
                        swapcard1.append(card12)
                    if card13["x"]<mx<card13["x"]+50:
                        pygame.draw.rect(screen,red,(card13["x"]-10,card1["y"]-10,70,100))
                        swapcard1.append(card13)
                if 200<my<296:
                    if 250<mx<316:
                        swapcard2.append(upcard)
            if len(swapcard1)>1:
                swapcard1[-1]["name"],swapcard1[-2]["name"]=swapcard1[-2]["name"],swapcard1[-1]["name"]
                swapcard1=[]

            if len(swapcard2)>=1 and len(swapcard1)>=1:
                swapcard1[-1]["name"],facedown[ini]=facedown[ini],swapcard1[-1]["name"]
                comturn+=1
                swapcard1=[]
                swapcard2=[]
            """com ka code iske baaad hoga  """
    displaycard("pass",320,270)
    if 320<mx<470 and 270<my<350:
        displaycard("pass1",320,270)
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                comturn+=1



    fflag=0
    ffflag=0
    if comturn%2==1:
        print(comturn,"com ki baari")
        # ini+=1
        comturn+=1
        ll=facedown[ini].find("_")
        xn=int(facedown[ini][:ll])
        xt=facedown[ini][ll+1:]
        ran=random.randint(0,12)
        for i in range (13):
            if comnum[i]==xn:
                fflag+=1
            elif comtype[i]==xt:
                if abs(comnum[i]-xn)==1:
                    ffflag+=1
            if fflag==2:
                facedown[ini],comdic[ran]["name"]=comdic[ran]["name"],facedown[ini]
                print("com dropping card")
            if ffflag==2:
                facedown[ini],comdic[ran]["name"]=comdic[ran]["name"],facedown[ini]
                print("com dropping card")

        if ffflag<2 and fflag<2:
            ini+=1
            print("unfolding card")
            

            
                    


    
    

    # displaycard(card1["name"],card1["x"],card1["y"])
    #to display back of oponents card 

    k=0
    for i in range(0,13):
        displaycard("back",50+k,50)
        k+=50

    """position of upcard and down card  """
    upcard["name"]=facedown[ini]
    downcard["name"]=facedown[ini+1]
    cc="back"
    displaycard(upcard["name"],250,200)

    displaycard(cc,500,200)

    """to unfold the downcard 
    
    
     """
    if 562>mouse[0]>500 and 286>mouse[1]>200:
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                displaycard(downcard["name"],300,200)
                pygame.time.delay(600)
                ini+=1
                print(ini)
                if ini>=25:
                    ini=0
                    pygame.time.delay(2000)
                    screen.blit(reset,resetrect)
                    
            
            
    """ conditions for displaying card and movement of hover  """
    #card1
    if card2["x"]>mouse[0]>card1["x"] and 490>mouse[1]>400:
        displaycard(card1["name"],card1["x"],380)
            

    # if 100>mouse[0]>50 and 490>mouse[1]>400 and click[0]==1:
    #     pygame.draw.rect(screen,red,(45,375,85,400))
    #     displaycard(card1["name"],50,380)
    else:
        displaycard(card1["name"],card1["x"],card1["y"])
    #card2
    if card3["x"]>mouse[0]>card2["x"] and 490>mouse[1]>400:
        displaycard(card2["name"],card2['x'],380)
    else:
        displaycard(card2["name"],card2["x"],card2["y"])
    #card3
    if card3["x"]+60>mouse[0]>card3["x"] and 490>mouse[1]>400:
        displaycard(card3["name"],card3["x"],380)
    else:
        displaycard(card3["name"],card3["x"],card3["y"])
    #card4
    if card5["x"]>mouse[0]>card4["x"] and 490>mouse[1]>400:
        displaycard(card4["name"],card4["x"],380)
    else:
        displaycard(card4["name"],card4["x"],card4["y"])
    #card 5
    if card6["x"]>mouse[0]>card5["x"] and 490>mouse[1]>400:
        displaycard(card5["name"],card5["x"],380)
    else:
        displaycard(card5["name"],card5["x"],card5["y"])
    
    if card6["x"]+60>mouse[0]>card6["x"] and 490>mouse[1]>400:
        displaycard(card6["name"],card6["x"],380)
    else:
        displaycard(card6["name"],card6["x"],card6["y"])
    
    if card8["x"]>mouse[0]>card7["x"] and 490>mouse[1]>400:
        displaycard(card7["name"],card7["x"],380)
    else:
        displaycard(card7["name"],card7["x"],card7["y"])

    if card9["x"]>mouse[0]>card8["x"] and 490>mouse[1]>400:
        displaycard(card8["name"],card8["x"],380)
    else:
        displaycard(card8["name"],card8["x"],card8["y"])
    if card9["x"]+60>mouse[0]>card9["x"] and 490>mouse[1]>400:
        displaycard(card9["name"],card9["x"],380)
    else:
        displaycard(card9["name"],card9["x"],card9["y"])
    if card11["x"]>mouse[0]>card10["x"] and 490>mouse[1]>400:
        displaycard(card10["name"],card10["x"],380)
    else:
        displaycard(card10["name"],card10["x"],card10["y"])
    if card12["x"]>mouse[0]>card11["x"] and 490>mouse[1]>400:
        displaycard(card11["name"],card11["x"],380)
    else:
        displaycard(card11["name"],card11["x"],card11["y"])
    if card13["x"]>mouse[0]>card12["x"] and 490>mouse[1]>400:
        displaycard(card12["name"],card12["x"],380)
    else:
        displaycard(card12["name"],card12["x"],card12["y"])
    if card13["x"]+60>mouse[0]>card13["x"] and 490>mouse[1]>400:
        displaycard(card13["name"],card13["x"],380)
    else:
        displaycard(card13["name"],card13["x"],card13["y"])

    """ condition for completion of sets """
    #function to extract num 
    num1=numb(card1["name"])
    num2=numb(card2["name"])
    num3=numb(card3["name"])
    type1=ty(card1["name"])
    type2=ty(card2["name"])
    type3=ty(card3["name"])
    #set 1
    if (num1==num2 and num1==num3):
        screen.blit(text1,text1rect)
        flag1a=True
    else:
        flag1a=False
    if num3==1:
        num3=14
    if (type1==type2 and type1==type3 and num2==num1+1 and num3==num2+1):
        screen.blit(text1,text1rect)
        flag1=True
    else:
        flag1=False

    #function to extract num 
    num4=numb(card4["name"])
    num5=numb(card5["name"])
    num6=numb(card6["name"])
    type4=ty(card4["name"])
    type5=ty(card5["name"])
    type6=ty(card6["name"])
    #set 2
    if (num4==num5 and num4==num6):
        screen.blit(text2,text2rect)
        flag2a=True
    else:
        flag2=False
    if num6==1:
        num6=14
    if (type4==type5 and type4==type6 and num5==num4+1 and num6==num5+1):
        screen.blit(text2,text2rect)
        flag2=True
    else:
        flag2=False
    #function to extract num 
    num7=numb(card7["name"])
    num8=numb(card8["name"])
    num9=numb(card9["name"])
    type7=ty(card7["name"])
    type8=ty(card8["name"])
    type9=ty(card9["name"])
    #set 2
    if (num7==num8 and num7==num9):
        screen.blit(text3,text3rect)
        flag3a=True
    else:
        flag3a=False
    if num9==1:
        num9=14
    if (type7==type8 and type7==type9 and num8==num7+1 and num9==num8+1):
        screen.blit(text3,text3rect)
        flag3=True
    else:
        flag3=False
    # print("flag3:",flag3, flag3a)
    # print("flag2:",flag2, flag2a)


    #function to extract num 
    num10=numb(card10["name"])
    num11=numb(card11["name"])
    num12=numb(card12["name"])
    num13=numb(card13["name"])


    type10=ty(card10["name"])
    type11=ty(card11["name"])
    type12=ty(card12["name"])
    type13=ty(card13["name"])
    #set 1
    if (num10==num11 and num10==num12 and num10==num13):
        screen.blit(text4,text4rect)
        flag4a=True
    else:
        flag4a=False
    if num13==1:
        num13=14
    if (type10==type11 and type10==type12 and type10==type13 and num13==num12+1 and num11==num10+1 and num12==num11+1):
        screen.blit(text4,text4rect)
        flag4=True
    else:
        flag4=False
    a1=flag1 or flag1a
    a2=flag2 or flag2a
    a3=flag3 or flag3a
    a4=flag4 or flag4a
    if (a1 and a2) and (a3 and a4):
        screen.blit(win,winrect)
        # screen.blit(win2,winrect)

    # print("f1:",a1," ","f2:",a2, " ","f3:",a2,"f4:",a4)
    if comturn>=diff:
        screen.blit(lost,lostrect)
    pygame.display.update()


