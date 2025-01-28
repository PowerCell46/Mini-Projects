const removeElementIs = document.getElementsByClassName("remove-element");

Array.from(removeElementIs)
    .forEach(element => {
        element.addEventListener("click", function (e) {
            e.target.parentElement.remove();
        });
    });

const removeSecondElementIs = document.getElementsByClassName("remove-second-element");


Array.from(removeSecondElementIs)
    .forEach(element => {
        element.addEventListener("click", function (e) {
            e.target.parentElement.remove();
        });
    });