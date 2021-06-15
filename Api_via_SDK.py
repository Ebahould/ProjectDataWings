from amadeus import Client, ResponseError
import Api_utility as apu



def flight_offers_pricing(List_flights):

    amadeus = Client(
        client_id='jzhnkve7G1nVerkYjcdZuYIGl0qvXKhs',
        client_secret='1Um4mEwSREU2ZIoH'
    )

    try:
        
    # '''
    # Confirm availability and price from SYD to BKK in summer 2020
    # # '''
        List_flights_offre = List_flights['data']
        
        # List_flights = amadeus.shopping.flight_offers_search.get(originLocationCode='SYD', destinationLocationCode='BKK',
        #                                                 departureDate='2021-07-01', adults=1).data
        print("lenghth len(List_flights_offre) =>  "+ str(len(List_flights_offre)))

        for i in range(len(List_flights_offre)): 
            response_flight = amadeus.shopping.flight_offers.pricing.post(List_flights_offre[i])
            apu.WriteIntextFile('\n'.join(str(v) for v in response_flight.data['flightOffers']),"Data_Price.txt", 'a')
        
        # print(response_one_flight.data)

        # response_two_flights = amadeus.shopping.flight_offers.pricing.post(flights[0:2])
        # print(response_two_flights.data)
    except ResponseError as error:
         raise error

    return response_flight.data

