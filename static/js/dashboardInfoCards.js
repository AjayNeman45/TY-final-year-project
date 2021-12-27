$.ajax({
	type: "GET",
	url: "/ajax/societyInfo",
	success: response => {
		document.getElementsByClassName("number-of-wings")[0].innerHTML =
			response.numberOfWings
		document.getElementsByClassName("number-of-flats")[0].innerHTML =
			response.numberOfFlats
		document.getElementsByClassName("number-of-residents")[0].innerHTML =
			response.numberOfResidents
		document.getElementsByClassName("number-of-tenants")[0].innerHTML =
			response.numberOfTenants
	},
	error: function (error) {
		console.log(error)
	},
})
