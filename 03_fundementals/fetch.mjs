import fetch from "node-fetch";

const res = await fetch("https://api.github.com/users/octocat");
const data = await res.json();
console.log(data);
