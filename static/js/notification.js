function send(at, requestID, notiID) {
    document.getElementById(notiID).style.backgroundColor = 'white';
    document.getElementById(notiID).children[2].style.display = 'none';
    document.getElementById(notiID).children[3].style.display = 'none';

    var data = {
        at : at,
        requestID : requestID,
        notiID : notiID,
    };
    go(data);
}
function read(notiID) {
    console.log(notiID);
    document.getElementById(notiID).style.backgroundColor = 'white';
    var data = {
        at : 'noneedy',
        notiID : notiID,
    };
    go(data);
}