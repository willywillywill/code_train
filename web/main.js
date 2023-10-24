var data = [];

function update(){
    var out = "";

    for(var i=0 ; i < data.length ; i++){
        out += "<button class='text_sub'>"+data[i]+"</button>";
    }
    document.getElementById("text").innerHTML = out;

};


function insert(){
    var txt = document.getElementById("insert_txt").value;
    data.push(txt);
    update();
};