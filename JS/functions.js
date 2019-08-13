function hello(name = "Carlos") {
  console.log("Hello world and " + name + "!");
}

function addNumber(num1, num2) {
  console.log(num1 + num2);
}

// Return key in order to not just print it but use it
function formalName(name = "Edgar", title = "Sir") {
  // Create local scope variable
  var space = " ";
  return title + space + name;
}

// Call action when page is loaded
hello();
console.log("Hey, there!");
