import pytest
from selene.support.shared import browser


@pytest.fixture(scope='session', autouse=True)
def config_browser():
    browser.config.window_width = 1280
    browser.config.window_height = 720