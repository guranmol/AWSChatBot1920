import requests

def LocationToCoors(Location,Country):
    url= "https://geocode.xyz/"+Location+Country+"?json=1" #//https://geocode.xyz/api
    #LattLong = []
    #return LattLong
    print (requests.get(url).content)


def WeatherOutput(Loaction,Country):## Location to take format Paris,FR https://darksky.net/poweredby/
    LattLong = LocationToCoors(Loaction,Country) ## Latitude = 0 ,Longitutde = 1
   # url =""
    #return requests.get(url)
    
LocationToCoors("Cologne","DE")