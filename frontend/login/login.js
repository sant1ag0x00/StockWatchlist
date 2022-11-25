function writeCookie() {
    name = encodeURI(document.getElementById("name").value);
    document.cookie = `username = ${name}`;
    window.location = "/homepage/homepage.html"
    }
function resetCookie() {
    document.cookie = "username=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
}

