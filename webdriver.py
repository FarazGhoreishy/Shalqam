from selenium import webdriver

class Webdriver:
    def __init__(self) -> None:
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options = options)
        self.driver.minimize_window()