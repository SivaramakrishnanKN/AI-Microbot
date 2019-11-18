from cx_Freeze import *

setup(
      name = "gui",
      options = {'build_exe': {'packages': ['pygame', 'numpy'], "include_files":["libifcoremd.dll", "libmmd.dll"]}},
      executables = [Executable("gui.py")]
      )