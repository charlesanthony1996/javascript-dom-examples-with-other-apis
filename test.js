let num = 3
let towerA = []
let towerB = []
let towerC = []

for(let i = num; i > 0; i--) {
    result = towerA.push("*".repeat(i))
    // console.log(towerA)
    // last step gives you that towerA has all stars
}

function printTowers() {
    console.log("Tower A " + towerA.join(" "))
    console.log("Tower B " + towerB.join(" "))
    console.log("Tower C:" + towerC.join(" "))
    console.log("\n")
}

function moveDisk(from, to) {
    to.push(from.pop())
    printTowers()
}

function hanoi(n, source, target, auxiliary) {
    if(n > 0) {
        hanoi(n - 1, source, auxiliary, target)
        moveDisk(source, target)
        hanoi(n- 1, auxiliary, target, source)
    }
}

// printTowers()
// order of hanoi is really important
// discusses the role of each tower

hanoi(3, towerA, towerC, towerB)
printTowers()