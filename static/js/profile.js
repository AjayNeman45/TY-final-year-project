let editProfileBtn = document.getElementsByClassName("edit_profile_btn")[0]
let name = document.getElementsByClassName("name")
let surname = document.getElementsByClassName("surname")
let phoneNumber = document.getElementsByClassName("phone-number")
let email = document.getElementsByClassName("email")
let username = document.getElementsByClassName("username")
let profile_Photo = document.getElementsByClassName("profile-img")
let cameraIcon = document.getElementsByClassName("camera-icon")
let uploadedPhoto = document.getElementsByClassName("upload-photo")

function getCookie(name) {
	var cookieValue = null
	if (document.cookie && document.cookie !== "") {
		var cookies = document.cookie.split(";")
		for (var i = 0; i < cookies.length; i++) {
			var cookie = cookies[i].trim()
			if (cookie.substring(0, name.length + 1) === name + "=") {
				cookieValue = decodeURIComponent(
					cookie.substring(name.length + 1)
				)
				break
			}
		}
	}
	return cookieValue
}

// editProfileBtn.addEventListener("click", () => {
// 	console.log("yes ....")
// 	cameraIcon[0].style.display = "block"
// 	if (editProfileBtn.innerText == "Edit Profile") {
// 		name[0].removeAttribute("readonly")
// 		surname[0].removeAttribute("readonly")
// 		username[0].removeAttribute("readonly")
// 		phoneNumber[0].removeAttribute("readonly")
// 		email[0].removeAttribute("readonly")
// 		editProfileBtn.innerText = "Save Profile"
// 	} else {
// 		let formData = new FormData()
// 		formData.append("first_name", name[0].value)
// 		formData.append("last_name", surname[0].value)
// 		formData.append("username", username[0].value)
// 		formData.append("phone_Number", phoneNumber[0].value)
// 		formData.append("email", email[0].value)
// 		// formData.append("profile_Photo", uploadedPhoto[0].files[0])
// 		formData.append("csrfmiddlewaretoken", getCookie("csrftoken"))
// 		// let info = {
// 		// 	first_name: name[0].value,
// 		// 	last_name: surname[0].value,
// 		// 	username: username[0].value,
// 		// 	phone_Number: phoneNumber[0].value,
// 		// 	email: email[0].value,
// 		// 	profile_Photo = uploadedPhoto[0].files[0]
// 		// }
// 		let options = {
// 			method: "POST",
// 			headers: {
// 				"X-Requested-With": "XMLHttpRequest",
// 			},
// 			body: formData,
// 		}
// 		fetch("/members/edit-profile", options)
// 			.then(res => {
// 				return res.json()
// 			})
// 			.then(data => {
// 				console.log(data.status)
// 				if (data.status) {
// 					location.reload()
// 				} else {
// 					document
// 						.querySelectorAll("small")
// 						.forEach(error => error.remove())
// 					name[0].insertAdjacentHTML(
// 						"afterend",
// 						`<small class="px-2 text-danger">${
// 							data.errors.first_name ? data.errors.first_name : ""
// 						}</small>`
// 					)
// 					surname[0].insertAdjacentHTML(
// 						"afterend",
// 						`<small class="px-2 text-danger">${
// 							data.errors.last_name ? data.errors.last_name : ""
// 						}</small>`
// 					)
// 					username[0].insertAdjacentHTML(
// 						"afterend",
// 						`<small class="px-2 text-danger">${
// 							data.errors.username ? data.errors.username : ""
// 						}</small>`
// 					)
// 					phoneNumber[0].insertAdjacentHTML(
// 						"afterend",
// 						`<small class="px-2 text-danger">${
// 							data.errors.phone_Number
// 								? data.errors.phone_Number
// 								: ""
// 						}</small>`
// 					)
// 					email[0].insertAdjacentHTML(
// 						"afterend",
// 						`<small class="px-2 text-danger">${
// 							data.errors.email ? data.errors.email : ""
// 						}</small>`
// 					)
// 				}
// 			})
// 			.catch(err => {
// 				console.log(err)
// 			})
// 	}
// })

const addImageToPost = () => {
	const reader = new FileReader()
	if (uploadedPhoto[0].files[0]) {
		reader.readAsDataURL(uploadedPhoto[0].files[0])
	}
	reader.onload = readerEvent => {
		profile_Photo[0].setAttribute("src", readerEvent.target.result)
	}
	console.log(uploadedPhoto[0].files[0])
}
