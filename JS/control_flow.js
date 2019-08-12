var ham = prompt("How much ham was sold? ");
var cheese = prompt("How much cheese was sold? ");
var report = "blank";

if (ham >= 10 && cheese >= 10) {
  report = "Strong sales of both ham and cheese!";
} else if (ham === 0 && cheese === 0) {
  report = "Someone needs to get fire!";
} else {
  report = "Sales can be improved!";
}

alert(report);
console.log(report);
