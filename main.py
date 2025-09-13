import time
from operator import contains

from pygments.styles.dracula import background

import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import (Service)
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

    metodo_pago_field = (By.CSS_SELECTOR, ".pp-button.filled")
    agregar_tarjeta_field = (By.CSS_SELECTOR, ".pp-row.disabled")
    numero_tarjeta_field = (By.ID, "number")
    codigo_field = (By.CSS_SELECTOR, "[placeholder='12']")
    tarjeta = (By.CSS_SELECTOR, ".card-wrapper")
    agregar_button = (By.CSS_SELECTOR, '.pp-buttons > button:nth-child(1)')
    close_button = (By.CSS_SELECTOR, '.payment-picker .close-button')
    imagen_tarjeta_field = (By.CSS_SELECTOR, "img[src='/static/media/card.411e0152.svg']")

    comment_field = (By.ID, "comment")
    mantas_pañuelos_field = (By.XPATH, "//div[text()='Manta y pañuelos']/..//span[@class='slider round']")
    agregar_helado_field = (By.XPATH, "//div[text()='Helado']/..//div[@class='counter-plus']")
    numero_helado_field = (By.XPATH, "//div[text()='Helado']/..//div[@class='counter-value']")
    pedir_taxi_boton = (By.CLASS_NAME, 'smart-button')
    modal_busca_taxi = (By.XPATH, "//div[@class='order shown']//div[@class='order-body']")


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

    def field_metodo_pago(self):
        element = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.metodo_pago_field))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()


    def get_field_Agregar_tarjeta(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.agregar_tarjeta_field))

    def click_agregar_tarjeta(self):
        self.get_field_Agregar_tarjeta().click()

    def add_numero_tarjeta(self):
        tarjeta = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.numero_tarjeta_field))
        tarjeta.click()
        tarjeta.clear()
        tarjeta.send_keys(data.card_number)

    def add_code(self):
        codigo = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.codigo_field))
        codigo.click()
        codigo.clear()
        codigo.send_keys(data.card_code)

    def click_agregar_field(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.tarjeta)).click()
        agregar = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.agregar_button))
        agregar.click()

    def click_cerrar_ventana(self):
        cerrar = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.close_button))
        cerrar.click()

    def get_imagen_tarjeta(self):
        imagen_tarjeta = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.imagen_tarjeta_field))
        self.driver.execute_script("arguments[0].scrollIntoView();", imagen_tarjeta)
        return imagen_tarjeta

    def get_colocar_comentario(self):
        comentario = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.comment_field))
        self.driver.execute_script("arguments[0].scrollIntoView();", comentario)
        return comentario

    def colocar_comentario(self):
        self.get_colocar_comentario().clear()
        self.get_colocar_comentario().send_keys(data.message_for_driver)

    def get_manta_pañuelos(self):
        manta_pañuelos = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.mantas_pañuelos_field))
        self.driver.execute_script("arguments[0].scrollIntoView();", manta_pañuelos)
        return manta_pañuelos

    def click_manta_pañuelos(self):
        self.get_manta_pañuelos().click()

    def get_adicionar_helados(self):
        helados = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.agregar_helado_field))
        self.driver.execute_script("arguments[0].scrollIntoView();", helados)
        return helados

    def click_adicionar_helados(self):
        self.get_adicionar_helados().click()

    def get_numero_helados(self):
        valor_helados = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.numero_helado_field))
        self.driver.execute_script("arguments[0].scrollIntoView();", valor_helados)
        return valor_helados

    def get_button_solicitar_taxi(self):
        solicitar_taxi = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.pedir_taxi_boton))
        self.driver.execute_script("arguments[0].scrollIntoView();", solicitar_taxi)
        return solicitar_taxi

    def is_visible_modal_taxi(self):
        modal_taxi = WebDriverWait(self.driver, 5).until(
        EC.visibility_of_element_located(self.modal_busca_taxi))
        return modal_taxi.is_displayed()

    def click_button_solicitar_taxi(self):
        self.get_button_solicitar_taxi().click()

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        chrome_options = webdriver.ChromeOptions()
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(service=Service(), options=chrome_options)

    def test1_set_route(self):
        self.driver.get(data.urban_routes_url)

        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test2_seleccionar_comfort(self):
        self.test_set_route()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_button_Flash()
        routes_page.click_button_PedirTaxi()
        routes_page.click_button_comfort()

        assert "Comfort" in routes_page.get_comfort_button().text

    def test3_colocar_numero_telefono(self):
        self.test_seleccionar_comfort()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_button_telefono()
        telefono_field = data.phone_number
        routes_page.set_telefono(telefono_field)
        routes_page.click_button_siguiente()
        code = utils.retrieve_phone_code(self.driver)
        routes_page.set_code(code)
        routes_page.click_button_confirmar()
        currect_phone_number = data.phone_number
        assert routes_page.get_telefono_field().text == currect_phone_number

    def test4_agregar_tarjeta_credito(self):
        self.test_colocar_numero_telefono()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.field_metodo_pago()
        routes_page.click_agregar_tarjeta()
        routes_page.add_numero_tarjeta()
        routes_page.add_code()
        routes_page.click_agregar_field()
        routes_page.click_cerrar_ventana()
        expected_src = "/static/media/card.411e0152.svg"
        imagen = routes_page.get_imagen_tarjeta()
        current_src = imagen.get_attribute("src")
        assert expected_src in current_src

    def test5_colocar_comentario(self):
        self.test_agregar_tarjeta_credito()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.colocar_comentario()
        assert routes_page.get_colocar_comentario().get_property('value') == data.message_for_driver

    def test6_seleccionar_manta_pañuelos(self):
        self.test_colocar_comentario()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_manta_pañuelos()
        background_color = routes_page.get_manta_pañuelos().value_of_css_property("background-color")
        assert background_color != "rgba(128,128,128,1)"
        time.sleep(7)

    def test7_adicionar_helados(self):
        self.test_seleccionar_manta_pañuelos()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_adicionar_helados()
        routes_page.click_adicionar_helados()
        assert routes_page.get_numero_helados().text == "2"

    def test8_modal_buscar_taxi(self):
        self.test_adicionar_helados()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_button_solicitar_taxi()
        assert routes_page.is_visible_modal_taxi()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
