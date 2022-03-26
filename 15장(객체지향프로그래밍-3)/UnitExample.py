'''

Unit, Tank, Dropship, Marine 클래스의 실행파일

'''

from Tank import *
from DropShip import *
from Marine import *

if __name__ == "__main__":
    print("=" * 40)
    tank = Tank()
    tank.move(100, 300)
    tank.size_mode()
    tank.stop("탱크", 300, 400)

    print("=" * 40)
    marine = Marine()
    marine.move(200, 550)
    marine.stimpack()
    marine.stop("마린", 300, 400)

    print("=" * 40)
    dropship = DropShip()
    dropship.move(1000, 2000)
    dropship.load()
    dropship.unload()
    dropship.stop("드랍쉽", 0, 0)
    print("=" * 40)