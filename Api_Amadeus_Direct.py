
import requests, json
from amadeus import ResponseError
from flatten_json import flatten
import Api_utility as util


class Api_AmadeusDirect:

    def getToken(self):
        parametres ={'grant_type': 'client_credentials', 'client_id': 'jzhnkve7G1nVerkYjcdZuYIGl0qvXKhs', 'client_secret': '1Um4mEwSREU2ZIoH'}    
        headers ={'Content-Type': 'application/x-www-form-urlencoded'}
        response =requests.post("https://test.api.amadeus.com/v1/security/oauth2/token", data=parametres,headers =headers)
        responseJson = json.loads(response.text)
        token = 'Bearer {0}'.format(responseJson['access_token'])
        return token


    def flight_offers(self,travelClassParam):
        listDicJsonFlight = None
        try:
            '''
            Find the cheapest flights from SYD to BKK
            '''
            #Get the flights on a given journey
            #travelClass=PREMIUM_ECONOMY
            parametres ={'originLocationCode': 'DSS', 'destinationLocationCode': 'CDG', 'departureDate': '2021-06-28', 'returnDate': '2021-07-28',  'adults': '1', 'nonStop':'false', 'max':'250' ,'travelClass': travelClassParam}
            headers ={'Authorization': self.getToken()}
            response =requests.get("https://test.api.amadeus.com/v2/shopping/flight-offers", params=parametres,headers =headers)
    
            responseJson = json.loads(response.text)
        
            listDicJsonFlight = responseJson
            
            
        except ResponseError as error:
            raise error 
            
    
        return listDicJsonFlight
        
        





    

    
