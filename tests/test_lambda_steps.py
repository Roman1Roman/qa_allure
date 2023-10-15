import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@allure.tag('web')
@allure.feature("task in repo by lambda steps")
@allure.story('Authorised user can make an issue in the repo')
@allure.label("Owner", "Bazaleev")
@allure.description('testing with lambda steps')
def test_dynamic_github():
    with allure.step('Opening main page'):
        browser.open('https://github.com')

    with allure.step('Finding the repo'):
        s(".header-search-button").click()
        s("#query-builder-test").send_keys("eroshenkoam/allure-example")
        s("#query-builder-test").submit()

    with allure.step('click on lin of the repo'):
        s(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Opening tap issues'):
        s('#issues-tab').click()

    with allure.step('checking issue #76'):
        s(by.partial_text('#76')).should(be.visible)



