import os
import win32api
import win32file
from pathlib import Path
from dirsync import sync

os.system("cls")
drive_types = { # liste des types de disques
                win32file.DRIVE_UNKNOWN : "Unknown\n   Drive type can't be determined.",
                win32file.DRIVE_REMOVABLE : "Removable\n   Drive has removable media. This includes all floppy drives and many other varieties of storage devices.",
                win32file.DRIVE_FIXED : "Fixed\n   Drive has fixed (nonremovable) media. This includes all hard drives, including hard drives that are removable.",
                win32file.DRIVE_REMOTE : "Remote\n   Network drives. This includes drives shared anywhere on a network.",
                win32file.DRIVE_CDROM : "CDROM\n   Drive is a CD-ROM. No distinction is made between read-only and read/write CD-ROM drives.",
                win32file.DRIVE_RAMDISK : "RAMDisk\n   Drive is a block of random access memory (RAM) on the local computer that behaves like a disk drive.",
                win32file.DRIVE_NO_ROOT_DIR : "The root directory does not exist."
            }

drives = win32api.GetLogicalDriveStrings().split('\x00')[:-1] # obtention liste des disques de l'ordinateur

for device in drives: # on affiche les infos
    type = win32file.GetDriveType(device)
    info = win32api.GetVolumeInformation(device)
    print("Drive: %s" % device)
    print("Volume: %s" % info[0])
    print(drive_types[type])
    print("-"*72)

os.system('pause')

my_file = Path("D:\.Spotlight-V100\Sync\key.txt") # ! la c'est un test, securite a venir
if my_file.is_file():
    print("File exist")
    sync('C:\\Users\\ferta\\Documents\\test', 'D:\\test', 'sync', purge = True) # syncronisation des fichiers
    # * sync('source', 'destination', 'sync', purge = True) -> un seul sens
    print("Sync done")
