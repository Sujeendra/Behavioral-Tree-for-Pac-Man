from ActionNode import ActionNode
from NodeStatus import *
import time
import random
from distanceCalculator import *
from searchAgents import *
import numpy as np

class ActionTest(ActionNode):

    def __init__(self,name):
        ActionNode.__init__(self,name)


    def Execute(self,args):
        self.SetStatus(NodeStatus.Running)
        self.SetColor(NodeColor.Gray)

        while self.GetStatus() == NodeStatus.Running:
            #print self.name + ' executing'
            time.sleep(10)

        self.SetStatus(NodeStatus.Success)
        self.SetColor(NodeColor.Green)




class Greedy(ActionNode):

    def __init__(self,name):
        ActionNode.__init__(self,name)
        self.distances = None

    def Execute(self,args):
        self.SetStatus(NodeStatus.Running)
        self.SetColor(NodeColor.Gray)
        self.Directions = args.Directions
        self.distances = args.distances
        print('Executing Action Greedy')
        args.action_executed.SetAction(self.getAction(args.state))
        self.SetStatus(NodeStatus.Success)
        self.SetColor(NodeColor.Green)




    def getAction(self, state):
        # Generate candidate actions
        legal = state.getLegalPacmanActions()
        if self.Directions.STOP in legal: legal.remove(self.Directions.STOP)
        successors = [(state.generateSuccessor(0, action), action) for action in legal]
        scored = [(self.scoreEvaluation(state), action) for state, action in successors]
        bestScore = max(scored)[0]
        bestActions = [pair[1] for pair in scored if pair[0] == bestScore]
        return random.choice(bestActions)

    def scoreEvaluation(self,state):
        return state.getScore()

class Custom(ActionNode):

    def __init__(self,name):
        ActionNode.__init__(self,name)
        self.index = 0  # Pacman is always agent index 0
        evalFn = 'evaluationFunction'
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = 6

    def Execute(self,args):
        self.SetStatus(NodeStatus.Running)
        self.SetColor(NodeColor.Gray)
        self.Directions = args.Directions
        self.distances = args.distances
        print('Executing Action Custom')
        args.action_executed.SetAction(self.getAction(args.state))
        self.SetStatus(NodeStatus.Success)
        self.SetColor(NodeColor.Green)

    def deepSearch(self, depth, gameState):
        if len(getLegalActionsNoStop(0, gameState)) == 0 or gameState.isLose() \
                or depth == self.depth or gameState.isWin():
            return self.evaluationFunction(gameState) - depth * 100
        newPos = gameState.getPacmanPosition()
        gameState.data.layout.walls[newPos[0]][newPos[1]] = True
        val = []
        for action in getLegalActionsNoStop(0, gameState):
            val.append(self.deepSearch(depth + 1, gameState.generateSuccessor(0, action)))
        max_val = max(val)
        gameState.data.layout.walls[newPos[0]][newPos[1]] = False
        return max_val + self.evaluationFunction(gameState) - depth * 100

    def getAction(self, gameState):

        # as the food begins running out it is better to decrease the research depth, in an empty maze there is not too much to search
        if gameState.getNumFood() <= self.depth:
            self.depth = gameState.getNumFood() - 1
        possibleActions = getLegalActionsNoStop(0, gameState)
        action_scores = []
        newPos = gameState.getPacmanPosition()
        gameState.data.layout.walls[newPos[0]][newPos[1]] = True
        for action in possibleActions:
            action_scores.append(self.deepSearch(0, gameState.generateSuccessor(0, action)))
        gameState.data.layout.walls[newPos[0]][newPos[1]] = False
        max_action = max(action_scores)
        max_indices = [index for index in range(len(action_scores)) if action_scores[index] == max_action]
        chosenIndex = random.choice(max_indices)

        """print(possibleActions)
        print(action_scores)
        input()"""

        return possibleActions[chosenIndex]


    def scoreEvaluationFunction(currentGameState):
        return currentGameState.getScore()


