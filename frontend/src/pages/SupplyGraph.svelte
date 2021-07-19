<script>
import { onMount } from "svelte";
import Chart from 'chart.js/auto';
import AppLayout from "../components/AppLayout.svelte";
import { fetchWorkforceData } from '../api/fetch';

const fetchData = async () => {
    const response = await fetchWorkforceData();
    console.log(response);
    mapData(response);
}

const mapData = (data) => {
    var labels = data.result.attrition.map(function(e) {
        return e.FTE;
    });
    var data = data.result.attrition.map(function(e) {
        return e[`Country of Personnel Area`];
    });
    createChart(labels, data)
}
fetchData();

function createChart(chartData, chartLabels) {
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: chartLabels,
        datasets: [{
            label: '# of Votes',
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
        }]
    },
    options: {
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
    <div class="relative flex container-flex">
        <div class="flex-1 font-bold space-y-7">
            <canvas id="myChart" width="400" height="400"></canvas>

        </div>
    </div>
</AppLayout>