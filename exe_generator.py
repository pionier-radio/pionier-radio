# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 13:26:17 2019

@author: paulh
"""


import sys

import os


import PyInstaller.__main__





def create_executable(python_file_dir ,exe_file_name):

    PyInstaller.__main__.run([

            '--name=%s' % exe_file_name,

            '--onefile',

            '--distpath=%s' % os.path.join('*', r'C:\Users\paulh\Documents\GitHub\pionier-radio'),

            os.path.join(r'C:\Users\paulh\Documents\GitHub\pionier-radio', python_file_dir)])



create_executable('gui_param_desc_comp.py', 'gui_param_desc_comp')

