# PyQt5 Weather_App 

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit)
from PyQt5.QtCore import Qt
import requests 

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter City Name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("get weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self) 

        self.initUI()
    
    def initUI(self):
        
        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: calibre;
            }
            QPushButton{
                font-size: 10px;
            }
            QLabel#city_label{
                font-size: 25px;
                font-weight: bold;                   
            }
            QLineEdit#city_input{
                font-size: 30px;               
            } 
            QLabel#temperature_label{
                font-size: 20px;
            }
            QLabel#emoji_label{
                font-size: 35px;
                font-family: segoe UI emoji;               
            }
            QLabel#description_label{
                font-size: 20px;               
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)



    def get_weather(self):

        api_key = "5c4f8b34c34e06511a1b06b0f3a8af4c"
        city = self.city_input.text()
        
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try: 
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if response.status_code == 200:
                self.display_weather(data)
            
            
        
        except requests.exceptions.HTTPError:
            print(response.status_code)
            match response.status_code:
                case 400:
                    self.display_error("Bad request.\nInvalid request parameters")
                case 401:
                    self.display_error("Unauthorized.\nInvalid api key")
                case 403:
                    self.display_error("Forbidden.\nAccess to weather service denied.")
                case 404:
                    self.display_error("Not Found.\nCity not found.")
                case 429:
                    self.display_error("Too many requests.\nRequest limit reached.")
                case 500:
                    self.display_error("Internal server error.\nWeather service unavailable")
                case 502:
                    self.display_error("Bad Gateway.\nWeather service currently unavailable.")
                case 503:
                    self.display_error("Server maintenance.\nWeather service currently under maintenance.")
                case 504:
                    self.display_error("Gateway timeout.\nServer took too long to respond.")
        except requests.exceptions.ConnectionError:
            self.display_error("Check your internet connection")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many redirects.")
        except requests.exceptions.RequestException as other_error:
            self.display_error(other_error)

    def display_weather(self, data):
        print(data)
        temperature_K = data["main"]["temp"]
        temperature_C = temperature_K - 273
        temperature_F = (temperature_K * 9/5) - 459.6
        # print(temperature_K)
        # print(temperature_C)
        # print(temperature_F)

        description = data["weather"][0]["description"]

        weather_id = data["weather"][0]["id"]


        self.temperature_label.setText(f"{temperature_C:.0f}° C")
        self.description_label.setText(description)
        self.get_weather_emoji(weather_id)
        


    def display_error(self, message):
        self.description_label.setText(message)
        self.temperature_label.setText("")
        self.emoji_label.setText("")    

    def get_weather_emoji(self, id):

        print(id)

        if 200 <= id <= 232:
            self.emoji_label.setText("⛈️")
        elif 300 <= id <= 321:
            self.emoji_label.setText("🌦️") 
        elif 500 <= id <= 531:
            self.emoji_label.setText("🌧️")
        elif 600 <= id <= 622:
            self.emoji_label.setText("❄️")
        elif 701 <= id <= 741:
            self.emoji_label.setText("🌫️")
        elif id == 762:
            self.emoji_label.setText("🌋")
        elif id == 771:
            self.emoji_label.setText("💨")
        elif id == 781:
            self.emoji_label.setText("🌪️")
        elif id == 800:
            self.emoji_label.setText("☀️")
        elif id == 801:
            self.emoji_label.setText("☁️ 10-15% clouds")
        elif id == 802:
            self.emoji_label.setText("☁️ 20-25% clouds")
        elif id == 803:
            self.emoji_label.setText("☁️ 51-84% clouds")
        elif id == 804:
            self.emoji_label.setText("☁️ 85-100% clouds")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())