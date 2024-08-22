import pygame
import sys

#code

pygame.init()

background_colour = (255,255,255)

screen = pygame.display.set_mode((660,400))
pygame.display.set_caption("window")
screen.fill(background_colour)

#images

rock = pygame.image.load("images/rock.gif").convert()
rock_rect = rock.get_rect(topleft=(0,0))
paper = pygame.image.load("images/paper.jpeg").convert()
paper_rect = paper.get_rect(topleft=(220,0))
paper = pygame.transform.scale(paper, (220,220))
scissors = pygame.image.load("images/scissors.jpeg").convert()
scissors = pygame.transform.scale(scissors, (220, 220))
scissors_rect = scissors.get_rect(topleft=(440,0))

userchoice = 1
aichoice = 3

running = True

while running:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()  # Get mouse click position
            
            if rock_rect.collidepoint(mouse_pos):
                print("user chose rock")
                userchoice = 1
            if paper_rect.collidepoint(mouse_pos):
                print("user chose paper")
                userchoice = 2
            if scissors_rect.collidepoint(mouse_pos):
                print("user chose scissors")
                userchoice = 3


            if userchoice == 1 and aichoice == 2:
                print("ai wins!")
            elif userchoice == 2 and aichoice == 1:
                print("user wins!")
            elif userchoice == 1 and aichoice == 3:
                print("user wins!")
            elif userchoice == 3 and aichoice == 1:
                print("ai wins!")
            elif userchoice == 1 and aichoice == 1:
                print("tie!")
            elif userchoice == 2 and aichoice == 3:
                print("ai wins!")
            elif userchoice == 3 and aichoice == 2:
                print("user wins!")
            elif userchoice == 2  and aichoice == 2:
                print("tie!")
            elif userchoice == 3 and aichoice == 3:
                print("tie")


        screen.blit(rock,rock_rect)
        screen.blit(paper, paper_rect)
        screen.blit(scissors, scissors_rect)
        pygame.display.flip()
