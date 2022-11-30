async function fetchData(url) {
    const response = await fetch(url);
    var data = await response.json();
    return data;
}

function getStocklist() {
    const value = `; ${document.cookie}`;
    const parts = value.split("; username=");

    if (parts.length === 2) {
        let name = parts.pop().split(';').shift();
    }
    data = fetchData(`http://0.0.0.0:8080/stocklist/${name}`);
    //console.log(data)
    return data;
}

function appendData(data) {
    var mainContainer = document.getElementById("myData");
    for (var i = 0; i < data.length; i++) {
      var div = document.createElement("div");
      div.innerHTML = 'Name: ' + data[i].data.name;
      mainContainer.appendChild(div);
    }
  }
async function convertStocklist(){
    data = getStocklist();
	let responseArr = [];
	await data.then(value => {responseArr.concat(Object.entries(value))});
	console.log(responseArr);
    return responseArr.then(value => {console.log(value)})
}
function Sleep(milliseconds) {
    return new Promise(resolve => setTimeout(resolve, milliseconds));
}