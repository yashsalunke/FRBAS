from setuptools import setup
import sys
from distutils.core import setup
import py2exe
import csv
import json
import shutil
from datetime import datetime
import tkinter
import tkinter.ttk

import cv2
import face_recognition
from firebase import firebase
from numpy import argmin


setup(
    name='FRBAS',
    version='1.0.0.0',
    url='',
    license='',
    author='Yash Salunke',
    author_email='yash3a@gmail.com',
    description='Face-Recognition based Attendance System',
    options={'py2exe': {'bundle_files': 1, 'compressed': True}},
    windows=[{'script': "AttendanceProject.py"}],
    zipfile=None,
)
