var i = 0;
function load() {
    highlighter.innerHTML = memory[i][0];
    texxt.innerHTML = memory[i][1];
    result.innerHTML = memory[i][2];
}

function left() {
    if (i > 0) i--;
    else i = memory.length - 1;

    load();
}

function right() {
    if (i < memory.length - 1) i++;
    else i = 0;

    load();
}