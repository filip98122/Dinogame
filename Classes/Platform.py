from General_info import *
lbolts=[]
prozor="menu"
class Bolt:
    def __init__(s,dx,dy,y,x,dirrec,textures,id):
        s.dx=dx
        s.id=id
        s.dy=dy
        s.x=x
        s.y=y
        s.dir=dirrec
        s.speed=7
        s.w=textures[f"bolt{s.dir}"].get_width()
        s.h=textures[f"bolt{s.dir}"].get_height()
        s.x-=s.w//2
        s.y-=s.h//2
    def everything(s,window,textures):
        s.x+=s.dx*s.speed
        s.y+=s.dy*s.speed
        window.blit(textures[f"bolt{s.dir}"],(s.x,s.y))
    def end(self):
        self=None
class Platform:
    def __init__(s,pos,width,height):
        s.id=-1
        s.x,s.y=pos
        s.width=width
        s.height=height
        yalllow=5
    def draw(s,window,damage,textures):
        if type(s)==damage[0]:
            window.blit(textures["barbedwire"],(s.x,s.y))
        elif type(s)==damage[1]:
            window.blit(textures[f"crossbow{s.dir}"],(s.x,s.y))
            if damage[2]=="game":
                s.time=max(s.time-1,0)
                if s.time==0:
                    dx,dy=1,1
                    if s.dir=="u":
                        dx=0
                    if s.dir=='l':
                        dx*=-1
                        dy=0
                    if s.dir=="d":
                        dy*=-1
                        dx=0
                    if s.dir=="r":
                        dy=0
                    s.time=100
                    damage[3].append(Bolt(dx,dy,s.y+s.height//2,s.x+s.width//2,s.dir,textures,s.id))
            #pygame.draw.rect(window,(0,0,255),pygame.Rect(s.x,s.y,s.width,s.height))
        else:
            pygame.draw.rect(window,(255,255,100),pygame.Rect(s.x,s.y,s.width,s.height))
        return damage
    def ifplayerontop(s,px,py,pwidth,pheight):
        if ((s.x<=px<=s.x+s.width) or (s.x<=px+pwidth<=s.x+s.width) or (px<=s.x<=px+pwidth)) and py+pheight<=s.y:
                return [True,s.y,s.x,s.width,s.height,s]
        return [False,-1,-1,-1]
    def ifplayerbelow(s,px,py,pwidth,pheight):
        if ((s.x<=px<=s.x+s.width) or (s.x<=px+pwidth<=s.x+s.width) or (px<=s.x<=px+pwidth)) and py>=s.y+s.height:
            return [True,s.y+s.height,s.x,s.width,s.height,s]
        return [False,-1,-1,-1]
    def ifplayeronleftside(s,px,py,pwidth,pheight):
        if ((s.y<=py<=s.y+s.height) or (s.y<=py+pheight<=s.y+s.height) or (py<=s.y<=py+pheight)) and px+pwidth<s.x:
            return [True,s.y,s.x,s.width,s.height,s]
        return [False,-1,-1,-1]
    def ifplayeronrightside(s,px,py,pwidth,pheight):
        if ((s.y<=py<=s.y+s.height) or (s.y<=py+pheight<=s.y+s.height) or (py<=s.y<=py+pheight)) and px>s.x+s.width:
            return [True,s.y,s.x+s.width,s.width,s.height,s]
        return [False,-1,-1,-1]
    def colidewithclicked(s,mousepos,mousestate):
        if s.x+s.width>=mousepos[0]>=s.x and s.y+s.height>=mousepos[1]>=s.y and mousestate:
            return True
        return False
    def ifplayeronleftsidefor(s,px,py,pwidth,pheight):
        if ((s.y<py<s.y+s.height) or (s.y<py+pheight<s.y+s.height) or (py<s.y<py+pheight)) and px+pwidth<=s.x:
            return [True,s.y,s.x,s.width,s.height,s]
        return [False,-1,-1,-1]
    def ifplayeronrightsidefor(s,px,py,pwidth,pheight):
        if ((s.y<py<s.y+s.height) or (s.y<py+pheight<s.y+s.height) or (py<s.y<py+pheight)) and px>=s.x+s.width:
            return [True,s.y,s.x+s.width,s.width,s.height,s]
        return [False,-1,-1,-1]