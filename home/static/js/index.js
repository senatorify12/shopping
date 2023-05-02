

// loader
const container = document.querySelector(".kevin");

window.addEventListener("load", ()=> {
    container.style.display = "none"
});

// light-dark-mood
let body = document.body 
let toggle = document.querySelector(".toggle");
let icon = document.querySelector(".fa-moon");
let iconB = document.querySelector(".dark");

toggle.addEventListener("click", ()=> {
    body.classList.contains("dark")    
    if (body.classList.toggle("dark")) {
        icon.classList.remove("fa-moon");
        icon.classList.add("fa-sun");
    } else {
        icon.classList.remove("fa-sun");
        icon.classList.add("fa-moon");
    }
});

// show and hide password
let icons = document.querySelector(".shower")
let change = document.querySelector(".show");
let changeB = document.querySelector(".grab");

change.addEventListener("click", ()=> {
    change.classList.toggle("shower")
    if (changeB.type === "password") {
        changeB.type = "text";
    } else {
        changeB.type = "password";
    };
});



































































































// toggle.addEventListener("click", ()=> {
//     body.classList.contains("dark")    
//     if (body.classList.toggle("dark")) {
//         icon.classList.replace("fa-moon", "fa-sun");
//     } else {
//         icon.classList.replace("fa-sun", "fa-moon");
//     }
// });




