#create dictionaries using an expression

cities_in_F = {'NewYork':50,'Accra':90,'Tibet':78,'Italy':70, }

# cities_in_C ={key:round((value -32)*(5/9)) for (key,value) in cities_in_F.items()}
# print(cities_in_C) 
def check_temp(value):
  if value > 70:
    return 'Hot'
  elif 69 >= value >=40:
    return 'Meh'
  else:
    return 'Cold'



weather = {'NewYork':'cold','Accra':'sunny','Tibet':'sunny','Italy':'cloudy',}

sunny_weather = {key: value for (key,value)in weather.items() if value == 'sunny'}
print(sunny_weather)

desc_cities = {key: check_temp(value) for (key,value)in cities_in_F.items()}
print(desc_cities)