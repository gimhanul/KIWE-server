function showPopup(user) {
    const popup = document.getElementById(user);
    popup.classList.remove('hide');
}

function closePopup(user) {
    const popup = document.getElementById(user);
    popup.classList.add('hide');
}