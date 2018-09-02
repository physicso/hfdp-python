"""
Weather station

Author: m1ge7 and Eric Wang
Date: 2018/09/02
"""

from abc import ABCMeta, abstractmethod


###############################################################################
# Observables
###############################################################################

class Subject:
    __metaclass__ = ABCMeta

    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


class WeatherData(Subject):
    
    def __init__(self):
        self._observers = []
        self._temperature = None
        self._humidity = None
        self._pressure = None

    def register_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        try:
            self._observers.remove(observer)
        except:
            pass

    def notify_observers(self):
        for obs in self._observers:
            obs.update(self._temperature, self._humidity, self._pressure)

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temperature, humidity, pressure):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        
        self.measurements_changed()


###############################################################################
# Observers
###############################################################################

class Observer:
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, temp, humidity, pressure):
        pass


class DisplayElement:
    __metaclass__ = ABCMeta

    @abstractmethod
    def display(self):
        pass


class CurrentConditionsDisplay(Observer, DisplayElement):

    def __init__(self, input_weather_data):
        self._temperature = None
        self._humidity = None
        self._weather_data = input_weather_data

        weather_data.register_observer(self)

    def update(self, temperature, humidity, pressure):
        self._temperature = temperature
        self._humidity = humidity
        self.display()

    def display(self):
        print("Current conditions: " + str(self._temperature) +
                "F degrees and " + str(self._humidity) + " % humidity");


class StatisticsDisplay(Observer, DisplayElement):

    def __init__(self, input_weather_data):
        self._max_temp = 0.0
        self._min_temp = 200
        self._temp_sum = 0.0
        self._num_readings = 0
        self._weather_data = input_weather_data

        weather_data.register_observer(self)

    def update(self, temp, humidity, pressure):
        self._temp_sum += temp
        self._num_readings += 1

        if temp > self._max_temp:
            self._max_temp = temp

        if temp < self._min_temp:
            self._min_temp = temp

        self.display()

    def display(self):
        avg_temp = self._temp_sum / self._num_readings
        print("Statistics Avg/Max/Min temperature = {0}/{1}/{2}".format(
            avg_temp, self._max_temp, self._min_temp))


class ForecastDisplay(Observer, DisplayElement):

    def __init__(self, input_weather_data):
        self._current_pressure = 29.92
        self._last_pressure = 0.0
        self._weather_data = input_weather_data

        weather_data.register_observer(self)

    def update(self, temp, humidity, pressure):
        self._last_pressure = self._current_pressure
        self._current_pressure = pressure
        self.display()

    def display(self):
        print("Forecast: "),
        if self._current_pressure > self._last_pressure:
            print("Improving weather on the way!")
        elif self._current_pressure == self._last_pressure:
            print("More of the same")
        elif self._current_pressure < self._last_pressure:
            print("Watch out for cooler, rainy weather")


if __name__ == '__main__':
    # WeatherStation code
    weather_data = WeatherData()

    current_display = CurrentConditionsDisplay(weather_data)
    statistics_display = StatisticsDisplay(weather_data)
    forecast_display = ForecastDisplay(weather_data)

    weather_data.set_measurements(80, 65, 30.4)
    weather_data.set_measurements(82, 70, 29.2)
    weather_data.set_measurements(78, 90, 29.2)

