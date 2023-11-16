import os

libraries_to_install = ['pywifi', 'colorama', 'termcolor', 'pyfiglet']

for library in libraries_to_install:
    os.system(f"pip install {library}")
