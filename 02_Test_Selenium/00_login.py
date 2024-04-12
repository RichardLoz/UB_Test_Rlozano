from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Ruta del driver
path_chrome = r'C:\Drivers\chromedriver.exe'  # Usar una cadena raw (raw string) para evitar el error de escape

# Crear un objeto Options
options = Options()

# Configurar opciones según sea necesario
# Por ejemplo, para evitar que Chrome muestre notificaciones:
options.add_argument('--disable-notifications')

# Inicializar el driver con las opciones y la ruta del controlador
driver = webdriver.Chrome(options=options)

# Abrir página de login
driver.get('https://sdi.rilozano.com/')

# Esperar unos segundos
driver.implicitly_wait(10)  # Espera 10 segundos

# Encontrar los campos de usuario y contraseña e ingresar los datos
usuario_input = driver.find_element(By.ID, 'dni')
usuario_input.send_keys('1')

contraseña_input = driver.find_element(By.ID, 'contraseña')
contraseña_input.send_keys('123456')

# Encontrar y hacer clic en el botón de inicio de sesión
validarLogin = driver.find_element(By.ID, 'login')
validarLogin.click()

# Ingresar al modulo de cursos
boton_cursos = driver.find_element(By.ID, 'cursos')
boton_cursos.click()

# Ingreso al modulo del curso que voy a testear
curso_ASME_2005 = driver.find_element(By.ID, 'asme_2005')
curso_ASME_2005.click()

# Ingreso al modal del modulo 2
curso_ASME_2005_modal = driver.find_element(By.ID, 'asme_2005_m2_modal')
curso_ASME_2005_modal.click()

# Realizo el test del modulo 2
rpta_modulo2 = driver.find_element(By.ID, 'asme_2005_m2_test')
rpta_modulo2.click()

time.sleep(2)


# Selecciono las respuestas deseadas
respuestas_m2 = [
    'ef3fea31-f18b-4e34-af21-9344fb229ee5',
    '7e8ab13e-593a-42ef-81f1-e5d02652a8c9',
    '60d2583c-7203-4a23-ba4a-28cd54fcbd25',
    '2ec7b84b-eb64-4a65-bf6f-2b574bfdc10a',
    '4b4b9a4a-3be3-4417-a8d7-8b4d1882d657',
    '2b4c52fa-0651-45bf-a3ae-25d6bcc9c4c6',
    '025f7b92-b9cc-435a-832f-5c752a6dd68b',
    '4bf37d4c-bb3a-4da0-84e3-2b6d81c3411c',
    '7a76b59b-d901-4fd4-832f-6f5e4c89da25',
    '0309ac0f-3d21-4717-bf12-333fc88d4e36',
    '90024ae5-f6fa-4035-8abe-6057f7a08a22',
    'cb023abe-f489-41b3-8ef7-6d87bd7ae745'
]

# Itero sobre las respuestas
for respuesta_m2 in respuestas_m2:
    respuesta = driver.find_element(By.ID, respuesta_m2)
    respuesta.click()

# Enviar respuestas
btn_enviar_rpta_m2 = driver.find_element(By.ID, 'enviarRespuestasBtn')
btn_enviar_rpta_m2.click()

time.sleep(2)

# Esperar hasta que aparezca el cuadro de diálogo
cuadro_dialogo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'aceptar_m2')))


#Mantener abierto el navegador
input("Presione enter para continuar...")

# Cerrar el navegador
driver.quit()
