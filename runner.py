from os.path import abspath, dirname
from os import chdir, getcwd
from sys import argv
from golem import main


def run_test(test_file=None, env="devenv", browser="chrome"):
    test_file = getcwd() if not test_file else test_file
    dir_, test = abspath(test_file).split('projects\\demo_project\\tests\\')
    chdir(dirname(abspath(__file__)))
    args = ["run", "demo_project", test, "-e", env, "-b", browser]
    for i in args:
        argv.append(i)
    main.execute_from_command_line(dir_)
