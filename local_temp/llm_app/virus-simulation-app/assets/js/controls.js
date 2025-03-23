document.getElementById('sim-speed').value = DEFAULTS.simSpeed;
document.getElementById('pop-size').value = DEFAULTS.populationSize;
document.getElementById('initial-infected').value = DEFAULTS.initialInfected;
document.getElementById('infection-length').value = DEFAULTS.infectionLength;
document.getElementById('infectiousness').value = DEFAULTS.infectiousness;

document.getElementById('new-sim').onclick = () => {
    DEFAULTS.simSpeed = parseInt(document.getElementById('sim-speed').value);
    DEFAULTS.populationSize = parseInt(document.getElementById('pop-size').value);
    DEFAULTS.initialInfected = parseInt(document.getElementById('initial-infected').value);
    DEFAULTS.infectionLength = parseInt(document.getElementById('infection-length').value);
    DEFAULTS.infectiousness = parseFloat(document.getElementById('infectiousness').value);
    isPaused = true;
    clearTimeout(animationFrame);
    initSimulation();
};

document.getElementById('start-sim').onclick = () => {
    if (isPaused) {
        isPaused = false;
        clearTimeout(animationFrame);
        animate();
    }
};

document.getElementById('pause-sim').onclick = () => {
    isPaused = true;
    clearTimeout(animationFrame);
};

