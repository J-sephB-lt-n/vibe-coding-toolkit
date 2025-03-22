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