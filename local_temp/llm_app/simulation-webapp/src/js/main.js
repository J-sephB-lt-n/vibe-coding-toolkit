document.addEventListener('DOMContentLoaded', () => {
  const canvas = document.getElementById('simulationCanvas');
  const simulation = new Simulation(canvas);

  setupControls(simulation);
  simulation.initialize();
});