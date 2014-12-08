//Make query string for tag information
function searchTag(form) {
	var tag = form.tag.value;
	window.location.href = "/CaseList?tag=" + encodeURIComponent(tag);
}

//Checks all check boxes
function checkAll() {
	var myCheckBoxes = document.getElementsByTagName('input');

	for (var i = 0, n = myCheckBoxes.length; i < n; i++)
		if ( myCheckBoxes[i].type == 'checkbox' ) {
			myCheckBoxes[i].checked = true;
			myCheckBoxes[i].parentNode.style.backgroundColor = "#FFC266";
		}
}

//Unchecks all check boxes
function checkNone() {
	var myCheckBoxes = document.getElementsByTagName('input');

	for (var i = 0, n = myCheckBoxes.length; i < n; i++)
		if ( myCheckBoxes[i].type == 'checkbox' ) {
			myCheckBoxes[i].checked = false;
			myCheckBoxes[i].parentNode.style.backgroundColor = "#EEEEEE";
		}
}

//Creates query based divs of class scans that have orange background
//Not used at the moment
function viewSelected() {
	var myScans = document.querySelectorAll("label.scan");
	var selectedScans = [];
	
	for (var i = 0, n = myScans.length; i < n; i++)
		if (myScans[i].style.backgroundColor === hexToRgb("#FFC266") )
			for (var o = 0, m = myScans[i].childNodes.length; o < m; o++)
				selectedScans.push(myScans[i].childNodes[o]);
	
	var test = "";
	for (var i = 0, n = selectedScans.length; i < n; i++)
	 test += selectedScans[i].text + '\n';
	 
	alert(test);
	
	if ( selectedScans.length === 0 ) {
		alert("Error: No cases selected.");
	} else {
		//var queryString = "";
		
		//for (var i = 0, n = selectedScans.length; i < n; i++)
			//queryString += "id[]=" + selectedScans[i] + "&";
		
		//queryString = queryString.substring(0, queryString.length - 1);
		//window.location.href = "\Case?" + encodeURIComponent(queryString);
	}
	
}

//Change element background to orange
function toggleBGColor(caseID) {
	if (caseID.parentNode.style.backgroundColor === "") 
		caseID.parentNode.style.backgroundColor = "#EEEEEE";
	
	if ( caseID.parentNode.style.backgroundColor === hexToRgb("#EEEEEE") )
		caseID.parentNode.style.backgroundColor = "#FFC266";
	else 
		caseID.parentNode.style.backgroundColor = "#EEEEEE";    
}

//Convert hex string to RGB format
function hexToRgb(hex) {
	var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
	result = {
		r: parseInt(result[1], 16),
		g: parseInt(result[2], 16),
		b: parseInt(result[3], 16)
	};
	return "rgb(" + result.r + ", " + result.g + ", " + result.b + ")";
}