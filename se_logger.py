import requests,json
with requests.Session() as s :
    #ouvrir une session sur le site
   
    url = 'https://www.accounts.sellingplatformconnect.amadeus.com/LoginService/services/rs/auth2.0/identify?responseType=JSON&service=SECO&nonce=hETDIZSLbKAUFEwu'
    s.get(url)
    data ={"configurationToken":"eyJhbGciOiJIUzI1NiJ9.eyJWQUxJREFURV9QQVNTV09SRF9VUkwiOiJodHRwczpcL1wvd3d3LnNlbGxpbmdwbGF0Zm9ybWNvbm5lY3QuYW1hZGV1cy5jb21cL0xvZ2luU2VydmljZVwvbG9naW4uanNwP1NJVEU9TE9HSU5VUkwmTEFOR1VBR0U9R0ImQUNUSU9OPXZhbGlkYXRlIiwiVU1fRElTUExBWV9GT1JDRVNJR04iOiJUUlVFIiwiVU1fREVURUNUX0xBTkciOiJUUlVFIiwiVU1fUFdEX0VYUF9OQkRBWVMiOiI1IiwiVU1fTEFOR19CT1hfRkxBRyI6IkZBTFNFIiwiQVBQTElDQVRJT05fSUQiOiJTRUNPIiwibm9uY2UiOiJmcFRPeDRXUUN3MHJCbWRiIiwiVU1fRElTUExBWV9SRU1fTUUiOiJUUlVFIiwiVU1fTE9HSU5fTEFOR19CT1giOiJUUlVFIiwiVU1fTUFJTF9GUk9NIjoiXCJBbWFkZXVzIFNlY3VyaXR5IFNlcnZpY2VcIjxub3JlcGx5QGFtYWRldXMuY29tPiIsIlVNX0RJU1BMQVlfRFVUWV9DT0RFIjoiVFJVRSIsIlVNX1JFTV9NRV9ERUZBVUxUIjoiVFJVRSIsIlVNX09GRklDRV9ORUVERUQiOiJUUlVFIiwiTE9DQVRJT05fSUQiOiIzRTYxRkU0QUNCNzg3RDY1OEYwNEFGMUNBMDNFMDg3M0FBNjMxODQ5ODg0MkEyNzc5QzAxQTZDMkRDRUJFRkZGIiwiVU1fUFdEX0VYUF9XQVJOIjoiVFJVRSJ9.u9PnBNEMlTJpiQ70Gv34ZOLD6K0Vio9mPxAVaNPXrgY","officeId":"SGNVM27R2","userAlias":"DATAWINGS","language":"en_us","authMode":"HOS"}
    r = s.post(url, data = data)
    response = r.text
    response_json = json.loads(response)
    acces_token = response_json["accessToken"]
    data1 = {"configurationToken":"eyJhbGciOiJIUzI1NiJ9.eyJWQUxJREFURV9QQVNTV09SRF9VUkwiOiJodHRwczpcL1wvd3d3LnNlbGxpbmdwbGF0Zm9ybWNvbm5lY3QuYW1hZGV1cy5jb21cL0xvZ2luU2VydmljZVwvbG9naW4uanNwP1NJVEU9TE9HSU5VUkwmTEFOR1VBR0U9R0ImQUNUSU9OPXZhbGlkYXRlIiwiVU1fRElTUExBWV9GT1JDRVNJR04iOiJUUlVFIiwiVU1fREVURUNUX0xBTkciOiJUUlVFIiwiVU1fUFdEX0VYUF9OQkRBWVMiOiI1IiwiVU1fTEFOR19CT1hfRkxBRyI6IkZBTFNFIiwiQVBQTElDQVRJT05fSUQiOiJTRUNPIiwibm9uY2UiOiJmcFRPeDRXUUN3MHJCbWRiIiwiVU1fRElTUExBWV9SRU1fTUUiOiJUUlVFIiwiVU1fTE9HSU5fTEFOR19CT1giOiJUUlVFIiwiVU1fTUFJTF9GUk9NIjoiXCJBbWFkZXVzIFNlY3VyaXR5IFNlcnZpY2VcIjxub3JlcGx5QGFtYWRldXMuY29tPiIsIlVNX0RJU1BMQVlfRFVUWV9DT0RFIjoiVFJVRSIsIlVNX1JFTV9NRV9ERUZBVUxUIjoiVFJVRSIsIlVNX09GRklDRV9ORUVERUQiOiJUUlVFIiwiTE9DQVRJT05fSUQiOiIzRTYxRkU0QUNCNzg3RDY1OEYwNEFGMUNBMDNFMDg3M0FBNjMxODQ5ODg0MkEyNzc5QzAxQTZDMkRDRUJFRkZGIiwiVU1fUFdEX0VYUF9XQVJOIjoiVFJVRSJ9.u9PnBNEMlTJpiQ70Gv34ZOLD6K0Vio9mPxAVaNPXrgY","accessToken":acces_token,"authenticationFactors":{"password":"1A2VN-fr","uba":"{}"},"language":"en_us","authMode":"HOS"}
    url1 = 'https://www.accounts.sellingplatformconnect.amadeus.com/LoginService/services/rs/auth2.0/authenticate?responseType=JSON&service=SECO&nonce=hETDIZSLbKAUFEwu'
    r1 = s.post(url1,data = data1)
    response1 = r1.text
    print(response1)