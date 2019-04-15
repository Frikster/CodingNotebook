/* Get Our Elements */
const player = document.querySelector(".player");
const video = player.querySelector(".viewer");
const progress = player.querySelector(".progress");
const progressBar = player.querySelector(".progress__filled");
const toggle = player.querySelector(".toggle");
const skipButtons = player.querySelectorAll("[data-skip]");
const ranges = player.querySelectorAll(".player__slider");

function togglePlay() {
    video.paused ? video.play() : video.pause();
}

function updateButton(e) {
    toggle.innerHTML = e.currentTarget.paused ? "►" : "❚ ❚";
}

function handleProgress() {
    const percent = (video.currentTime / video.duration) * 100;
    progressBar.style.flexBasis = `${percent}%`;
}

function handleRangeUpdate(e) {
    video[e.currentTarget.name] = e.currentTarget.value;
}

function skip(e) {
    video.currentTime += parseFloat(e.currentTarget.dataset.skip);
}

function scrub(e) {
    // if(e.mousedown) see below for why this is suboptimal
    video.currentTime = (e.offsetX / progress.offsetWidth) * video.duration;
}
 
video.addEventListener('click', togglePlay);
video.addEventListener("play", (e) => updateButton(e));
video.addEventListener("pause", (e) => updateButton(e));
video.addEventListener("timeupdate", handleProgress);

toggle.addEventListener('click', togglePlay);

skipButtons.forEach(button => button.addEventListener("click", (e) => skip(e)));
ranges.forEach(range => range.addEventListener("mousemove", e => handleRangeUpdate(e)));

progress.addEventListener("click", (e) => scrub(e));
progress.addEventListener("mousemove", e => mouseDown && scrub(e));
// using this var is better otherwise a million events fire even if they immediately exit
let mouseDown = false;
progressBar.addEventListener("mousedown", () => mouseDown = true);
progressBar.addEventListener("mouseup", () => mouseDown = false);



