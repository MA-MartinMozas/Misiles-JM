
var frontSectionType = 0;
var canardType = 0;
var finType = 0;

function selectGeometry(geometry,Type){



    if(geometry==1){
        frontSectionType = Type;
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


