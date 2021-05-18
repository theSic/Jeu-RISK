from cx_Freeze import setup, Executable
base = None

executables = [Executable("main.py", base=base)]

packages = ["pygame", "random", "ctypes", "pickle", 'time', 'socket', 'select', 'init', 'objs', 'server', 'script/menu', 'script/host', 'script/settings', 'script/settingsLocalisation']
options = {
    'build_exe': {    
        'packages':packages,
    },
}

setup(
    name = "Mon Programme",
    options = options,
    version = "1.0",
    description = 'Voici mon programme',
    executables = executables
)