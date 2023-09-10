<template>
  <div class="p-6">
    <table class="min-w-full divide-y divide-gray-200">
      <thead>
        <tr>
          <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Airline</th>
          <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Price</th>
          <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Time of Departure</th>
          <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Time of Arrival</th>
          <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Duration</th>
          <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Changes</th>
          <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Link</th>
        </tr>
      </thead>
      <tbody class="bg-white divide-y divide-gray-200">
        <tr v-for="(itinerary, itineraryId) in itineraries" :key="itineraryId">
          <td class="px-6 py-4 whitespace-nowrap">'Airline XY'</td>
          <td class="px-6 py-4 whitespace-nowrap font-semibold">{{ (itinerary.pricingOptions[0].price.amount / 1000).toFixed(2) }} EUR</td>
          <td class="px-6 py-4 whitespace-nowrap">{{ formatDatetimeFromObject(legs[itineraryId].departureDateTime)}}</td>
          <td class="px-6 py-4 whitespace-nowrap">{{ formatDatetimeFromObject(legs[itineraryId].arrivalDateTime) }}</td>
          <td class="px-6 py-4 whitespace-nowrap">{{ legs[itineraryId].durationInMinutes }} mins</td>
          <td class="px-6 py-4 whitespace-nowrap">{{ legs[itineraryId].stopCount }}</td>
          <td class="px-6 py-4 whitespace-nowrap">
            <button @click="openLink(itinerary.pricingOptions[0].items[0].deepLink)" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">Check offer</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

  
<script>
import axios from 'axios';

export default {
  name: 'Results',
  data() {
    return {
      itineraries: {},
      legs: {},
      formattedDate: '',
    };
  },
  methods: {
    getResults() {
      const path = 'http://localhost:5000/results';
      axios.get(path)
        .then((response) => {
          this.itineraries = response.data.content.results.itineraries;
        })
        .catch((error) => {
          console.error(error);
        });

      axios.get(path)
      .then((response) => {
        this.legs = response.data.content.results.legs;
      })
      .catch((error) => {
          console.error(error);
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
    // Open the link in a new tab
      window.open(link, '_blank');
    },
  },
  created() {
    this.getResults();
  },
};
</script>