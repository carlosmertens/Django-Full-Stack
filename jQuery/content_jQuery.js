// Action when click on an element
$("h1").click(function() {
  console.log("There was a click");
  $(this).text("I was clicked and changed!!!");
});

$("li").click(function() {
  console.log("Any li element was clicked");
});

// Action when we press a key from the keyword
// event.which === 13 is the 'enter' keyword
$("input")
  .eq(0)
  .keypress(function(event) {
    $("h3").toggleClass("turnBlue");
    if (event.which === 13) {
      $("h3").toggleClass("turnRed");
    }
  });

// Method on() - Works like the even listener in 'vanilla' JS
$("h1").on("dblclick", function() {
  $(this).toggleClass("turnRed");
});

$("h2").on("mouseenter", function() {
  $(this).toggleClass("turnBlue");
});

// Use animation fro jQuery
$("input")
  .eq(1)
  .on("click", function() {
    $(".container").fadeOut(3000);
  });
