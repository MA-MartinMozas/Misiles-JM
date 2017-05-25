
  $(document).ready(function () {
    //change example.com with your IP or your host
    var ws = new WebSocket("ws://localhost:8888/ws");
    ws.onopen = function(evt) {
      var conn_status = document.getElementById('conn_text');
      conn_status.innerHTML = "Connection status: Connected!"
    };
    ws.onmessage = function(evt) {
      var newMessage = document.createElement('p');
      var obj = JSON.parse(evt.data);
//      creamos una variable llamando al marcador del diccionario por lo que unimos el valor a esa variable
      var Rex = obj.Rex
      document.getElementById("Rex").innerHTML = Rex;
//      var supcil = obj.supcil
//      document.getElementById("supcil").innerHTML = supcil;
//      var supcil = obj.supref
//      document.getElementById("supref").innerHTML = supref;


    };
    ws.onclose = function(evt) {
      alert ("Connection closed");
    };
    $("#button2").click(function(evt) {
      evt.preventDefault();
//        aqui tenemos que meter tantas variables como inputs tenemos que introducir
      var d = $("#d").val();
      var M = $("#M").val();
      var rho = $("#rho").val();
      var a = $("#a").val();
      var mu= $("#mu").val();
      var la = $("#la").val();
      var lx = $("#lx").val();
      var lc = $("#lc").val();
      var ln = $("#ln").val();
      var b = $("#b").val();
      var c = $("#c").val();
      var lt = $("#lt").val();
      var xe = $("#xe").val();
      var lmaxu = $("#lmaxu").val();
      var lflatu = $("#lflatu").val();
      var xcanard = $("#xcanard").val();
      var lrd = $("#lrd").val();
      var mfuselaje = $("#mfuselaje").val();
      var mcabeza = $("#mcabeza").val();
      var maletas = $("#maletas").val();
      var mcanard = $("#mcanard").val();
      var Cnalphabeta = $("#Cnalphabeta").val();





      <!--With this line the dict format is constructed-->
      <!--note that the ` is crucial-->
//      dentro del str tenemos que meter el marcador de la variable y sera igual a la variable que hemos definido anteriormente y que se asocia a su input

      var str1 = `{"d": "${d}", "M": "${M}", "rho": "${rho}", "a": "${a}", "mu": "${mu}", "la": "${la}","lx": "${lx}","lc": "${lc}","ln": "${ln}",
      "b": "${b}","c": "${c}","lt": "${lt}","xe": "${xe}","lmaxu": "${lmaxu}","lflatu": "${lflatu}","xcanard": "${xcanard}","lrd": "${lrd}","mfuselaje": "${mfuselaje}","mcabeza": "${mcabeza}",
      "maletas": "${maletas}","mcanard": "${mcanard}","Cnalphabeta": "${Cnalphabeta}"}`;
      ws.send(str1);
//      var newMessage = document.createElement('p');
//      newMessage.textContent = "Client: " + message;
//      document.getElementById('messages_txt').appendChild(newMessage);

    });
  });