var martingaleInput = document.getElementById("martingale");
var stopWinInput = document.getElementById("stopwin");
var stopLossInput = document.getElementById("stoploss");
var valorApostaInput = document.getElementById("valoraposta");

var mt = martingaleInput.value = localStorage.getItem("martingale") !== null ? localStorage.getItem("martingale") : "";
var sw = stopWinInput.value = localStorage.getItem("stopwin") !== null ? localStorage.getItem("stopwin") : "";
var sl = stopLossInput.value = localStorage.getItem("stoploss") !== null ? localStorage.getItem("stoploss") : "";
var va = valorApostaInput.value = localStorage.getItem("valoraposta") !== null ? localStorage.getItem("valoraposta") : "";

var saveButton = document.getElementById("sv");
saveButton.addEventListener("click", () => {
 localStorage.setItem("martingale", martingaleInput.value);
 localStorage.setItem("stopwin", stopWinInput.value);
 localStorage.setItem("stoploss", stopLossInput.value);
 localStorage.setItem("valoraposta", valorApostaInput.value);
 console.log(mt, sw,sl,va);

 // AJAX Request
 $.ajax({
  url: '/bot/config',
  type: 'POST',
  data: {martingale: mt, stopwin: sw, stoploss: sl, valor: va},
  success: function(response) {
    console.log(response);
  }
})

});