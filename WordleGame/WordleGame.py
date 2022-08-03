from concurrent.futures import thread
from this import s
import threading
from distutils.log import debug
from turtle import Screen
import pygame,sys
import WordleSystem
import random


WORDS = open("wordlist10000.txt").read().splitlines()
pygame.init()

#window
clock = pygame.time.Clock()
background_colour = (20, 20, 20)
screen = pygame.display.set_mode([800, 600], pygame.NOFRAME)
pygame.display.set_caption('Wordle')
pygame_events = pygame.event.get()
programIcon = pygame.image.load('icon.png')
pygame.display.set_icon(programIcon)
#Fonts
base_font = pygame.font.Font(None, 32)
title_font = pygame.font.Font(None, 150)
windowBarFont = pygame.font.SysFont("segoeuisymbol", 16)

#loop
running = True
def YouWin():
    pass

def windowBar():
    pygame.draw.rect(screen, (255, 195, 0), pygame.Rect(0, 0, 800, 20), 0)
    pygame.draw.rect(screen, (231, 76, 60), pygame.Rect(780, 0, 20, 20), 0)
    pygame.draw.rect(screen, (255, 195, 0), pygame.Rect(0, 0, 800, 600), 1)
    TextSurface = windowBarFont.render( "✖", True, (255,255,255))
    screen.blit(TextSurface ,TextSurface.get_rect(center=(pygame.Rect(780, 0, 20, 20).x + 10, pygame.Rect(780, 0, 20, 20).y + 10)))


def screenUpdate():
    pygame.display.flip()
    screen.fill(background_colour)
    clock.tick(60)

def closeWindow(event):
    if pygame.Rect(780, 0, 20, 20).collidepoint(event.pos):
       global running
       running = False
       pygame.quit()
       sys.exit()

class TextRender():
    def __init__(self, Text, Color, x, y, font):
        self.Text = Text
        self.Color =  Color
        self.x = x
        self.y = y
        self.font = font
    def createCentered(self):
        TextSurface = self.font.render(self.Text, True, self.Color)
        screen.blit(TextSurface ,TextSurface.get_rect(center=(screen.get_size()[0]/2, self.y)))
    def createManual(self):
        TextSurface = self.font.render(self.Text, True, self.Color)
        screen.blit(TextSurface ,(self.x, self.y))
    def input(self, text):
        self.Text += text
    def change(self, text):
        self.Text = text



        #110 to the side
class boxes():
    x = 205
    y = 85
    color = (255, 255, 255)
    border_color = (255, 195, 0)
    fill = 2
    def __init__(self, Letter, x_Index, y_Index):
        self.Letter = Letter
        self.x_Index = x_Index
        self.y_Index = y_Index
    def create(self):
        inprect = pygame.Rect(self.x + 80 * self.x_Index, self.y + 80*self.y_Index, 70, 70)
        TextSurface = base_font.render(self.Letter, True, self.color)
        pygame.draw.rect(screen, self.border_color, inprect, self.fill)
        screen.blit(TextSurface ,TextSurface.get_rect(center=(inprect.x + 35, inprect.y + 35)))
    def changeLetter(self, Letter, State):
        if State == "True":
            self.border_color = (46, 204, 113)
            self.Letter = Letter
            self.fill = 0
        elif State == "Exists":
            self.Letter = Letter
            self.fill = 0
        elif State == "False":
            self.border_color = (231, 76, 60)
            self.Letter = Letter
            self.fill = 0
        elif State == "Neutral":
            self.Letter = Letter.upper()

        
class Menu():
        def __init__(self, Statso):
           self.Status = Statso

        def Start(self):

            Description = TextRender("Press Enter To Start",(255, 195, 0),screen.get_size()[0]/2 - 90, screen.get_size()[1]/2 + 45, base_font)
            Title = TextRender("WORDLE.",(255, 195, 0),screen.get_size()[0]/2 - 105, 275, title_font)
            while self.Status:
                #inputs
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        closeWindow(event)
                    if event.type == pygame.KEYDOWN:
                        if event.key  == pygame.K_RETURN:
                             randoWord = random.choice(WORDS)
                             while True:
                                 if len(randoWord) == 5:
                                     print(randoWord)
                                     break
                                 else:
                                     randoWord = random.choice(WORDS)
                             WordleSystem.AddWord(randoWord.upper())
                             threading.Thread(target=InProgress(True).Start()).start()
                             self.Status = False
                #Rectangle
                #Render
                Title.createCentered()
                Description.createCentered()
                windowBar()
                screenUpdate()
                



