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
	if (color === "black") {
		cur_repeater = setInterval(() => {
			console.log("pinging backend");
			getData("setup_state", {player:color, id:game_id}).then(data => {
				console.log(data.ready)
				if (data.ready === "True") {
					console.log("Your turn again");
					clearInterval(cur_repeater);
					cur_repeater = undefined;
					myTurn = true;
					remaining_actions = 8;
				}
			});
		}, 500);
	}
}

const upgradeLookup = {
	"black-ant": "black-squirrel",
	"black-squirrel": "black-swan",
	"black-turtle": "black-monkey",
	"black-monkey": "black-lion",
	"black-bee": "black-fox",
	"black-fox": "black-tiger",
	"black-rabbit": "black-hyena",
	"black-hyena": "black-tiger",
	"black-mouse": "black-shark",
	"black-shark": "black-kangaroo",
	"white-ant": "white-squirrel",
	"white-squirrel": "white-swan",
	"white-turtle": "white-monkey",
	"white-monkey": "white-lion",
	"white-bee": "white-fox",
	"white-fox": "white-tiger",
	"white-rabbit": "white-hyena",
	"white-hyena": "white-tiger",
	"white-mouse": "white-shark",
	"white-shark": "white-kangaroo",
};
async function getData(endpoint, data) {
	const response = await fetch(`http://34.75.42.233:5000/${endpoint}?${Object.keys(data).map(k => `${k}=${data[k]}`).join("&")}`, {
		method: "GET",
	});
	return response.json();
}
async function postData(endpoint, data) {
	const url = `http://34.75.42.233:5000/${endpoint}?${Object.keys(data).map(k => `${k}=${data[k]}`).join("&")}`;
	console.log(url);
	const response = await fetch(url, {
		method: "POST",
	});
	return response.json();
}

let cur_selected = undefined;
let backrank = undefined;
let myTurn = color === "white";
let remaining_upgrades = 6;
let remaining_actions  = myTurn ? 4 : 0;
let cur_repeater = undefined;

const select = function(elem) {
	if (cur_selected)
		cur_selected.classList.remove("selected");
	elem.classList.add("selected");
	cur_selected = elem;
}
const action = function(elem) {
	remaining_actions -= 1;
	if (remaining_actions === 0) {
		document.querySelector("#upgrade").setAttribute("style", `display: none;`);
		document.querySelector(".selected").classList.remove("selected");
		postData("set_pieces", readBoard()).then(d => {
			myTurn = false;
			console.log(d);
			cur_repeater = setInterval(() => {
				getData("setup_state", {player:color, id:game_id}).then(data => {
					if (data.ready) {
						console.log("Your turn again");
						clearInterval(cur_repeater);
						cur_repeater = undefined;
						myTurn = true;
					}
				});
			}, 500);
		});
	}
}
const readBoard = function() {
	const out = {
		id: game_id,
		player: color,
	}
	const rows = ["1", "2"];
	const cols = ["a", "b", "c", "d", "e", "f"];
	rows.forEach(r => {
		cols.forEach(c => {
			out[c+r] = document.querySelector(`#row${r} [data-col="${c}"]`).getAttribute("data-piece").replace(/.{5}-/,"");
		});
	});
	return out;
}

const upgrade_click = function(elem) {
	if (remaining_actions > 0 && remaining_upgrades > 0) {
		select(elem);
		backrank.forEach(e => e.classList.remove("highlight"));
		if (upgradeLookup[elem.getAttribute("data-piece")])
			document.querySelector("#upgrade").setAttribute("style", `position: absolute; top: ${elem.getBoundingClientRect().top}px; left: ${elem.getBoundingClientRect().left}px;`);
		else
			document.querySelector("#upgrade").setAttribute("style", "display: none;");
	}
}
const upgrade = function() {
	cur_selected.setAttribute("data-piece", upgradeLookup[cur_selected.getAttribute("data-piece")]);
	remaining_upgrades -= 1;
	if (!upgradeLookup[cur_selected.getAttribute("data-piece")] || remaining_upgrades === 0)
		document.querySelector("#upgrade").setAttribute("style", `display: none;`);
	action();
}
const unplaced_piece_click = function(elem) {
	if (remaining_actions > 0) {
		document.querySelector("#upgrade").setAttribute("style", `display: none;`);
		select(elem);
		backrank.forEach(e => e.getAttribute("data-piece") || e.classList.add("highlight"));
	}
}
const empty_square_click = function(elem) {
	if (cur_selected && cur_selected.parentElement.classList.contains("piece-pane")) {
		elem.setAttribute("data-piece", cur_selected.getAttribute("data-piece"));
		elem.setAttribute("onclick", "upgrade_click(this);")
		cur_selected.remove();
		cur_selected = undefined;
		backrank.forEach(e => e.classList.remove("highlight"));
		action();
	}
}