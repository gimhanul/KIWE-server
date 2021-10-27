const sub = document.getElementsByClassName("sub")
const m = document.getElementsByClassName("m-list")

function show(name) {
      for (var i = 0; i < sub.length; i++) {
          sub[i].style.display = 'none';
          m[i].style.boxShadow = 'none';
      }
    
    document.getElementById(name).style.boxShadow = "inset 0 -15px #EEF6D6"
    name = 'sub-'+name;
    document.getElementById(name).style.display='list-item';
  }