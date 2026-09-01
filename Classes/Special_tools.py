from Classes.Platform import *
class Special(Platform):
    def __init__(s,pos,width,height,specialfunc,listofplatforms,lockedfor):
        super().__init__(pos,width,height)
        s.listofplats=listofplatforms
        s.listofplats2=[s]+s.listofplats
        s.specialfunc=specialfunc
        s.lockedmove=lockedfor
    def do_special(s,args):
        return s.specialfunc(args)
    
    def draws_cols(s,window,poses,mouse1,mouse2,textures,lsitofclasses):
        first=False
        second=False
        for i in range(len(s.listofplats2)):
            lsitofclasses=s.listofplats2[i].draw(window,lsitofclasses,textures)
            a=s.listofplats2[i].colidewithclicked(poses[0],mouse1)
            a1=s.listofplats2[i].colidewithclicked(poses[1],mouse2)
            if a:
                first=True
            elif a1:
                second=True
        return [[first,s],[second,s]],lsitofclasses
class Button:
    def __init__(s, x,y,w,h,picname):
        s.x=x
        s.y=y
        s.w=w
        s.h=h
        s.x-=s.w//2
        s.y-=s.h//2
        s.picname=picname
        
    def clickedon(s,mousePos,mouseState):
        if mouseState[0]:
            if pygame.Rect(s.x,s.y,s.w,s.h).collidepoint(mousePos[0],mousePos[1]):
                return True
        return False
    def draw(s,window,textures):
        window.blit(textures[s.picname],(s.x,s.y))
startbutton=Button(WIDTH//2,HEIGHT//2,WIDTH//(1920//200),HEIGHT//(1080//75),"startbutton")
class Startend(Platform):
    def __init__(s,pos,width,height):
        super().__init__(pos,width,height)
class Offerer:
    def __init__(s, offfers,height):
        s.offers=offfers
        s.height=height
        for i in range(len(s.offers)):
            for j in range(len(s.offers[i].listofplats2)):
                if j==0:
                    s.offers[i].x=WIDTH//6*(i+1)
                    s.offers[i].x+=s.offers[i].lockedmove[j][0]
                    s.offers[i].y=height//2
                    s.offers[i].y+=s.offers[i].lockedmove[j][1]
                else:
                    s.offers[i].listofplats2[j].x=WIDTH//6*(i+1)
                    s.offers[i].listofplats2[j].x+=s.offers[i].lockedmove[j][0]
                    s.offers[i].listofplats2[j].y=height//2
                    s.offers[i].listofplats2[j].y+=s.offers[i].lockedmove[j][1]
        s.width=WIDTH
    def draw(s,window):
        pass
    def move_offers(s,poses,mouse1,mouse2,textures,listofclasses):
        taken=[False,False,False,False]
        count=0
        for i in range(len(s.offers)):
            l,listofclasses=s.offers[count].draws_cols(window,poses,mouse1,mouse2,textures,listofclasses)
            if l[0][0] or l[1][0]:
                del s.offers[count]
                count-=1
            count+=1
            if l[0][0]:
                taken[0]=True
                taken[2]=l[0][1]
            if l[1][0]:
                taken[1]=True
                taken[3]=l[1][1]
        return taken,listofclasses
class Background:
    def drawbg(s,window,prozor,textures):
        if prozor=="menu":
            window.blit(textures["dinogame"],(0,0))
        if prozor=="game" or prozor=="taking":
            window.blit(textures["game"],(0,0))
bg=Background()
def empty(self):
    return []
class damage(Special):
    def __init__(s,pos,width,height,specialfunc,listofplatforms,lockedfor):
        super().__init__(pos,width,height,specialfunc,listofplatforms,lockedfor)
offerer=Offerer([Special((0,0),100,20,empty,[Platform((0,0),20,100)],[[0,0],[100,-100]]),Special((0,0),250,20,empty,[],[[0,0]]),Special((0,0),100,20,empty,[],[[0,0]]),Special((0,0),100,20,empty,[],[[0,0]]),Special((0,0),100,20,empty,[],[[0,0]])],300)
class gun(Special):
    pubid=0
    def __init__(s,pos,width,height,specialfunc,listofplatforms,lockedfor,time,direction,textures):
        super().__init__(pos,width,height,specialfunc,listofplatforms,lockedfor)
        s.time=time
        s.dir=direction
        s.id=s.pubid
        s.pubid+=1
        s.width=textures[f"crossbow{s.dir}"].get_width()
        s.height=textures[f"crossbow{s.dir}"].get_height()