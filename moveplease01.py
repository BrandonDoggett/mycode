#!/usr/bin/env python3
# Written by Brandon Doggett
# A script to move stuff

## Import statements
import shutil
import os

## Set directory no matter where we are executing from
os.chdir('/home/student/mycode/')

## Move file or folder
shutil.move('raynor.obj', 'ceph_storage/')

## Prompt user for new file name, then move and rename file based on input
xname = input('What is the new name for kerrigan.obj?')
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)