def getLegalActionsNoStop(index, gameState):
    possibleActions = gameState.getLegalActions(index)
    if Directions.STOP in possibleActions:
        possibleActions.remove(Directions.STOP)
    return possibleActions



def evaluationFunction(currentGameState):

        newPos = currentGameState.getPacmanPosition()
        newFood = currentGameState.getFood()
        newGhostStates = currentGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        """Calculate distance to the nearest food"""
        newFoodList = np.array(newFood.asList())
        distanceToFood = [util.euclideanDistance(newPos, food) for food in newFoodList]
        min_food_distance = 0
        if len(newFoodList) > 0:
            min_food_distance = distanceToFood[np.argmin(distanceToFood)]

        """Calculate the distance to nearest ghost"""
        ghostPositions = np.array(currentGameState.getGhostPositions())
        if len(ghostPositions) > 0:
            distanceToGhost = [util.manhattanDistance(newPos, ghost) for ghost in ghostPositions]
            min_ghost_distance = distanceToGhost[np.argmin(distanceToGhost)]
            nearestGhostScaredTime = newScaredTimes[np.argmin(distanceToGhost)]
            # avoid certain death
            if min_ghost_distance <= 1 and nearestGhostScaredTime == 0:
                return -999999
            # eat a scared ghost
            if min_ghost_distance <= 1 and nearestGhostScaredTime > 0:
                return 999999

        return currentGameState.getScore() * 5 - min_food_distance

class Chase(ActionNode):

    def __init__(self,name):
        ActionNode.__init__(self,name)
        self.distances = None
        self.distance_calculator = None

    def Execute(self,args):
        if self.distance_calculator is None:
            self.distance_calculator = Distancer(args.state.data.layout)
        self.SetStatus(NodeStatus.Running)
        self.SetColor(NodeColor.Gray)
        self.Directions = args.Directions
        self.distances = args.distances
        print('Executing Action Chase')
        args.action_executed.SetAction(self.getAction(args.state))
        self.SetStatus(NodeStatus.Success)
        self.SetColor(NodeColor.Green)




    def getAction(self, state):
        # Generate candidate actions
        legal = state.getLegalPacmanActions()
        if self.Directions.STOP in legal: legal.remove(self.Directions.STOP)

        successors = [(state.generateSuccessor(0, action), action) for action in legal]
        scored = [(self.closestDistance(state), action) for state, action in successors]
        bestScore = min(scored)[0] #get to the one with the minumim distance
        bestActions = [pair[1] for pair in scored if pair[0] == bestScore]
        actionperformed = random.choice(bestActions)
        # print ('successors', successors)
        # print ('scored', scored)
        #print ('actionperformed',actionperformed)
        #input("Press Enter to continue...")

        return actionperformed

    def closestDistance(self,state):
        minumim_distance = 999 #distance to the closest ghost

        for i in range(state.getNumAgents() - 1):
            ghostState = state.getGhostState(i + 1)
            isGhostScared = ghostState.scaredTimer > 0
            if isGhostScared:
                distance = self.distance_calculator.getDistance(state.getPacmanPosition(), state.getGhostPosition(i+1))
                print('distance from ghost ', i, 'is: ', distance )
                minumim_distance = min (minumim_distance, distance)

        return minumim_distance


