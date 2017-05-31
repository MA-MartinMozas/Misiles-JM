
  $(document).ready(function () {
    //change example.com with your IP or your host
    var ws = new WebSocket("ws://localhost:8888/ws");
    ws.onopen = function(evt) {
      var conn_status = document.getElementById('conn_text');
//      conn_status.innerHTML = "Connection status: Connected!"
    };
    ws.onmessage = function(evt) {
      var newMessage = document.createElement('p');
      var obj = JSON.parse(evt.data);

//      creamos una variable llamando al marcador del diccionario por lo que unimos el valor a esa variable
// #Primero, lo realizamos para diseño aerodinámico del misil

      document.getElementById("Rex").innerHTML = obj.Rex;
      document.getElementById("supcil").innerHTML = obj.supcil;
      document.getElementById("supref").innerHTML = obj.supref;
      document.getElementById("supcono").innerHTML = obj.supcono;
      document.getElementById("angucono").innerHTML = obj.angucono;
      document.getElementById("CDWC").innerHTML = obj.CDWC;
      document.getElementById("DWcono").innerHTML = obj.DWcono;
      document.getElementById("anguojiva").innerHTML = obj.anguojiva;
      document.getElementById("CDWO").innerHTML = obj.CDWO;
      document.getElementById("DWojiva").innerHTML = obj.DWojiva;
      document.getElementById("CDfilam").innerHTML = obj.CDfilam;
      document.getElementById("CDfi").innerHTML = obj.CDfi;
      document.getElementById("CDflam").innerHTML = obj.CDflam;
      document.getElementById("Xcgfus").innerHTML = obj.Xcgfus;
      document.getElementById("Xcgcabeza").innerHTML = obj.Xcgcabeza;
      document.getElementById("Xcgaletas").innerHTML = obj.Xcgaletas;
      document.getElementById("Xcgcanard").innerHTML = obj.Xcgcanard;
      document.getElementById("m").innerHTML = obj.m;
      document.getElementById("Xcg").innerHTML = obj.Xcg;
      document.getElementById("Cnalphawing").innerHTML = obj.Cnalphawing;
      document.getElementById("Xcpwing").innerHTML = obj.Xcpwing;
      document.getElementById("Kwb").innerHTML = obj.Kwb;
      document.getElementById("Kbw").innerHTML = obj.Kbw;
      document.getElementById("Cnalpha").innerHTML = obj.Cnalpha;
      document.getElementById("Cmalpha").innerHTML = obj.Cmalpha;
      document.getElementById("h").innerHTML = obj.h;
      document.getElementById("Cndelta").innerHTML = obj.Cndelta;
      document.getElementById("Cmdelta").innerHTML = obj.Cmdelta;
      document.getElementById("Kbm").innerHTML = obj.Kbm;
      document.getElementById("maniobrabilidad").innerHTML = obj.maniobrabilidad;
      document.getElementById("alphasatur").innerHTML = obj.alphasatur;
      document.getElementById("nmaximo").innerHTML = obj.nmaximo;
      document.getElementById("deltamani").innerHTML = obj.deltamani;

// #Segundo, lo realizamos para definir la misión
      document.getElementById("K").innerHTML = obj.K;
      // POR QUÉ ME SALE LA K MORADAAAAAAAAAAAAAAAAAAAAAAAAA?????????????
      document.getElementById("deltati").innerHTML = obj.deltati;
      document.getElementById("etamnm").innerHTML = obj.etamnm;
      document.getElementById("t").innerHTML = obj.t;
      document.getElementById("ri").innerHTML = obj.ri;
      document.getElementById("xt").innerHTML = obj.xt;
      document.getElementById("deltamc").innerHTML = obj.deltamc;
      document.getElementById("incrementdeltam").innerHTML = obj.incrementdeltam;
      document.getElementById("ti").innerHTML = obj.ti;
      document.getElementById("etamncalculado").innerHTML = obj.etamncalculado;








    };
    ws.onclose = function(evt) {
      alert ("Connection closed");
    };
// este boton será el que este en la pag de datos de geometría al pulsarlo se mandan las variables
    $("#button1").click(function(evt) {
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
      var xcanard = $("#xcanard").val();
      var lrd = $("#lrd").val();
      var mfuselaje = $("#mfuselaje").val();
      var mcabeza = $("#mcabeza").val();
      var maletas = $("#maletas").val();
      var mcanard = $("#mcanard").val();
      var Cnalphabeta = $("#Cnalphabeta").val();
      var Cnsat = $("#Cnsat").val();




      <!--With this line the dict format is constructed-->
      <!--note that the ` is crucial-->
//      dentro del str tenemos que meter el marcador de la variable y sera igual a la variable que hemos definido anteriormente y que se asocia a su input

      var str1 = `{"tipo": "geo","d": "${d || "1"}", "M": "${M || "1"}", "rho": "${rho || "1"}", "a": "${a || "1"}", "mu": "${mu || "1"}", "la": "${la || "1"}","lx": "${lx || "1"}","lc": "${lc || "1"}","ln": "${ln || "1"}",
      "b": "${b || "1"}","c": "${c || "1"}","lt": "${lt || "1"}","xe": "${xe || "1"}","lmaxu": "${lmaxu || "1"}","xcanard": "${xcanard || "1"}","lrd": "${lrd || "1"}","mfuselaje": "${mfuselaje || "1"}","mcabeza": "${mcabeza || "1"}",
      "maletas": "${maletas || "1"}","mcanard": "${mcanard || "1"}","Cnalphabeta": "${Cnalphabeta || "1"}","Cnsat": "${Cnsat || "1"}"}`;
      ws.send(str1);
//      var newMessage = document.createElement('p');
//      newMessage.textContent = "Client: " + message;
//      document.getElementById('messages_txt').appendChild(newMessage);

    });

//    este boton será el que este en datos misión y al pulsarlo se mandarán estas variables
    $("#button2").click(function(evt) {
      evt.preventDefault();
//        aqui tenemos que meter tantas variables como inputs tenemos que introducir en mision con el id del input donde lo introducimos
      var etamnnmax = $("#etamnnmax").val();
      var vm = $("#vm").val();
      var vt = $("#vt").val();
      var deltato = $("#deltato").val();
      var ro= $("#ro").val();
      var deltat = $("#deltat").val();
      var deltamo = $("#deltamo").val();
      var etatn = $("#etatn").val();
      var am = $("#am").val();
      var t = $("#t").val();



      <!--With this line the dict format is constructed-->
      <!--note that the ` is crucial-->
//      dentro del str tenemos que meter el marcador de la variable y sera igual a la variable que hemos definido anteriormente y que se asocia a su input

      var str2 = `{"tipo": "mis","etamnnmax": "${etamnnmax|| "1"}", "vm": "${vm|| "1"}", "vt": "${vt || "1"}", "deltato": "${deltato || "1"}", "ro": "${ro || "1"}",
      "deltat": "${deltat || "1"}","deltamo": "${deltamo || "1"}","etatn": "${etatn || "1"}","am": "${am || "1"}","t": "${t || "1"}"}`;
      ws.send(str2);

//      var newMessage = document.createElement('p');
//      newMessage.textContent = "Client: " + message;
//      document.getElementById('messages_txt').appendChild(newMessage);

    });
    $("#button3").click(function(evt) {
      var str1 = `{"tipo": "actualiza"}`;
      ws.send(str1);
    });

});
