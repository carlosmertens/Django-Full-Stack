// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = [];

// Create the functions for the tasks

// ADD A NEW STUDENT

// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array

function addNew() {
  roster.push(prompt("Name to add: "));
}

// REMOVE STUDENT

// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster

// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//

function remove() {
  var index = roster.indexOf(prompt("Name to remove: "));
  roster.splice(index, 1);
}

// DISPLAY ROSTER

// Create a function called display that prints out the roster to the console.

function display() {
  console.log(roster);
}

// Start by asking if they want to use the web app

var start = prompt("Do you want to use the web? y/n");

// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.

var action = "";

if (start === "y") {
  while (action !== "quit") {
    action = prompt("To do: add, remove, display or quit?");
    if (action === "add") {
      addNew();
    } else if (action === "remove") {
      remove();
    } else if (action === "display") {
      display();
    } else {
      alert("No action selected!");
      action = "quit";
    }
  }
}

alert("Good bye and we hope to see you soon!!!");
