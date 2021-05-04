"""
    This file is the constants of the peer to peer network
"""

import socket 
import threading 
import sys
import time
import os
from random import randint
from music import *
import fileIO


HOSTNAME = socket.gethostname()
BYTE_SIZE = 1024
HOST = socket.gethostbyname(HOSTNAME)
PORT = 5000
PEER_BYTE_DIFFERENTIATOR = b'\x11' 
RAND_TIME_START = 1
RAND_TIME_END = 2
REQUEST_STRING = "req"


# directories
cwd = os.getcwd()
uploadedfilesdir = os.path.join(cwd,'sharedfolder')
filelistdir = os.path.join(uploadedfilesdir,'.filelist')

# uploadedfiles = os.listdir(os.path.join(cwd, 'sharedfolder'))
