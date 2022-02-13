const render = function() {
	let html = "";
	const rows = color === "white" ? [6,5,4,3,2,1] : [1,2,3,4,5,6];
	const rowHTML = ["a","b","c","d","e","f"].map(c => `<div class="square" data-piece="" data-col="${c}"></div>`).join("")
	document.querySelector("#board").innerHTML = rows.map(i => `<div id="row${i}" class="row">${rowHTML}</div>`).join("");

	document.querySelectorAll("#row2 > .square").forEach(e => {
		e.setAttribute("data-piece", "white-ant")
		if (color==="white")
			e.setAttribute("onclick", "upgrade_click(this);")
	});
	document.querySelectorAll("#row5 > .square").forEach(e => {
		e.setAttribute("data-piece", "black-ant");
		if (color==="black")
			e.setAttribute("onclick", "upgrade_click(this);")
	});
	backrank = document.querySelectorAll(`#row${color==="white" ? "1" : "6"} > .square`);
	backrank.forEach(e => e.setAttribute("onclick", "empty_square_click(this);"))

	const toPlaceHTML = ["turtle", "bee", "bee", "rabbit", "rabbit", "mouse"].map(a => `<div class="square" data-piece="%color%-${a}" onclick="%onclick%"></div>`).join("");
	document.querySelector("#self > .piece-pane").innerHTML = toPlaceHTML.replaceAll("%color%", color).replaceAll("%onclick%", "unplaced_piece_click(this);");
	document.querySelector("#enemy > .piece-pane").innerHTML = toPlaceHTML.replaceAll("%color%", color === "white" ? "black" : "white").replaceAll("%onclick%", "");
}
let cur_selected = undefined;
let backrank = undefined;
const select = function(elem) {
	if (cur_selected)
		cur_selected.classList.remove("selected");
	elem.classList.add("selected");
	cur_selected = elem;
}
const upgrade_click = function(elem) {
	select(elem);
	document.querySelectorAll(`#row${color==="white" ? "1" : "6"} > .square`).forEach(e => {
		e.classList.remove("highlight");
	});
}
const unplaced_piece_click = function(elem) {
	select(elem);
	backrank.forEach(e => e.getAttribute("data-piece") || e.classList.add("highlight"));
}
const empty_square_click = function(elem) {
	if (cur_selected && cur_selected.parentElement.classList.contains("piece-pane")) {
		elem.setAttribute("data-piece", cur_selected.getAttribute("data-piece"));
		cur_selected.remove();
		cur_selected = undefined;
		backrank.forEach(e => e.classList.remove("highlight"));
	}
}