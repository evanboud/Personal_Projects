import pygame
import random

class Ball():

    def __init__(self, position=(0,0), velocity=(.5,.5), r=12):
                self.position = (random.randint(220,550),random.randint(150,480))
                self.velocity = random.uniform(-.5,.5),.5
                self.r = r
                

    def create_ball(self, screen):
         pygame.draw.circle(screen, (0,0,255), self.position, self.r )

    def change_position(self):
        gravity = .5
        friction = .95
        x , y = self.position
        vx , vy = self.velocity
        x = x + vx 
        vy = vy + gravity
        y = y + vy 
        if x + self.r >= 593:
            vx = -vx
            x = 593 - self.r
        if x - self.r <= 207:
            vx = -vx
            x = 207 + self.r
        if y + self.r >= 493:
            vy = -vy
            y = 493 - self.r
        if y == (493- self.r):
            vx = vx * friction
        if y - self.r <= 107:
            vy = -vy
            y = 107 + self.r        
        self.position = (x,y)
        self.velocity = (vx,vy)

    def bounce_vx(self):
        vx , vy = self.velocity
        self.velocity = (-vx, vy)
    def bounce_vy(self):
            vx , vy = self.velocity
            self.velocity = (vx,-vy)
    
pygame.init()   

screen = pygame.display.set_mode((800, 600))

square = pygame.Rect(0,0,400,400)
square.center = (400,300)

clock = pygame.time.Clock()

total_balls = [Ball() for i in range(5)]
run = True
while run:
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255, 255, 255),square, width=7)
    clock.tick(5)
    for ball in total_balls:
        ball.create_ball(screen)
        ball.change_position()
        for ball1 in total_balls:
            if ball is ball1:
                continue
            v1 = pygame.math.Vector2(ball.position)
            v2 = pygame.math.Vector2(ball1.position)
            v3 = pygame.math.Vector2(ball.velocity)
            v4 = pygame.math.Vector2(ball1.velocity)
            
            overlap = (ball.r + ball1.r) - v1.distance_to(v2) 
            if v1.distance_to(v2) < (ball.r + ball1.r):
                line_vector = (v2 - v1).normalize()
                push = line_vector * (overlap/2)
                ball.position = (ball.position - push)
                ball1.position = (ball1.position + push)

                velocity_vector = (v3 - v4)
                dot_product = pygame.math.Vector2.dot(velocity_vector,line_vector)
                v_out = velocity_vector -2 * (dot_product) *line_vector
                ball.velocity = v_out
                
            
                
                    
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
        
