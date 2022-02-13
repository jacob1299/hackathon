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
			getData("setup_state", {player:color, id:game_id}).then(data => {
				console.log(`My turn: ${data.ready}`)
				if (data.ready === "True") {
					update_board(data);
					clearInterval(cur_repeater);
					cur_repeater = undefined;
					myTurn = true;
					document.querySelector("#status").innerHTML = "Place/upgrade your pieces";
					remaining_actions = 8;
				}
			});
		}, 1000);
	}
	document.querySelector("#status").innerHTML = (color === "white" ? "Place/upgrade your pieces" : "Wait for opponent");
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
	const response = await fetch(`http://${window.location.hostname}:5000/${endpoint}?${Object.keys(data).map(k => `${k}=${data[k]}`).join("&")}`, {
		method: "GET",
	});
	return response.json();
}
async function postData(endpoint, data) {
	const url = `http://${window.location.hostname}:5000/${endpoint}?${Object.keys(data).map(k => `${k}=${data[k]}`).join("&")}`;
	console.log(url);
	const response = await fetch(url, {
		method: "POST",
	});
	return response.json();
}
const get_div = function(square) {
	return document.querySelector(`#row${square[1]} > [data-col="${square[0]}"]`);
}
const get_coords = function(elem) {
	return elem.getAttribute("data-col") + elem.parentElement.id.substring(3);
}
const update_board = function(data) {
	const rows = ["1", "2", "3", "4", "5", "6"];
	const cols = ["a", "b", "c", "d", "e", "f"];
	rows.forEach(r => {
		cols.forEach(c => {
			get_div(c+r).setAttribute("data-piece", data[c+r]);
		});
	});
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
		document.querySelectorAll(".selected").forEach(e => e.classList.remove("selected"));	//only one but maybe zero
		postData("set_pieces", readBoard()).then(d => {
			myTurn = false;
			document.querySelector("#status").innerHTML = "Wait for opponent";
			cur_repeater = setInterval(() => {
				getData("setup_state", {player:color, id:game_id}).then(data => {
					console.log(`My turn: ${data.ready}`)
					if (data.ready === "True") {
						update_board(data);
						clearInterval(cur_repeater);
						cur_repeater = undefined;
						myTurn = true;
						if (donePlacing()) {
							initGame();
							document.querySelector("#status").innerHTML = "Your move";
						}
						else {
							document.querySelector("#status").innerHTML = "Place/upgrade your pieces";
							remaining_actions = color === "white" ? 8 : 4;
						}
					}
				});
			}, 500);
		});
	}
}
const donePlacing = function() {
	return remaining_upgrades === 0 && document.querySelector("#self > .piece-pane").childElementCount === 0;
}
const readBoard = function() {
	const out = {
		id: game_id,
		player: color,
	}
	const rows = color==="white" ? ["1", "2"] : ["5", "6"];
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


let moves = undefined;
const initGame = function() {
	console.log("game start");
	cur_selected = undefined;
	const rows = ["1", "2", "3", "4", "5", "6"];
	const cols = ["a", "b", "c", "d", "e", "f"];
	rows.forEach(r => {
		cols.forEach(c => {
			get_div(c+r).setAttribute("onclick", "gameClick(this);");
		});
	});
	cur_repeater = setInterval(waitTurn, 1000);
}
const waitTurn = function() {
	getData("my_move", {
		id: game_id,
		player: color,
	}).then(data => {
		console.log(`My game turn: ${data.turn}`)
		if (data.turn == "True") {
			clearInterval(cur_repeater);
			moves = data.moves;
			myTurn = true;
			update_board(data.board);
		}
	});
}
const gameClick = function(elem) {
	if (myTurn) {
		if (cur_selected && cur_selected == elem) {	//click piece again, deselect
			cur_selected = undefined;
			elem.classList.remove("selected");
			remove_highlights();
		}
		else if (elem.classList.contains("highlight")) {	//make a move
			postData("move", {
				id: game_id,
				from: get_coords(cur_selected),
				to: get_cords(elem),
			}).then(data => {
				moves = undefined;
				myTurn = false;
				cur_selected.classList.remove("selected");
				cur_selected = undefined;
				remove_highlights();
				cur_repeater = setInterval(waitTurn, 1000);
			})
		}
		else if (elem.getAttribute("data-piece").includes(color)) {	//select piece
			select(elem);
			highlight_moves(elem);
		}
	}
}
const highlight_moves = function(elem) {
	moves.filter(m => m.from == get_coords(elem)).forEach(m => get_div(m.to).classList.add("highlight"));
}
const remove_highlights = function() {
	document.querySelectorAll(".row > .square").forEach(e => e.classList.remove("highlight"));
}