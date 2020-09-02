class PageItemElement:

    def __init__(self, my_driver):
        self.driver = my_driver
        self.quantity_box = 'quantity_wanted'
        self.plus = 'icon-plus'

    def enter_quantity(self, quantity):
        self.driver.find_element_by_id(self.quantity_box).clear().send_keys(quantity)

    def add_element(self, quantity_plus):
        for i in range(quantity_plus):
            self.driver.find_element_by_class_name(self.plus).click()

    def get_number_of_element(self):
        return self.driver.find_element_by_id(self.quantity_box).get_attribute('value')


