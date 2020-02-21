from appium import webdriver


def select_control_by_id(id):
    pass


def start_activity(driver):
    driver.start_activity("com.example", "ActivityName");

def screenshot(driver):
    screenshotBase64 = driver.get_screenshot_as_base64()
    return screenshotBase64

