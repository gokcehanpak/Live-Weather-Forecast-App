from datetime import datetime
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
import requests


api_key = '#YOUR API KEY HERE!!!'
turkey_cities = [
    'Adana', 'Adıyaman', 'Afyonkarahisar', 'Ağrı', 'Amasya', 'Ankara', 'Antalya', 'Artvin',
    'Aydın', 'Balıkesir', 'Bilecik', 'Bingöl', 'Bitlis', 'Bolu', 'Burdur', 'Bursa', 'Çanakkale',
    'Çankırı', 'Çorum', 'Denizli', 'Diyarbakır', 'Edirne', 'Elazığ', 'Erzincan', 'Erzurum', 'Eskişehir',
    'Gaziantep', 'Giresun', 'Gümüşhane', 'Hakkari', 'Hatay', 'Isparta', 'Mersin', 'İstanbul', 'İzmir',
    'Kars', 'Kastamonu', 'Kayseri', 'Kırklareli', 'Kırşehir', 'Kocaeli', 'Konya', 'Kütahya', 'Malatya',
    'Manisa', 'Kahramanmaraş', 'Mardin', 'Muğla', 'Muş', 'Nevşehir', 'Niğde', 'Ordu', 'Rize', 'Sakarya',
    'Samsun', 'Siirt', 'Sinop', 'Sivas', 'Tekirdağ', 'Tokat', 'Trabzon', 'Tunceli', 'Şanlıurfa', 'Uşak',
    'Van', 'Yozgat', 'Zonguldak', 'Aksaray', 'Bayburt', 'Karaman', 'Kırıkkale', 'Batman', 'Şırnak', 'Bartın',
    'Ardahan', 'Iğdır', 'Yalova', 'Karabük', 'Kilis', 'Osmaniye', 'Düzce'
]

# Create the main window
root = tk.Tk()
root.title("Weather App")
root.geometry("400x400")  # Set a larger size for the window

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y positions for the window to be centered
x = (screen_width/2) - (400/2)  # 400 is the width of the window
y = (screen_height/2) - (300/2)  # 300 is the height of the window

# Set the window to be centered
root.geometry(f"400x300+{int(x)}+{int(y)}")


# Create a label to display "Hello!" when the app starts
hello_label = ttk.Label(root, text="Hello Forecaster!", font=("Helvetica", 30))
hello_label.pack(pady=20)

# Function to update weather after 2 seconds
def delayed_update():
    hello_label.destroy()  # Remove the "Hello!" label
    update_weather()  # Update weather information

# After 2 seconds, remove the "Hello!" label and update weather
root.after(3000, delayed_update)

# Apply a theme with reds, blacks, and turquoises
style = ThemedStyle(root)
style.set_theme("arc")  # You can choose a different theme with the desired colors

# Customize the style settings for the widgets
style.configure('TLabel', font=('Helvetica', 16))  # Set label font style
style.configure('TButton', font=('Helvetica', 14))  # Set button font style
style.map('TButton', background=[('active', 'black'), ('disabled', 'grey')])  # Set button background colors

# Add Combobox to select city
selected_city = tk.StringVar()
city_combobox = ttk.Combobox(root, textvariable=selected_city, values=turkey_cities)
city_combobox.pack(pady=10)  # Add padding to position the combobox

# Add labels to display weather information with custom fonts and icons
label_city = ttk.Label(root, text="City: ", font=("Helvetica", 16))
label_city.pack()

label_temp = ttk.Label(root, text="Temperature: ", font=("Helvetica", 16))
label_temp.pack()

label_desc = ttk.Label(root, text="Description: ", font=("Helvetica", 16))
label_desc.pack()

def update_weather():
    city = selected_city.get()
    current_weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}'
    

    response = requests.get(current_weather_url)
    data = response.json()

    # Parse current weather data
    if 'name' in data:
        city = data['name']
    else:
        city = 'N/A'

    if 'main' in data and 'temp' in data['main']:
        temp_kelvin = data['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        temp_celsius_formatted = f"{temp_celsius:.2f}"
    else:
        temp_celsius_formatted = 'N/A'

    if 'weather' in data and len(data['weather']) > 0 and 'description' in data['weather'][0]:
        description = data['weather'][0]['description']
    else:
        description = 'N/A'

    if 'main' in data and 'humidity' in data['main']:
        humidity = data['main']['humidity']
    else:
        humidity = 'N/A'

    if 'wind' in data and 'speed' in data['wind']:
        wind_speed = data['wind']['speed']
    else:
        wind_speed = 'N/A'

    if 'sys' in data and 'sunrise' in data['sys']:
        sunrise_timestamp = data['sys']['sunrise']
        sunrise_time = datetime.utcfromtimestamp(sunrise_timestamp).strftime('%H:%M:%S')
    else:
        sunrise_time = 'N/A'

    if 'sys' in data and 'sunset' in data['sys']:
        sunset_timestamp = data['sys']['sunset']
        sunset_time = datetime.utcfromtimestamp(sunset_timestamp).strftime('%H:%M:%S')
    else:
        sunset_time = 'N/A'

    label_city.config(text=f"City: {city}")
    label_temp.config(text=f"Temperature: {temp_celsius_formatted}°C")
    label_desc.config(text=f"Description: {description}")
    label_humidity.config(text=f"Humidity: {humidity}%")
    label_wind.config(text=f"Wind Speed: {wind_speed} m/s")
    label_sunrise.config(text=f"Sunrise: {sunrise_time}")
    label_sunset.config(text=f"Sunset: {sunset_time}")

# Add labels for sunrise, sunset, humidity, and wind speed
label_humidity = ttk.Label(root, text="Humidity: ", font=("Helvetica", 16))
label_humidity.pack()

label_wind = ttk.Label(root, text="Wind Speed: ", font=("Helvetica", 16))
label_wind.pack()

label_sunrise = ttk.Label(root, text="Sunrise: ", font=("Helvetica", 16))
label_sunrise.pack()

label_sunset = ttk.Label(root, text="Sunset: ", font=("Helvetica", 16))
label_sunset.pack()

# Add a button to update weather information
update_button = ttk.Button(root, text="Update Weather", command=update_weather)
update_button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()