const API_KEY = "d1LHp8sB2wASjEtxYv5bmxbqE2RtFquj2DIvFZ2K";
const url = `https://api.nasa.gov/planetary/apod?api_key=${API_KEY}`;


fetch(url)
  .then(res => res.json())
  .then(data => {
    const c = document.getElementById("content");
    if(data.media_type === "image"){
       c.innerHTML = `<h2>${data.title}</h2><img src="${data.url}" width="80%"> <p>${data.explanation}</p>`;
    } else {
       c.innerHTML = `<h2>${data.title}</h2><iframe width="560" height="315" src="${data.url}" frameborder="0" allowfullscreen></iframe><p>${data.explanation}</p>`;
    }
  });
