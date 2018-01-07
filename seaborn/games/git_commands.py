import os, sys
from subprocess import *

PATH = os.path.abspath(__file__).replace('\\','/')
DIS_PATH = PATH.split('/')

i = None
for i in range(len(DIS_PATH)):
    if DIS_PATH[-i]=='games':
        depth = i

DEPTH = depth

SUPER_PATH = '/'.join(DIS_PATH[:-DEPTH])
SISTER_PATHS = [SUPER_PATH + '/' + i for i in os.listdir(SUPER_PATH)
               if '.' not in i and i != DIS_PATH[-DEPTH]]

def seaborn_status(echo=True, *args):
    result = check_output('git status', shell=True)
    if echo:
        print(result)
    return result

def seaborn_commit(*args):
    commit = 'not staged' in seaborn_status(False)
    if commit:
        print(check_output('git add -A', shell=True))
        print(check_output('git commit -m "%s"' % args[0], shell=True))
    else:
        print('Not committing: Everything up-to-date\n')
    return commit

def seaborn_push(*args):
    push = 'up-to-date' in seaborn_status(False)
    if push:
        check_output('git push', shell=True)

FUNCS = {'status':seaborn_status,
         'commit':seaborn_commit,
         'push':seaborn_push}

def dir_iter(func_name,*args):
    for path in SISTER_PATHS:
        os.chdir(path)
        print('\n\n'+path)
        func = FUNCS[func_name.replace('seaborn_','')]
        try:
            func(*args)
        except BaseException as e:
            pass

if __name__ == '__main__':
    dir_iter(sys.argv[1], sys.argv[2:])