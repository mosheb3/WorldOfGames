## Moshe Barazani
## Date: 03-05-2020
## filename: Utils.py
import sys
import subprocess
import pkg_resources

def install_packages(package_name):
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = package_name - installed

    if missing:
        try:
            python = sys.executable
            subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
        except subprocess.CalledProcessError:
            pass  # handle errors in the called executable
        except OSError:
            pass


def get_operation_system():
    opr = sys.platform
    return opr

def get_host_ip():
    import socket
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    #print("Your Computer Name is:" + hostname)
    #print("Your Computer IP Address is:" + IPAddr)
    return IPAddr


## -----------------------------------------------------##

required_packages = {'setuptools', 'flask', 'python-exchangeratesapi', 'selenium'}
install_packages(required_packages)

SCORES_FILE_NAME = "data/data.json"
BAD_RETURN_CODE = 500
WINNING_CODE = 1000
LOSSING_CODE = 2000

black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
bright_black = "\033[0;90m"
bright_red = "\033[0;91m"
bright_green = "\033[0;92m"
bright_yellow = "\033[0;93m"
bright_blue = "\033[0;94m"
bright_magenta = "\033[0;95m"
bright_cyan = "\033[0;96m"
bright_white = "\033[0;97m"