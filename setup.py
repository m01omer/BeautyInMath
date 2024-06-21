from cx_Freeze import setup, Executable

# Specify the main script file
APP = ['SexyMath.py']

# Options for cx_Freeze
OPTIONS = {
    'build_exe': {
        'packages': ['pygame', 'math', 'numpy', 'time', 'sys'],
        'include_files': ['MyFirstApp.ico'],
        'include_msvcr': True,  # Include Microsoft Visual C++ Redistributable
    }
}

# Define the setup
setup(
    name="SexyMath",
    version="0.1",
    description="Your app description",
    options=OPTIONS,
    executables=[Executable(APP[0], base="Win32GUI", icon="MyFirstApp.jfif")],
)
