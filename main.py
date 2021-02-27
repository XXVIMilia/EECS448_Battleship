import pygame
from subclass import game_logic

# Initialize the pygame 
pygame.init()

#Create gameLogic
myGame = game_logic.gameLogic()

# Setup.txt parser
setupfile = open('setup.txt')
SetupPacket = setupfile.readlines()
setupfile.close()

myGame.run(SetupPacket)
