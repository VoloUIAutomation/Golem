from golem.actions import *
from projects.demo_project.pages import account, sign_in
from runner import run_test


description = '''
 
'''

tags = ['demo']


def setup(data):
    store('url', data.env.url)
    store('login_name', data.env.users[data.user_name]['user_login'])
    store('user_pass', data.env.users[data.user_name]['user_pswd'])
    store('account_name', data.env.users[data.user_name]['user_name'])


def test(data):
    step('_____________Navigation_______________')
    navigate(data.url)
    step('_____________Sign in_______________')
    sign_in.login_as_a_user_by_name_and_pass(data.login_name, data.user_pass)
    step('_____________Assert account name_______________')
    account.assert_account_name('isdhkfhlblbf')


def teardown(data):
    step('_____________Sing out and check_______________')
    account.user_logout_and_check()


if __name__ == '__main__':
    run_test(__file__)
