# Simplify the process of obtaining meteorological data with Weather
#
# USAGE:
#
# import Weather
#
# Weather.temp() - Temperature
# Weather.temp_fell() - Feels like temperature
# Weather.max_temp() - Max temperature
# Weather.wind_speed() - Wind speed
# Weather.snow() - Snow depth
# Weather.pressure() - Atmosphere pressure
# Weather.precip() - Precipitation
#
# The Weather method takes 2 arguments.
# The first is the need to return just a number (integer or float) without units of measurement (by default False)
# The second is the city (by default moskva)
#
# Weather.total() - General description of the weather
# Takes the city as an argument
#
# Dependencies: weathercom
# >> pip install weathercom
#
#
# © AniJack Industries
#

import weathercom
print('Weather init')


def temp(num=False, city='moscow'):
    weatherDetails = weathercom.getCityWeatherDetails(city)
    weatherDetails = eval(weatherDetails.replace("null", "None"))
    s = weatherDetails['vt1observation']['temperature']
    if num:
        return s
    else:
        return '%s °C' % s


def temp_feel(num=False, city='moscow'):
    weatherDetails = weathercom.getCityWeatherDetails(city)
    weatherDetails = eval(weatherDetails.replace("null", "None"))
    s = weatherDetails['vt1observation']['feelsLike']
    if num:
        return s
    else:
        return '%s °C' % s


def max_temp(num=False, city='moscow'):
    weatherDetails = weathercom.getCityWeatherDetails(city)
    weatherDetails = eval(weatherDetails.replace("null", "None"))
    s = weatherDetails['vt1observation']['temperatureMaxSince7am']
    if num:
        return s
    else:
        return '%s °C' % s


def wind_speed(num=False, city='moscow'):
    weatherDetails = weathercom.getCityWeatherDetails(city)
    weatherDetails = eval(weatherDetails.replace("null", "None"))
    s = weatherDetails['vt1observation']['windSpeed']
    if num:
        return s
    else:
        return '%s км/ч' % s


def snow(num=False, city='moscow'):
    weatherDetails = weathercom.getCityWeatherDetails(city)
    weatherDetails = eval(weatherDetails.replace("null", "None"))
    s = weatherDetails['vt1observation']['snowDepth']
    if num:
        return s
    else:
        return '%s м' % s


def pressure(num=False, city='moscow'):
    weatherDetails = weathercom.getCityWeatherDetails(city)
    weatherDetails = eval(weatherDetails.replace("null", "None"))
    s = weatherDetails['vt1observation']['altimeter']
    if num:
        return s
    else:
        return '%s мбар' % s


def precip(num=False, city='moscow'):
    weatherDetails = weathercom.getCityWeatherDetails(city)
    weatherDetails = eval(weatherDetails.replace("null", "None"))
    s = weatherDetails['vt1observation']['precip24Hour']
    if num:
        return s
    else:
        return '%s мм' % s


def total(city='moscow'):
    return 'Погода на сегодня: \n🌡Температура: %d °C \n🌡Чувствуется как: %d °C \n🌡Максимальная: %d °C \n💨Ветер: %d км/ч \n🌀Давление: %f мбар \n🌧Осадки: %f мм \n🌨Снег: %f м' % (temp(True, city), temp_feel(True, city), max_temp(True, city), wind_speed(True, city), pressure(True, city), precip(True, city), snow(True, city))
