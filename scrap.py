from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd


driver_path = "Driver/chromedriver"
driver = webdriver.Chrome(driver_path)

driver.get("https://eltiempo.es")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "didomi-notice-agree-button"))
).click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "term"))
).send_keys("Buenos Aires")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='search']/div/ul/li[7]/a/span[2]"))
).click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='cityTable']/div/article/section/ul/li[2]/a"))
).click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='page']/main/div[4]/div/section[3]/section/div[1]/ul"))
)

text_columns = driver.find_element(By.XPATH, "//*[@id='page']/main/div[4]/div/section[3]/section/div[1]/ul")
text_columns = text_columns.text

today_weather = text_columns.split("Mañana")[0].split("\n")[1:-1]

hours = list()
temp = list()
wind_velocity = list()

for i in range(0, len(today_weather), 4):
    hours.append(today_weather[i])
    temp.append(today_weather[i+1])
    wind_velocity.append(today_weather[i+2])

data_frame = pd.DataFrame({"Hours": hours, "Temperature": temp, "Wind": wind_velocity})
print(data_frame)
data_frame.to_csv("today_weather", index = False)


driver.close()
