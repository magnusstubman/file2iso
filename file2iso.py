#!/usr/bin/env python3

import sys
import pycdlib
from io import BytesIO
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file', type=argparse.FileType('rb'), help='file to turn into a Joliet level 3 ISO file')
args = parser.parse_args()

fileData = args.file.read()
fileName = args.file.name
level1name = fileName.replace('.','').replace('-','').upper()[0:8]

iso = pycdlib.PyCdlib()
iso.new(joliet=3)
iso.add_fp(BytesIO(fileData), len(fileData), '/' + level1name + '.;1', joliet_path='/' + fileName)
iso.write(fileName + '.iso')
iso.close()
