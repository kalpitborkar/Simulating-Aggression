Doves = []
Hawks = []

class Agent:
    """
    Agents are of two types : Doves and Hawks
    They compete for food and survival in this simulation
    """
    
    
    def __init__(self, strat = None, loc = None):
        """
        Initialization of agent.
        """
        self.strategy = strat
        self.location = loc
        
    def survive(self):
        pass
    
    def die(self):
        if(self.strategy == "Dove"):
            Doves.pop()
        if(self.strategy == "Hawk"):
            Hawks.pop()
            
    def add_agent(self, strat):
        new_agent = Agent(self, strat)
        if(self.strategy == "Dove"):
            Doves.append(new_agent)
        if(self.strategy == "Hawk"):
            Hawks.append(new_agent)
    
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
                
    
                
            
        