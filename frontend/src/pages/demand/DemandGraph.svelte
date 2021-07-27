<script>
  import { onMount } from 'svelte';
  import Chart from 'chart.js/auto';
  import AppLayout from '../../components/layouts/AppLayout.svelte';
  import { demandDataStore } from '../../stores/demandData';
  import DemandDataProvider from '../../components/dataProviders/DemandDataProvider.svelte';

  let canvas;
  var mounted = false;
  var myChart;
  let dataLabels;

  const getVizForYear = (year) => {
    const data = $demandDataStore.formattedData;
    const dataForYear = data.find((yearData) => yearData.year == year);
    return dataForYear.jobFamilies.reduce((accumulator, jobFamily) => {
      if (!accumulator.roles) accumulator.roles = [];
      if (!accumulator.amounts) accumulator.amounts = [];

      accumulator.roles.push(...jobFamily.FTEs.map((FTE) => FTE.role));
      accumulator.amounts.push(...jobFamily.FTEs.map((FTE) => FTE.amount));
      return accumulator;
    }, {});
  };

  const updateViz = (e, defaultYear) => {
    const year = defaultYear || e.currentTarget.value;

    const { roles, amounts } = getVizForYear(year);
    if (typeof myChart === 'undefined') {
      createChart(roles, amounts);
    } else {
      myChart.data.datasets[0].data = amounts;
      myChart.update();
    }
  };

  onMount(() => {
    mounted = true;
  });

  $: if (!$demandDataStore.isLoading && mounted) {
    updateViz(null, 2021);
  }

  function createChart(chartlabels, chartData) {
    var ctx = canvas.getContext('2d');

    myChart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: chartlabels,
        datasets: [
          {
            label: 'Amount of FTEs per Job Title',
            data: chartData,
            backgroundColor: [
              'rgba(255, 99, 132, 0.2)',
              'rgba(54, 162, 235, 0.2)',
              'rgba(255, 206, 86, 0.2)',
              'rgba(75, 192, 192, 0.2)',
              'rgba(153, 102, 255, 0.2)',
              'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
              'rgba(255, 99, 132, 1)',
              'rgba(54, 162, 235, 1)',
              'rgba(255, 206, 86, 1)',
              'rgba(75, 192, 192, 1)',
              'rgba(153, 102, 255, 1)',
              'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
          }
        ]
      },
      options: {
        tooltips: {
          callbacks: {
            label: {}
          }
        },
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });
  }
</script>

<AppLayout>
  <DemandDataProvider>
    <div class="relative flex container-flex">
      <div class="flex-1 font-bold space-y-7">
        <div>
          <h2>Demand: Visualization</h2>
          <p>Here you can find FTEs per every Job Title per one year at the time.</p>
        </div>
        <select on:input={updateViz} class="text-gray-700 block px-4 py-2 border-2">
          {#each $demandDataStore.formattedData || [] as yearData}
            <option>{yearData.year}</option>
          {/each}
        </select>

        <div style="width: 100%; height:100%">
          <canvas bind:this={canvas} width="20%" height="7rem" id="myChart" />
        </div>
      </div>
    </div>
  </DemandDataProvider>
</AppLayout>
