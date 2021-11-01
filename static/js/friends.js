function show(id) {
    des = document.getElementById(id).children[0].children[2].children[0];
    del = document.getElementById(id).children[0].children[2].children[1];
    right = document.getElementById(id).children[0].children[2];

    if(des.className == "description") {
        del.style.display = "none";
        right.style.top = "15%";
        des.className = "more-description";
    }
    else {
        del.style = "";
        right.style = "";
        des.className = "description";
    }
}