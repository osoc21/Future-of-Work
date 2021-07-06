(() => {
  // API will return calculated values
  const API_URL = './data/data.json';

  // Cache myChart element
  let myChart = document.getElementById('myChart').getContext('2d');

  // Init Chart.js and create chart
  let landingPageRating = new Chart(myChart, {
    type: 'bar',
    data: {
      labels:['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
      datasets:[{
        label:'Amount of votes',
        // Data is
        data:[0, 0, 0, 0, 0, 1, 2, 4, 4, 2, 4],
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
          max: 5,
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
  const app = {
    init() {
      this.fetchData();
    },
    async fetchData() {
      const response = await fetch(API_URL);
      const data = await response.json();
      this.populateHTML(data);
    },
    populateHTML(data) {
      console.log(data)
    }
  };
  app.init();
})();