import pygame 
import random
import math

pygame.init()#初始化

#音效
pygame.mixer.music.load('bg.mp3')#导入背景音乐
pygame.mixer.music.set_volume(0.1) #音量
pygame.mixer.music.play(loops=-1)#循环播放
#击中音效
bao_sound = pygame.mixer.Sound('jz.mp3')

#1显示背景
bg=pygame.image.load('bg.jpg')#背景图片变量导入
bgpos=bg.get_rect() #获取大小
size=width,height=1024, 576 #根据图片大小设定
screen=pygame.display.set_mode(size) #创建窗口
pygame.display.set_caption("歼灭敌机")

#分数
score = 0
font = pygame.font.Font('freesansbold.ttf',32)#分数字体，此处用pygane自带的

def show_score():
    text = f"Score: {score}"#注意：pygame自带的字体不支持中，可自行更换字体
    score_render = font.render(text,True,(0,255,0))
    screen.blit(score_render,(10,10))

#2玩家设定（定义变量）
wanjia=pygame.image.load('wanjia.gif')#设置玩家初始位置
wanjiaX = 525
wanjiaY = 470
wanjiaStepX = 0#玩家移动速度
wanjiaStepY = 0
    
#添加敌人
number_of_enemies = 8#敌人数量

#结束游戏
is_over = False
over_font = pygame.font.Font('freesansbold.ttf',64)
def check_is_over():
    if is_over:
        text = "GAME OVER !"
        render = over_font.render(text,True,(255,0,0))
        screen.blit(render,(330,220))


#子弹和敌人之间的距离，勾股定理计算
def distance1(bx,by,ex,ey):
    a = bx - ex
    b = by - ey
    return math.sqrt(a*a + b*b)#开根号

#敌人与玩家之间的距离
def distance2(cx,cy,ex,ey):
    c = cx - ex
    d = cy - ey
    return math.sqrt(c*c + d*d)


#敌人类
class Enemy():
    def __init__(self):
        self.img = pygame.image.load('enemy.png')
        self.x = random.randint(225,700)
        self.y = random.randint(100,200)
        self.stepx = random.randint(1,2)#移速范围
        self.stepy = random.randint(1,2)
    #当被射中时恢复位置
    def reset(self):
        self.x = random.randint(225,700)
        self.y = random.randint(100,150)
        
    def bump(self):#敌人与玩家相撞
            global is_over
            for e in enemies:
                if (distance2(self.x,self.y,wanjiaX,wanjiaY)  < 30):
                    is_over = True
                    enemies.clear()#敌人清屏
                    print("GAME OVER !")
                      
        
enemies = []#保存所有敌人
for i in range (number_of_enemies):
    enemies.append(Enemy())



#子弹类
class Bullet():
    def __init__(self):#类中定义一个函数必须有参数self
        self.img = pygame.image.load('bullet.png')
        self.x = wanjiaX +29.5 #(wanjia-bullet)/2
        self.y = wanjiaY + 10
        self.step = 4 #子弹速度
     #击中
    def hit(self):
        global score
        for e in enemies:
            if(distance1(self.x,self.y,e.x,e.y) < 30):
                #射中后
                bao_sound.play()
                bullets.remove(self)
                e.reset()
                score += 1#击中加分
                print(score)
             
bullets = [] #保存现有子弹

#显示并移动子弹
def show_bullets():
    for b in bullets:
        screen.blit(b.img,(b.x,b.y))
        b.hit()#看是否击中敌人
        b.y -= b.step#子弹只在Y上移动
        
        #判断子弹是否出界，若出界则移除
        if b.y < 0:
            bullets.remove(b)


#显示敌人且移动
def show_enemy():#防止出界
    for e in enemies:
        screen.blit(e.img,(e.x,e.y))
        e.bump()
        e.x += e.stepx
        e.y += e.stepy
        if(e.x > 978 or e.x < 0):
            e.stepx *= -1
        if(e.y> 512 or e.y < 0):
            e.stepy *= -1

def move_wanjia():
    global wanjiaX,wanjiaY
    wanjiaX += wanjiaStepX
    wanjiaY += wanjiaStepY

    if wanjiaX > 959:#防止出界
        wanjiaX = 959
    if wanjiaX < 0:
        wanjiaX = 0
    if wanjiaY > 497:
        wanjiaY = 497
    if wanjiaY < 0:
        wanjiaY=0

      
#主循环
running = True
while running:
    screen.blit(bg,(0,0))
    show_score()#显示分数
    for event in pygame.event.get():#获取事件
        if event.type==pygame.QUIT:#如果获取的事件等于退出
            running = False
        #设置按键控制飞机左右移动
        if event.type == pygame.KEYDOWN:#按下移动
            if event.key == pygame.K_RIGHT:#按→向右移动
                wanjiaStepX = 4
            elif event.key == pygame.K_LEFT:#按←向左移动
                wanjiaStepX = -4
            elif event.key == pygame.K_SPACE:#按下空格，发射子弹
                print('发射子弹...')
                      #创建一颗子弹
                bullets.append(Bullet())
                
        if event.type == pygame.KEYUP:#抬起就停止
            wanjiaStepX = 0
        #设置按键控制飞机上下移动
        if event.type == pygame.KEYDOWN:#按下移动
            if event.key == pygame.K_UP:#按↑向上移动
                wanjiaStepY = -4
            elif event.key == pygame.K_DOWN:#按↓向下移动
                wanjiaStepY = 4
        if event.type == pygame.KEYUP:#抬起就停止
            wanjiaStepY = 0
        
    screen.blit(wanjia,(wanjiaX,wanjiaY))#玩家初位置
    
    move_wanjia()#移动玩家
    show_enemy()#显示敌人
    show_bullets()#显示子弹
    check_is_over()#显示游戏结束字幕
    pygame.display.update()
