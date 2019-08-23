// Let's type this into the console, follow along with the video lecture

var x = document.querySelector("p");

// Show Text
//x.textContent;

// Reassign Text
function changeParagraph() {
  x.textContent = "Uppssss!!! What is happening in this web???";
}

setInterval("changeParagraph()", 3000);

// Refresh the page
// Show actual HTML
//x.innerHTML;

// Edit HTML
function changeBold() {
  // Can't do that with just textContent
  x.innerHTML = "<strong>Again!!! What is happening in this web???</strong>";
}

setInterval("changeBold()", 4000);

/////////////////
// Attributes //
///////////////

var special = document.querySelector("#special");
var specialA = special.querySelector("a");

//specialA.getAttribute("href");

function changeLink() {
  specialA.setAttribute("href", "https://www.amazon.com");
  specialA.textContent = "AMAZON LINK";
}

setInterval("changeLink()", 6000);
