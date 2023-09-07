function solve() {
    const buttons = document.querySelectorAll("button");

    const checkButton = buttons[0];
   
    checkButton.addEventListener("click", function checkSudoku() {
        let cells = document.querySelectorAll("input");
        let theSudokuIsValid = true;

        if (cells.length === 9) { // Small Playing Field 3x3

        // Check rows
        let arrayOfElements = []
        for (let index = 0; index < 9; index += 3) {
            const firstPos = cells[index].value;
            const secondPos = cells[index + 1].value;
            const thirdPos = cells[index + 2].value; 
           
            // console.log(firstPos, secondPos, thirdPos);
            arrayOfElements.push(firstPos, secondPos, thirdPos);
            const currentArray = [firstPos, secondPos, thirdPos];
            const currentSet = new Set(currentArray);
            if (currentArray.length != currentSet.size) {
                theSudokuIsValid = false;
                break;
            }
        }

        //Check columns
        for (let index = 0; index < 3; index++) {
            const firstCol = cells[index].value;
            const secondCol = cells[index + 3].value;
            const thirdCol = cells[index + 6].value;
          
            // console.log(firstCol, secondCol, thirdCol);
            const currentArray = [firstCol, secondCol, thirdCol];
            const currentSet = new Set(currentArray);
            if (currentArray.length != currentSet.size) {
                theSudokuIsValid = false;
                break;
            }
        }

    } else if (cells.length === 81) { // Standard Playing field
           
        // Check rows
        let arrayOfElements = []
        for (let index = 0; index < 81; index += 9) {
            const firstPos = cells[index].value;
            const secondPos = cells[index + 1].value;
            const thirdPos = cells[index + 2].value; 
            const fourthPos = cells[index + 3].value;
            const fifthPos = cells[index + 4].value;
            const sixthPos = cells[index + 5].value;
            const seventhPos = cells[index + 6].value;
            const eightPos = cells[index + 7].value;
            const ninthPos = cells[index + 8].value;
           
            // console.log(firstPos, secondPos, thirdPos, fourthPos, fifthPos, sixthPos, seventhPos, eightPos, ninthPos);
            arrayOfElements.push(firstPos, secondPos, thirdPos, fourthPos, fifthPos, sixthPos, seventhPos, eightPos, ninthPos);
            const currentArray = [firstPos, secondPos, thirdPos, fourthPos, fifthPos, sixthPos, seventhPos, eightPos, ninthPos];
            const currentSet = new Set(currentArray);
            if (currentArray.length != currentSet.size) {
                theSudokuIsValid = false;
                break;
            }
        }

        //Check columns
        for (let index = 0; index < 9; index++) {
            const firstCol = cells[index].value;
            const secondCol = cells[index + 3].value;
            const thirdCol = cells[index + 6].value;
            const fourthCol = cells[index + 9].value;
            const fifthCol = cells[index + 12].value;
            const sixthCol = cells[index + 15].value;
            const seventhCol = cells[index + 18].value;
            const eigthCol = cells[index + 21].value;
            const ninthCol = cells[index + 24].value;
          
            // console.log([firstCol, secondCol, thirdCol, fourthCol, fifthCol, sixthCol, seventhCol, eigthCol, ninthCol]);
            const currentArray = [firstCol, secondCol, thirdCol, fourthCol, fifthCol, sixthCol, seventhCol, eigthCol, ninthCol];
            const currentSet = new Set(currentArray);
            if (currentArray.length != currentSet.size) {
                theSudokuIsValid = false;
                break;
            }
        }

        //Check inner squares
        let i = 0;
        while (i < 81 ) {

        for (let index = i; index <= i + 6; index+= 3) {
            if (index + 20 >= 81) {
                break;
            }
            const firstPos = cells[index].value;;
            const secondPos = cells[index + 1].value;
            const thirdPos = cells[index + 2].value;
            const fourthPos = cells[index + 9].value;
            const fifthPos = cells[index + 10].value;
            const sixthPos = cells[index + 11].value;
            const seventhPos = cells[index + 18].value;
            const eigthPos = cells[index + 19].value;
            const ninthPos = cells[index + 20].value;

            // console.log(firstPos, secondPos, thirdPos, fourthPos, fifthPos, sixthPos, seventhPos, eigthPos, ninthPos);
            const currentArray = [firstPos, secondPos, thirdPos, fourthPos, fifthPos, sixthPos, seventhPos, eigthPos, ninthPos];
            const currentSet = new Set(currentArray);
            if (currentSet.length !== currentArray.length) {
                theSudokuIsValid = false;
                break;
            }
        }
        if (i === 6 || i === 33 || i === 59) {
            i += 18; // end of the current line

        } else {
            i += 3;
        }

        }

    }
    
    let table = document.querySelector("table");
    let finalMessage = document.querySelector('#check p');
    if (theSudokuIsValid) {
        table.style.border = "2px solid green";
        finalMessage.textContent = "You solve it! Congratulations!";
        finalMessage.style.color = "green";
    } else { 
        table.style.border = "2px solid red";
        finalMessage.textContent = "NOP! You are not done yet...";
        finalMessage.style.color = "red";
    }
    })


    const clearButton = buttons[1];

    clearButton.addEventListener("click", function clearSudoku() {
        let finalMessage = document.querySelector('#check p');
        finalMessage.textContent = "";
        let table = document.querySelector("table");
        table.style.border = "none";
        let cells = document.querySelectorAll("input");
        
        if (cells.length === 9) {
            for (let index = 0; index < 9; index++) {
                let currentCell = cells[index];
                currentCell.value = "";
            }

        } else if (cells.length === 81) {
            for (let index = 0; index < 81; index++) {
                let currentCell = cells[index];
                currentCell.value = "";
            }
        }
        console.log("cleared");
    })

}
