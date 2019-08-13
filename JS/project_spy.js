alert("Welcome to the website!");

var first_name = prompt("First name, please: ");
var last_name = prompt("Last name, please: ");
var age = prompt("How old are you? ");
var tall = prompt("How tall in centimeters are you? ");
var pet = prompt("Pet's name, please: ");

if (
  first_name[0] === last_name[0] &&
  20 > age < 30 &&
  tall >= 170 &&
  pet[pet.length - 1] === "y"
) {
  console.log("Welcome back, Conrade!!");
} else {
  console.log("Sorry, we do not recognize you!");
}
