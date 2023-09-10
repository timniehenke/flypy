import requests

url = "https://partners.api.skyscanner.net/apiservices/v3/flights/live/search/create"

def data(flightSearchForm: dict) -> dict:    
	payload = { 
        "query": {
			"market": "DE",
			"locale": "de-DE",
			"currency": "EUR",
			"preferDirects": "true",
			"queryLegs": [
				{
					"originPlaceId": { "iata": flightSearchForm["departure"] },
					"destinationPlaceId": { "iata": flightSearchForm["destination"] },
					"date": {
						"year": 2023,
						"month": 9,
						"day": 20
					},
				}
			],
			"cabinClass": "CABIN_CLASS_ECONOMY",
			"adults": 1,
		} 
    }
	headers = {
		"x-api-key": "sh428739766321522266746152871799",
	}

	response = requests.post(url, json=payload, headers=headers)

	return response.json()