const displayFilter = () => {
	const gridCheck = document.getElementById("gridCheck");
	const datafilter = document.getElementById("datafilter");
	console.log("gridheck---- " + gridCheck);
	console.log("datafilter---- " + datafilter);
	if (gridCheck != undefined && gridCheck != undefined) {
		if (gridCheck.checked) {
			datafilter.classList.remove('d-none');
		} else {
			datafilter.classList.add('d-none');
		}
	}
}

const showEditUI = (emailid) => {
	const first_name = document.getElementById("first_name");
	const last_name = document.getElementById("last_name");
	const emailaddr = document.getElementById("emailaddr");
	const orgrole = document.getElementById('m_id_orgrole');
	const approle = document.getElementById('m_id_approle');
	var url = '/getMemberData/';
	fetch(url, {
		method:'GET',
		headers:{
			'Content-Type':'application/json',
			'X-CSRFToken':csrftoken,
			'emailId': emailid,
		},
	})
	.then((response) => {
		return response.json();
	 })
	 .then((jsondata) => {
		//console.log(jsondata)
		memberdata = JSON.parse(jsondata);
		memberfields = memberdata[0].fields;
		first_name.value = `${memberfields.first_name}`;
		last_name.value	= `${memberfields.last_name}`;
		emailaddr.innerHTML	= `${emailid}`;
		selectedval = memberfields.orgrole.filter((val) => val);
		$("#m_id_orgrole").val(selectedval);
		approle.value = `${memberfields.approle}`;
	 })
}

const saveChanges = () => {

	const first_name = document.getElementById("first_name");
	const last_name = document.getElementById("last_name");
	const emailaddr = document.getElementById("emailaddr");
	const approle = document.getElementById('m_id_approle');

	var url = '/updateMemberProfile/';
	fetch(url, {
		method:'POST',
		headers:{
			'Content-Type':'application/json',
			'X-CSRFToken':csrftoken,
		},
		body:JSON.stringify({
			'first_name': first_name.value,
			'last_name': last_name.value,
			'emailaddr': emailaddr.innerHTML,
			'orgrole': $('#m_id_orgrole').val(),
			'approle': approle.value,
		})
	})
	.then((response) => {
		return response.json();
		})
	.then((data) => {
		location.reload()
	});
}

const updateMemberStatus = (emailId, val, message, bodymessage) => {

	const status_label = document.getElementById(`${emailId}_member_status`);
	var url = '/updateMemberStatus/';
	fetch(url, {
		method:'POST',
		headers:{
			'Content-Type':'application/json',
			'X-CSRFToken':csrftoken,
		},
		body:JSON.stringify(bodymessage)
	})
	.then((response) => {
		return response.json();
		})
	.then((data) => {
		status_label.innerHTML = message
		console.log("updated successfully" + data);
	});
}

const setMemberStatus = (emailId) => {
	const member_status = document.getElementById(`${emailId}_member_status`);
	if (member_status.innerHTML === 'Approved' ) {
		updateMemberStatus(emailId, 0, 'Pending_Approval', {"member_status": "0", 'emailaddr': emailId});
	} else {
		updateMemberStatus(emailId, 1, 'Approved', {"member_status": "1", 'emailaddr': emailId});
	}
}

const enableNotification = () => {
	const emailofficer = document.getElementById("emailofficer");
	var url = 'enableNotification/';
	fetch(url, {
		method:'POST',
		headers: {
			'Content-Type':'application/json',
			'X-CSRFToken':csrftoken,
		},
		body:JSON.stringify({
			'notification': emailofficer.checked,
			'regionid' : emailofficer.dataset.regionid,
		})
	}).then(response => {
		console.log(response);
	})
}