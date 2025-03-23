Here’s your complete and high-quality production-level code for each specified file in the project structure:

### ✅ **Project File Contents:**

---

virus-simulation-app/index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Virus Spread Simulation</title>
    <link rel="stylesheet" href="assets/css/styles.css">
    <link rel="icon" href="assets/images/favicon.ico">
</head>
<body>
    <div class="container">
        <h1>Virus Spread Simulation</h1>
        <div id="controls">
            <button id="new-sim" title="Creates a new simulation with current parameters.">New Simulation</button>
            <button id="start-sim" title="Starts or resumes the simulation.">Start Simulation</button>
            <button id="pause-sim" title="Pauses the simulation.">Pause Simulation</button>

            <label>Simulation speed (fps):
                <input type="number" id="sim-speed" min="1" max="60" title="Number of simulation updates per second. Higher value = faster simulation.">
            </label>

            <label>Population size:
                <input type="number" id="pop-size" min="10" max="500" title="Total number of individuals in the simulation.">
            </label>

            <label>Initially infected:
                <input type="number" id="initial-infected" min="1" max="100" title="Number of individuals initially infected.">
            </label>

            <label>Infection length:
                <input type="number" id="infection-length" min="10" max="500" title="Duration (frames) an individual remains infectious.">
            </label>

            <label>Infectiousness:
                <input type="number" id="infectiousness" step="0.01" min="0" max="1" title="Probability of infection on contact. (0=no infection, 1=always infect)">
            </label>
        </div>
        <canvas id="simulation-canvas" width="800" height="600"></canvas>
        <div id="legend">
            <span class="dot healthy"></span> Healthy
            <span class="dot sick"></span> Sick
            <span class="dot recovered"></span> Recovered
        </div>
    </div>
    <script src="config/defaults.js"></script>
    <script src="assets/js/simulation.js"></script>
    <script src="assets/js/controls.js"></script>
</body>
</html>
```

---

virus-simulation-app/assets/css/styles.css
```css
body {
    font-family: Arial, sans-serif;
    background-color: #f5f7fa;
    margin: 0;
    padding: 20px;
    color: #333;
}

.container {
    max-width: 840px;
    margin: 0 auto;
    padding: 20px;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

h1 {
    text-align: center;
    margin-bottom: 15px;
}

#controls {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 10px;
    margin-bottom: 15px;
}

#controls label {
    display: flex;
    flex-direction: column;
    font-size: 0.9em;
}

#controls input {
    padding: 5px;
    border-radius: 4px;
    border: 1px solid #ccc;
    width: 120px;
}

button {
    cursor: pointer;
    padding: 8px 12px;
    border-radius: 4px;
    border: none;
    background-color: #4CAF50;
    color: white;
    transition: background-color 0.3s;
}

button:hover {
    background-color: #45a049;
}

canvas {
    border: 1px solid #ddd;
    display: block;
    margin: 0 auto;
}

#legend {
    text-align: center;
    margin-top: 10px;
}

.dot {
    display: inline-block;
    width: 12px;
    height: 12px;
    border-radius: 50%;
    margin-right: 5px;
}

.healthy { background-color: green; }
.sick { background-color: red; }
.recovered { background-color: grey; }
```

---

virus-simulation-app/config/defaults.js
```javascript
const DEFAULTS = {
    simSpeed: 30,
    populationSize: 100,
    initialInfected: 1,
    infectionLength: 200,
    infectiousness: 0.3,
    canvasWidth: 800,
    canvasHeight: 600,
    dotRadius: 4
};
```

---

virus-simulation-app/assets/js/simulation.js
```javascript
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
```

---

virus-simulation-app/assets/js/controls.js
```javascript
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

document.getElementById('start-sim').onclick = () => { isPaused = false; };
document.getElementById('pause-sim').onclick = () => { isPaused = true; };
```

✅ **This completes the full production-ready implementation.**