class InProgress():
        def __init__(self, Statso):
           self.Status = Statso

        def Start(self):
            inprect = pygame.Rect(screen.get_size()[0]/2 - 40,screen.get_size()[1]/2 + 230,90,32)
            Description = TextRender("Guess",(255, 195, 0),screen.get_size()[0]/2 - 30, screen.get_size()[1]/2 + 215, base_font)
            You_Win = TextRender("",(255, 255, 255),screen.get_size()[0]/2 - 30, screen.get_size()[1]/2, title_font)            
            You_Win_Overlay = pygame.Surface((screen.get_size()[0],screen.get_size()[1]))
            You_Win_Toggle = 0
            You_Win_Overlay.fill((0, 0, 0))   
            input_text = TextRender("",(255, 255, 255),inprect.x + 10, inprect.y + 5, base_font)
            Attempts = 0
            AttemptsLeft = 5
            colrect = (255, 195, 0)
            borderToggle = 2
            TB1_1 = boxes("", 0, 0)
            TB1_2 = boxes("", 1, 0)
            TB1_3 = boxes("", 2, 0)
            TB1_4 = boxes("", 3, 0)
            TB1_5 = boxes("", 4, 0)
            row1 = [TB1_1,TB1_2,TB1_3,TB1_4,TB1_5]
            TB2_1 = boxes("", 0, 1)
            TB2_2 = boxes("", 1, 1)
            TB2_3 = boxes("", 2, 1)
            TB2_4 = boxes("", 3, 1)
            TB2_5 = boxes("", 4, 1)
            row2 = [TB2_1,TB2_2,TB2_3,TB2_4,TB2_5]
            TB3_1 = boxes("", 0, 2)
            TB3_2 = boxes("", 1, 2)
            TB3_3 = boxes("", 2, 2)
            TB3_4 = boxes("", 3, 2)
            TB3_5 = boxes("", 4, 2)
            row3 = [TB3_1,TB3_2,TB3_3,TB3_4,TB3_5] 
            TB4_1 = boxes("", 0, 3)
            TB4_2 = boxes("", 1, 3)
            TB4_3 = boxes("", 2, 3)
            TB4_4 = boxes("", 3, 3)
            TB4_5 = boxes("", 4, 3)
            row4 = [TB4_1,TB4_2,TB4_3,TB4_4,TB4_5]
            TB5_1 = boxes("", 0, 4)
            TB5_2 = boxes("", 1, 4)
            TB5_3 = boxes("", 2, 4)
            TB5_4 = boxes("", 3, 4)
            TB5_5 = boxes("", 4, 4)
            row5 = [TB5_1,TB5_2,TB5_3,TB5_4,TB5_5]
            BoxesTotal = [[TB1_1,TB1_2,TB1_3,TB1_4,TB1_5], [TB2_1,TB2_2,TB2_3,TB2_4,TB2_5], [TB3_1,TB3_2,TB3_3,TB3_4,TB3_5], [TB4_1,TB4_2,TB4_3,TB4_4,TB4_5], [TB5_1,TB5_2,TB5_3,TB5_4,TB5_5]]
            count = 0
            typeCount = 0
            while self.Status:
                #inputs
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        closeWindow(event)
                    if event.type == pygame.KEYDOWN:
                        #Enter
                        if event.key  == pygame.K_RETURN:
                            print("============================================================")
                            if len(input_text.Text) < 5:
                             print("Too Short")
                             Description.change("Too Short")
                            #Main
                            else:
                             typeCount = 0
                             if count == 0:
                                 corrects = 0
                                 for x in row1:
                                        x.changeLetter(WordleSystem.getLetter(input_text.Text, x.x_Index), WordleSystem.CheckGuess(input_text.Text, AttemptsLeft, x.x_Index))
                                        if WordleSystem.CheckGuess(input_text.Text, AttemptsLeft, x.x_Index) == "True":
                                            corrects = corrects + 1
                                 if corrects == 5:
                                     You_Win.change("YOU WIN!")
                                     You_Win_Toggle = 175
                                 Attempts = Attempts + 1
                                 AttemptsLeft = AttemptsLeft - 1
                                 count = count + 1
                                 input_text.change("")
                             elif count == 1:
                                 corrects = 0
                                 for x in row2:
                                        x.changeLetter(WordleSystem.getLetter(input_text.Text, x.x_Index), WordleSystem.CheckGuess(input_text.Text, AttemptsLeft, x.x_Index))                           
                                        if WordleSystem.CheckGuess(input_text.Text, AttemptsLeft, x.x_Index) == "True":
                                            corrects = corrects + 1
                                 if corrects == 5:
                                     You_Win.change("YOU WIN!")
                                     You_Win_Toggle = 175
                                 Attempts = Attempts + 1
                                 AttemptsLeft = AttemptsLeft - 1
                                 count = count + 1
                                 input_text.change("")
                             elif count == 2:
                                 corrects = 0
                                 for x in row3:
                                        x.changeLetter(WordleSystem.getLetter(input_text.Text, x.x_Index), WordleSystem.CheckGuess(input_text.Text, AttemptsLeft, x.x_Index))                           
                                        if WordleSystem.CheckGuess(input_text.Text, AttemptsLeft, x.x_Index) == "True":
                                            corrects = corrects + 1
                                 if corrects == 5:
                                     You_Win.change("YOU WIN!")
                                     You_Win_Toggle = 175
                                 Attempts = Attempts + 1
                                 AttemptsLeft = AttemptsLeft - 1
                                 count = count + 1
                                 input_text.change("")
                             elif count == 3:
                                 corrects = 0
                                 for x in row4:
                                        x.changeLetter(WordleSystem.getLetter(input_text.Text, x.x_Index), WordleSystem.CheckGuess(input_text.Text, AttemptsLeft, x.x_Index))                           
                                        if WordleSystem.CheckGuess(input_text.Text, AttemptsLeft, x.x_Index) == "True":
                                            corrects = corrects + 1
                                 if corrects == 5:
                                     You_Win.change("YOU WIN!")
                                     You_Win_Toggle = 175
                                 Attempts = Attempts + 1
                                 AttemptsLeft = AttemptsLeft - 1
                                 count = count + 1
                                 input_text.change("")
                             elif count == 4:
                                 corrects = 0
                                 for x in row5:
                                        x.changeLetter(WordleSystem.getLetter(input_text.Text, x.x_Index), WordleSystem.CheckGuess(input_text.Text, AttemptsLeft, x.x_Index))                           
                                        if WordleSystem.CheckGuess(input_text.Text, AttemptsLeft, x.x_Index) == "True":
                                            corrects = corrects + 1
                                 if corrects == 5:
                                     You_Win.change("YOU WIN!")
                                     You_Win_Toggle = 175
                                 else:
                                     You_Win.change("YOU LOSE")
                                     You_Win_Toggle = 175
                                     Attempts = Attempts + 1
                                     AttemptsLeft = AttemptsLeft - 1
                                     count = count + 1
                                 input_text.change("")

                        #Backspace
                        elif event.key  == pygame.K_BACKSPACE:
                            if typeCount > 0:
                               typeCount = typeCount - 1
                            BoxesTotal[count][typeCount].changeLetter("", "Neutral")
                            input_text.change(input_text.Text[:-1])
                        #Keyboard
                        elif event.key  == pygame.K_SPACE:
                            pass
                        elif len(input_text.Text) < 5:
                            BoxesTotal[count][typeCount].changeLetter(event.unicode, "Neutral")
                            if typeCount <= 4:
                             typeCount = typeCount + 1
                            input_text.input(event.unicode)
                #Rectangle
                pygame.draw.rect(screen, colrect, inprect, borderToggle)
                #Render
                Description.createCentered()
                input_text.createManual()
                for x in row1:
                    x.create()
                for x in row2:
                    x.create()
                for x in row3:
                    x.create()
                for x in row4:
                    x.create()
                for x in row5:
                    x.create()
                You_Win_Overlay.set_alpha(You_Win_Toggle)
                screen.blit(You_Win_Overlay, (0,0))
                You_Win.createCentered()
                windowBar()
                screenUpdate()




MenuStart = threading.Thread(target=Menu(True).Start())
MenuStart.start()

