import socket
import time
import json
import pygame
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
ourwindow=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverconnect=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverconnect.bind(("127.0.0.1",9997))
serverconnect.listen(1)
client.connect(("127.0.0.1",9999))
client2,address2=serverconnect.accept()
from Local_2_player.main import *
while True:
    ourwindow.fill((0,0,0))
    try:
        data_to_send={"Hi":"Bye"}
        jsonstr=json.dumps(data_to_send)
        byte_data=jsonstr.encode('utf-8')
        client.sendall(byte_data)
    except:
        pass
    data=b""
    try:
        print("Client connected!")
        chunk=client2.recv(4096)#4 kb
        data+=chunk
        actualdatajson=data.decode("utf-8")
        actualdata=json.loads(actualdatajson)
    except:
        pass
    listofclasses[2]=prozor
    listofclasses[3]=lbolts
    bg.drawbg(ourwindow,prozor,textures)
    events=pygame.event.get()
    keys=pygame.key.get_pressed()
    mousePos=pygame.mouse.get_pos()
    mouseState=pygame.mouse.get_pressed()
    if holdingescape==True:
        if not keys[pygame.K_ESCAPE]:
            holdingescape=False
    if prozor=="pause":
        if keys[pygame.K_ESCAPE] and not holdingescape:
            prozor="menu"
            holdingescape=True
        halftransparent.fill((0,0,0))
        bg.drawbg(ourwindow,prozor,textures)
        player1.draw(ourwindow,nokeys,True,textures,playerpic,True)
        player2.draw(ourwindow,nokeys,True,textures,playerpic,True)
        for i in range(len(lpatforms)):
            lpatforms[i].draw(ourwindow,listofclasses,textures)
        for i in range(len(lbolts)):
            lbolts[i].draw(ourwindow,textures)
        for i in range(len(lbombs)):
            lbombs[i].draw(ourwindow,textures,False)
        ourwindow.blit(halftransparent,(0,0))
        ourwindow.blit(textures["pausemenu"],(WIDTH//2-textures["pausemenu"].get_width()//2,HEIGHT//2-textures["pausemenu"].get_height()//2))
        
        
    if prozor=="game":
        if keys[pygame.K_ESCAPE] and not holdingescape:
            prozor="pause"
            holdingescape=True
        if keys[pygame.K_b]:
            breakpoint()    
        if keys[pygame.K_2]:
            fps=2           
        if keys[pygame.K_1]:
            fps=60          
        player1.playsound(keys,player2,textures,won)
        player2.playsound(keys,player1,textures,won2)
        count=0
        for i in range(len(lbolts)):
            lbolts[count].move(True)
            lbolts[count].draw(ourwindow,textures)
            if pygame.Rect(lbolts[count].x,lbolts[count].y,lbolts[count].w,lbolts[count].h).colliderect(player1.x-player1.w//2,player1.y-player1.h//2,player1.w,player1.h) and player1.untill==-1:
                player1.health-=1
                player1.untill=180
                del lbolts[count]
                continue
            if pygame.Rect(lbolts[count].x,lbolts[count].y,lbolts[count].w,lbolts[count].h).colliderect(player2.x-player2.w//2,player2.y-player2.h//2,player2.w,player2.h) and player2.untill==-1:
                player2.health-=1
                player2.untill=180
                del lbolts[count]
                continue
            count+=1
        count=0
        for i in range(len(lbolts)):
            for j in range(len(lpatforms)):
                if lbolts[count].id!=lpatforms[j].pubid:
                    if pygame.Rect(lbolts[count].x,lbolts[count].y,lbolts[count].w,lbolts[count].h).colliderect(lpatforms[j].x,lpatforms[j].y,lpatforms[j].width,lpatforms[j].height):
                        del lbolts[count]
                        count-=1
                        break
            count+=1
        for i in range(len(lpatforms)):
            listofclasses=lpatforms[i].draw(ourwindow,listofclasses,textures)
            lbolts=listofclasses[3]
        for i in range(len(lpatforms)):
            if type(lpatforms[i])==blackhole:
                if circle_rect_collison((lpatforms[i].x+lpatforms[i].width//2,lpatforms[i].y+lpatforms[i].height//2),lpatforms[i].eatradius,pygame.Rect(player1.x-player1.w//2,player1.y-player1.h//2,player1.w,player1.h)) and player1.untill==-1:
                    player1.health-=1
                    player1.untill=180
        for i in range(len(lpatforms)):
            if type(lpatforms[i])==blackhole:
                if circle_rect_collison((lpatforms[i].x+lpatforms[i].width//2,lpatforms[i].y+lpatforms[i].height//2),lpatforms[i].eatradius,pygame.Rect(player2.x-player2.w//2,player2.y-player2.h//2,player2.w,player2.h)) and player2.untill==-1:
                    player2.health-=1
                    player2.untill=180
        player1.draw(ourwindow,keys,fordraw ,textures,playerpic,won)
        player2.draw(ourwindow,keys,fordraw1,textures,playerpic,won2)
        if player1.health==0 and player2.health==0:
            to_play=True
        ourwindow.blit(roundsuptohundred[roundof],(WIDTH//2-roundsuptohundred[roundof].get_width()//2,HEIGHT-roundsuptohundred[roundof].get_height()))
        ourwindow.blit(scoreuptohundred[int(p1score*2)][0],(WIDTH//2-roundsuptohundred[roundof].get_width()//2-scoreuptohundred[int(p1score*2)][0].get_width()*1.1,HEIGHT-scoreuptohundred[int(p1score*2)][0].get_height()))
        ourwindow.blit(scoreuptohundred[int(p3score*2)][1],(WIDTH//2+roundsuptohundred[roundof].get_width()//2+scoreuptohundred[int(p3score*2)][1].get_width()*0.1,HEIGHT-scoreuptohundred[int(p3score*2)][1].get_height()))
        
    if to_play:
        player1=Player((WIDTH//10,HEIGHT//2),3,0,True,[pygame.K_a,pygame.K_d,pygame.K_w,pygame.K_s],"z")
        player2=Player((50,HEIGHT//2),3,0,True,[pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,pygame.K_DOWN],"b")
        fordraw=player1.move(keys,lpatforms,player2,True,change,textures)
        fordraw1=player2.move(keys,lpatforms,player1,True,change,textures)
        
        selected=[]
        for i in range(5):
            indexrandom=random.randint(0,len(listofplatformsrandomselect)-1)
            if type(listofplatformsrandomselect[indexrandom])==gun:
                gun.pubid+=1
                listofplatformsrandomselect[indexrandom].pubid=gun.pubid
            selected.append(copy.deepcopy(listofplatformsrandomselect[indexrandom]))
        offerer=Offerer(selected,HEIGHT//(currentwannabeh/225))
        for i in range(len(lpatforms)):
            listofclasses=lpatforms[i].draw(ourwindow,listofclasses,textures)
            lbolts=listofclasses[3]
        player1.draw(ourwindow,keys,fordraw ,textures,playerpic,True)
        player2.draw(ourwindow,keys,fordraw1,textures,playerpic,True)
        countdown=1500
        prozor="taking"
        player1.curse_u_r,player2.curse_u_r=(WIDTH//2,HEIGHT//2),(WIDTH//2,HEIGHT//2)
        roundof+=1
        to_play=False
        p1took=False
        p2took=False
        p1placed=False
        p2placed=False
        change=0
        won=False
        won2=False
        did=False
        did2=False
        player1.building=None
        player2.building=None
        lbolts=[]
        listofclasses=[damage,gun,prozor,lbolts,Startend,bomb,blackhole]
    if prozor=="taking":
        if keys[pygame.K_ESCAPE] and not holdingescape:
            prozor="menu"
            holdingescape=True
        for i in range(len(lpatforms)):
            listofclasses=lpatforms[i].draw(ourwindow,listofclasses,textures)
            lbolts=listofclasses[3]
        player1.draw(ourwindow,nokeys,True,textures,playerpic,True)
        player2.draw(ourwindow,nokeys,True,textures,playerpic,True)
        if not p1took or not p2took:
            offerer.draw(ourwindow)
        if not p1took:
            player1.operate_cursor(ourwindow,keys,textures)
        if not p2took:
            player2.operate_cursor(ourwindow,keys,textures)
        player1.curse_u_r=(min(max(int(player1.curse_u_r[0]),0),WIDTH),min(max(int(player1.curse_u_r[1]),0),HEIGHT))
        player2.curse_u_r=(min(max(int(player2.curse_u_r[0]),0),WIDTH),min(max(int(player2.curse_u_r[1]),0),HEIGHT))
        if p1took and not p1placed:
            player1.move_cursor(keys)
            player1.curse_u_r=(int(player1.curse_u_r[0]),int(player1.curse_u_r[1]))
            if type(player1.building)==bomb:
                a=player1.building.do_special([ourwindow,textures])
            for i in range(len(player1.building.listofplats2)):
                listofclasses=player1.building.listofplats2[i].draw(ourwindow,listofclasses,textures)
                lbolts=listofclasses[3]
                player1.building.listofplats2[i].x=player1.curse_u_r[0]+player1.building.lockedmove[i][0]
                player1.building.listofplats2[i].y=player1.curse_u_r[1]+player1.building.lockedmove[i][1]
        if p2took and not p2placed:
            player2.move_cursor(keys)
            player2.curse_u_r=(int(player2.curse_u_r[0]),int(player2.curse_u_r[1]))
            if type(player2.building)==bomb:
                a=player2.building.do_special([ourwindow,textures])
            for i in range(len(player2.building.listofplats2)):
                listofclasses=player2.building.listofplats2[i].draw(ourwindow,listofclasses,textures)
                lbolts=listofclasses[3]
                player2.building.listofplats2[i].x=int(player2.curse_u_r[0])+int(player2.building.lockedmove[i][0])
                player2.building.listofplats2[i].y=int(player2.curse_u_r[1])+int(player2.building.lockedmove[i][1])
        if not p1took or not p2took:
            taken,listofclasses=offerer.move_offers([[player1.curse_u_r[0],player1.curse_u_r[1]],[player2.curse_u_r[0],player2.curse_u_r[1]]],keys[pygame.K_q] and not p1took,keys[pygame.K_DELETE] and not p2took,textures,listofclasses)
            lbolts=listofclasses[3]
            if taken[0]:
                p1took=True
                player1.curse_u_r=(WIDTH//2,HEIGHT//2)
                player1.building=taken[2]
            if taken[1]:
                p2took=True
                player2.curse_u_r=(WIDTH//2,HEIGHT//2)
                player2.building=taken[3]
        countdown=max(countdown-1,0)
        if keys[pygame.K_PAGEDOWN] and p2placed==False and p2took:
            can=True
            p2placed=True
            if type(player2.building)!=bomb:
                lpatforms.append(Platform((0,100),WIDTH//7,HEIGHT))
                lpatforms.append(Platform((WIDTH//7*6,100),WIDTH//7,HEIGHT))
            for i in range(len(lpatforms)): 
                for j in range(len(player2.building.listofplats2)):
                    if pygame.Rect(player2.building.listofplats2[j].x,player2.building.listofplats2[j].y,player2.building.listofplats2[j].width,player2.building.listofplats2[j].height).colliderect(pygame.Rect(lpatforms[i].x,lpatforms[i].y,lpatforms[i].width,lpatforms[i].height)):
                        can=False
            if type(player2.building)!=bomb:
                del lpatforms[-1]
                del lpatforms[-1]
            if type(player2.building)==bomb:
                can=True
            if can:
                lpatforms.extend(player2.building.listofplats2)
            else:
                p2placed=False
            if type(player2.building)==bomb and can:
                lbombs.append(Placedbomb(player2.building.x+player2.building.width//2,
                                         player2.building.y+player2.building.height//2))
                countj=0
                for j in range((len(lpatforms))):
                    if pygame.Rect(player2.building.x-WIDTH//(currentwannabew/135)//2+player2.building.width//2,player2.building.y-HEIGHT//(currentwannabeh/135)//2+player2.building.height//2,WIDTH//(currentwannabew/135),HEIGHT//(currentwannabeh/135)).colliderect(pygame.Rect(lpatforms[countj].x,lpatforms[countj].y,lpatforms[countj].width,lpatforms[countj].height)):
                        if type(lpatforms[countj])!=Startend:
                            del lpatforms[countj]
                            countj-=1
                    countj+=1

        if keys[pygame.K_e] and not p1placed and p1took:
            can=True
            p1placed=True
            if type(player1.building)!=bomb:
                lpatforms.append(Platform((0,100),WIDTH//7,HEIGHT))
                lpatforms.append(Platform((WIDTH//7*6,100),WIDTH//7,HEIGHT))
            for i in range(len(lpatforms)):
                for j in range(len(player1.building.listofplats2)):
                    if pygame.Rect(player1.building.listofplats2[j].x,player1.building.listofplats2[j].y,player1.building.listofplats2[j].width,player1.building.listofplats2[j].height).colliderect(pygame.Rect(lpatforms[i].x,lpatforms[i].y,lpatforms[i].width,lpatforms[i].height)):
                        can=False
            
            if type(player1.building)!=bomb:
                del lpatforms[-1]
                del lpatforms[-1]
            if type(player1.building)==bomb:
                can=True
            if can:
                lpatforms.extend(player1.building.listofplats2)
            else:
                p1placed=False
            if type(player1.building)==bomb and can:
                lbombs.append(Placedbomb(player1.building.x+player1.building.width//2,
                                         player1.building.y+player1.building.height//2))
                countj=0
                for j in range((len(lpatforms))):
                    if pygame.Rect(player1.building.x-WIDTH//(currentwannabew/135)//2+player1.building.width//2,player1.building.y-HEIGHT//(currentwannabeh/135)//2+player1.building.height//2,WIDTH//(currentwannabew/135),HEIGHT//(currentwannabeh/135)).colliderect(pygame.Rect(lpatforms[countj].x,lpatforms[countj].y,lpatforms[countj].width,lpatforms[countj].height)):
                        if type(lpatforms[countj])!=Startend:
                            del lpatforms[countj]
                            countj-=1
                    countj+=1

        if p1placed and p2placed and countdown!=0:
            countdown=1
        if keys[pygame.K_e] and not p1took:
            p1placed=True
            p1took=True
        if keys[pygame.K_PAGEDOWN] and not p2took:
            p2placed=True
            p2took=True
        if countdown//fps<=5 and countdown>1:
            ourwindow.blit(seconds[countdown//fps],(WIDTH//2-seconds[countdown//fps].get_width()//2,HEIGHT//2-seconds[countdown//fps].get_height()//2))
            
    if countdown==0 and prozor!="game" and prozor=="taking":
        prozor="game"
    if prozor=="menu":
        if keys[pygame.K_ESCAPE] and holdingescape==False:
            break
        if pygame.mouse.get_visible()==False:
            pygame.mouse.set_visible(True)
        startbutton.draw(ourwindow,textures)
        if startbutton.clickedon(mousePos,mouseState):
            to_play=True
            p1score=0
            p2score=0
            lpatforms=[Startend((0,HEIGHT//2+1),WIDTH//7,HEIGHT//9),Startend(((WIDTH//7)*6,HEIGHT//2),WIDTH//7,HEIGHT//9)]
            pygame.mouse.set_visible(False)
    countbombs=0
    for i in range(len(lbombs)):
        lbombs[countbombs].draw(ourwindow,textures,True)
        if lbombs[countbombs].alive==False:
            del lbombs[countbombs]
            continue
        countbombs+=1
    if keys[pygame.K_ESCAPE]:
        holdingescape=True
    pygame.display.update()
    clock.tick(fps)
    
    pygame.display.update()