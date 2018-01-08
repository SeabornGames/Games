import os
import sys
from subprocess import *

CWD = os.getcwd().replace('\\','/').split('/')
SUPER_PATH = os.path.join(*CWD[:CWD.index('seaborn')+1])
if CWD[0] == '':
    SUPER_PATH = '/'+SUPER_PATH
SISTER_PATHS = [os.path.join(SUPER_PATH, i) for i in os.listdir(SUPER_PATH)
                if '.' not in i and i != 'games']

def cmd(command):
    """
    :param command: str of the command to execute e.g. ls -ls
    :return: str of the STDOUT of the command
    """
    process = Popen(command, stdout=PIPE, stderr=STDOUT, shell=True,
                    close_fds=True)
    process.wait()
    if process.returncode == 0:
        ret = process.communicate()[0].strip()
        return ret.decode() if sys.version_info[0] == 3 else ret
    else:  # error
        raise Exception("\n\nFailed to execute command: %s \n\n%s" % (
            command, process.communicate()[0]))

def tab(result, space= '    '):
    print(space+('\n'+space).join(result.split('\n')))


def status(echo=True, *args):
    result = cmd('git status')
    if echo:
        tab(result)
    return result


def commit(*args):
    commit = 'not staged' in status(False)
    if commit:
        tab(cmd('git add -A'))
        tab(cmd('git commit -m "%s"' % args[0]))
    else:
        tab('Not committing: Everything up-to-date\n')
    return commit


def push(*args):
    push = 'up-to-date' in status(False)
    if push:
        cmd('git push')


def install(*args):
    cmd('pip install -e .')


def uninstall(*args):
    with open('setup.py', 'r') as fp:
        name = fp.read().split("name='")[-1].split("'")[0]
    cmd('pip uninstall -y %s'%name)


def seaborn_status():
    dir_iter(status, *sys.argv[1:])


def seaborn_commit():
    dir_iter(commit, *sys.argv[1:])


def seaborn_push():
    dir_iter(push, *sys.argv[1:])


def seaborn_install():
    dir_iter(install, *sys.argv[1:])
    dir_iter(install, *sys.argv[1:])


def seaborn_uninstall():
    dir_iter(uninstall, *sys.argv[1:])


def dir_iter(func, *args):
    print("\n" * 20)
    for path in SISTER_PATHS:
        os.chdir(path)
        print('\n\n' + path)
        try:
            func(*args)
        except BaseException as e:
            pass


if __name__ == '__main__':
    dir_iter(status)
    # dir_iter(eval(sys.argv[1]), sys.argv[2:])
