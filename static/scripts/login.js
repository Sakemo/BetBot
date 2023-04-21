function conect() {
 // Definindo Conta Principal
 var username = document.getElementById("main_ac").value;
 var password = document.getElementById("main_pass").value;
 var telegram = document.getElementById("telegram").value;
 
 // Verificar se as credenciais foram preenchidas
 if (username && password && telegram) {
   // Mostrar spinner durante 15 segundos
   var spinner = document.createElement("div");
   spinner.classList.add("container");
   spinner.innerHTML = `
     <div class="canvas canvas4">
       <div class="spinner4"></div>   
     </div>
   `;
   document.body.appendChild(spinner);
   setTimeout (function() {
     spinner.remove(), 15000;
     // Mostrar mensagem de sucesso
     let btn = document.getElementById('con_1');
     btn.disabled = true;
     btn.value = 'Carregando...';
     setTimeout(function() {
       btn.value = 'Conectado';
       btn.disabled = false;
     }, 15000);
   })
   document.getElementById("main_ac").disabled = true;
   document.getElementById("main_pass").disabled = true;
   document.getElementById("telegram").disabled = true;
   document.getElementById("con_1").disabled=true;
   document.getElementById("con_1").style.opacity = "0.5";
   
   // Enviar solicitação AJAX para o servidor Python
   $.ajax({
     url: '/login/conect',
     type: 'POST',
     data: {username: username, password: password, telegram: telegram},
     success: function(response) {
       console.log(response);
     }
   });
 } else {
   // Mostrar mensagem de erro
   let btn = document.getElementById('con_1');
   btn.disabled = true;
   btn.value = 'Erro: Insira credenciais';
   setTimeout(function() {
     btn.value = 'Conectar';
     btn.disabled = false;
   }, 5000);
 }
}

function conect_2() {
 // Contas de Scrapper
 // Conta 1
 var user_2 = document.getElementById("ac_2").value;
 var pass_2 = document.getElementById("ps_2").value;
 
 if (document.getElementById("con_1").disabled){
  // Verificar se as credenciais foram preenchidas
  if (user_2 === "" || pass_2 === "") {
    // Mostrar mensagem de erro
    let btn = document.getElementById('con_2');
    btn.value = 'Insira Credenciais';
    setTimeout(function() {
      btn.value = 'Conectar';
    }, 1000);
  } else {
    // Mostrar mensagem de carregando
    let btn = document.getElementById('con_2');
    btn.disabled = true;
    btn.value = 'Carregando...';
    setTimeout(function() {
      btn.value = 'Conectado';
    }, 15000);
    
    btn.disabled = false;
    document.getElementById("ac_2").disabled = true;
    document.getElementById("ps_2").disabled = true;
    document.getElementById("con_2").disabled=true;
    document.getElementById("con_2").style.opacity = "0.5";

    // Enviar solicitação AJAX para o servidor Python
    $.ajax({
      url: '/login/conect_2',
      type: 'POST',
      data: {user_2: user_2, pass_2: pass_2},
      success: function(response) {
        console.log(response);
      }
    });
  }}
  else{
   // Mostrar mensagem de erro
   let btn = document.getElementById('con_2');
   btn.disabled = true;
   btn.value = 'Conecte a conta principal primeiro';
   setTimeout(function() {
     btn.value = 'Conectar';
     btn.disabled = false;
   }, 1000);
  }
}

function conect_3() {
 // Conta 2
 var user_3 = document.getElementById("ac_3").value;
 var pass_3 = document.getElementById("ps_3").value;
 
 // Verificar se a função conect() foi executada com sucesso
 if (document.getElementById("con_1").disabled) {
  // Verificar se as credenciais foram preenchidas
  if (user_3 === "" || pass_3 === "") {
    // Mostrar mensagem de erro
    let btn = document.getElementById('con_3');
    btn.value = 'Insira Credenciais';
    setTimeout(function() {
      btn.value = 'Conectar';
    }, 1000);
  } else {
    // Mostrar mensagem de carregando
    let btn = document.getElementById('con_3');
    btn.disabled = true;
    btn.value = 'Carregando...';
    setTimeout(function() {
      btn.value = 'Conectado';
    }, 15000);

    btn.disabled = false;
    document.getElementById("ac_3").disabled = true;
    document.getElementById("ps_3").disabled = true;
    document.getElementById("con_3").disabled=true;
    document.getElementById("con_3").style.opacity = "0.5";

    // Enviar solicitação AJAX para o servidor Python
    $.ajax({
      url: '/login/conect_3',
      type: 'POST',
      data: {user_3: user_3, pass_3: pass_3},
      success: function(response) {
        console.log(response);
      }
    });
  }}else {
   // Mostrar mensagem de erro
   let btn = document.getElementById('con_3');
   btn.disabled = true;
   btn.value = 'Conecte a conta principal primeiro';
   setTimeout(function() {
     btn.value = 'Conectar';
     btn.disabled = false;
   }, 1000);
 }
}