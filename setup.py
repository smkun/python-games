from cx_Freeze import setup, Executable

setup(
    name="Main Menu",
    version="1.0",
    description="Game Main Menu",
    executables=[Executable("main_menu.py")],
)