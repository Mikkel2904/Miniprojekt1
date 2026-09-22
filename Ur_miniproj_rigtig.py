import pygame
import math
import time


pygame.init() #starter pygame
screen_size = (640, 640) # laver størrelsen på vinduet
screen = pygame.display.set_mode((640, 640))


run_flag = True
while run_flag is True:

    screen.fill((255, 255, 255)) #laver skærmen hvid
    #indsætter billede af laks:
    laks = pygame.image.load("laks.png")
    laks = pygame.transform.scale(laks, (150,80))
    screen.blit(laks, (255, 320))
    
    #længder for visere:
    length_second = 185
    length_minute = 150
    length_hour = 100

    radius = 200
    x_start = 320 #320 er i midten fordi screen er 640
    y_start = 320

    #finder lokal tid:
    rn=time.localtime()
    hour = rn.tm_hour
    minute = rn.tm_min
    second = rn.tm_sec
    

    #fikser vinkler for visere:
    angle_sec = second*6-90
    angle_min = minute*6-90
    angle_tim = hour*30-90

    #sekunder
    x_end_sec = x_start + length_second*math.cos(math.radians(angle_sec))
    y_end_sec = y_start + length_second*math.sin(math.radians(angle_sec))
    pygame.draw.line(screen, (0,0,0),(x_start,y_start),(x_end_sec,y_end_sec), 2)

    #minutter
    x_end_min = x_start + length_minute*math.cos(math.radians(angle_min))
    y_end_min = y_start + length_minute*math.sin(math.radians(angle_min))
    pygame.draw.line(screen, (0,0,0),(x_start,y_start),(x_end_min,y_end_min), 2)

    #timer
    x_end_tim = x_start + length_hour*math.cos(math.radians(angle_tim))
    y_end_tim = y_start + length_hour*math.sin(math.radians(angle_tim))
    pygame.draw.line(screen, (0,0,0),(x_start,y_start),(x_end_tim,y_end_tim), 2)


    #tegner uret:
    pygame.draw.circle(screen, (0,0,0), (320, 320), 210, 2)
    pygame.draw.circle(screen, (0,0,0), (320, 320), 2, 3)
    start_position = (screen_size[0]/2, screen_size[1]/2)

    font = pygame.font.Font(None, 30)
    
    
    #streger til uret:
    for i in range(60):
        angle_streg = math.radians(i * 6 - 90)
        x_ude = 320 + 210 * math.cos(angle_streg)
        x_inde = 320 + 195 * math.cos(angle_streg)
        y_ude = 320 + 210 * math.sin(angle_streg)
        y_inde = 320 + 195 * math.sin(angle_streg)
        pygame.draw.line(screen, (0,0,0),(x_ude,y_ude),(x_inde,y_inde),2)

    #tykke streger til urets timer:(slet det hvis uret driller for at få det tilbage som normalt)
    for i in range(12):
        angle_streg = math.radians(i * 30 - 90)
        x_ude_1 = 320 + 210 * math.cos(angle_streg)
        x_inde_1 = 320 + 195 * math.cos(angle_streg)
        y_ude_1 = 320 + 210 * math.sin(angle_streg)
        y_inde_1 = 320 + 210 * math.sin(angle_streg)
        pygame.draw.line(screen, (0,0,0,), (x_ude_1,y_ude_1),(x_ude_1-15 * math.cos(angle_streg), y_ude_1-15*math.sin(angle_streg)), 5)



    #tal til timerne:
    font = pygame.font.Font(None, 30)

    for i in range(1, 13):
        angle_tal = math.radians(i * 30 - 90)
        x = 320 + 180 * math.cos(angle_tal)
        y = 320 + 180 * math.sin(angle_tal)
        text = font.render(str(i), True, (0, 0, 0))
        text_rect = text.get_rect(center=(x,y))
        screen.blit(text,text_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False
    pygame.display.flip()