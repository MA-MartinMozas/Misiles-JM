var misionType;
var targetType;


function selectMision(mision,Type){



    if(mision==1){
        misionType = Type;
        sessionStorage.setItem("misionType",Type);
    }
    if(mision==2){
        targetType = Type;
        sessionStorage.setItem("targetType",Type);
    }


    console.log("Mision Type :" + misionType);
    console.log("Target Type :" + targetType);



}

function customMisionDatos(){
    var misionType = sessionStorage.getItem("misionType");
    if (misionType==1) {

        $("#deltamo").hide();$("#deltamop").hide();
        $("#etatn").hide();$("#etatnp").hide();
        $("#am").hide();$("#amp").hide();
        $("#deltamc").hide();$("#deltamcp").hide();
        $("#incrementodeltam").hide();$("#incrementodeltamp").hide();
        $("#etamncalculado").hide();$("#etamncalculadop").hide();
        $("#ti").hide();$("#tip").hide();
        misionType= "P_Pura"


    }
    if (misionType==2) {
        $("#K").hide();$("#Kp").hide();
        $("#deltati").hide();$("#deltatip").hide();
        $("#etamnm").hide();$("#etamnmp").hide();
        $("#t").hide();$("#tp").hide();
        $("#ri").hide();$("#rip").hide();
        $("#xt").hide();$("#xtp").hide();

        misionType= "N_Proporcional"

    }
    var targetType = sessionStorage.getItem("targetType");


     if (targetType==1) {
       targetType= "maniobrante"
    }
    else {
        targetType = "No_maniobrante"
        $("#etatn").hide();$("#etatnp").hide();
    }
  document.getElementById("targetType").innerHTML = targetType;
  document.getElementById("misionType").innerHTML = misionType;



}







