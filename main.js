function hanoi(n, source, target, auxiliary) {
    // Base case: when there are no more disks to move, stop the recursion
    if (n > 0) {
      // Step 1: Move the n-1 smaller disks from the source peg to the auxiliary peg,
      // using the target peg as temporary storage
      hanoi(n - 1, source, auxiliary, target);
  
      // Step 2: Print the move for the current disk (the largest one) from the source peg to the target peg
      printMove(n, source, target);
  
      // Step 3: Move the current disk (the largest one) from the source peg to the target peg
      moveDisk(source, target);
  
      // Step 4: Display the current state of the towers
      displayTowers();
  
      // Step 5: Move the n-1 smaller disks from the auxiliary peg to the target peg,
      // using the source peg as temporary storage
      hanoi(n - 1, auxiliary, target, source);
    }
  }
  
  
  function printMove(n, source, target) {
    console.log(`Move disk ${n} from ${source} to ${target}`);
  }
  
  function moveDisk(source, target) {
    // Remove the top disk from the source tower
    const topDisk = towers[source].pop();
  
    // Add the top disk to the target tower
    towers[target].push(topDisk);
  }
  
  
  function displayTowers() {
    // Step 1: Create the ASCII art representation of the current state of the towers
    const output = createTowerOutput();
  
    // Step 2: Print the ASCII art representation to the console
    console.log(output);
  }
  
  
  function createTowerOutput() {
    // Step 1: Get the maximum height of the towers
    const maxHeight = getMaxTowerHeight(towers);
  
    // Initialize an empty string for the output
    let output = "";
  
    // Step 2: Iterate through the rows of the towers from top to bottom
    for (let i = maxHeight - 1; i >= 0; i--) {
      // Step 3: Create an ASCII art row for the current row number and append it to the output
      output += createDiskRow(i);
  
      // Step 4: Add a newline character to separate rows
      output += "\n";
    }
  
    // Step 5: Add labels (A, B, C) for the pegs at the bottom of the output
    output += "A      B      C\n";
  
    // Return the final ASCII art representation of the towers
    return output;
  }
  

  function getMaxTowerHeight(towers) {
    // Initialize a variable to store the maximum height
    let maxHeight = 0;
  
    // Iterate through each tower
    for (let i = 0; i < towers.length; i++) {
      // Get the height of the current tower
      const towerHeight = towers[i].length;
  
      // If the current tower's height is greater than the maxHeight, update maxHeight
      if (towerHeight > maxHeight) {
        maxHeight = towerHeight;
      }
    }
  
    // Return the highest tower height after completing the loop
    return maxHeight;
  }
  
  
  
  function createDiskRow(rowNumber) {
    let row = "";
  
    // Iterate through each tower
    for (let towerIndex = 0; towerIndex < 3; towerIndex++) {
      // Check if there is a disk at the current row of the tower
      const diskSize = towers[towerIndex][rowNumber];
  
      if (diskSize !== undefined) {
        // Calculate the number of spaces before and after the asterisks (padding)
        const padding = 3 - diskSize;
  
        // Calculate the number of asterisks needed to represent the disk (diskWidth)
        const diskWidth = 2 * diskSize - 1;
  
        // Add padding spaces, disk asterisks, and padding spaces to the row string
        row += " ".repeat(padding) + "*".repeat(diskWidth) + " ".repeat(padding);
      } else {
        // If there's no disk at the current row, add 5 spaces to represent an empty space
        row += " ".repeat(5);
      }
  
      // Add a space between towers
      row += " ";
    }
  
    // Return the ASCII art row for the current row number
    return row;
  }
  
  
  const numDisks = 3;
  const towers = [
    Array.from({ length: numDisks }, (_, i) => numDisks - i),
    [],
    [],
  ];
  
  console.log("Initial state:");
  displayTowers();
  hanoi(numDisks, 0, 2, 1);
