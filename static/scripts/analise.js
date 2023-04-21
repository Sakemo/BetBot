var tableData = [];
var selectedCell;
var savedData = JSON.parse(localStorage.getItem("savedData")) || {};

function showOptions() {
  var options = document.getElementById("options");
  if (options.style.display === "none") {
    options.style.display = "block";
  } else {
    options.style.display = "none";
  }
}

function showOptions2() {
  var options2 = document.getElementById("options2");
  if (options2.style.display === "none") {
    options2.style.display = "block";
  } else {
    options2.style.display = "none";
  }
}

function changeText(text) {
  var square = document.getElementsByClassName("square")[0];
  square.innerHTML = text;
  savedData.selectedOption = text;
  localStorage.setItem("savedData", JSON.stringify(savedData));
}

function changeText2(text) {
  var square2 = document.getElementsByClassName("square2")[0];
  square2.innerHTML = text;
  savedData.selectedOption2 = text;
  localStorage.setItem("savedData", JSON.stringify(savedData));
}

function selectCell(cell) {
  if (selectedCell) {
    selectedCell.style.border = "1px solid black";
  }
  selectedCell = cell;
  selectedCell.style.border = "2px solid var(--lg_yellow)";
}

function saveText2() {
  var name = document.getElementById("name").value;
  var selectedOption = document.getElementsByClassName("square")[0].innerHTML;
  var selectedOption2 = document.getElementsByClassName("square2")[0].innerHTML;
  if (selectedOption === "Tipo" || selectedOption === "Padrão") {
    selectedCell.style.backgroundColor = "#FDBD0F";
    if (selectedOption2 == "Casa Vence") {
      tableData.push(10);
    } else if (selectedOption2 == "Empate") {
      tableData.push(11);
    } else if (selectedOption2 == "Fora Vence") {
      tableData.push(12);
    } else if (selectedOption2 == "AM | Sim") {
      tableData.push(13);
    } else if (selectedOption2 == "AM | Não") {
      tableData.push(14);
    } else if (selectedOption2 == "Over 0.5") {
      tableData.push(15);
    } else if (selectedOption2 == "Over 1.5") {
      tableData.push(16);
    } else if (selectedOption2 == "Over 2.5") {
      tableData.push(17);
    } else if (selectedOption2 == "Over 3.5") {
      tableData.push(18);
    } else if (selectedOption2 == "PM | Casa") {
      tableData.push(19);
    } else if (selectedOption2 == "PM | Fora") {
      tableData.push(110);
    }
  } else {
    selectedCell.style.backgroundColor = "#126E51";
    if (selectedOption2 == "Casa Vence") {
      tableData.push(20);
    } else if (selectedOption2 == "Empate") {
      tableData.push(21);
    } else if (selectedOption2 == "Fora Vence") {
      tableData.push(22);
    } else if (selectedOption2 == "AM | Sim") {
      tableData.push(23);
    } else if (selectedOption2 == "AM | Não") {
      tableData.push(24);
    } else if (selectedOption2 == "Over 0.5") {
      tableData.push(25);
    } else if (selectedOption2 == "Over 1.5") {
      tableData.push(26);
    } else if (selectedOption2 == "Over 2.5") {
      tableData.push(27);
    } else if (selectedOption2 == "Over 3.5") {
      tableData.push(28);
    } else if (selectedOption2 == "PM | Casa") {
      tableData.push(29);
    } else if (selectedOption2 == "PM | Fora") {
      tableData.push(210);
    }
  }
  selectedCell.innerHTML = selectedOption2;
  //console.log(tableData);
  var data = JSON.stringify(tableData);
  console.log(data);

  var league1 = "";
  var league2 = "";
  var league3 = "";
  var league4 = "";
  var checkboxes = document.querySelectorAll(
    '.league input[type="checkbox"]:checked'
  );
  for (var i = 0; i < checkboxes.length; i++) {
    if (i === 0) {
      league1 = checkboxes[i].value;
    } else if (i === 1) {
      league2 = checkboxes[i].value;
    } else if (i === 2) {
      league3 = checkboxes[i].value;
    } else if (i === 3) {
      league4 = checkboxes[i].value;
    }
  }
  console.log(name);
  console.log(selectedOption);
  console.log(selectedOption2);
  console.log(selectedCell);
  console.log("League 1: " + league1);
  console.log("League 2: " + league2);
  console.log("League 3: " + league3);
  console.log("League 4: " + league4);
  savedData.league1 = league1;
  savedData.league2 = league2;
  savedData.league3 = league3;
  savedData.league4 = league4;
  localStorage.setItem("savedData", JSON.stringify(savedData));

  // Enviar solicitação AJAX para o servidor Python
  $.ajax({
    url: "/bot/aposta",
    type: "POST",
    data: { array: data, 
        league1: league1, 
        league2: league2, 
        league3: league3, 
        league4:  league4},
    success: function (response) {
      console.log(response);
    },
  });
}

document.addEventListener("click", function (event) {
  if (selectedCell && !selectedCell.contains(event.target)) {
    selectedCell.style.border = "1px solid black";
  }
});

function reset() {
  var cells = document.getElementsByTagName("td");
  for (var i = 0; i < cells.length; i++) {
    cells[i].innerHTML = "";
    cells[i].style.backgroundColor = "white";
  }
  localStorage.removeItem("savedData");
}
