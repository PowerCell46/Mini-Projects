function handleSectionDiv(e) {
    const hiddenElement = e.target.parentNode.parentNode.querySelector(".hidden");
    const iconElement = e.target.parentNode.parentNode.querySelector('i');

    if (hiddenElement.classList.contains('active')) {
        hiddenElement.classList.remove('active');
        iconElement.style.transform = 'rotate(0deg)';
        
        setTimeout(() => {
            hiddenElement.style.height = '0';
        }, 1000);
    } else {
        hiddenElement.classList.add('active');
        hiddenElement.style.height = 'auto'; // Set to your preferred height or 'auto'
        iconElement.style.transform = 'rotate(180deg)';
    }
}
