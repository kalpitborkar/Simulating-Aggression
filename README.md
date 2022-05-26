# Simulating-Aggression
Simulating the evolution of aggression using Python.

## Simulation Idea
Simulation of N agents for a survival resource.

Iterate over X number of generations:
  - Each agent goes to a random location.
  - The `food` is shared according to the agent strategy.
  - The agent survives, dies or reproduces depending on the food quantity consumed in each interation.

## Agent rules
The `Simulation` includes two strategies:
  - `Dove` strategy - Passive
  - `Hawk` strategy - Aggressive


- `Dove` shares the food if against a dove.
- `Hawk` steals both pieces of food if against a dove.
- No agent gets any food if both the agents are `Hawks`

## Simulation Rules
In each iteration of `Simulation`:
  - Each location has two pieces of `food`.
  - Consumption of a single piece of `food` leads to surival of the agent.
  - Consumption of a two pieces of `food` leads to reproduction of the agent.
  - No consumption of `food` leads to the death of the agent.

## References
This simulation is based on [Simulating the Evolution of Aggression](https://www.youtube.com/watch?v=YNMkADpvO4w&ab_channel=Primer) by [Primer](https://www.youtube.com/channel/UCKzJFdi57J53Vr_BkTfN3uQ)
