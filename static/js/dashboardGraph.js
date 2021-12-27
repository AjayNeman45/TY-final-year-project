$.ajax({
	type: "GET",
	url: "/ajax/expenses",
	success: function (response) {
		var areaChartData = {
			labels: response.expenses_dates,
			datasets: [
				{
					label: "Expenses",
					data: response.expenses_amounts,
					backgroundColor: "rgb(170, 246, 252)",
					borderColor: "#007bff",
					borderWidth: 2,
				},
			],
		}

		var barChartCanvas = $("#myChart").get(0).getContext("2d")
		var barChartData = jQuery.extend(true, {}, areaChartData)
		var temp0 = areaChartData.datasets[0]
		barChartData.datasets[0] = temp0

		var barChartOptions = {
			responsive: true,
			maintainAspectRatio: false,
			datasetFill: false,
		}

		var barChart = new Chart(barChartCanvas, {
			type: "bar",
			data: barChartData,
			options: {
				maintainAspectRatio: false,
				responsive: true,
				legend: {
					position: "top",
				},
				// hover: {
				//     mode: "label",
				// },
				scales: {
					xAxes: [
						{
							display: true,
							scaleLabel: {
								display: true,
								labelString: "Dates",
							},
						},
					],
					yAxes: [
						{
							display: true,
							ticks: {
								min: 100,
							},
						},
					],
				},
				title: {
					display: true,
					text: "Expenses report of the society",
					position: "bottom",
				},
			},
		})
	},
	error: function (response) {
		console.log(response)
	},
})

//-------------
//- DONUT CHART -
//-------------
// Get context with jQuery - using jQuery's .get() method.

$.ajax({
	type: "GET",
	url: "/ajax/complaints",
	success: response => {
		var totalComplains =
			response.pendingComplaints +
			response.activeComplaints +
			response.resolvedComplaints

		var donutChartCanvas = $("#donutChart").get(0).getContext("2d")
		var donutData = {
			labels: ["Total", "Active", "Pending", "Resolved"],
			datasets: [
				{
					data: [
						totalComplains,
						response.activeComplaints,
						response.pendingComplaints,
						response.resolvedComplaints,
					],
					backgroundColor: [
						"#f56954",
						"#00a65a",
						"#f39c12",
						"#00c0ef",
					],
				},
			],
		}
		var donutOptions = {
			maintainAspectRatio: false,
			responsive: true,
		}
		//Create pie or douhnut chart
		// You can switch between pie and douhnut using the method below.
		var donutChart = new Chart(donutChartCanvas, {
			type: "doughnut",
			data: donutData,
			options: donutOptions,
		})
	},
	error: error => {
		console.log(error)
	},
})
