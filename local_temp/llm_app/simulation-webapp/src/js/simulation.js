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
      initialInfected: 1, // Newly added parameter
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
