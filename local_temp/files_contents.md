/virus_simulation/app/__init__.py
```python
from flask import Flask
from .config import Config
from .simulation import Simulation
from .ui import create_ui

def create_app():
    """Factory function to create and configure the Flask application."""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize simulation
    app.simulation = Simulation()

    # Register UI components
    create_ui(app)

    return app
```

/virus_simulation/app/main.py
```python
from . import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
```

/virus_simulation/app/config.py
```python
import os

class Config:
    """Configuration settings for the application."""
    
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
    SIMULATION_SPEED = int(os.getenv("SIMULATION_SPEED", 1))
    POPULATION_SIZE = int(os.getenv("POPULATION_SIZE", 100))
    INFECTION_RATE = float(os.getenv("INFECTION_RATE", 0.1))
    RECOVERY_RATE = float(os.getenv("RECOVERY_RATE", 0.05))
    INITIAL_INFECTED = int(os.getenv("INITIAL_INFECTED", 1))
```

/virus_simulation/app/simulation.py
```python
import random
from .state import Person, SimulationState

class Simulation:
    """Class to manage the virus simulation logic."""

    def __init__(self, population_size=100, infection_rate=0.1, recovery_rate=0.05, initial_infected=1):
        self.population_size = population_size
        self.infection_rate = infection_rate
        self.recovery_rate = recovery_rate
        self.state = SimulationState(population_size, initial_infected)

    def step(self):
        """Advance the simulation by one step."""
        for person in self.state.population:
            if person.infected:
                if random.random() < self.recovery_rate:
                    person.recover()
                else:
                    for other in self.state.population:
                        if not other.infected and random.random() < self.infection_rate:
                            other.infect()

    def get_state(self):
        """Return the current state of the simulation."""
        return self.state.get_summary()
```

/virus_simulation/app/state.py
```python
class Person:
    """Represents an individual in the population."""

    def __init__(self, infected=False):
        self.infected = infected
        self.recovered = False

    def infect(self):
        """Mark the person as infected."""
        if not self.recovered:
            self.infected = True

    def recover(self):
        """Mark the person as recovered and immune."""
        self.infected = False
        self.recovered = True


class SimulationState:
    """Manages the population and their health states."""

    def __init__(self, population_size, initial_infected):
        self.population = [Person(infected=(i < initial_infected)) for i in range(population_size)]

    def get_summary(self):
        """Return the summary of the current simulation state."""
        infected_count = sum(1 for person in self.population if person.infected)
        recovered_count = sum(1 for person in self.population if person.recovered)
        healthy_count = len(self.population) - infected_count - recovered_count
        return {
            "healthy": healthy_count,
            "infected": infected_count,
            "recovered": recovered_count
        }
```

/virus_simulation/app/ui.py
```python
from flask import render_template, jsonify
from .simulation import Simulation

def create_ui(app):
    """Register routes for the UI and API endpoints."""

    @app.route("/")
    def index():
        """Render the main UI page."""
        return render_template("index.html")

    @app.route("/api/state")
    def get_state():
        """Return the current simulation state as JSON."""
        return jsonify(app.simulation.get_state())

    @app.route("/api/step", methods=["POST"])
    def step():
        """Advance the simulation by one step and return the updated state."""
        app.simulation.step()
        return jsonify(app.simulation.get_state())
```

/virus_simulation/assets/styles.css
```css
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 0;
}

.container {
    max-width: 800px;
    margin: auto;
    padding: 20px;
    background: white;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
    color: #333;
}

button {
    display: block;
    margin: 20px auto;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
    background: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
}

button:hover {
    background: #0056b3;
}
```

/virus_simulation/requirements.txt
```
Flask==2.3.2
gunicorn==21.2.0
```

/virus_simulation/run.sh
```sh
#!/bin/bash

export FLASK_APP=virus_simulation.app.main
export FLASK_ENV=development

flask run --host=0.0.0.0 --port=5000
```

This structure provides a well-organized, modern Flask-based simulation of virus spread with a simple API and UI. Let me know if you need enhancements! 🚀
