#!/usr/bin/env python3
# Written by Brandon Doggett
# Playing around with copying files and folders

## Import statements
import shutil
import os

## Force Python to start this program in the home user directory
os.chdir('/home/student/mycode/')

## Copy function for single file
shutil.copy('5g_research/sdn_network.txt', '5g_research/sdn_network.txt.copy')

## Copy function for a dir tree
shutil.copytree('5g_research/', '5g_research_backup/')