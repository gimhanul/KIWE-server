function show() {
    des = document.getElementById('description');
    del = document.getElementById('delete');
    right = document.getElementById('right');

    if(des) {
        del.style.display = 'none';
        right.style.top = '15%';
        des.id = 'more-description';
    }

    else {
        des = document.getElementById('more-description')
        del.style = "";
        right.style = "";
        des.id = 'description';
    }
}