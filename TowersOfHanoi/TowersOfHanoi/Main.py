from HanoiGame import HanoiGame
from HanoiDraw import *


def main():
    Game = HanoiGame(3)
    Drawer = HanoiDraw()
    Drawer.DrawStacks(Game)
   

if __name__ == "__main__": main()

