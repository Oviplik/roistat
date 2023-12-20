function openModalWin() {
    var modalWin = document.getElementById('modal_win');document.getElementById('modal_win');
    modalWin.style.display = 'block';
}
function closeModalWin() {
    var modalWin = document.getElementById('modal_win');
    modalWin.style.display = 'none';
}
function openModalsuccessWin() {
    var modalWin = document.getElementById('modal_win_success');document.getElementById('modal_win_success');
    modalWin.style.display = 'block';
}
function closeModalsuccessWin() {
    var modalWin = document.getElementById('modal_win_success');
    modalWin.style.display = 'none';
}
window.onload = openModalsuccessWin;