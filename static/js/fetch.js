 submitFunction = function(){
    const url = "/process";
    const form = document.getElementById("form");
    const data = new FormData(form);
    const config = {
        method: "POST",
        body: data,
    }

    fetch(url, config)
    .then(data => data.json())
    .then(binary => {
        console.log(binary)
    })
    .catch(e => {
        console.log(e)
    })
}