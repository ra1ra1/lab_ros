#!/usr/bin/env python
import subprocess
import time
from subprocess import call
from subprocess import Popen
from time import  sleep

print('start')
#cmd = "./ready.sh"
#plot = call(cmd, shell=True)

cmd = "./plot.sh"

for i in range(10):
    print("data_"+str(i))
    plot = call(cmd, shell=True)
    time.sleep(5)

print('end')

