import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

@allure.tag('web')
@allure.feature("task in repo by decorator")
@allure.story('Authorised user can make an issue in the repo')
@allure.label("Owner", "Bazaleev")
@allure.description('testing with decorator steps')
def test_decorator_steps():
    open_main_page()
    search_for_repo('eroshenkoam/allure-example')
    go_to_repo('eroshenkoam/allure-example')
    open_issue_tap()
    check_issue_w_number(76)


@allure.step('Opening main page')
def open_main_page():
    browser.open('https://github.com')


@allure.step('Finding the repo {repo}')
def search_for_repo(repo):
    s(".header-search-button").click()
    s("#query-builder-test").send_keys(repo)
    s("#query-builder-test").submit()


@allure.step('click on lin of the repo {repo}')
def go_to_repo(repo):
    s(by.link_text(repo)).click()


@allure.step('Opening tap issues')
def open_issue_tap():
    s('#issues-tab').click()


@allure.step('checking issue #{number}')
def check_issue_w_number(number):
    s(by.partial_text(f'#{number}')).should(be.visible)