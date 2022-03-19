'''

Disk, HddDisk의 실행파일

'''

from HddDisk import *

if __name__ == "__main__":
    disk = Disk(500, 7200)
    hdd_disk = HddDisk(32, 520)

    disk.show_print()
    hdd_disk.show_print()