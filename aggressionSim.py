import random

Doves = []
Hawks = []


def add_agent(strat):
    new_agent = Agent(strat)
    if(strat == "Dove"):
        Doves.append(new_agent)
    if(strat == "Hawk"):
        Hawks.append(new_agent)


class Agent:
    """
    Agents are of two types : Doves and Hawks
    They compete for food and survival in this simulation
    """

    def __init__(self, strat=None, loc=None):
        """
        Initialization of agent.
        """
        self.strategy = strat
        self.location = loc

    def survive(self):
        pass

    def die(self):
        if(self.strategy == "Dove"):
            del Doves[-1]
        if(self.strategy == "Hawk"):
            del Hawks[-1]

    # def add_agent(self, strat):
    #     new_agent = Agent(self, strat)
    #     if(self.strategy == "Dove"):
    #         Doves.append(new_agent)
    #     if(self.strategy == "Hawk"):
    #         Hawks.append(new_agent)

    def survive_and_reproduce(self):
        if(self.strategy == "Dove"):
            self.add_agent(self, "Dove")
        if(self.strategy == "Hawk"):
            self.add_agent(self, "Hawk")

    def compete_with_agent(self, agent2):
        """
        Logic for survival, death and reproduction of agents when competing for food.
        """
        if(self.strategy == "Dove"):
            if(agent2.strategy == "Dove"):
                self.survive()
                agent2.survive()
            if(agent2.strategy == "Hawk"):
                self.die()
                agent2.survive_and_reproduce()
        if(self.strategy == "Hawk"):
            if(agent2.strategy == "Dove"):
                self.survive_and_reproduce()
                agent2.die()
            if(agent2.strategy == "Hawk"):
                self.die()
                agent2.die()


class FoodMap:
    """
    There are n different locations - with two pieces of food in each location
    """
    number_of_locations = 100
    food_map = [2 for x in range(0, number_of_locations)]
    agents_at_location = [[] for _ in range(0, number_of_locations)]

    def reset(self):
        for i in range(0, self.number_of_locations):
            self.food_map[i] = 2
        for i in range(0, self.number_of_locations):
            self.number_of_agents_at_location[i] = 0

    def remove_food(self, loc, quantity=1):
        self.food_map[loc] -= quantity

    def get_food_quantity(self, loc):
        return self.food_map[loc]



class Simulation:
    """This is where the simulation happens"""

    def __init__(self, number_of_doves, number_of_hawks):
        self.current_generation = 0
        self.my_food_map = FoodMap()
        for _ in range(number_of_doves):
            add_agent("Dove")
        for _ in range(number_of_hawks):
            add_agent("Hawk")

    def assign_location_to_agents(self, my_food_map: FoodMap):
        for dove in Doves:
            while(True):
                rand_loc = random.randint(0, my_food_map.number_of_locations)
                if len(my_food_map.agents_at_location[rand_loc]) < 2:
                    my_food_map.agents_at_location[rand_loc].append(dove)
                    break
        for hawk in Hawks:
            while(True):
                rand_loc = random.randint(0, my_food_map.number_of_locations)
                if len(my_food_map.agents_at_location[rand_loc]) < 2:
                    my_food_map.agents_at_location[rand_loc].append(hawk)
                    break
            

        
            

    def prepare_for_simulation(self):
        self.my_food_map.reset()

    def simulate_generation(self):
