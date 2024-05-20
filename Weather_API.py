import requests
import tkinter as tk

API_KEY = "7b1e3a050a1781190d225e7b51507991"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_temperature():
    city = entry.get()
    request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
    response = requests.get(request_url)
    data = response.json()
    if response.status_code == 200:
        data = response.json()
        temperature_in_kelvin = data['main']['temp']
        temperature_in_celsius = round(temperature_in_kelvin - 273.15)
        result_label.config(text=f"A temperatura em Celsius da cidade\n {city} é de {temperature_in_celsius} °C")
    else:
        result_label.config(text="Erro desconhecido")

window = tk.Tk()
window.title("Conversor de Temperatura")
window.geometry("800x400")

label = tk.Label(window, text="Digite o nome da cidade:",font=('Arial',20),
                 fg='#31255a',bg='#8fe0ff')
label.pack(pady=10)

entry = tk.Entry(window,font=('Arial',20))
entry.pack()

get_button = tk.Button(window, text="Obter Temperatura", command=get_temperature,font=('Arial',20),
                 fg='#31255a',bg='#75b4e3')
get_button.pack(pady=10)

result_label = tk.Label(window, text="",font=('Arial',30),
                 fg='#8fe0ff',bg='#54416d')
result_label.pack()

window.mainloop()