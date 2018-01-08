import os
import sys
from subprocess import *


PATH = os.path.dirname(os.path.abspath(__file__))
print(PATH)
SUPER_PATH = os.path.dirname(PATH)
SISTER_PATHS = [os.path.join(SUPER_PATH, i) for i in os.listdir(SUPER_PATH)
                if '.' not in i and i != PATH]

print("\n".join(SISTER_PATHS))



def cmd(command):
    return check_output(command, shell=True)


def status(echo=True, *args):
    result = cmd('git status')
    if echo:
        print(result)
    return result


def commit(*args):
    commit = 'not staged' in status(False)
    if commit:
        print(cmd('git add -A'))
        print(cmd('git commit -m "%s"' % args[0]))
    else:
        print('Not committing: Everything up-to-date\n')
    return commit


def push(*args):
    push = 'up-to-date' in status(False)
    if push:
        cmd('git push')


def install(*args):
    with open('setup.py', 'r') as fp:
        name = fp.read().split("name='")[-1].split("'")[0]
    cmd('pip uninstall %s'%name)
    cmd('pip install -e .')


def seaborn_status():
    dir_iter(status, sys.argv[1:])


def seaborn_commit():
    dir_iter(commit, sys.argv[1:])


def seaborn_push():
    dir_iter(push, sys.argv[1:])


def seaborn_install():
    dir_iter(install, sys.argv[1:])
    dir_iter(install, sys.argv[1:])


def dir_iter(func, *args):
    for path in SISTER_PATHS:
        os.chdir(path)
        print('\n\n' + path)
        try:
            func(*args)
        except BaseException as e:
            pass


if __name__ == '__main__':
    dir_iter(eval(sys.argv[1]), sys.argv[2:])
