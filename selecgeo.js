
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
    }
    if(geometry==3){
        finType = Type;
    }

    console.log("Front Type :" + frontSectionType);
    console.log("Canard Type :" + canardType);
    console.log("Fin Type :" + finType);


}

function customFormDatosGeo(){
    var frontSectionType = sessionStorage.getItem("frontSectionType");
    if (frontSectionType==1) {
        $("#variable1").hide();

    }
    if (frontSectionType==2) {
        $("#variable2").hide();

    }
}







