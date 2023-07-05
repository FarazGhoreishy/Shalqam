from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver import Webdriver
from item import Item

class WebFunctions:
    @staticmethod
    def search_web(search_entry):
        
        wd = Webdriver()
        page_url = "https://emalls.ir/"
        wd.driver.get(page_url)


        search_box = wd.driver.find_element(By.ID, "SearchInBottom_txtSearch")
        search_box.send_keys(search_entry)
        search_box.send_keys(Keys.ENTER)

        wd.driver.implicitly_wait(5)

        product_elements = list(wd.driver.find_elements(By.CLASS_NAME, "item-title"))
        price_elements = list(wd.driver.find_elements(By.CLASS_NAME, "price-box"))

        for product_element, price_element in list(zip(product_elements, price_elements))[:4]:

            product_price = price_element.find_element(By.CLASS_NAME, "prd-price").text[:-6]
            print(product_price)

            product_element = product_element.find_element(By.CLASS_NAME, "prd-name")
             
            product_link = product_element.get_attribute('href')

            product_info = WebFunctions.getProductInfo(product_link)
            Item.register(*product_info, product_price)

    @staticmethod
    def getProductInfo(product_link):
        # print("This Link :", product_link)
        wd = Webdriver()
        wd.driver.get(product_link)

        category_breadcrumb = wd.driver.find_element(By.ID, "divbreadcrumb")
        category_breadcrumb = category_breadcrumb.text.split('\n')

        name = category_breadcrumb[-1]
        category = category_breadcrumb[2]
        
        shop_links = []
        for i in range(5):
            try:
                id = f"ContentPlaceHolder1_rptShops_hlkDescription_{i}"
                shop_link_element = wd.driver.find_element(By.ID, id)
                shop_link_url = shop_link_element.get_attribute('href')
                shop_links.append(shop_link_url)
            except:
                break

        return [name, category, shop_links, product_link]

if __name__ == "__main__":
    se = "هدست گیمینگ"
    WebFunctions.search_web(se)