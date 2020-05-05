## Moshe Barazani
## Date: 03-05-2020
## filename: Utils.py
import sys
import subprocess
import pkg_resources

required_packages = {'flask', 'python-exchangeratesapi'}
install_packages(required_packages)


def install_packages(required_packages):
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = required_packages - installed

    if missing:
        try:
            python = sys.executable
            subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
        except subprocess.CalledProcessError:
            pass  # handle errors in the called executable
        except OSError:
            pass

SCORES_FILE_NAME = "data/data.json"
BAD_RETURN_CODE  = 500
WINNING_CODE     = 1000
LOSSING_CODE     = 2000
