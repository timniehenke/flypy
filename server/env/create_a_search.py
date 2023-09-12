import requests

url = "https://partners.api.skyscanner.net/apiservices/v3/flights/live/search/create"

def data(flightSearchForm: dict) -> dict:

	departure_date_parts = flightSearchForm[0]["departureDate"].split('-')
	year = int(departure_date_parts[0])
	month = int(departure_date_parts[1])
	day = int(departure_date_parts[2])

	payload = { 
        "query": {
			"market": "DE",
			"locale": "de-DE",
			"currency": "EUR",
			"preferDirects": "true",
			"queryLegs": [
				{
					"originPlaceId": { "iata": flightSearchForm[0]["departure"] },
					"destinationPlaceId": { "iata": flightSearchForm[0]["destination"] },
					"date": {
						 "year": year,
						"month": month,
						"day": day
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