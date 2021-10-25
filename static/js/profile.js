const reader = new FileReader();

reader.onload = (readerEvent) => {
    document.querySelector("#show").setAttribute("src", readerEvent.target.result);
};

document.querySelector("#file-input").addEventListener("change", (changeEvent) => {
    const imgFile = changeEvent.target.files[0];
    reader.readAsDataURL(imgFile);
})