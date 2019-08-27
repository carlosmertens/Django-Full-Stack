// Clear all squares function
var squares = document.querySelectorAll("td");

function clearBoard() {
  for (var i = 0; i < squares.length; i++) {
    squares[i].textContent = "";
  }
}

// Start Again!!! - Button
var restart = document.querySelector("#restart-button");

restart.addEventListener("click", clearBoard);

// Pick your game
function pickGame() {
  if (this.textContent === "") {
    this.textContent = "x";
  } else if (this.textContent === "x") {
    this.textContent = "o";
  } else {
    this.textContent = "";
  }
}

for (var i = 0; i < squares.length; i++) {
  squares[i].addEventListener("click", pickGame);
}
