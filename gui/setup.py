import cx_Freeze
import sys
import json

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("main.py", base=base)]

cx_Freeze.setup(
    name = "Clearing-Finder",
    options = {"build_exe": {"packages":["tkinter","json"], "include_files":["uni_infos.txt"]}},
    version = "0.01",
    description = "Good luck with clearing",
    executables = executables
    )
