function medalClickHandler(event) {
    const medal = event.target;
    medal.classList.add('big');

    setTimeout(function () {
        medal.classList.remove('big');
    }, 2000)
}

function init() {
    const medals = document.querySelectorAll('.medal');

    for (let medal of medals) {
        medal.addEventListener('click', medalClickHandler);
    }
}

init();