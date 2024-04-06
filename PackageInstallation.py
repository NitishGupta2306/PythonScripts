import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install("pandas")
install("lxml")
install("opencv-python")
install("ghostscript")
install("camelot-py")
