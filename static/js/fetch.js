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
    const blob = await res.blob();
    const reader = new FileReader();
    const imageField = document.getElementById("imageField");
    reader.onload = (e) => {
        imageField.src = e.target.result;
    }
    reader.readAsDataURL(blob);
}