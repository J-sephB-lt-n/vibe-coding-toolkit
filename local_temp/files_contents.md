Below is the complete production-quality content for each of the requested files, organized neatly according to your specification:

---

simulation-webapp/public/index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Virus Spread Simulation</title>
  <link rel="stylesheet" href="../src/css/style.css">
  <link rel="stylesheet" href="../src/css/controls.css">
</head>
<body>
  <div class="container">
    <h1>Virus Spread Simulation</h1>
    <canvas id="simulationCanvas"></canvas>
    <div class="controls">
      <button id="startBtn">Start Simulation</button>
      <button id="pauseBtn">Pause Simulation</button>
      <button id="resetBtn">New Simulation</button>

      <label>Simulation Speed (FPS): <input id="speed" type="number" value="30" min="1" max="120"></label>
      <label>Population Size: <input id="population" type="number" value="100" min="10" max="1000"></label>
      <label>Infection Duration (frames): <input id="infectionDuration" type="number" value="200" min="1"></label>
      <label>Infectiousness (0-1): <input id="infectiousness" type="number" step="0.01" value="0.5" min="0" max="1"></label>
    </div>
  </div>
  
  <script src="../src/js/simulation.js"></script>
  <script src="../src/js/controls.js"></script>
  <script src="../src/js/main.js"></script>
</body>
</html>
```

---

simulation-webapp/src/js/main.js
```javascript
document.addEventListener('DOMContentLoaded', () => {
  const canvas = document.getElementById('simulationCanvas');
  const simulation = new Simulation(canvas);

  setupControls(simulation);
  simulation.initialize();
});
```

---

simulation-webapp/src/js/simulation.js
```javascript
class Individual {
  constructor(x, y, status = 'healthy') {
    this.x = x;
    this.y = y;
    this.status = status; // healthy, sick, recovered
    this.infectedFrames = 0;
    this.vx = Math.random() * 2 - 1;
    this.vy = Math.random() * 2 - 1;
  }

  update(bounds, infectionDuration) {
    this.x += this.vx;
    this.y += this.vy;

    if (this.x <= 0 || this.x >= bounds.width) this.vx *= -1;
    if (this.y <= 0 || this.y >= bounds.height) this.vy *= -1;

    if (this.status === 'sick') {
      this.infectedFrames++;
      if (this.infectedFrames >= infectionDuration) {
        this.status = 'recovered';
      }
    }
  }
}

class Simulation {
  constructor(canvas) {
    this.canvas = canvas;
    this.ctx = canvas.getContext('2d');
    this.individuals = [];
    this.animationFrameId = null;
    this.isRunning = false;

    // Default settings
    this.settings = {
      population: 100,
      speed: 30,
      infectionDuration: 200,
      infectiousness: 0.5,
    };

    this.resizeCanvas();
    window.addEventListener('resize', () => this.resizeCanvas());
  }

  resizeCanvas() {
    this.canvas.width = 600;
    this.canvas.height = 400;
  }

  initialize() {
    this.stop();
    this.individuals = [];
    for (let i = 0; i < this.settings.population; i++) {
      this.individuals.push(new Individual(
        Math.random() * this.canvas.width,
        Math.random() * this.canvas.height
      ));
    }
    // Infect one individual initially
    this.individuals[0].status = 'sick';
    this.draw();
  }

  start() {
    if (this.isRunning) return;
    this.isRunning = true;
    this.run();
  }

  stop() {
    this.isRunning = false;
    if (this.animationFrameId) cancelAnimationFrame(this.animationFrameId);
  }

  run() {
    const fpsInterval = 1000 / this.settings.speed;
    let then = Date.now();

    const animate = () => {
      this.animationFrameId = requestAnimationFrame(animate);
      const now = Date.now();
      const elapsed = now - then;
      if (elapsed > fpsInterval) {
        then = now - (elapsed % fpsInterval);
        this.update();
        this.draw();
      }
    };
    animate();
  }

  update() {
    this.individuals.forEach(individual => individual.update(this.canvas, this.settings.infectionDuration));
    // Check for infections
    for (let i = 0; i < this.individuals.length; i++) {
      for (let j = i + 1; j < this.individuals.length; j++) {
        this.checkInfection(this.individuals[i], this.individuals[j]);
      }
    }
  }

  checkInfection(indiv1, indiv2) {
    if ((indiv1.status === 'sick' && indiv2.status === 'healthy') ||
        (indiv2.status === 'sick' && indiv1.status === 'healthy')) {
      const dx = indiv1.x - indiv2.x;
      const dy = indiv1.y - indiv2.y;
      const distance = Math.sqrt(dx * dx + dy * dy);
      if (distance < 5 && Math.random() < this.settings.infectiousness) {
        if (indiv1.status === 'healthy') indiv1.status = 'sick';
        if (indiv2.status === 'healthy') indiv2.status = 'sick';
      }
    }
  }

  draw() {
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    this.individuals.forEach(indiv => {
      this.ctx.fillStyle = indiv.status === 'healthy' ? 'green' : indiv.status === 'sick' ? 'red' : 'black';
      this.ctx.beginPath();
      this.ctx.arc(indiv.x, indiv.y, 3, 0, 2 * Math.PI);
      this.ctx.fill();
    });
  }
}
```

---

simulation-webapp/src/js/controls.js
```javascript
function setupControls(simulation) {
  document.getElementById('startBtn').addEventListener('click', () => simulation.start());
  document.getElementById('pauseBtn').addEventListener('click', () => simulation.stop());
  document.getElementById('resetBtn').addEventListener('click', () => simulation.initialize());

  document.getElementById('speed').addEventListener('change', (e) => {
    simulation.settings.speed = parseInt(e.target.value) || 30;
  });

  document.getElementById('population').addEventListener('change', (e) => {
    simulation.settings.population = parseInt(e.target.value) || 100;
    simulation.initialize();
  });

  document.getElementById('infectionDuration').addEventListener('change', (e) => {
    simulation.settings.infectionDuration = parseInt(e.target.value) || 200;
  });

  document.getElementById('infectiousness').addEventListener('change', (e) => {
    simulation.settings.infectiousness = parseFloat(e.target.value) || 0.5;
  });
}
```

---

simulation-webapp/src/css/style.css
```css
body {
  font-family: Arial, sans-serif;
  background-color: #f8f9fa;
  margin: 0;
  padding: 0;
}

.container {
  width: 700px;
  margin: auto;
  padding: 20px;
  text-align: center;
}

#simulationCanvas {
  border: 1px solid #ccc;
  background-color: #ffffff;
  margin-top: 10px;
}
```

---

simulation-webapp/src/css/controls.css
```css
.controls {
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding: 15px;
  background-color: #ffffff;
  border-radius: 8px;
  margin-top: 15px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.controls button {
  padding: 8px;
  cursor: pointer;
  border: none;
  background-color: #007bff;
  color: #fff;
  border-radius: 4px;
  font-size: 14px;
}

.controls button:hover {
  background-color: #0056b3;
}

.controls label {
  font-size: 14px;
}

.controls input {
  margin-left: 8px;
  padding: 4px;
  width: 80px;
}
```
