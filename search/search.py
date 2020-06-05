# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
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
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    # "*** YOUR CODE HERE ***"
    # print "Start:", problem.getStartState()
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    # print "Start's successors:", problem.getSuccessors(problem.getStartState())

    stateMap = {}
    pathMap = {}
    visited, stack, retList = set(), util.Stack(), list()
    vertex = (problem.getStartState(), "", "")
    stack.push(vertex)
    while not stack.isEmpty() and not problem.isGoalState(vertex[0]):
        vertex = stack.pop()
        if vertex not in visited and not problem.isGoalState(vertex[0]):
            visited.add(vertex[0])
            for s in problem.getSuccessors(vertex[0]):
                if s[0] not in visited:
                    stack.push(s)
                    stateMap[s[0]] = vertex[0]
                    pathMap[s[0]] = (s[1])

    firstElemBack = vertex[0]
    while firstElemBack != problem.getStartState():
        retList.insert(0, pathMap[firstElemBack])
        firstElemBack = stateMap[firstElemBack]

    return retList


def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """

    stateMap = {}
    pathMap = {}
    visited, q, retList = set(), util.Queue(), list()
    vertex = (problem.getStartState(), "", "")
    q.push(vertex)
    while not q.isEmpty() and not problem.isGoalState(vertex[0]):
        vertex = q.pop()
        if vertex[0] not in visited and not problem.isGoalState(vertex[0]):
            visited.add(vertex[0])
            for s in problem.getSuccessors(vertex[0]):
                if s[0] not in visited and s[0] not in stateMap.keys():
                    q.push(s)
                    stateMap[s[0]] = vertex[0]
                    pathMap[s[0]] = (s[1])

    firstElemBack = vertex[0]
    while firstElemBack != problem.getStartState():
        retList.insert(0, pathMap[firstElemBack])
        firstElemBack = stateMap[firstElemBack]

    return retList



def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    stateMap = {}
    pathMap = {}
    costMap = {}
    costMap[problem.getStartState()] = 0
    visited, pq, retList = set(), util.PriorityQueue(), list()
    vertex = (problem.getStartState(), "", "")
    pq.push(vertex,0)
    while not pq.isEmpty() and not problem.isGoalState(vertex[0]):
        vertex = pq.pop()
        if vertex[0] not in visited and not problem.isGoalState(vertex[0]):
            visited.add(vertex[0])
            for s in problem.getSuccessors(vertex[0]):
                cost = float(s[2]) + costMap[vertex[0]]
                if s[0] not in costMap.keys() or cost < costMap[s[0]]:
                    pq.push(s, cost)
                    stateMap[s[0]] = vertex[0]
                    pathMap[s[0]] = (s[1])
                    costMap[s[0]] = cost


    firstElemBack = vertex[0]
    while firstElemBack != problem.getStartState():
        retList.insert(0, pathMap[firstElemBack])
        firstElemBack = stateMap[firstElemBack]

    return retList



def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "Search the node that has the lowest combined cost and heuristic first."
    stateMap = {}
    pathMap = {}
    costMap = {}
    costMap[problem.getStartState()] = 0
    visited, pq, retList = set(), util.PriorityQueue(), list()
    vertex = (problem.getStartState(), "", "")
    pq.push(vertex, 0)
    while not pq.isEmpty() and not problem.isGoalState(vertex[0]):
        vertex = pq.pop()
        if vertex[0] not in visited and not problem.isGoalState(vertex[0]):
            visited.add(vertex[0])
            for s in problem.getSuccessors(vertex[0]):
                cost = float(s[2]) + costMap[vertex[0]] + heuristic(s[0], problem)
                if s[0] not in costMap.keys() or cost < costMap[s[0]]:
                    pq.push(s, cost)
                    stateMap[s[0]] = vertex[0]
                    pathMap[s[0]] = (s[1])
                    costMap[s[0]] = float(s[2]) + float(costMap[vertex[0]])

    firstElemBack = vertex[0]
    while firstElemBack != problem.getStartState():
        retList.insert(0, pathMap[firstElemBack])
        firstElemBack = stateMap[firstElemBack]

    return retList



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