class KeepDistance(ActionNode):

    def __init__(self,name):
        ActionNode.__init__(self,name)
        self.distances = None
        self.distance_calculator = None
        self.old_distance = 0


    def Execute(self,args):
        if self.distance_calculator is None:
            self.distance_calculator = Distancer(args.state.data.layout)
        self.SetStatus(NodeStatus.Running)
        self.SetColor(NodeColor.Gray)
        self.Directions = args.Directions
        self.distances = args.distances
        print('Executing Action Keep Distance')
        args.action_executed.SetAction(self.getAction(args.state))
        self.SetStatus(NodeStatus.Success)
        self.SetColor(NodeColor.Green)




    def getAction(self, state):
        # Generate candidate actions
        legal = state.getLegalPacmanActions()
        if self.Directions.STOP in legal: legal.remove(self.Directions.STOP)

        successors = [(state.generateSuccessor(0, action), action) for action in legal]
        scored = [(self.sumDistance(state), action) for state, action in successors]

        bestScore = max(scored)[0]
        bestActions = [pair[1] for pair in scored if pair[0] == bestScore]
        actionperformed = random.choice(bestActions)
        # print ('successors', successors)
        # print ('scored', scored)
        # print ('actionperformed',actionperformed)
        #input("Press Enter to continue...")

        return actionperformed

    def sumDistance(self,state):
        sum_distance = 0
        for i in range(state.getNumAgents() - 1):
            ghostState = state.getGhostState(i + 1)
            isGhostScared = ghostState.scaredTimer > 0
            if not isGhostScared:
                sum_distance += self.distance_calculator.getDistance(state.getPacmanPosition(), state.getGhostPosition(i+1))
        if float(sum_distance).is_integer():
            return sum_distance
            self.old_distance = sum_distance
        else:
            return self.old_distance

class Escape(ActionNode):

    def __init__(self,name):
        ActionNode.__init__(self,name)
        self.distances = None
        self.distance_calculator = None
        self.old_distance = 1000


    def Execute(self,args):
        if self.distance_calculator is None:
            self.distance_calculator = Distancer(args.state.data.layout)
        self.SetStatus(NodeStatus.Running)
        self.SetColor(NodeColor.Gray)
        self.Directions = args.Directions
        self.distances = args.distances
        print('Executing Action Escape')
        args.action_executed.SetAction(self.getAction(args.state))
        self.SetStatus(NodeStatus.Success)
        self.SetColor(NodeColor.Green)




    def getAction(self, state):
        # Generate candidate actions
        legal = state.getLegalPacmanActions()
        if self.Directions.STOP in legal: legal.remove(self.Directions.STOP)



        successors = [(state.generateSuccessor(0, action), action) for action in legal]
        scored = [(self.closestDistance(state), action) for state, action in successors]

        bestScore = max(scored)[0]
        bestActions = [pair[1] for pair in scored if pair[0] == bestScore]
        actionperformed = random.choice(bestActions)
        # print ('successors', successors)
        # print ('scored', scored)
        # print ('actionperformed',actionperformed)
        #input("Press Enter to continue...")

        return actionperformed

    def closestDistance(self,state):
        closest = 1000
        for i in range(state.getNumAgents() - 1):
            ghostState = state.getGhostState(i + 1)
            isGhostScared = ghostState.scaredTimer > 0
            if not isGhostScared:
                closest = min(closest,
                              self.distance_calculator.getDistance(state.getPacmanPosition(), state.getGhostPosition(i+1)))
        if float(closest).is_integer():
            return closest
            self.old_distance = closest
        else:
            return self.old_distance





class ClosestDotSearch(ActionNode):

    def __init__(self,name):
        ActionNode.__init__(self,name)
        self.agent = ClosestDotSearchAgent()
        self.init = False

    def Execute(self,args):
        if not self.init:
            self.agent.registerInitialState(args.state)
            self.init =  True
        self.SetStatus(NodeStatus.Running)
        self.SetColor(NodeColor.Gray)
        self.Directions = args.Directions
        self.distances = args.distances
        print('Executing Action Search')
        legal = args.state.getLegalPacmanActions()
        if self.Directions.STOP in legal: legal.remove(self.Directions.STOP)

        action_executed = self.agent.getAction(args.state)

        if action_executed in legal:
            args.action_executed.SetAction(action_executed)
            self.SetStatus(NodeStatus.Success)
            self.SetColor(NodeColor.Green)
        else:
            #handle illegal move
            self.SetStatus(NodeStatus.Failure)
            self.SetColor(NodeColor.Red)







