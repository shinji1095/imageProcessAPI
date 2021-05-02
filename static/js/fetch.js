 submitFunction = async function(){
    const url = "/process";
    const form = document.getElementById("form");
    const data = new FormData(form);
    const config = {
        method: "POST",
        body: data,
    }

    const res = await fetch(url, config)
    console.log(res)
    //.then(data => data.json())
    const blob = res.blob();
    console.log(blob)
    
}