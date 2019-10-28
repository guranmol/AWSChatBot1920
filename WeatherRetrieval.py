def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        def LocationToCoors(Location,Country):
            url= "https://geocode.xyz/"+Location+","+Country+"?json=1" #//https://geocode.xyz/api
            JSONReturn = requests.get(url).json()
            LattLong = []
            LattLong.append(JSONReturn['alt']['loc']['longt'])
            LattLong.append(JSONReturn['alt']['loc']['latt'])
            return LattLong

        def WeatherDataRetreival(Loaction,Country):## Location to take format Paris,FR https://darksky.net/poweredby/
            LattLong = LocationToCoors(Loaction,Country) ## Latitude = 0 ,Longitutde = 1
            url ="https://api.darksky.net/forecast/60a4da2fceb77dce7d44656141cc6bbf/"+LattLong[1]+","+LattLong[0]
            print(url)
            return requests.get(url).json()
       
        def CurrentTemperature(Location,Country):
            JSONReturn = WeatherDataRetreival(Location,Country)
            #print(JSONReturn)
            return JSONReturn["currently"]["temperature"]
        
        def CurrentDescription(Location,Country):
            JSONReturn = WeatherDataRetreival(Location,Country)
            #print(JSONReturn)
            return JSONReturn["currently"]["summary"]
        
        def TommorowTemperature(Location,Country):
            JSONReturn = WeatherDataRetreival(Location,Country)
            #print(JSONReturn)
            HighTemp = JSONReturn["daily"]["data"][2]["temperatureHigh"]
            LowTemp = JSONReturn["daily"]["data"][2]["temperatureLow"]
            AvgTemp = HighTemp + LowTemp
            AvgTemp = AvgTemp/2
            return AvgTemp

        
           
        result = (TommorowTemperature("Bern","CH"))
        speak_output = str(result)

