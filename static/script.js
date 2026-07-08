const activity = document.getElementById("activity");
const confidence = document.getElementById("confidence");

const xValue = document.getElementById("x");
const yValue = document.getElementById("y");
const zValue = document.getElementById("z");

const status = document.getElementById("status");

const ctx = document.getElementById("chart").getContext("2d");

const chart = new Chart(ctx, {

    type: "line",

    data: {

        labels: [],

        datasets: [

            {
                label: "X",
                data: [],
                borderColor: "#ef4444",
                tension: 0.3
            },

            {
                label: "Y",
                data: [],
                borderColor: "#22c55e",
                tension: 0.3
            },

            {
                label: "Z",
                data: [],
                borderColor: "#3b82f6",
                tension: 0.3
            }

        ]

    },

    options: {

        responsive: true,

        animation: false,

        scales: {

            x: {

                ticks: {

                    color: "white"

                }

            },

            y: {

                ticks: {

                    color: "white"

                }

            }

        },

        plugins: {

            legend: {

                labels: {

                    color: "white"

                }

            }

        }

    }

});

async function updatePrediction() {

    try {

        const response = await fetch("/predict");

        const data = await response.json();

        if (data.status === "collecting") {

            status.innerHTML =
                "Collecting Samples (" +
                data.samples +
                "/" +
                data.required +
                ")";

            return;

        }

        if (data.status === "error") {

            status.innerHTML = "Disconnected";

            return;

        }

        status.innerHTML = "Connected";

        activity.innerHTML = data.activity;

        confidence.innerHTML = data.confidence + "%";

        xValue.innerHTML = data.x;

        yValue.innerHTML = data.y;

        zValue.innerHTML = data.z;

        chart.data.labels.push("");

        chart.data.datasets[0].data.push(data.x);

        chart.data.datasets[1].data.push(data.y);

        chart.data.datasets[2].data.push(data.z);

        if (chart.data.labels.length > 50) {

            chart.data.labels.shift();

            chart.data.datasets[0].data.shift();

            chart.data.datasets[1].data.shift();

            chart.data.datasets[2].data.shift();

        }

        chart.update();

    }

    catch (e) {

        status.innerHTML = "Connection Error";

    }

}

setInterval(updatePrediction, 300);

updatePrediction();