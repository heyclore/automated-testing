from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from utilities.Config import Config
import pytest
import logging


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        #extra.append(pytest_html.extras.url("http://www.example.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            driver.get_screenshot_as_file('Logs/assets/'+file_name)
            if file_name:
                html = '<div><img src="assets/{}" alt="screenshot" style="width:304px;heighti onclick="window.open(this.src)" align="right"/></div>'.format(file_name)
                extra.append(pytest_html.extras.html(html))
            # only add additional html on failure
            #extra.append(pytest_html.extras.html("<div>Additional HTML</div>"))
            #extra.append(pytest_html.extras.png('foo/some_image.png'))
        report.extra = extra



@pytest.fixture(scope='class')
def init_driver(request):
    global driver
    if Config.browser == 'chrome':
        driver = webdriver.Chrome('chromium.chromedriver')
    elif Config.browser == 'firefox':
        driver = webdriver.Firefox(service_log_path='build/geckodriver.log')
    else:
        message = 'browser DATA IN config.yaml IS NOT SET !!!'
        logging.getLogger(__name__).error(message)
        pytest.exit(message)

    if Config.url == '':
        driver.close()
        message = 'env DATA IN config.yaml IS NOT SET !!!'
        logging.getLogger(__name__).error(message)
        pytest.exit(message)
    else:
        driver.get(Config.url)

    request.cls.driver = driver
    yield
    driver.quit()
