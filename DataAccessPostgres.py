import re
import psycopg2
import Api_Amadeus_Direct as ApiDirect


class Data_Acces_Postgres:
    
    def GetConnexion(self):
        try:
            conn = psycopg2.connect(
                user = "postgres",
                password = "96130055",
                host = "localhost",
                port = "5432",
                database = "Test"
            )
        
            return conn
        except (Exception, psycopg2.Error) as error :
            print ("Erreur lors de la connexion à PostgreSQL", error)



    def InsertOfferflight(self,source,instantTicketingRequired,numberofbookableseats,disablepricing,oneway,lastticketingdate,validatingairlinecodes,nonhomogeneous,paymentcardrequired,pricingoptionsfaretype,baseprices,totalprices,currencyprices,grandtotal, idJson):
        try:
            conn = self.GetConnexion()
            cur = conn.cursor()

            #Récupérer la séquence
            cur.execute("SELECT nextval('seqflightoffre');")
            Next_Id_flightoffre = cur.fetchone()
            

        
            sqlInsert = """INSERT INTO public.flightoffers(idflightoffers, source, instantTicketingRequired,numberofbookableseats,disablepricing,oneway,lastticketingdate,validatingairlinecodes,nonhomogeneous,paymentcardrequired,pricingoptionsfaretype,baseprices,totalprices,currencyprices,grandtotal, idjson) VALUES ( %s,%s, %s, %s,%s, %s, %s,%s,%s, %s,%s, %s, %s,%s,%s,%s)"""
            value = (Next_Id_flightoffre,source, instantTicketingRequired,numberofbookableseats,disablepricing,oneway,lastticketingdate,validatingairlinecodes,nonhomogeneous,paymentcardrequired,pricingoptionsfaretype,baseprices,totalprices,currencyprices,grandtotal, idJson)
            cur.execute(sqlInsert, value)


            conn.commit()
            count = cur.rowcount
            # print (count, "enregistrement inséré avec succès dans la table flightoffers.")
        
            #fermeture de la connexion à la base de données
            cur.close()
            conn.close()
            # print("La connexion PostgreSQL est fermée")

            # retourner idflightoffre pour qu'il soit utilisé dans les prochaine methode
            return Next_Id_flightoffre
        except (Exception, psycopg2.Error) as error:
            print ("Erreur lors de la connexion à PostgreSQL (InsertOfferflight) ", error)


    #C'est une méthode pour récuperer les informations d'un flight offre depuis une liste de flight offres
    def InsertAllofferflight(self,Listes_flights_complete):
        for flight in Listes_flights_complete:
            
            #    idflightoffers = Listes_flights_complete[j]["id"]
            source= flight["source"]
            instantTicketingRequired= flight["instantTicketingRequired"]
            
            # if flight["numberofbookableseats"] 
            # numberofbookableseats = flight["numberofbookableseats"]
            # else
            numberofbookableseats = 1


            disablepricing =  True #flight["disablepricing"]
            oneWay = flight["oneWay"]
            lastTicketingDate = flight["lastTicketingDate"]
            validatingairlinecodes= flight["validatingAirlineCodes"]
            nonhomogeneous = flight["nonHomogeneous"]
            paymentcardrequired = True #flight["paymentcardrequired"]
            pricingoptionsfaretype =flight["pricingOptions"]["fareType"]
            currencyprices = flight["price"]["currency"]
            totalprices = flight["price"]["total"]
            baseprices = flight["price"]["base"]
            grandtotal = flight["price"]["grandTotal"]
            idJson = flight["id"] 
            
            idFlightOffre = self.InsertOfferflight(source, instantTicketingRequired,numberofbookableseats,disablepricing,oneWay,lastTicketingDate,validatingairlinecodes,nonhomogeneous,paymentcardrequired,pricingoptionsfaretype,baseprices,totalprices,currencyprices,grandtotal, idJson)

            #insert tAlltravelerpricings
            listOneFlight = [flight]
            self.InsertAlltravelerpricings(listOneFlight, idFlightOffre)

            #insert tAllSegments
            self.InsertAllSegments(listOneFlight, idFlightOffre)

            #Inseration Segments

    def InsertSegments(self,carriercode,number,duration,numberofstops,blacklistedineu,aircraft,arrival_iataCode,arrival_at,departureiatacode,departureat,idFlightOffre):
        try:
            conn = self.GetConnexion()
            cur = conn.cursor()

            #Récupérer la séquence
            cur.execute("SELECT nextval('sequencesegments');")
            Next_Id_Segments = cur.fetchone()
            

            
            sqlInsert = """INSERT INTO public.segments(idsegments,carriercode,number,duration,numberofstops,blacklistedineu,aircraft,\"arrival_iataCode\",arrival_at,departureiatacode,departureat,idflightoffers) VALUES ( %s, %s,%s, %s, %s,%s, %s,%s, %s,%s, %s, %s)"""
            
            value = (Next_Id_Segments,carriercode,number,duration,numberofstops,blacklistedineu,aircraft,arrival_iataCode,arrival_at,departureiatacode,departureat,idFlightOffre)
            cur.execute(sqlInsert, value)


            conn.commit()
            count = cur.rowcount
            # print (count, "enregistrement inséré avec succès dans la table flightoffers.")
        
            #fermeture de la connexion à la base de données
            cur.close()
            conn.close()
            # print("La connexion PostgreSQL est fermée")

        except (Exception, psycopg2.Error) as error :
            print ("Erreur lors de la connexion à PostgreSQL", error)


    #Inseretion de toutes les lignes

    def InsertAllSegments(self,Listes_flight,idFlightOffre):
        
        for flight in Listes_flight:
            
            itinirairies= flight["itineraries"]
            for itiniraire in itinirairies :
                segments = itiniraire["segments"]

                for segment in segments:
                    carrierCode = segment["carrierCode"]
                    number = segment["number"]
                    aircraft= segment["aircraft"]["code"]
                    #carrierCode =segments["operating"]
                    duration = segment["duration"]
                    blacklistedInEU = segment["blacklistedInEU"]
                    numberofstops= segment["numberOfStops"]
                    arrival_iataCode = segment["arrival"]["iataCode"]
                    arrival_at =segment["arrival"]["at"]
                    departureiatacode = segment["departure"]["iataCode"]
                    # departureTerminal = segment["departure"]["terminal"]
                    departureat = segment["departure"]["at"]

                    self.InsertSegments(carrierCode,number,duration,numberofstops,blacklistedInEU,aircraft,arrival_iataCode,arrival_at,departureiatacode,departureat,idFlightOffre)
            
    
    # Insération du tableau TravelPricings
    def Inserttravelerpricings(self,fareoption,travelerType,basePrice,totalPrice,priceCurrency, cabin ,idFlightOffre):
        try:
            conn = self.GetConnexion()
            cur = conn.cursor()

    #Récupérer la séquence
            cur.execute("SELECT nextval('sequencetravelerpricings');")
            Next_traveler_pricings = cur.fetchone()
            

            
            sqlInsert = """INSERT INTO public.travelerpricings(idtravelerpricings,fareoption,travelerType,basePrice,totalPrice,priceCurrency,cabin, idflightoffers) VALUES ( %s,%s,%s,%s,%s,%s,%s,%s)"""
            
            value = (Next_traveler_pricings,fareoption,travelerType,basePrice,totalPrice,priceCurrency,cabin,idFlightOffre)
            cur.execute(sqlInsert, value)


            conn.commit()
            count = cur.rowcount
            # print (count, "enregistrement inséré avec succès dans la table flightoffers.")
        
            #fermeture de la connexion à la base de données
            cur.close()
            conn.close()
            # print("La connexion PostgreSQL est fermée")
            
            return Next_traveler_pricings

        except (Exception, psycopg2.Error) as error :
            print ("Erreur lors de la connexion à PostgreSQL (Inserttravelerpricings) ", error)


    #Inseretion de toutes les lignes

    def InsertAlltravelerpricings(self,Listes_flights, idFlightOffre):

        for flight  in Listes_flights:
            travels= flight["travelerPricings"]

            for travel in travels :
            
                fareoption= travel["fareOption"]
                travelerType= travel["travelerType"]
                baseprice =travel["price"]["base"]
                totalprice =travel["price"]["total"]
                pricecurrency =travel["price"]["currency"]
                cabin = travel["fareDetailsBySegment"][0]["cabin"]
                #Recuperer IdTravelPricingd afin de pouvoir l'injecter dans le tableau faredetailbysgment
                IdTravelPricing = self.Inserttravelerpricings(fareoption,travelerType,baseprice,totalprice,pricecurrency,cabin,idFlightOffre)
                listFlight =[flight]
                self.InsertAllfareDetailsBySegment(listFlight,IdTravelPricing)

    #Inseretion du tableau fareDetailsBySegment
    # Insération du tableau fareDetailsBySegment
    def InsertFareDetailsBySegment(self,cabin,fareBasis,classe,quantity,IdTravelPricing):
        try:
            conn = self.GetConnexion()
            cur = conn.cursor()

            #Récupérer la séquence
            cur.execute("SELECT nextval('sequencefareDetailsBySegment');")
            Next_Id_Segments = cur.fetchone()
            

            IdTravelPricing_as_int = int(IdTravelPricing[0])
            sqlInsert = """INSERT INTO public.fareDetailsBySegment(idfaredetailsbysegment,cabin,fareBasis, classe, quantity, idtravelerpricings) VALUES ( %s, %s,%s, %s,%s,%s)"""
            
            value = (Next_Id_Segments,cabin,fareBasis,classe,quantity,IdTravelPricing_as_int)
            cur.execute(sqlInsert, value)


            conn.commit()
            count = cur.rowcount
            # print (count, "enregistrement inséré avec succès dans la table flightoffers.")
        
            #fermeture de la connexion à la base de données
            cur.close()
            conn.close()
            # print("La connexion PostgreSQL est fermée")

        except (Exception, psycopg2.Error) as error :
            print ("Erreur lors de la connexion à PostgreSQL(InsertFareDetailsBySegment) ", error)


    #Inseretion de toutes les lignes de la table fareDetailsBySegment

    def InsertAllfareDetailsBySegment(self,Listes_flights,IdTravelPricing):

        for flight  in Listes_flights:
            travelerPricings= flight["travelerPricings"][0]
            fareDetailsBySegments =travelerPricings["fareDetailsBySegment"]
            for segment in fareDetailsBySegments :
                cabin= segment["cabin"]
                fareBasis= segment["fareBasis"]
                classe = segment["class"]
                quantity = segment["includedCheckedBags"]["quantity"]
        
                self.InsertFareDetailsBySegment(cabin,fareBasis,classe,quantity,IdTravelPricing)
            

    #fees
    #Inseretion du tableau fee
    # Insération du tableau fee
    def InsertFees(self,amount,type):
        try:
            conn = self.GetConnexion()
            cur = conn.cursor()

    #Récupérer la séquence
            cur.execute("SELECT nextval('sequencefee');")
            Next_Id_fees = cur.fetchone()
            

            
            sqlInsert = """INSERT INTO public.fee(idfee,amount,type) VALUES ( %s,%s, %s)"""
            
            value = (Next_Id_fees,amount,type)
            cur.execute(sqlInsert, value)


            conn.commit()
            count = cur.rowcount
            # print (count, "enregistrement inséré avec succès dans la table flightoffers.")
        
            #fermeture de la connexion à la base de données
            cur.close()
            conn.close()
            # print("La connexion PostgreSQL est fermée")

        except (Exception, psycopg2.Error) as error :
            print ("Erreur lors de la connexion à PostgreSQL (InsertFees) ", error)


    #Inseretion de toutes les lignes

    def InsertAllfees(self,Listes_flights_complete):

        for flight  in Listes_flights_complete:
            Prices= flight["price"]
            fees = Prices["fees"]
            for fee in fees :
                amount= fee["amount"]
                type= fee["type"]
        
                self.InsertFees(amount,type)
            





