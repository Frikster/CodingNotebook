document.addEventListener("DOMContentLoaded", e => {

    // Add promise out here
    // and in the handleClick, chain on a promise onto it with a .then. Return the resulting promise.
    let promise = new Promise(function (resolve, reject) {
        resolve("Root");
    });

    function handleClick() {
        let container = document.getElementById("loading_container");
        let loadingBar = document.createElement("div");
        loadingBar.className = "loadingBar";
        container.appendChild(loadingBar);
        promise = promise.then(() => new Promise((resolve) => {
            loadingBar.style.animationName = "load";
            setTimeout(() => {
                loadingBar.style.backgroundSize = "100% 100%";
                resolve();
            }, 1000);
        }))
    }

    let btn = document.getElementById("create_loading_button");
    btn.addEventListener("click", handleClick);    


    // Above code is absurdly better
    // handleClickOld = function(e) {
    //     // console.log(e)
    //     let container = document.getElementById("loading_container");
    //     let loadingBar = document.createElement("div");
    //     loadingBar.className = "loadingBar";
    //     loadingBar.style.backgroundSize = "0% 100%";
    //     container.appendChild(loadingBar);
    //     // console.log(container.children.length);
    //     let secondLastLoad = container.children[container.children.length - 2];

    //     let interval = function(resolve) {
    //         // A way to do this without a setInterval?
    //         return setInterval(() => {
    //             console.log(secondLastLoad.style.backgroundSize)
    //             if (secondLastLoad.style.backgroundSize === "100% 100%") {
    //                 resolve("Done");
    //             }
    //         }, 100);
    //     }

    //     // console.log(secondLastLoad);
    //     let promise = new Promise(function (resolve, reject) {
    //         if (container.children.length <= 1) resolve("Done");
    //         else {
    //           interval(resolve);
    //         }
    //     });

    //     promise.then(() => {
    //         clearInterval(interval); // doesn't work?
    //         loadingBar.style.animationName = "load";
    //         // I should't have to use a setTimeout here? Bad to have the "1000" logic in two different places.
    //         // But there is no way to see whether an element is "mid-animation" that I can find
    //         setTimeout(() => {
    //             loadingBar.style.backgroundSize = "100% 100%";
    //         }, 1000)
    //     });
    // }
});