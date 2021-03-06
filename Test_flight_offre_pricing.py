from amadeus import Client, ResponseError

amadeus = Client(
    client_id='jzhnkve7G1nVerkYjcdZuYIGl0qvXKhs',
    client_secret='1Um4mEwSREU2ZIoH'
)

try:
    '''
    Confirm availability and price from SYD to BKK in summer 2020
    '''
    flights = amadeus.shopping.flight_offers_search.get(originLocationCode='SYD', destinationLocationCode='BKK',
                                                        departureDate='2021-07-01', adults=1).data
    response_one_flight = amadeus.shopping.flight_offers.pricing.post(flights[0])
    print(response_one_flight.data)

    response_two_flights = amadeus.shopping.flight_offers.pricing.post(flights[0:2])
    print(response_two_flights.data)
except ResponseError as error:
    raise error