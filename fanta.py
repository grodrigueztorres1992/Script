from selenium import webdriver
from selenium.webdriver.common.by import By
import time

controlador = webdriver.Firefox(executable_path="Driver/geckodriver.exe")

controlador.get("https://www.fantasilandia.cl/")
time.sleep(2)

BotonLogin = controlador.find_element(By.CLASS_NAME, "btn-login")

BotonLogin.click()

usuario = controlador.find_element(By.ID, "txtUserTop")
clave = controlador.find_element(By.ID, "txtPasswordTop")

#paso 1
usuario.send_keys("grodriguez@proredes.net")
time.sleep(2)
#paso 2
clave.send_keys("Guille_2")
time.sleep(2)
#paso 3
boton = controlador.find_element(By.ID, "btnEnviarTop")

boton.click()
time.sleep(10)
controlador.quit()
