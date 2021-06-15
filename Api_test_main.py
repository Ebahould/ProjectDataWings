import Api_via_SDK as api_SDK
from Api_Amadeus_Direct import Api_AmadeusDirect as ApiDirect

from Api_Amadeus_Direct_PROD import Api_Amadeus_DirectPROD as ApiDirectPROD
from Api_utility import Apiutility as apu
from DataAccessPostgres import Data_Acces_Postgres as dataAccess

travelClassParam =  ["ECONOMY","PREMIUM_ECONOMY","BUSINESS","FIRST"]
#travelClassParam =  ["BUSINESS"]

def main():
    # L = []
    #api_SDK.flight_offers_search()
    Listes_flights_complete=[]
    #Création d'un objet
    ApiDirectObject = ApiDirect()
    DataAccessObject = dataAccess()
    ApiDirectPodObject = ApiDirectPROD()
    Apiutility = apu()
    
    Listes_flights_data=[]
    
    for classe in travelClassParam:
        #Liste flight date
        
        
        
        List_flights = ApiDirectObject.flight_offers(classe)
        
        #Pour environement prod
        
        # List_flights = ApiDirectPodObject.flight_offers(classe)
        Listes_flights_data.append(List_flights)

        #list flights
        List_flights_data = List_flights['data']
        for i in List_flights_data:
            Listes_flights_complete.append(i)
    
    
   
    Liste_colonne = ["id", "source", "instantTicketingRequired","numberofbookableseats","disablepricing","oneway","lastticketingdate","validatingairlinecodes","nonhomogeneous","paymentcardrequired"]
    
    
    #Inserer toutes les lignes de la flightoffre
    DataAccessObject.InsertAllofferflight(Listes_flights_complete)
    
    # DataAccessObject.InsertAllSegments(Listes_flights_complete)
    
    # DataAccessObject.InsertAlltravelerpricings(Listes_flights_complete)
    # DataAccessObject.InsertAllfees(Listes_flights_complete)
    # DataAccessObject.InsertAllfareDetailsBySegment(Listes_flights_complete)


    # DataAccessObject.InsertAllSegments(Listes_flights_complete)

    print("######################fin######################")

    # print(id, " ", source, " ", instantTicketingRequired)


    # Ecrire dans un fichier  txt le resultat
    Apiutility.WriteIntextFile('\n'.join(str(v) for v in Listes_flights_complete),"Data.27.05.txt")
   
   
    # for v in Listes_flights_complete:
    #     response_list_price = api_SDK.flight_offers_pricing(v)
    #     L.append(response_list_price)
    
    # for data in Listes_flights_data :
    #     if(len(data['data']) < 1):
    #         continue
    #     api_SDK.flight_offers_pricing(data)
        
  
    # print(Listes_flights_complete)
    # print("*********flight pricing ******** ")
    # api_SDK.flight_offers_pricing(List_flights[0])
    #APi Production
    # ApiDirectPROD.flight_offers()
    # ApiDirect.flight_offers()
if __name__ == "__main__":
    main()

