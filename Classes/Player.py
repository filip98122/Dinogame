from Classes.Special_tools import *

playerpic={"walk":[5,25],"idle":[1,10],"jump":[1,10]}
class Player:
    def __init__(s,stpos,health,time,dirr,keybinds,color):
        s.x,s.y=stpos
        s.stpos=stpos
        s.h=HEIGHT//(10.8*2)
        s.w=WIDTH//(27.42857142857143*2)
        s.y-=s.h//2
        s.stpos=(s.x,s.y)
        s.stpos=None
        s.dirr=dirr
        s.health=health
        s.time=time
        s.speed=8
        s.permady=11
        s.dy=0
        s.ddy=0.5
        s.ddyperma=0.5
        s.dx=0
        s.onground=False
        s.previousx=s.x
        s.offgrounddx=0
        s.keybinds=keybinds
        s.curse_u_r=(0,0)
        s.building=None
        s.offgroundneojumpmaxspeed=2
        s.untill=0
        s.color=color
        s.lastpic=None
        s.score=0
    def operate_cursor(s,window,keys,txt):
        s.move_cursor(keys)
        s.draw_cursor(window,txt)
    def draw(s,window,keys,onplat,textures,playerpic,lockedin):
        if s.untill==-1:
            s.pic="idle"
            if keys!=[False]:
                if keys[s.keybinds[0]] ^ keys[s.keybinds[1]]:
                    s.pic="walk"
                if onplat==False:
                    s.pic="walk"
                    s.time=0
            if lockedin:
                s.pic="idle"
            s.time+=1
            if s.lastpic!=s.pic:
                s.time=0
            s.time%=playerpic[s.pic][1]
            s.lastpic=s.pic
            strana="l"
            if s.dirr:
                strana="r"
            window.blit(textures[f"{strana}{s.pic}{s.time//(playerpic[s.pic][1]//playerpic[s.pic][0])}{s.color}"],(s.x-s.w//2,s.y-s.h/2))
            #pygame.draw.rect(window,(255,0,0),pygame.Rect(s.x-s.w//2,s.y-s.h//2,s.w,s.h))
    def draw_cursor(s,window,textures):
        window.blit(textures[f"cursor{s.color}"],s.curse_u_r)
    def move_cursor(s,keys):
        x=s.curse_u_r[0]
        y=s.curse_u_r[1]
        if keys[s.keybinds[0]]:
            x-=s.speed
        if keys[s.keybinds[1]]:
            x+=s.speed
        if keys[s.keybinds[2]]:
            y-=s.speed
        if keys[s.keybinds[3]]:
            y+=s.speed
        s.curse_u_r=(x,y)
    def move(s,keys,lplatforms,contempuary,cantmove,change):
        s.dx=0
        ylimitu=-1
        ylimitd=WIDTH+1
        xlimitl=WIDTH+1
        xlimitr=-1
        pamti=[0,0,0,0]
        index=-1
        if change==0 and not cantmove and not contempuary.untill>-1:
            lplatforms.append(Platform((contempuary.x-contempuary.w//2,contempuary.y-contempuary.h//2),contempuary.w,contempuary.h))
        verdict=[[False],[False],[False],[False]]
        for j in range(len(lplatforms)):
            functi=[lplatforms[j].ifplayerontop,lplatforms[j].ifplayerbelow,lplatforms[j].ifplayeronleftsidefor,lplatforms[j].ifplayeronrightsidefor]
            if j==len(lplatforms)-1:
                functi[2]=lplatforms[j].ifplayeronleftside
                functi[3]=lplatforms[j].ifplayeronrightside
            
            verdict[0]=functi[0](s.x-s.w//2,s.y-s.h//2,s.w,s.h)
            verdict[1]=functi[1](s.x-s.w//2,s.y-s.h//2,s.w,s.h)
            verdict[2]=functi[2](s.x-s.w//2,s.y-s.h//2,s.w,s.h)
            verdict[3]=functi[3](s.x-s.w//2,s.y-s.h//2,s.w,s.h)
            for i in range(4):
                if verdict[i][0]==True:
                    if i==0:
                        if pamti[i]==0:
                            index=j
                            pamti[i]=[abs(verdict[i][1]-s.y),verdict[i]]
                        else:
                            if pamti[i][0]>abs(s.y-verdict[i][1]):
                                index=j
                                pamti[i]=[abs(verdict[i][1]-s.y),verdict[i]]
                    elif i==1:
                        if pamti[i]==0:
                            pamti[i]=[abs(s.y-verdict[i][1]),verdict[i]]
                        else:
                            if pamti[i][0]>abs(verdict[i][1]-s.y):
                                pamti[i]=[abs(s.y-verdict[i][1]),verdict[i]]
                    elif i==3:
                        if pamti[i]==0:
                            pamti[i]=[abs(s.x-verdict[i][2]),verdict[i]]
                        else:
                            if pamti[i][0]>abs(verdict[i][2]-s.x):
                                pamti[i]=[abs(s.x-verdict[i][2]),verdict[i]]
                    elif i==2:
                        if pamti[i]==0:
                            pamti[i]=[abs(verdict[i][2]-s.x),verdict[i]]
                        else:
                            if pamti[i][0]>abs(s.x-verdict[i][2]):
                                pamti[i]=[abs(verdict[i][2]-s.x),verdict[i]]
        if change==0 and not cantmove and not contempuary.untill>-1:
            del lplatforms[-1]
        wining=False
        if index==1:
            if pamti[0][1][1]-1-s.h//2==s.y:
                wining=True
        if pamti[0]!=0:
            ylimitd=pamti[0][1][1]-1
        if pamti[1]!=0:
            ylimitu=pamti[1][1][1]+1
        if pamti[2]!=0:
            xlimitl=pamti[2][1][2]-1
        if pamti[3]!=0:
            xlimitr=pamti[3][1][2]+1
        if pamti[0]!=0:
            if pamti[0][1][1]-1-s.h//2==s.y:
                s.onground=True
                s.offgrounddx=0
            else:
                if s.onground==True:
                    s.onground=False
                    s.offgrounddx=s.dx
        else:
            if s.onground==True:
                s.onground=False
                s.offgrounddx=s.dx
        
        if keys[s.keybinds[0]] and not cantmove and s.untill==-1:
            if not s.onground:
                if s.offgrounddx!=-s.speed:
                    s.offgrounddx-=s.speed/s.offgroundneojumpmaxspeed
                    s.offgrounddx=max(s.offgrounddx,-s.speed/s.offgroundneojumpmaxspeed)
            else:
                s.dx-=s.speed
            s.dirr=False
        
        if keys[s.keybinds[1]] and not cantmove and s.untill==-1:
            if not s.onground:
                if s.offgrounddx!=s.speed:
                    s.offgrounddx+=s.speed/s.offgroundneojumpmaxspeed
                    s.offgrounddx=min(s.offgrounddx,s.speed/s.offgroundneojumpmaxspeed)
            else:
                s.dx+=s.speed
            s.dirr=True
        if pamti[1]!=0:
            if pamti[1][1][1]+1+s.h//2==s.y:
                s.dy=0
        if s.onground:
            s.dy=0
        if s.dy==0:
            s.ddy=s.ddyperma
        if keys[s.keybinds[2]] and s.onground and pamti[0]!=0 and not cantmove and s.untill==-1:
            if pamti[0][1][1]-1-s.h//2==s.y:
                s.offgrounddx=s.dx
                s.dy=-s.permady
                s.onground=False
        if not s.onground:
            if pamti[2]!=0:
                if pamti[2][1][2]-1-s.w//2==s.x:
                    s.offgrounddx=0
            if pamti[3]!=0:
                if pamti[3][1][2]+1+s.w//2==s.x:
                    s.offgrounddx=0
            s.dx=s.offgrounddx
        if s.untill==-1:
            if pamti[0]!=0:
                if pamti[0][1][1]-1-s.h//2==s.y:
                    if type(pamti[0][1][5])==damage:
                        s.health-=1
                        s.untill=180

            if pamti[2]!=0:
                if pamti[2][1][2]-1-s.w//2==s.x:
                    if type(pamti[2][1][5])==damage:
                        s.health-=1
                        s.untill=180

            if pamti[3]!=0:
                if pamti[3][1][2]+1+s.w//2==s.x:
                    if type(pamti[3][1][5])==damage:
                        s.health-=1
                        s.untill=180

            if pamti[1]:
                if pamti[1][1][1]+s.h//2==s.y:
                    if type(pamti[1][1][5])==damage:
                        s.health-=1
                        s.untill=180
                    
    
        
        
        
        s.x+=s.dx
        if not s.onground:
            s.dy+=s.ddy
        s.y+=s.dy
        s.y=max(ylimitu,s.y-s.h//2)+s.h//2
        s.y=min(ylimitd,s.y+s.h//2)-s.h//2
        s.x=min(xlimitl,s.x+s.w//2)-s.w//2
        s.x=max(xlimitr,s.x-s.w//2)+s.w//2
        s.previousx=s.x
        for i in range(len(lplatforms)):
            if pygame.Rect(lplatforms[i].x,lplatforms[i].y+1,lplatforms[i].width,lplatforms[i].height).colliderect(s.x-s.w//2,s.y-s.h//2,s.w,s.h) and not s.onground:
                s.y=lplatforms[i].y-1-s.h//2
                pass
        if s.y-s.h-1>=HEIGHT and s.untill==-1:
            s.health-=1
            s.untill=180
            
        if s.health==0:
            s.untill=2
        s.untill=max(s.untill-1,-1)
        if s.untill==0:
            s.x,s.y=s.stpos
        if s.stpos==None:
            s.stpos=(s.x,s.y)
        if pamti[0]!=0:
            return s.y+s.h//2+1==pamti[0][1][1],wining
        return False,wining
    def draw_health(s):
        pass