## Moshe Barazani
## Date: 03-05-2020
## filename: Utils.py
import sys
import subprocess
import pkg_resources

# def install_package(package_name, import_package_name):
#    # subprocess.call(['pip', 'install', package_name])
#    try:
#        import import_package_name
#    except ImportError:
#        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
#    finally:
#        import import_package_name

def install_package(required_packages):
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

#-r / path / to / requirements.txt

# SCORES_FILE_NAME = "templates/score.html"
SCORES_FILE_NAME = "data/data.json"
BAD_RETURN_CODE  = 500
WINNING_CODE     = 1000
LOSSING_CODE     = 2000
