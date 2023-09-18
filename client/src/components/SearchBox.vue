<template>
    <div>
        <div class="bg-primary">
            <div class="relative">
                <h1 class="text-5xl text-center p-2 font-bold text-white">FlyPy</h1>
                <img class="absolute top-2 left-2 w-64" src="data:image/webp;base64,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" alt="Powered by Skyscanner">
                <p class="absolute top-2 right-2 text-white">By Tim Niehenke</p>                
                <br>
                <p class="text-center font-medium text-white">The Flight Search Project powered by Python, Flask, Vue.js, Tailwind CSS & Skyscanner API.</p>
            </div>
            <br>   
            <div class="text-center">
                <form>
                    <input type="text" v-model="flightSearchForm.departure" placeholder="Departure airport (IATA)" class="rounded-l-lg px-4 py-4" maxlength="3">           
                    <input type="text" v-model="flightSearchForm.destination" class="px-4 py-4 ml-2" placeholder="Destination airport (IATA)" maxlength="3">
                    <input type="date" v-model="flightSearchForm.departureDate" class="rounded-r-lg px-4 py-4 ml-2" placeholder="Departure date">
                    <button type="button" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-4 px-4 rounded-lg ml-4" @click="getResults(); checkResults();">Search!</button>
                </form> 
            </div>
            <br>
            <p class="text-center text-xs text-white">Please enter the Departure & Destination Airport as IATA Code, e.g. DUS (Düsseldorf). <br> IATA Codes are 3-letter-codes used to identify airports. A list can be found <a href="https://www.iata.org/en/publications/directories/code-search/" target="_blank">here</a>. </p>
            <br>
        </div>

        <div v-if="showErrorWarning" class="bg-red-100 border border-red-400 text-red-700 text-center px-4 py-3 rounded relative" role="alert">
            <strong class="font-bold">Warning! </strong>
            <span class="block sm:inline">The request took to long or your input was invalid. Please check the input and press "Search" again!</span>
            <span class="absolute top-0 bottom-0 right-0 px-4 py-3">
                <svg class="fill-current h-6 w-6 text-red-500" role="button" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" @click="showErrorWarning=false"><title>Close</title><path d="M14.348 14.849a1.2 1.2 0 0 1-1.697 0L10 11.819l-2.651 3.029a1.2 1.2 0 1 1-1.697-1.697l2.758-3.15-2.759-3.152a1.2 1.2 0 1 1 1.697-1.697L10 8.183l2.651-3.031a1.2 1.2 0 1 1 1.697 1.697l-2.758 3.152 2.758 3.15a1.2 1.2 0 0 1 0 1.698z"/></svg>
            </span>
        </div>

        <table v-if="showResults" class="min-w-full divide-y divide-gray-200">
            <thead>
                <tr>
                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Operating Airline</th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Departure</th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Arrival</th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Duration</th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Changes</th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Price</th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Link</th>
                </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
                <tr v-for="(itinerary, itineraryId) in itineraries" :key="itineraryId">
                    <td class="px-6 py-4 whitespace-nowrap">{{ carriers[legs[itineraryId].operatingCarrierIds[0]].name }}</td>
                    <td class="px-6 py-4 whitespace-nowrap">{{ formatDatetimeFromObject(legs[itineraryId].departureDateTime)}}</td>
                    <td class="px-6 py-4 whitespace-nowrap">{{ formatDatetimeFromObject(legs[itineraryId].arrivalDateTime) }}</td>
                    <td class="px-6 py-4 whitespace-nowrap">{{ formatDuration(legs[itineraryId].durationInMinutes) }}</td>
                    <td class="px-6 py-4 whitespace-nowrap">{{ legs[itineraryId].stopCount }}</td>
                    <td class="px-6 py-4 whitespace-nowrap font-semibold">{{ (itinerary.pricingOptions[0].price.amount / 1000).toFixed(2) }} EUR</td>
                    <td class="px-6 py-4 whitespace-nowrap">
                        <button @click="openLink(itinerary.pricingOptions[0].items[0].deepLink)" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">Check offer</button>
                    </td>
                </tr>
            </tbody>
        </table>
        <div v-if="showPicture" class="container mx-auto px-8 mt-8 ">
            <img src="https://images.pexels.com/photos/12993380/pexels-photo-12993380.jpeg" alt="Surf pic" class="rounded-3xl">
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import formatDurationX from '../utils/formatDuration.js'

export default {
    data() {
        return {
            flightSearchForm: {
                departure: '',
                destination: '',
                departureDate: '',
            },
            itineraries: {},
            legs: {},
            carriers: {},
            formattedDate: '',
            showPicture: true,
            showResults: false,
            showErrorWarning: false,
        }
    },
    methods: {
        formatDuration: formatDurationX,

        getResults() {
            const payload = {
                departure: this.flightSearchForm.departure.toUpperCase(),
                destination: this.flightSearchForm.destination.toUpperCase(),
                departureDate: this.flightSearchForm.departureDate,
            };
            
            const path = `http://localhost:5000/?from=${payload.departure}&to=${payload.destination}&date=${payload.departureDate}`;

            axios.get(path)
                .then((response) => {
                    this.itineraries = response.data.content.results.itineraries;
                    this.legs = response.data.content.results.legs;
                    this.carriers = response.data.content.results.carriers;
                })
                .catch((error) => {
                    this.itineraries = {};
                    this.legs = {};
                    this.carriers = {};
                });
        },

        formatDatetimeFromObject(dateObject) {
            try {
                const year = dateObject.year;
                const month = dateObject.month - 1; 
                const day = dateObject.day;
                const hour = dateObject.hour;
                const minute = dateObject.minute;

                const dt = new Date(year, month, day, hour, minute);

                const options = { year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit' };
                const formattedDate = dt.toLocaleString('de-DE', options);

                return formattedDate;
            } 
            catch (error) {
                console.error(`Error: ${error} key is missing in the object.`);
                return null;
            }
        },
   
        openLink(link) {
            window.open(link, '_blank');
        },
        toggleBodyContent() {
            this.showPicture = false;
            this.showResults = true;
        },
        checkResults() {
            setTimeout(() => {
                if( ! Object.keys(this.itineraries).length) {
                    this.showErrorWarning = true;
                    this.showResults = false;
                }
                else {
                    this.showErrorWarning = false;
                    this.toggleBodyContent();
                }
            }, 1000);
        }
    }
};
</script>