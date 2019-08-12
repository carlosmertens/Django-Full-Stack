// While Loops
console.log("WHILE LOOPS ***");

var x = 0;

while (x < 5) {
  console.log("x is currently: " + x);
  console.log("x is still less than 5, adding 1 to x");

  x = x + 1;
}

var i = 0;

while (i < 10) {
  console.log("Number is: " + i);
  if (i === 7) {
    console.log("It works, lets break now!");
    break;
  }
  i++; // or i += 1
}

// For Loops
console.log("FOR LOOPS ***");

var word = "ABCDEFGHIJK";
for (var i = 0; i < word.length; i++) {
  console.log(word[i]);
}
