
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
//se crea una variable obj que será igual al diccionario result mandado por python
// mediante el comando document.getElementById asignaremos el valor del diccionario obj que tenga el marcador nombrado a la id indicada
//lo cual se utilizará en su representación en ResultadosGeo
// #Primero, lo realizamos para diseño aerodinámico del misil
    //  ej: asigna a la id = Rex el valor del diccionario obj que este asociado al marcador Rex
    if (obj.tipo == "geo"){
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
      document.getElementById("CDfilt").innerHTML = obj.CDfilam;
      document.getElementById("CDfi").innerHTML = obj.CDfi;
      document.getElementById("CDf").innerHTML = obj.CDflam;
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
      document.getElementById("Flujo").innerHTML = obj.Flujo;
    }


// #Segundo, lo realizamos para definir la misión
    else {
    document.getElementById("fun").innerHTML = obj.fun;
        if (misionType==1) {

          document.getElementById("K").innerHTML = obj.K;
          document.getElementById("deltati").innerHTML = obj.deltati;
          document.getElementById("etamnm").innerHTML = obj.etamnm;
          document.getElementById("t").innerHTML = obj.t;
          document.getElementById("ri").innerHTML = obj.ri;
          document.getElementById("xt").innerHTML = obj.xt;
            }
        else{
          document.getElementById("deltamc").innerHTML = obj.deltamc;
          document.getElementById("incrementodeltam").innerHTML = obj.incrementodeltam;
          document.getElementById("ti").innerHTML = obj.ti;
          document.getElementById("etamncalculado").innerHTML = obj.etamncalculado;
      }

    }








    };
    ws.onclose = function(evt) {
      alert ("Connection closed");
//      en caso de cierre de conexión o fallo de la página aparecerá una ventana donde indica que la conexión ha sido cerrada
    };
// la siguiente función se activa al clickear en el boton "calcular" de la página DatosGeo
    $("#button1").click(function(evt) {
      evt.preventDefault();
//    se crea una variable a la que se le asigna el valor del input indentificado por su id
      var d = $("#d").val();
      var M = $("#M").val();
      var rho = $("#rho").val();
      var a = $("#a").val();
      var mu= $("#mu").val();
      var la = $("#la").val();
      var lc = $("#lc").val();
      var b = $("#b").val();
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
      var finType = document.getElementById('finType').innerHTML;

      <!--With this line the dict format is constructed-->
      <!--note that the ` is crucial-->
//  se crea un diccionario (str1) donde se introducen un marcados y le asigna una de las variables anteriormente creadas
//además le asignaremos un valor por defecto que nos permitirá en caso de no introducir valores en los inputs o que uno no se introduzca la página siga funcionando
//tmabién nos permitirá en el caso del canard al esconder su input asignarle a sus datos un valor de 0 por lo que los cálculos se realizarán como si no tuviese canard
//evitando de esta manera un condicional en el código de python

      var str1 = `{"tipo": "geo","finType": "${finType}","d": "${d || "0.15"}", "M": "${M || "2"}", "rho": "${rho || "1.225"}", "a": "${a || "340"}", "mu": "${mu || "0.000017894"}", "la": "${la || "2.99"}","lc": "${lc || "0.578"}",
      "b": "${b || "0.66"}","xe": "${xe || "3.40"}","lmaxu": "${lmaxu || "0.1652"}","xcanard": "${xcanard || "0"}","lrd": "${lrd || "0.0827"}","mfuselaje": "${mfuselaje || "51.14"}","mcabeza": "${mcabeza || "4.96"}",
      "maletas": "${maletas || "7.9"}","mcanard": "${mcanard || "4"}","Cnalphabeta": "${Cnalphabeta || "2"}","Cnsat": "${Cnsat || "1.4"}"}`;
//      mandamos el diccionario (str1) a python
      ws.send(str1);


    });



//   esta función se activará al pulsar el botón de "calcular" de la página DatosMis
    $("#button2").click(function(evt) {
      evt.preventDefault();
//        aqui tenemos que meter tantas variables como inputs tenemos que introducir en mision con el id del input donde lo introducimos
      var etamnmax = $("#etamnmax").val();
      var vm = $("#vm").val();
      var vt = $("#vt").val();
      var deltato = $("#deltato").val();
      var ro= $("#ro").val();
      var deltat = $("#deltat").val();
      var deltamo = $("#deltamo").val();
      var etatn = $("#etatn").val();
      var am = $("#am").val();
      var targetType = document.getElementById('targetType').innerHTML;
      var misionType = document.getElementById('misionType').innerHTML;


      <!--With this line the dict format is constructed-->
      <!--note that the ` is crucial-->
//      dentro del str tenemos que meter el marcador de la variable y sera igual a la variable que hemos definido anteriormente y que se asocia a su input

      var str2 = `{"tipo": "mis", "blanco": "${targetType}", "mision": "${misionType}","etamnmax": "${etamnmax|| "180"}", "vm": "${vm|| "950"}", "vt": "${vt || "500"}", "deltato": "${deltato || "40"}", "ro": "${ro || "2000"}",
      "deltat": "${deltat || "0"}","deltamo": "${deltamo || "15"}","etatn": "${etatn || "85"}","am": "${am || "5"}"}`;
      ws.send(str2);


    });
    $("#button3").click(function(evt) {
      var str1 = `{"tipo": "actualiza"}`;
      ws.send(str1);
    });
    $("#button4").click(function(evt) {
      var str2 = `{"tipo": "actualiza2"}`;
      ws.send(str2);
    });
});
