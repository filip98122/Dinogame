import socket
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("127.0.0.1",9999))
server.listen(2)
print("Waiting")
import json
client1,address=server.accept()
client2,address2=server.accept()

serverasclient2=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverasclient2.connect(("127.0.0.1",9997))

serverasclient1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverasclient1.connect(("127.0.0.1",9998))

from Local_2_player.main import *
listofclasses=[damage,gun,prozor,lbolts,Startend,bomb,blackhole,False]
while True:
    data=b""
    data2=b""
    try:
        print("Server connected!")
        chunk=client1.recv(4096)#4 kb
        chunk2=client2.recv(4096)
        if not chunk and not chunk2:
            break
        data+=chunk
        data2+=chunk2
        actualdatajson=data.decode("utf-8")
        actualdata=json.loads(actualdatajson)
        actualdatajson2=data2.decode("utf-8")
        actualdata2=json.loads(actualdatajson2)
    except:
        pass
    listofclasses[2]=prozor
    listofclasses[3]=lbolts
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
        fordraw ,sad1=player1.move(keys,lpatforms,player2,won,change,textures)
        fordraw1,sad2=player2.move(keys,lpatforms,player1,won2,change,textures)
        if sad1:
            won=True
        if sad2:
            won2=True
        if won2 and did2==False:
            did2=True
            p3score+=1-change
            change+=0.5
        elif won and did ==False:
            did=True
            p1score+=1-change
            change+=0.5
        if change==1 or (((player2.health==0 and won) or (player1.health==0 and won2)) and change==0.5):
            to_play=True
        count=0
        for i in range(len(lbolts)):
            lbolts[count].move(True)
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
            listofclasses=lpatforms[i].draw(window,listofclasses,textures,False)
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
        if player1.health==0 and player2.health==0:
            to_play=True
        
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
            listofclasses=lpatforms[i].draw(window,listofclasses,textures,False)
            lbolts=listofclasses[3]
            
            
            
            
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
        if not p1took or not p2took:
            offerer.draw(window)
        if not p1took:
            player1.operate_cursor(window,keys,textures)
        if not p2took:
            player2.operate_cursor(window,keys,textures)
        player1.curse_u_r=(min(max(int(player1.curse_u_r[0]),0),WIDTH),min(max(int(player1.curse_u_r[1]),0),HEIGHT))
        player2.curse_u_r=(min(max(int(player2.curse_u_r[0]),0),WIDTH),min(max(int(player2.curse_u_r[1]),0),HEIGHT))
        if p1took and not p1placed:
            player1.move_cursor(keys)
            player1.curse_u_r=(int(player1.curse_u_r[0]),int(player1.curse_u_r[1]))
            for i in range(len(player1.building.listofplats2)):
                listofclasses=player1.building.listofplats2[i].draw(window,listofclasses,textures,False)
                lbolts=listofclasses[3]
                player1.building.listofplats2[i].x=player1.curse_u_r[0]+player1.building.lockedmove[i][0]
                player1.building.listofplats2[i].y=player1.curse_u_r[1]+player1.building.lockedmove[i][1]
        if p2took and not p2placed:
            player2.move_cursor(keys)
            player2.curse_u_r=(int(player2.curse_u_r[0]),int(player2.curse_u_r[1]))
            for i in range(len(player2.building.listofplats2)):
                listofclasses=player2.building.listofplats2[i].draw(window,listofclasses,textures,False)
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
   
    if countdown==0 and prozor!="game" and prozor=="taking":
        prozor="game"
    if prozor=="menu":
        if keys[pygame.K_ESCAPE] and holdingescape==False:
            break
        if pygame.mouse.get_visible()==False:
            pygame.mouse.set_visible(True)
        startbutton.draw(window,textures)
        if startbutton.clickedon(mousePos,mouseState):
            to_play=True
            p1score=0
            p2score=0
            lpatforms=[Startend((0,HEIGHT//2+1),WIDTH//7,HEIGHT//9),Startend(((WIDTH//7)*6,HEIGHT//2),WIDTH//7,HEIGHT//9)]
            pygame.mouse.set_visible(False)
    countbombs=0
    for i in range(len(lbombs)):
        lbombs[countbombs].draw(window,textures,True,False)
        if lbombs[countbombs].alive==False:
            del lbombs[countbombs]
            continue
        countbombs+=1
    if keys[pygame.K_ESCAPE]:
        holdingescape=True
    pygame.display.update()
    clock.tick(fps)
    
    #NEED TO PARSE
    #NEED TO PARSE
    parsed=[]
    serverasclient2.sendall((json.dumps(parsed)).encode("utf-8"))
    serverasclient1.sendall((json.dumps(parsed)).encode("utf-8"))