# Weather
 Simplify the process of obtaining meteorological data with Weather
 
 USAGE:

 ```import Weather```

- ```Weather.temp()``` - Temperature
- ```Weather.temp_fell()``` - Feels like temperature 
- ```Weather.max_temp()``` - Max temperature 
- ```Weather.wind_speed()``` - Wind speed 
- ```Weather.snow()``` - Snow depth
- ```Weather.pressure()``` - Atmosphere pressure
- ```Weather.precip()``` - Precipitation

 The Weather method takes 2 arguments.  
 The first is the need to return just a number (integer or float) without units of measurement (by default False)  
 The second is the city (by default moskva)  

 Weather.total() - General description of the weather  
 Takes the city as an argument  

 Dependencies: weathercom  
 `>> pip install weathercom`
