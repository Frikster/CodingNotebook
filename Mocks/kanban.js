// Might not be able to remove event listener with => because you are creating new function on the fly
// This is also why you can add the same event listener multiple times: each goes to a new function (probably what is going on)
// Less event listeners the better -> combine left/right click into one to reduce code redundancy

// TODO: modify with feedback 
// Can probably use e.currentTarget vs e.target to minimize eventListeners

function handleSubmit() {
    `<li>${taskTextInput.value}<span><span><span><li>`;
    let li = document.createElement('li');
    li.innerHTML = `${taskTextInput.value}`;
    let leftSpan = document.createElement('span');
    leftSpan.className = "moveLeft";
    leftSpan.innerHTML = "<<";
    leftSpan.addEventListener("click", (e) => handleLeftClick(e));
    let rightSpan = document.createElement('span');
    rightSpan.className = "moveRight";
    rightSpan.innerHTML = ">>";
    rightSpan.addEventListener("click", (e) => handleRightClick(e));
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
