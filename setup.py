import sys
from cx_Freeze import setup, Executable

import os
PYTHON_INSTALL_DIR = os.path.dirname(sys.executable)
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

packages = ["smtplib", "ssl"]
include_files = [(os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'), os.path.join('lib', 'tk86t.dll')),
                 (os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'), os.path.join('lib', 'tcl86t.dll')),
                 os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'libcrypto-1_1-x64.dll'),
                 os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'libssl-1_1-x64.dll'),
                ".env", "message.txt"]

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable('boxes.py', base=base, targetName = "SuperbowlBoxesGenerator.exe", icon="icon.ico", copyright="MIT", trademarks="CompuGenius Programs")
]

setup(name='Superbowl Boxes Generator',
      version = '2.0',
      description = 'An automated generator for the betting game Superbowl Boxes.',
      author = "CompuGenius Programs",
      author_email = "compugeniusprograms@gmail.com",
      options={'build_exe': {'include_files': include_files, 'packages': packages}},
      executables=executables)
