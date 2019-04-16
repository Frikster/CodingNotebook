function handleSubmit() {
    let li = document.createElement('li');
    li.innerHTML = `${taskTextInput.value}`;
    let leftSpan = document.createElement('span');
    leftSpan.className = "moveLeft";
    leftSpan.innerHTML = "<<";
    leftSpan.addEventListener("click", (e) => handleLeftClick(e));
    let rightSpan = document.createElement('span');
    rightSpan.className = "moveRight";
    rightSpan.innerHTML = ">>";
    rightSpan.addEventListener("click", e => handleRightClick(e));
    li.append(leftSpan);
    li.append(rightSpan);
    document.getElementById("colStart").append(li);
    taskTextInput.value = "";
}

function handleLeftClick(e) {
    let task = e.currentTarget.parentElement;
    let currentCol = e.currentTarget.parentElement.parentElement;
    let cols = Array.from(document.querySelectorAll(".col"));
    let currentIdx = cols.findIndex(col => col === currentCol);
    if (currentIdx - 1 >= 0) {
        cols[currentIdx - 1].append(task); // heh, this removes it from where it was as well?
    }    
}

function handleRightClick(e) {
    let task = e.currentTarget.parentElement;
    let currentCol = e.currentTarget.parentElement.parentElement;
    let cols = Array.from(document.querySelectorAll(".col"));
    let currentIdx = cols.findIndex(col => col === currentCol);
    if(currentIdx+1 <= cols.length-1) {
        cols[currentIdx + 1].append(task); 
    }    
}

let tastSubmitButton = document.getElementById("tastSubmitButton");
let taskTextInput = document.getElementById("taskTextInput");



tastSubmitButton.addEventListener("click", handleSubmit);
