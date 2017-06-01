
var frontSectionType;
var canardType;
var finType;
var finTypeStr;

function selectGeometry(geometry,Type){
//esta función se activa al clikear en el menu de selección de geometría
//recibe dos valores uno indicando a que parte del misil se refiere (geometry) y
//otra variable que indica el tipo de geometría elegida dentro de ese campo
//ej: selectGeometry(1,1): indica de la parte de la geometría=frontSectionType la opción = cónica
//el comando sessionStorage.setItem nos permitirá intercambiar el valor de una página html a otra (SeleccionGeo-->DatosGeo)

    if(geometry==1){
        frontSectionType = Type;
        sessionStorage.setItem("frontSectionType",Type);
    }
    if(geometry==2){
        canardType = Type;
        sessionStorage.setItem("canardType",Type);
    }
    if(geometry==3){
        finType = Type;
        sessionStorage.setItem("finType",Type);
    }
//    esta parte nos muestra por consola el valor de las variables en función de lo pickeado
    console.log("Front Type :" + frontSectionType);
    console.log("Canard Type :" + canardType);
    console.log("Fin Type :" + finType);


}

function getStrFinType(){
    if (finType==1) {
        return "Delta"
    }
    else {
        return "Rectangular"
    }
}

//esta función se activará al cargarse la página de DatosGeo lo que nos permite usar las variables de SeleccionGeo
function customFormDatosGeo(){
    var frontSectionType = sessionStorage.getItem("frontSectionType");
    var canardType = sessionStorage.getItem("canardType");
    var finType = sessionStorage.getItem("finType");
//en esta parte utilizamos condicionales para que en función de lo pickeado se nos muestren unos inputs u otros para la introdución de datos

    if (frontSectionType==1) {


    }
    if (frontSectionType==2) {
        $("#lc").hide();$("#lcp").hide();

    }
//    escondemos input de masa de canard si no hay canard
    if (canardType==2) {
        $("#xcanard").hide();$("#xcanardp").hide();
        $("#mcanard").hide();$("#mcanardp").hide();


        }
//    en el caso del tipo de aleta se adjudica un string con el nombre de lo seleccionado que se utilizará para el tipo de cálculo en python

    finTypeStr = getStrFinType();
    /*
    if (finType==1) {
        finType= "Delta"
    }
    else {
        finType = "Rectangular"
    }
    */
    document.getElementById("finType").innerHTML = finTypeStr;
//    mediante este comando se manda el valor seleccionado de tipo de aleta a la página de ResultadosGeo

}






