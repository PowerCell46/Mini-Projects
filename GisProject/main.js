function handleSectionDiv(e) {
    console.log(e.target.parentNode);
    if (document.querySelector(".hidden").style.display === 'block') {
        document.querySelector(".hidden").style.display = 'none';
        e.target.parentNode.parentNode.querySelector('i').style.transform = 'rotate(0deg)';

    } else {
        document.querySelector(".hidden").style.display = 'block';
        e.target.parentNode.parentNode.querySelector('i').style.transform = 'rotate(180deg)';
    }
}