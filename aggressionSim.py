from pkg_resources import safe_version
import random

class Agent:
    food = 0
    strategy = None
    location = None

    def __init__(self, strategy):
        self.strategy = strategy

    def updateFood(self, food):
        self.food = food


class FoodMap:
    foodQuantity = 100
    foodMap = []

    def __init__(self):
        for i in range(self.foodQuantity):
            self.foodMap.append(2)

    def removeFoodFromMap(self, location):  # if food is eaten, make it zero
        self.foodMap[location] = 0

    def resetFoodMap(self):
        for i in range(self.foodQuantity):
            self.foodMap[i] = 2


class Simulation:

    numberOfGenstoSimulate = 100
    
    # lists contaning the two different types of agents - "doves" and "hawks"
    agentType1 = [] #doves
    agentType2 = [] #hawks
    
    #initialize foodMap
    myFoodMap = FoodMap()
    
    def initializeAgents(agentType1, agentType2, initialNumberOfType1Agents, initialNumberOfType2Agents):
        """
        Creates agent objects and initializes the lists agentType1 and agentType2
        """
        for i in range(initialNumberOfType1Agents):
            agentType1.append(Agent("Dove"))
        for i in range(initialNumberOfType2Agents):
            agentType2.append(Agent("Hawk"))
        
    def setAgentLocations(agentType1, agentType2, myFoodMap):
        """
        Locates agents to food on the map - maximum two agents at a certain location
        """
            
        
        
    def competeAgents(agentType1, agentType2, location):
        """
        Agents compete for food - survive, die or reproduce depending on the conditions - update lists agentType1 and agentType2
        """
        
    
    
    for currGen in range(numberOfGenstoSimulate):
        #todo
        

        
        
        
