const render = function() {
	let html = "";
	const rows = color === "white" ? [6,5,4,3,2,1] : [1,2,3,4,5,6];
	const rowHTML = ["a","b","c","d","e","f"].map(c => `<div class="square" data-piece="" data-col="${c}"></div>`).join("")
	document.querySelector("#board").innerHTML = rows.map(i => `<div id="row${i}" class="row">${rowHTML}</div>`).join("");

	document.querySelectorAll("#row2 > .square").forEach(e => e.setAttribute("data-piece", "white-squirrel"));
	document.querySelectorAll("#row5 > .square").forEach(e => e.setAttribute("data-piece", "black-squirrel"));

	const toPlaceHTML = ["turtle", "bee", "bee", "rabbit", "rabbit", "mouse"].map(a => `<div class="square" data-piece="%color%-${a}" onclick="%onclick%"></div>`).join("");
	document.querySelector("#self > .piece-pane").innerHTML = toPlaceHTML.replaceAll("%color%", color).replaceAll("%onclick%", "unplaced_piece_click(this);");
	document.querySelector("#enemy > .piece-pane").innerHTML = toPlaceHTML.replaceAll("%color%", color === "white" ? "black" : "white").replaceAll("%onclick%", "");
}
const upgrade_click = function() {

}
const unplaced_piece_click = function(elem) {
	elem.classList.add("selected");
	document.querySelectorAll(" > ").forEach(e => {

	});
}