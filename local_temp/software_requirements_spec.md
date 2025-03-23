<project-scope>
The application is a simple aesthetic simulation running in a web app which is novel for users, allowing them to experiment with various virus parameters and visually see the effect of these on the spread of infection (in a toy population).
</project-scope>

<intended-audience>
The intended users of this app are the general public (people with no prior exposure to epidemiology).
</intended-audience>

<user-interface-requirements>
The simulation consists of dots which move around randomly within a bounded box on a single page web page. Each dot represents an individual in the simulated population.
At any given time, an individual can be healthy, sick or recovered.
The state of an individual is represented by their colour: healthy=green, sick=red, recovered=grey.
Individuals infect each other (with an infectiousness probability) when the dots representing them overlap.

The following controls are available to the user:
- Button: Start simulation (dots start moving again)
- Button: Pause simulation (dots stop moving in place)
- Button: New simulation (spawns a new population, and waits for user to click 'start simulation')
- Integer: Simulation speed (simulation frames per second)
- Integer: Population size (number of individuals)
- Integer: Number of infected individuals at simulation start
- Integer: Infection length (how long individuals are sick for, in simulation frames)
- Integer: Infectiousness (probability of infection when 2 individuals touch - a value between 0 and 1)

Set each initial parameter with a reasonable default.
Next to each control, add a hover tooltip explaining what the control means (in terms of epidemiology), and how it affects the simulation.
Include a clear legend indicating to the user what the colours of the individuals in the simulation mean.
</user-interface-requirements>

<hardware-interface-requirements>
The web app must run on a standard low-end laptop.
</hardware-interface-requirements>

<software-interface-requirements>
The web app must be written in vanilla html, css and javascript.
It must work in any modern browser.
</software-interface-requirements>

<functional-requirements>
- User can start a new simulation
- User can pause and resume the current simulation
- User can control the speed of the simulation (frame rate)
- User can set the population size in the simulation
- User can set the number of infected individuals at the start of the simulation
- User can control the infection length (how long individuals in the simulation are sick for)
- User can control the infectiousness of the virus in the simulation (how likely it is that the virus is transmitted on contact)
</functional-requirements>

<non-functional-requirements>
The application should not use excessive CPU, RAM or storage on the user's computer.
The app should work when I just open the index.html file on my local (no CORS errors please).
</non-functional-requirements>
