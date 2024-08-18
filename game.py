import pygame
import random
pygame.init()
win=pygame.display.set_mode(size=(500,480))
pygame.display.set_caption('First Game')

'''Importing the Images(Character and background)'''
walk_right=[pygame.image.load('Data/R1.png'),pygame.image.load('Data/R2.png'),pygame.image.load('Data/R3.png'),pygame.image.load('Data/R4.png'),pygame.image.load('Data/R5.png'),pygame.image.load('Data/R6.png'),pygame.image.load('Data/R7.png'),pygame.image.load('Data/R8.png'),pygame.image.load('Data/R9.png')]
walk_left=[pygame.image.load('Data/L1.png'),pygame.image.load('Data/L2.png'),pygame.image.load('Data/L3.png'),pygame.image.load('Data/L4.png'),pygame.image.load('Data/L5.png'),pygame.image.load('Data/L6.png'),pygame.image.load('Data/L7.png'),pygame.image.load('Data/L8.png'),pygame.image.load('Data/L9.png')]
bg=pygame.image.load('Data/bg.jpg')
char=pygame.image.load('Data/standing.png')


clock=pygame.time.Clock()

####################################################################################################################
class player(object):
    def __init__(self,x,y,width,height):
        '''Variables'''
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.velocity=5
        self.left=0
        self.right=0
        self.isjump=0
        self.walk_count=0
        self.jump_count=10
        self.standing=1
        self.hitbox=(int(self.x+17),int(self.y+11),29,52)  #making a rectangle with (x,y,width,height)


    def draw(self,win):
        self.hitbox=(int(self.x+17),int(self.y+11),29,52)
        #pygame.draw.rect(win,(0,0,0),self.hitbox,2)
        if self.walk_count+1>=27:
            self.walk_count=0

        if self.standing==0:
            if self.left==1:
                win.blit(walk_left[self.walk_count//3],(int(self.x),int(self.y)))
                self.walk_count+=1
            elif self.right==1:
                win.blit(walk_right[self.walk_count//3],(int(self.x),int(self.y)))
                self.walk_count+=1
        else:
            if self.right==1:
                win.blit(walk_right[0],(int(self.x),int(self.y)))
            else:
                win.blit(walk_left[0],(int(self.x),int(self.y)))



####################################################################################################################
class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.facing=facing
        self.velocity=8

    def draw(self,win):
        pygame.draw.circle(win,self.color,(int(self.x),int(self.y)),self.radius)



####################################################################################################################
class enemy(object):
    walk_right=[pygame.image.load('Data/R1E.png'),pygame.image.load('Data/R2E.png'),pygame.image.load('Data/R3E.png'),pygame.image.load('Data/R4E.png'),pygame.image.load('Data/R5E.png'),pygame.image.load('Data/R6E.png'),pygame.image.load('Data/R7E.png'),pygame.image.load('Data/R8E.png'),pygame.image.load('Data/R9E.png'),pygame.image.load('Data/R10E.png'),pygame.image.load('Data/R11E.png')]
    walk_left=[pygame.image.load('Data/L1E.png'),pygame.image.load('Data/L2E.png'),pygame.image.load('Data/L3E.png'),pygame.image.load('Data/L4E.png'),pygame.image.load('Data/L5E.png'),pygame.image.load('Data/L6E.png'),pygame.image.load('Data/L7E.png'),pygame.image.load('Data/L8E.png'),pygame.image.load('Data/L9E.png'),pygame.image.load('Data/L10E.png'),pygame.image.load('Data/L11E.png')]

    def __init__(self,x,y,width,height,end):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.end=end
        self.path=[self.x,self.end]
        self.x_velocity=0
        self.y_velocity=0
        self.walk_count=0
        self.velocity=3
        self.hitbox=(int(self.x+17),int(self.y+2),31,57)  #making a rectangle with (x,y,width,height)
        self.x_walk_count=0
        self.y_walk_count=0
        self.rand_count=20

    def draw(self,win):
        self.move()
        if self.walk_count+1>=33:
            self.walk_count=0

        if self.velocity>0:
            win.blit(self.walk_right[self.walk_count//3],(int(self.x),int(self.y)))
            self.walk_count+=1
        else:
            win.blit(self.walk_left[self.walk_count//3],(int(self.x),int(self.y)))
            self.walk_count+=1
        self.hitbox=(int(self.x+17),int(self.y+2),31,57)
        # pygame.draw.rect(win,(200,0,0),self.hitbox,2)




    def move(self):
        if self.velocity>0:
            if self.x+self.velocity<self.path[1]:
                self.x+=self.velocity
            else:
                self.velocity*=-1
                self.walk_count=0
        else:
            if self.x-self.velocity>self.path[0]:
                self.x+=self.velocity
            else:
                self.velocity*=-1
                self.walk_count=0


    def randmove(self):
        if self.x_walk_count>self.rand_count:
            self.x_walk_count=0
        if self.y_walk_count>self.rand_count:
            self.y_walk_count=0
        if self.x_walk_count==0:
            self.x_velocity=random.randint(-5,5)
            print('x',self.x_velocity)
        if self.y_walk_count==0:
            self.y_velocity=random.randint(-5,5)
            print('y',self.y_velocity)

        if self.x_velocity<0:
            if 0<self.x+(self.x_velocity*self.rand_count):
                self.x+=self.x_velocity
            self.x_walk_count+=1
        else:
            if self.x+(self.x_velocity*self.rand_count)<500:
                self.x+=self.x_velocity
            self.x_walk_count+=1

        if self.y_velocity<0:
            if (self.y+(self.y_velocity*self.rand_count))>200:
                self.y+=self.y_velocity
            self.y_walk_count+=1
        else:
            if self.y+(self.y_velocity*self.rand_count)<400:
                self.y+=self.y_velocity
            self.y_walk_count+=1            

    def randdraw(self,win):
        self.randmove()
        if self.x_velocity>0:
            win.blit(self.walk_right[0],(int(self.x),int(self.y)))
        else:
            win.blit(self.walk_left[0],(int(self.x),int(self.y)))
        self.hitbox=(int(self.x+17),int(self.y+2),31,57)
        # pygame.draw.rect(win,(200,0,0),self.hitbox,2)




    def hit(self):
        print('Hit')
        pass




####################################################################################################################
def redraw_game_window():
    win.blit(bg,(0,0))
    man.draw(win)
    goblin.randdraw(win)
    for bullet in bullets:
        bullet.draw(win)
    
    pygame.display.update()
    





####################################################################################################################
'''Mainloop'''
man=player(300,410,64,64)
goblin=enemy(100,410,64,64,450)
shoot_loop=0        #this is something like bullet cooldown
bullets=[]
run=1
while run==1:
    clock.tick(27)

    if shoot_loop>0:            #here we have given ooportunity to shoot_loop to increment automatically in a frame. The shoot_loop becomes 0 only if this runs. That means, if we had shoot a bullet, the gun gets hot (by making the shoot_loop=1, i.e. shoot_loop>0) & it takes some time to cooldown (to make shoot_loop=0).
        shoot_loop+=1
    if shoot_loop>3:
        shoot_loop=0
    


    
    for event in pygame.event.get(): 
        if event.type==pygame.QUIT:  
            run=0


    for bullet in bullets:
        if bullet.y-bullet.radius<goblin.hitbox[1]+goblin.hitbox[3] and bullet.y+bullet.radius>goblin.hitbox[1]:
            if bullet.x-bullet.radius<goblin.hitbox[0]+goblin.hitbox[2] and bullet.x+bullet.radius>goblin.hitbox[0]:
                goblin.hit()
                bullets.pop(bullets.index(bullet))

        if bullet.x<500 and bullet.x>0:
            bullet.x+=bullet.velocity*bullet.facing
        else:
            bullets.pop(bullets.index(bullet))  #remove the bullets going out of the window


    keys=pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shoot_loop==0:
        if man.left==1:
            facing=-1
        else:
            facing=1
        if len(bullets)<=5:
            bullets.append(projectile((round(man.x+man.width//2)),(round(man.y+man.height//2)),6,(255,0,0),facing))
        shoot_loop=1

    
    if keys[pygame.K_LEFT] and man.x>0:
        man.x-=man.velocity
        man.left=1
        man.right=0
        man.standing=0
    elif keys[pygame.K_RIGHT] and man.x<500-man.width:
        man.x+=man.velocity
        man.left=0
        man.right=1
        man.standing=0
    else:
        man.standing=1
        man.walk_count=0

    if man.isjump==0:
        if keys[pygame.K_UP]:
            man.isjump=1
            man.walk_count=0
    else:
        if man.jump_count>=-10:
            negative=1
            if man.jump_count<0:
                negative=-1
            man.y-=(man.jump_count**2)*negative/2
            man.jump_count-=1
        else:
            man.isjump=0
            man.jump_count=10

    redraw_game_window()
    
    


pygame.quit()
