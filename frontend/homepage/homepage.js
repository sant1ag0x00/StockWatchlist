async function fetchData(url){
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
    console.log(fetchData(`http://0.0.0.0:8080/${name}`));
    return name;
}
