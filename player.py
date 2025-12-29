import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
import pygame
from graph import Graph, Node



if __name__ == '__main__':
    pygame.mixer.init()
    g = Graph()
    while True:
        pygame.mixer.music.load(g.chooseNext())
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)