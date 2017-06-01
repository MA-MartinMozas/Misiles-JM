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


    }
    if (misionType==2) {
        $("#").hide();$("#").hide();

    }
    var targetType = sessionStorage.getItem("targetType");


     if (targetType==1) {
       targetType= "maniobrante"
    }
    else {
        targetType = "No_maniobrante"
    }
  document.getElementById("targetType").innerHTML = targetType;



}







