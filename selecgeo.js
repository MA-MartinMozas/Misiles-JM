
var frontSectionType;
var canardType;
var finType;

function selectGeometry(geometry,Type){



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

    console.log("Front Type :" + frontSectionType);
    console.log("Canard Type :" + canardType);
    console.log("Fin Type :" + finType);


}

function customFormDatosGeo(){
    var frontSectionType = sessionStorage.getItem("frontSectionType");
    if (frontSectionType==1) {


    }
    if (frontSectionType==2) {
        $("#lc").hide();$("#lcp").hide();

    }
    var frontSectionType = sessionStorage.getItem("canardType");


    var frontSectionType = sessionStorage.getItem("finType");
}







