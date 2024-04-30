# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
"""
  
   #use a stack data structure, so that 
   # we get a LIFO queuing policy,
   # the search explores from the last node visited 
   # we use fringe to keep track of the nodes 
   # to be explored 

    fringe = util.Stack()

  # since we were asked for a graph search
  # we need to keep track of the explored nodes 
  # explored is a list of the explored nodes
    explored = []

  # we create an list containing the actions 
  # we take to reach a certain state

    actionList = []

  # we add the start state to the fringe 
  # also with the empty set of actions

    fringe.push((problem.getStartState(), actionList))

   # create a loop that will run until the fringe is empty

    while fringe: 
        # remove and return the information about
        # the next node along with its associated actions
        # and assign it to the node and actions variables
        node, actions = fringe.pop()
      # if the node is not yet in the explored list, 
      # we add it to the explored list
        if not node in explored:
            explored.append(node)
            # if the node is a goal state, 
            # we are done and we return the set of actions
            if problem.isGoalState(node): 
               return actions
            # otherwhise, we iterate through the successors 
            for successor in problem.getSuccessors(node):
              # a tuple composed of three variables,
              # containing information about the successor
              coordinate, direction, cost= successor 
              # a list containing the sequence of actions 
              # to reach the successor
              # we extend the current list of actions 
              # with the new direction obtained 
              # from the successor
              nextActions = actions + [direction]
              # we add the new coordinates and 
              # list of actions to the fringe
              fringe.push((coordinate, nextActions))

    
    
    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # use a Queue data structure, so that we get a FIFO
    # priority queue, the search explores all the nodes 
    # on one level before going foreward
    # we use fringe to keep track of the nodes 
    # to be explored 

    fringe = util.Queue()

    # since we were asked for a graph search
    # we need to keep track of the explored nodes, 
    # explored is a list of the explored nodes
    explored = []

    # we create an list containing the actions 
    # we take to reach a certain state

    actionList = []

    # we add the start state to the fringe 
    # also with the empty set of actions

    fringe.push((problem.getStartState(), actionList))

    # create a loop that will run until the fringe is empty

    while fringe: 
        # remove and return the information about
        # the next node along with its associated actions
        # and assign it to the node and actions variables
        node, actions = fringe.pop()
        # if the node is not yet in the explored list
        # we add it to it
        if not node in explored:
            explored.append(node)
            # if the node is a goal state we are done 
            # and can return the list of actions
            if problem.isGoalState(node): 
               return actions
            # we iterate through the successors of the node
            for successor in problem.getSuccessors(node):
              # tuple containing information 
              # about the successor
              coordinate, direction, cost= successor 
              # a list containing the sequence of actions 
              # to reach the successor
              # we extend the current list of actions 
              # with the new direction obtained 
              # from the successor
              nextActions = actions + [direction]
              # we add the new coordinates and 
              # list of actions to the fringe
              fringe.push((coordinate, nextActions))


    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
  
    # use a PriorityQueue data structure so that we get 
    # a priority queue that retrieves 
    # the lowest priority first
    fringe = util.PriorityQueue()

   # make an empty list of explored nodes
    explored = []
  
   # make an empty list of actions
    actionList = []
  
   # place the starting point in the priority queue, 
   # with a priority of 0 (as the initial cost)
    fringe.push((problem.getStartState(), actionList), 0)
    while fringe:
      # removes and retrieves the node with the least cost
      # from the priority queue along with 
      # the actions associated to it 
      node, actions = fringe.pop()
      # if the node is not yet in the explored list
      # we add it to it
      if not node in explored:
          explored.append(node)
          # if the node is a goal state we are done 
          # and can return the list of actions
          if problem.isGoalState(node):
              return actions
          # we iterate through the successors of the node
          for successor in problem.getSuccessors(node):
              # tuple containing information 
              # about the successor
              coordinate, direction, cost = successor
              # a list containing the sequence of actions 
              # to reach the successor
              # we extend the current list of actions 
              # with the new direction obtained 
              # from the successor
              nextActions = actions + [direction]
              # calculates the cost of the next action
              nextCost = problem.getCostOfActions(nextActions)
              # adds the successor to the priority queue
              # with the updated cost
              fringe.push((coordinate, nextActions), nextCost)

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
  
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # use a PriorityQueue data structure so that we get 
    # a prioritization queue based on cost 
    # and heuristic value
    fringe = util.PriorityQueue()
    # make an empty list of explored nodes
    explored = []
    # make an empty list of actions
    actionList = []
    # place the starting point in the priority queue
    # with a priority of the combined cost and 
    # heuristic value
    fringe.push((problem.getStartState(), actionList), heuristic(problem.getStartState(), problem))

    # execute as loing as the fringe is not empty
    while fringe:
      # removes and retrieves the node with 
      # the lowest cmobined cost and heuristic value
      # from the priority queue along with 
      # the actions associated to it
      node, actions = fringe.pop() 
      # if the node is not yet in the explored list
      # we add it to it
      if not node in explored:
          explored.append(node)
          # if the node is a goal state we are done 
          # and can return the list of actions
          if problem.isGoalState(node):
              return actions
          # we iterate through the successors of the node
          for successor in problem.getSuccessors(node):
              # tuple containing information 
              # about the successor
              coordinate, direction, cost = successor
              # a list containing the sequence of actions 
              # to reach the successor
              # we extend the current list of actions 
              # with the new direction obtained 
              # from the successor
              nextActions = actions + [direction]
              # calculates the combined cost and 
              # heuristic value of the next action 
              nextCost = problem.getCostOfActions(nextActions) + \
                             heuristic(coordinate, problem)
              # adds the successor to the priority queue 
              # with the updated combined cost 
              # and heuristic value
              fringe.push((coordinate, nextActions), nextCost)
    
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
