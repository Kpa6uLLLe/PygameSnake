import pygame 
from random import randrange
difficult=int(input("Рекомендуемая сложность - 3, наибольшая - 1 \n"))
speed=int(input("Рекомендуемая скорость - 3, самая быстрая - 1 \n"))
RES = 600
length = 1
SIZE = 12
pygame.init()
sc = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()
score = 0
eaten = 0
dirs = {'W': True, 'A': True, 'S': True, 'D': True}
font_sc = pygame.font.SysFont('Arial', 26, bold=True)
timer = 600
maxm=-1
while True:
    x,y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
    apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
    snake = [(x,y)]
    dx,dy = 0,0
    fps = 600
    count=0
    length = 1
    lasteat=0
    sc = pygame.display.set_mode([RES, RES])
    clock = pygame.time.Clock()
    score = 0
    eaten = 0
    dirs = {'W': True, 'A': True, 'S': True, 'D': True}
    font_sc = pygame.font.SysFont('Arial', 18, bold=True)

    while True:
        if score>maxm:
            maxm=score
        while apple in snake:
            apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        dirs = {'W': True, 'A': True, 'S': True, 'D': True}
        sc.fill(pygame.Color('black'))
        #snake
        [(pygame.draw.rect(sc, pygame.Color('green'), (i,j, SIZE-2, SIZE-2))) for i, j in snake]
        pygame.draw.rect(sc, pygame.Color('red'), (*apple, SIZE, SIZE))
        #score
        tr = (((200*difficult-(count-lasteat))/60) + abs(((difficult*200-(count-lasteat))/60)))/2
        tr2 = (((300*difficult-(count-lasteat))/60) + abs(((300*difficult-(count-lasteat))/60)))/2
        rendersc = font_sc.render(f'Score: {score}', 1, pygame.Color('Grey'))
        rendereat = font_sc.render(f'Eaten: {eaten}', 1, pygame.Color('Grey'))
        rendertime = font_sc.render(f'Time: {"{0:.2f}".format((count/60))}', 1, pygame.Color('Grey'))
        if tr>=2:
            rendertr = font_sc.render(f'Bonuses burn in: {"{0:.2f}".format(tr)}', 1, pygame.Color('Green'))
        elif 0<tr<2 and count%30 < 10:
            rendertr = font_sc.render(f'Bonuses burn in: {"{0:.2f}".format(tr)}', 1, pygame.Color('Red'))
        elif 0<tr<2 and 9 < count%30 <20:
            rendertr = font_sc.render(f'Bonuses burn in: {"{0:.2f}".format(tr)}', 1, pygame.Color('Orange'))
        elif 0<tr<2 and count%30 >19:
            rendertr = font_sc.render(f'Bonuses burn in: {"{0:.2f}".format(tr)}', 1, pygame.Color('White'))
        else:
            if eaten<score and count%(int(20/difficult)):
                score-=1
            if tr2>0:
                rendertr = font_sc.render(f'Snake starts decreasing in: {"{0:.2f}".format(tr2)}', 1, pygame.Color('Gold'))
            elif tr2 == 0 :
                rendertr = font_sc.render(f'YOU LOOSING WEIGHT!!!{"{0:.2f}".format((count%(30*difficult)/60))}', 1, pygame.Color('Gold'))
                if count%(45*difficult) == 0:
                    length-=1
                
        sc.blit(rendersc, (4,0))
        sc.blit(rendereat, (4,20))
        sc.blit(rendertime, (4,40))
        sc.blit(rendertr, (4,60))
        
        #move
        if count%speed == 0:
            x += dx * SIZE
            y += dy * SIZE
            snake.append((x, y))
            snake = snake[-length:]
        #eat
        if snake[-1] == apple:
            apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
            length+=1
            eaten+=1
            score+=1+eaten
            lasteat=count
            
            
        #gg
        if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)) or length <= 0:
            pygame.display.flip()
            break
           
      

        if count%240 == 0:
            score+=1
        

        fontrecs = pygame.font.SysFont('Arial',21, bold=True)
        record = fontrecs.render(f'Your record: {maxm}', 1, pygame.Color('Orange'))
        sc.blit(record, (RES-180,RES-25))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        key = pygame.key.get_pressed()
        if key[pygame.K_w] and dirs['W'] and dy != 1 :
            dx,dy = 0, -1
            dirs = {'W': True, 'A': False, 'S': False, 'D': False}
        if key[pygame.K_s] and dirs['S'] and dy != -1:
            dx,dy = 0, 1
            dirs = {'W': False, 'A': False, 'S': True, 'D': False}
        if key[pygame.K_d] and dirs['D'] and dx != -1:
            dx,dy = 1, 0
            dirs = {'W': False, 'A': False, 'S': False, 'D': True}
        if key[pygame.K_a] and dirs['A'] and dx != 1 :
            dx,dy = -1, 0
            dirs = {'W': False, 'A': True, 'S': False, 'D': False}
        pygame.display.flip()
        clock.tick(60)
        count+=1
        
