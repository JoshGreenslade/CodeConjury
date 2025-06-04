function rollDie() {
  return Math.floor(Math.random() * 6) + 1;
}

let player = rollDie();
let opponent = rollDie();

console.log(`You: ${player}, Opponent: ${opponent}`);
console.log(
  player > opponent ? "You win!" : player < opponent ? "You lose!" : "Draw"
);
