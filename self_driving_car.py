import pygame
pygame.init()

drive   = True

window  = pygame.display.set_mode((1200,400))
track   = pygame.image.load("track6.png")

car     = pygame.image.load("tesla.png")
car     = pygame.transform.scale(car,(30,60))
car_x   = 155
car_y   = 305
direction = "up"

clock   = pygame.time.Clock()

focal_dis = 25
cam_x_offset = 0
cam_y_offset = 0

while drive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False
    
    clock.tick(60)

    cam_x = car_x + cam_x_offset + 15
    cam_y = car_y + cam_y_offset + 15

    # camera detection

    up    = window.get_at((cam_x,cam_y-focal_dis))[0]
    right = window.get_at((cam_x+focal_dis,cam_y))[0]
    down  = window.get_at((cam_x,cam_y+focal_dis))[0]
    
    print(up,right,down)


    # changing the direction

    if direction == "up" and up != 255 and right == 255:
        direction = "right"
        car       = pygame.transform.rotate(car, -90)
        cam_x_offset = 30

    elif direction == "right" and right != 255 and down == 255:
        direction = "down"
        car       = pygame.transform.rotate(car, -90)
        car_x     = car_x + 30
        cam_x_offset = 0
        cam_y_offset = 30
    
    elif direction == "down" and down != 255 and right == 255:
        direction = "right"
        car       = pygame.transform.rotate(car, 90)
        car_y     = car_y + 30
        cam_x_offset = 30
        cam_y_offset = 0
    
    elif direction == "right" and right != 255 and up == 255:
        direction = "up"
        car       = pygame.transform.rotate(car, 90)
        car_x    = car_x + 30
        cam_x_offset = 0

    # moving the car

    if direction == "up" and up == 255:
        car_y = car_y - 2

    elif direction == "right" and right == 255:
        car_x = car_x + 2
    
    elif direction == "down" and down == 255:
        car_y = car_y + 2
    

    window.blit(track,(0,0))
    window.blit(car,(car_x,car_y))
    pygame.draw.circle(window,(0,255,0),(cam_x,cam_y),5,5)

    pygame.display.update()