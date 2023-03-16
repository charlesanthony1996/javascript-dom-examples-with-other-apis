// Define the number of disks and towers
const NUM_DISKS = 3;
const NUM_TOWERS = 3;

// Define the initial state of the towers
const towers = [[3, 2, 1], [], []];

// Define a function to print the current state of the towers
function printTowers() {
  console.log("+---+   +---+   +---+");
  for (let i = NUM_DISKS - 1; i >= 0; i--) {
    let row = "";
    for (let j = 0; j < NUM_TOWERS; j++) {
      const disk = towers[j][i] || " ";
      row += `| ${disk} |   `;
    }
    console.log(row);
  }
  console.log("+---+   +---+   +---+");
  console.log();
}

// Define a recursive function to solve the problem
function moveDisks(numDisks, source, dest, temp) {
  if (numDisks === 1) {
    towers[dest].push(towers[source].pop());
    printTowers();
  } else {
    moveDisks(numDisks - 1, source, temp, dest);
    moveDisks(1, source, dest, temp);
    moveDisks(numDisks - 1, temp, dest, source);
  }
}

// Call the function to solve the problem
printTowers();
moveDisks(NUM_DISKS, 0, 2, 1);
