window.onload = () => {
	$.ajax({
		type: "GET",
		url: "/ajax/commiteeMembersInfo",
		success: response => {
			commiteeMembers = response.commitee_members
			var table = document.getElementsByClassName(
				"dashboard-commitee-member-table"
			)
			console.log(commiteeMembers[0])
			commiteeMembers.map(
				member =>
					(table[0].innerHTML += `
				<tr>
				<td><a href="/admin/members/member/${member.id}/change">${member.name}</a></td>
				<td>${member.position}</td>
				<td><span class="tag tag-success">${member.from_Date}</span></td>
			</tr>
				`)
			)
		},
		error: error => {
			console.log(error)
		},
	})
}
