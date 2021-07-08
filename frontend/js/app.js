import '../css/style.css';
import Chart from 'chart.js/auto';

const API_URL = './data/data.json';

// Fetch json data
const fetchData = async () => {
  const response = await fetch(API_URL);
  const data = await response.json();
  convertData(data);
}
fetchData();

// Converting json data to arrays
const convertData = (data) => {
  let labels = data.results.map(function(e) {
    return e.id
  })

  let values = data.results.map(function(e) {
    return e.value;
  })
  
  generateCharts(labels, values);
}

const generateCharts = (labels, values) => {
  // Cache myChart element
let myChart = document.getElementById('myChart').getContext('2d');

// Init Chart.js and create chart using parameters
let landingPageRating = new Chart(myChart, {
  type: 'bar',
  data: {
    labels:labels,
    datasets:[{
      label:'Amount of votes',
      data:values,
      backgroundColor: 'rgb(160, 220, 100)',
      borderWidth: 1,
      borderColor: '#777',
      hoverBorderWidth: 3,
      hoverBorderColor: '#000'
    }]
  },
  options: {
    title: {
      display: true,
      text: 'Landing page rating (out of 10)'
    },
    scales: {
      y : {
        max: 20,
        min: 0,
        ticks: {
          stepSize : 1
        }
      }
    },
    plugins: {
      legend: {
        labels: {
          font: {
            size: 20
          }
        }
      }
    }
  }
})
}

