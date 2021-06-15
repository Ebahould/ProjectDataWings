
import requests, json
from amadeus import ResponseError
from flatten_json import flatten
import Api_utility as util

class Api_Amadeus_DirectPROD:

    def getToken(self):
        parametresPROD ={'grant_type': 'client_credentials', 'client_id': 'Guy8Thyjz5xQ6kEfgA2zoha9v2k0TNNY', 'client_secret': 'b7NrCDXhq6hNJfw5'}
        
        headers ={'Content-Type': 'application/x-www-form-urlencoded'}
        response =requests.post("https://api.amadeus.com/v1/security/oauth2/token", data=parametresPROD,headers =headers)
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
            parametres ={'originLocationCode': 'DSS', 'destinationLocationCode': 'CDG', 'departureDate': '2021-05-28', 'returnDate': '2021-06-28',  'adults': '1', 'nonStop':'false', 'max':'250' ,'travelClass': travelClassParam}
            headers ={'Authorization': self.getToken()}
            response =requests.get("https://api.amadeus.com/v2/shopping/flight-offers", params=parametres,headers =headers)
    
            responseJson = json.loads(response.text)
        
            listDicJsonFlight = responseJson
            
            
        except ResponseError as error:
            raise error 
            
    
        return listDicJsonFlight
        
        
            # listDicJsonPrice = response.data
            # firstRow = True

            # print("************* Start converting in JSON *****************")
            # for DicJson in listDicJsonPrice : 
            #     json_flatten_data = flatten(DicJson)
            #     util.WriteInCsvFile (json_flatten_data, firstRow,"Data.csv")
            #     firstRow = False 
    
        
            # print("************* File CSV has been created *****************")
        #print(response.data)
        # # listeReslt = json.loads(response.data)
        # print(reslt)
        





        #     # Fetches a new access token
        # def fetch_access_token(self):
        #     return self.client._unauthenticated_request(
        #         'POST',
        #         '/v1/security/oauth2/token',
        #         {
        #             'grant_type': 'client_credentials',
        #             'client_id': 'jzhnkve7G1nVerkYjcdZuYIGl0qvXKhs',
        #             'client_secret': '1Um4mEwSREU2ZIoH'
        #         }
        #     )


        # Request({
        #             'host': self.host,
        #             'verb': verb,
        #             'path': path,
        #             'params': params,
        #             'bearer_token': bearer_token,
        #             'client_version': version,
        #             'language_version': python_version(),
        #             'app_id': self.custom_app_id,
        #             'app_version': self.custom_app_version,
        #             'ssl': self.ssl,
        #             'port': self.port
        #         }


        #     def build_request(self, verb, path, params, bearer_token):
        #             return Request({
        #                 'host': self.host,
        #                 'verb': verb,
        #                 'path': path,
        #                 'params': params,
        #                 'bearer_token': bearer_token,
        #                 'client_version': version,
        #                 'language_version': python_version(),
        #                 'app_id': self.custom_app_id,
        #                 'app_version': self.custom_app_version,
        #                 'ssl': self.ssl,
        #                 'port': self.port
        #             })


        # # Builds a HTTP request object that contains all the information about
        #     # this request
        #     def __build_request(self, verb, path, params, bearer_token):
        #         return Request({
        #             'host': self.host,
        #             'verb': verb,
        #             'path': path,
        #             'params': params,
        #             'bearer_token': bearer_token,
        #             'client_version': version,
        #             'language_version': python_version(),
        #             'app_id': self.custom_app_id,
        #             'app_version': self.custom_app_version,
        #             'ssl': self.ssl,
        #             'port': self.port
        #         })