# Simulating-Aggression
Simulating the evolution of aggression using Python.

## Simulation Idea
Simulation of N agents for a survival resource.

Iterate over X number of generations:
  - Each agent goes to a random location.
  - The `food` is shared according to the agent strategy.
  - The agent survives, dies or reproduces depending on the food quantity consumed in each interation.

## Agent rules
The simulation includes two strategies:
  - `Dov`e strategy - Passive
  - `Hawk` strategy - Aggressive

### Doves and Hawks
`Dove` shares the food if against a dove.
`Hawk` steals both pieces of food if against a dove.
No agent gets any food if both the agents are `Hawks`

## Simulation Rules
In each iteration of the simulation:
  - Each location has two pieces of `food`.
  - Consumption of a single piece of `food` leads to surival of the agent.
  - Consumption of a two pieces of `food` leads to reproduction of the agent.
  - No consumption of `food` leads to the death of the agent.
