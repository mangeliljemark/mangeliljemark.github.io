const playerList = document.querySelector("#player-list ul");
const table = document.querySelector("#table");

// Function to fetch player data from file
function fetchPlayerData() {
	// Add code here to fetch player data from file

}

function fetchMyTeam() {
	// Add code here to fetch my team from file

}



// Function to fetch game results from Svensk Fotboll API
function fetchGameResults() {
	// Add code here to fetch game results from API
}



// Function to generate player list
function generatePlayerList() {
	// Add code here to dynamically generate player list using player data
}

// Function to generate table
function generateTable() {
	// Add code here to dynamically generate table using game results

}

function clear_round_points() {
	// Add code here to clear round points

}


function player_score(player, goals, clean_sheet) {
	// Add code here to calculate player score
  // How to get value from the fields in html?

  const fileUrl = `players/${playerName}.csv`;
  const xhr = new XMLHttpRequest();
  xhr.open("GET", fileUrl);
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      let fileData = xhr.responseText;
      const [oldPlayerName, oldTeamName, oldPosition, oldTotalPoints, oldRoundPoints, oldTotalGoalsScored, oldTotalCleanSheets] = fileData.split(",");
	  if (goals > 0) {
		if (oldPosition == "MV") {
			const newTotalPoints = parseInt(oldTotalPoints) + goals*6;
			const newRoundPoints = parseInt(oldRoundPoints) + goals*6;
		}
		if (oldPosition == "FÖR") {
			const newTotalPoints = parseInt(oldTotalPoints) + goals*6;
			const newRoundPoints = parseInt(oldRoundPoints) + goals*6;
		}
		if (oldPosition == "MID") {
			const newTotalPoints = parseInt(oldTotalPoints) + goals*5;	
			const newRoundPoints = parseInt(oldRoundPoints) + goals*5;	
		}
		if (oldPosition == "ANF") {
			const newTotalPoints = parseInt(oldTotalPoints) + goals*4;
			const newRoundPoints = parseInt(oldRoundPoints) + goals*4;
		}
	  }
	  if (clean_sheet) {
		if (oldPosition == "MV") {
			const newTotalPoints = parseInt(oldTotalPoints) + 4;
			const newRoundPoints = parseInt(oldRoundPoints) + 4;
		}
		if (oldPosition == "FÖR") {
			const newTotalPoints = parseInt(oldTotalPoints) + 4;
			const newRoundPoints = parseInt(oldRoundPoints) + 4;
		}
		if (oldPosition == "MID") {
			const newTotalPoints = parseInt(oldTotalPoints) + 1;	
			const newRoundPoints = parseInt(oldRoundPoints) + 1;	
		}
		if (oldPosition == "ANF") {
			const newTotalPoints = parseInt(oldTotalPoints);
			const newRoundPoints = parseInt(oldRoundPoints);
		}
	}
      const newTotalGoalsScored = parseInt(oldTotalGoalsScored) + goalsScored;
      const newTotalCleanSheets = cleanSheet ? parseInt(oldTotalCleanSheets) + 1 : parseInt(oldTotalCleanSheets);
      const newData = `${oldPlayerName},${oldTeamName},${oldPosition},${newTotalPoints},${newRoundPoints},${newTotalGoalsScored},${newTotalCleanSheets}`;
      const saveXhr = new XMLHttpRequest();
      saveXhr.open("PUT", fileUrl);
      saveXhr.send(newData);
    }
  };
  xhr.send();
}

function add_player(playerName, teamName, position) {
	// Add code here to add player
  const fileUrl = `players/${playerName}.csv`;
  const fileData = `${playerName},${playerTeam},${position},0,0,0,0`;
  const xhr = new XMLHttpRequest();
  xhr.open("POST", fileUrl);
  xhr.setRequestHeader("Content-Type", "text/csv");
  xhr.send(fileData);
}


function enter_result(homeTeam, awayTeam, homeGoals, awayGoals) {
	// Add code here to enter result
	if (result_authority(username)) {
		var result = prompt("Enter result for " + homeTeam + " - " + awayTeam + ":");

	}
	else; {
		alert("You are not authorized to enter results.");
		return 
	}
}


function result_authority(username) {
	// Add code here to enter result
	return (username == "admin");
}

// Call fetchPlayerData and generatePlayerList functions
fetchPlayerData();
generatePlayerList();

// Call fetchGameResults and generateTable functions every 10 minutes
setInterval(() => {
	fetchGameResults();
	generateTable();
}, 600000);
