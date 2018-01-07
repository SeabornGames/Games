import os, unittest

DEPTH = 4
DIS_PATH = os.path.abspath(__file__).split('\\')
SUPER_PATH = '\\'.join(DIS_PATH[:-DEPTH])
SISTER_PATHS = [SUPER_PATH + '\\' + i for i in os.listdir(SUPER_PATH)
               if '.' not in i and i != DIS_PATH[-DEPTH]]

def main():
    print("Searching directory: %s"%SUPER_PATH)
    print("Found paths:")
    for path in SISTER_PATHS:
        print(path)
    testmodules = []
    for dir_ in SISTER_PATHS:
        if os.path.isdir(dir_+'\\test'):
            base = '.'.join(dir_.split('\\')[-2:])
            testmodules += [base + '.test.' + i.replace('.py','')
                            for i in os.listdir(dir_+'\\test') if 'test' in i]

    for tests in testmodules:
        print("Preparing to launch test: %s"%tests)
    suite = unittest.TestSuite()

    for test in testmodules:
        print(test)
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(test))

    print("Falsifying __init__.py")
    file = open(SUPER_PATH+'\\__init__.py')
    unittest.TextTestRunner().run(suite)
    print("Retracting __init__.py")
    file.close()
    os.remove(SUPER_PATH+'\\__init__.py')

if __name__ == '__main__':
    main()