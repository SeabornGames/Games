import os, sys
from subprocess import *

PATH = os.getcwd().replace('\\', '/')
if '/seaborn' in PATH:
    PATH = '%s/seaborn' % PATH.split('/seaborn')[0]

SISTER_PATHS = [PATH + '/' + i for i in os.listdir(PATH)
                if '.' not in i and not 'game' in i.lower()]


def func_iter(func):
    func_name = func.__name__

    def ret(*args):
        for path in SISTER_PATHS:
            os.chdir(path)
            print('\n\n' + func_name.replace('_', ' ') + '-\t' + path)
            try:
                func(*args)
            except BaseException as e:
                pass

    return ret

def status(echo=True):
    check_output('git fetch origin')
    result = check_output('git status', shell=True)
    if echo:
        print(result.decode('utf-8'))
    return result

@func_iter
def seaborn_install(*args):
    result = check_output('pip install . -U')
    print(result.decode('utf-8'))

@func_iter
def seaborn_status(*args):
    return status()

@func_iter
def seaborn_commit(*args):
    commit = 'not staged' in status(False).decode('utf-8')
    if commit:
        print(check_output('git add -A', shell=True).decode('utf-8'))
        print(check_output('git commit -m "%s"' % args[0], shell=True
                           ).decode('utf-8'))
    else:
        print('Not committing: Everything up-to-date\n')
    return commit


@func_iter
def seaborn_push(*args):
    push = 'up-to-date' in status(False).decode('utf-8')
    if push:
        print(check_output('git push', shell=True).decode('utf-8'))
    else:
        print('Not pushing: Not up-to-date')


@func_iter
def seaborn_pull(*args):
    mstr = '*master' in check_output('git branch').decode('utf-8')
    pull = 'up-to-date' in status(False).decode('utf-8')
    if mstr and pull:
        print(check_output('git pull origin master').decode('utf-8'))
    else:
        print(check_output('git fetch origin master').decode('utf-8'))
