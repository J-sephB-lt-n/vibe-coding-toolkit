const canvas = document.getElementById('simulation-canvas');
const ctx = canvas.getContext('2d');
let animationFrame, individuals = [], isPaused = true;

function initSimulation() {
    individuals = [];
    for(let i = 0; i < DEFAULTS.populationSize; i++) {
        individuals.push({
            x: Math.random() * DEFAULTS.canvasWidth,
            y: Math.random() * DEFAULTS.canvasHeight,
            vx: Math.random() * 2 - 1,
            vy: Math.random() * 2 - 1,
            status: i < DEFAULTS.initialInfected ? 'sick' : 'healthy',
            infectedFrames: 0
        });
    }
    draw();
}

function updatePositions() {
    individuals.forEach(ind => {
        ind.x += ind.vx;
        ind.y += ind.vy;

        if(ind.x < 0 || ind.x > DEFAULTS.canvasWidth) ind.vx *= -1;
        if(ind.y < 0 || ind.y > DEFAULTS.canvasHeight) ind.vy *= -1;
    });
}

function spreadInfection() {
    individuals.forEach(ind => {
        if(ind.status === 'sick') {
            ind.infectedFrames++;
            if(ind.infectedFrames > DEFAULTS.infectionLength) ind.status = 'recovered';

            individuals.forEach(other => {
                if(other.status === 'healthy') {
                    const dist = Math.hypot(ind.x - other.x, ind.y - other.y);
                    if(dist < DEFAULTS.dotRadius * 2 && Math.random() < DEFAULTS.infectiousness) {
                        other.status = 'sick';
                    }
                }
            });
        }
    });
}

function draw() {
    ctx.clearRect(0, 0, DEFAULTS.canvasWidth, DEFAULTS.canvasHeight);
    individuals.forEach(ind => {
        ctx.fillStyle = ind.status === 'healthy' ? 'green' : ind.status === 'sick' ? 'red' : 'grey';
        ctx.beginPath();
        ctx.arc(ind.x, ind.y, DEFAULTS.dotRadius, 0, Math.PI * 2);
        ctx.fill();
    });
}

function animate() {
    if(!isPaused) {
        updatePositions();
        spreadInfection();
        draw();
    }
    animationFrame = setTimeout(() => requestAnimationFrame(animate), 1000 / DEFAULTS.simSpeed);
}

initSimulation();
animate();