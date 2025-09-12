import time
from operator import contains

import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.edge.service import (Service)
import utils


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    flash_button = (By.CSS_SELECTOR, '.modes-container > div:nth-child(2)')
    pedir_taxi_button = (By.CSS_SELECTOR, ".button.round")
    comfort_button = (By.CSS_SELECTOR, '.tariff-cards > div:nth-child(5)')

    numero_telefono_field = (By.CSS_SELECTOR, '.np-text')
    ingresa_telefono_field = (By.ID, "phone")
    siguiente_button = (By.CSS_SELECTOR, ".buttons > button")
    code_field = (By.ID, "code")
    confirmar_button = (By.XPATH, "//button[text()='Confirmar']")



    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.from_field)
        ).send_keys(from_address)

    def set_to(self, to_address):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.to_field)
        ).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_Flash_button(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.flash_button)
        )

    def click_button_Flash(self):
       self.get_Flash_button().click()

    def get_pedir_taxi_button(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.pedir_taxi_button)
        )

    def click_button_PedirTaxi(self):
       self.get_pedir_taxi_button().click()

    def get_comfort_button(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((self.comfort_button))
        )
    def click_button_comfort(self):
        self.get_comfort_button().click()

    def get_telefono_field(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.numero_telefono_field)
        )

    def click_button_telefono(self):
        self.get_telefono_field().click()

    def get_ingresa_telefono_field(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.ingresa_telefono_field)
        )

    def set_telefono(self, telefono):
        self.get_ingresa_telefono_field().send_keys(telefono)

    def get_button_siguiente(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.siguiente_button)
        )

    def click_button_siguiente(self):
        self.get_button_siguiente().click()

    def set_code(self, code):
        self.driver.find_element(*self.code_field).send_keys(code)


    def get_button_confirmar(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.confirmar_button))

    def click_button_confirmar(self):
        self.get_button_confirmar().click()

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        edge_options = webdriver.EdgeOptions()
        edge_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Edge(service=Service(), options=edge_options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)

        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_seleccionar_comfort(self):
        self.test_set_route()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_button_Flash()
        routes_page.click_button_PedirTaxi()
        routes_page.click_button_comfort()

        assert "Comfort" in routes_page.get_comfort_button().text

    def test_colocar_numero_telefono(self):
        self.test_seleccionar_comfort()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_button_telefono()
        telefono_field = data.phone_number
        routes_page.set_telefono(telefono_field)
        routes_page.click_button_siguiente()
        code = utils.retrieve_phone_code(self.driver)
        routes_page.set_code(code)
        routes_page.click_button_confirmar()







    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
