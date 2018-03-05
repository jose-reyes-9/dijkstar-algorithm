# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 18:52:53 2018

@author: Jose
"""


""" Complete the two functions
findFinishLabel
and
calculatePathStartToFinish
and 
fix any errors so that
shortestPath(graph, start,finish) works
for example
if testD is as below
shortestPath(testD, 'a', 'f')
should return 
 {'a':0, 'b':20,'c':40,'d':15, 'e':30,'f':55}  55   ['a', 'b', 'e', 'c', 'f']

    """
    
    
testD =  {'a': [['b', 20], ['d', 15]],
 'b': [['a', 20], ['c', 35], ['e', 10]],
 'c': [['b', 35], ['e', 10], ['f', 15]],
 'd': [['a', 15], ['e', 20]],
 'e': [['d', 20], ['b', 10], ['c', 10], ['f', 35]],
 'f': [['c', 15], ['e', 35]]}
   
france = {'Bordeaux': [['Nantes', 150], ['Vichy', 450], ['Toulouse', 200]],
 'Briancon': [['Strasbourg', 400], ['Lyon', 200], ['Nice', 250]],
 'Lille': [['Paris', 350], ['Vichy', 400], ['Strasbourg', 500]],
 'Lyon': [['Toulouse', 600],
  ['Vichy', 250],
  ['Strasbourg', 650],
  ['Briancon', 200],
  ['Marseille', 150]],
 'Marseille': [['Nice', 150], ['Lyon', 150], ['Toulouse', 300]],
 'Nantes': [['Paris', 300], ['Bordeaux', 150]],
 'Nice': [['Briancon', 250], ['Marseille', 150]],
 'Paris': [['Nantes', 300], ['Vichy', 350], ['Lille', 500]],
 'Strasbourg': [['Lille', 500], ['Lyon', 650], ['Briancon', 400]],
 'Toulouse': [['Bordeaux', 200],
  ['Vichy', 300],
  ['Lyon', 600],
  ['Marseille', 300]],
 'Vichy': [['Toulouse', 300],
  ['Bordeaux', 450],
  ['Paris', 350],
  ['Lille', 400],
  ['Lyon', 250]]}
 
    
def notAllFalse(shortestPathDictionary):   ### THIS WAS A MISTAKE.  USE notAllTrue
    """spd lok like {node:[label, tOrF], node: ...}
    just and together all the true false values"""
    returnValue = True
    for value in shortestPathDictionary.values():
        returnValue = returnValue  and value[1]
    return(returnValue)
    
def notAllTrue(shortestPathDictionary):  # ie some still False
    """spd lok like {node:[label, tOrF], node: ...}
    retrurn True if not all labels are True
    that is if any one or more is False
    return True if any label is False"""
    returnValue = False
    for value in shortestPathDictionary.values():
        if not(value[1]):  ## So if any value is False, return True from this function
            returnValue = True
            break
    return(returnValue)
    
def calcTempLabel(node, lastAdded, spd, graph):
    """
    Take distance so far to lastAdded plus distance from lastSAdded to node
    and compare that to nodes label.  If shorter, update.  Return distance.
    """
    #print('\ncalcTempLabel(node, lastAdded, spd, graph)', node, lastAdded) #, spd, graph)
    upToLast = spd[lastAdded]  ## gives the list [distanceSoFar, TrueOrFalse]
    edgeList = graph[lastAdded]   ## graph[lastAdded] is a list of 
            ## [edgeLength, endNode] for nodes one edge away from lastAdded
            ## if that node is False in our spd we should add it to the frontier
    edgeNameList = []  ## bild a list of just the node names in edgeList
    for edge in edgeList:
        edgeNameList.append(edge[0])
    index = edgeNameList.index(node)  ## find node in the list of nadenames
    arcLen = edgeList[index][1]  ## find the length of the edge from lasteAdded to node
    #print('\nupToLast', upToLast, 'edgeList', edgeList, 'edgeNameList', edgeNameList)
    #print('\nindex', index, 'arcLen', arcLen)
    #print('\nupToLast', upToLast[0], 'arcLen', arcLen)
    newLabelLength = upToLast[0] + arcLen
    #print('\nnewLabelLength', newLabelLength)
    oldLabel = spd[node]
    #print('\noldLabel', oldLabel)
    if newLabelLength < oldLabel[0]:
        # so update the length to this new calculation since it is shorter
        labelLength = newLabelLength 
        spd[node][2] = lastAdded ## and update the predecessor slot
    else:  ## just to be explicit
        labelLength = oldLabel[0]
        ## and predecessor does not get updated
    #print('\nRetunr newLength',newLabelLength)
    return(labelLength, spd[node][2]) 
        
def findShortest(frontier, spd):
    """
    Return  bestLabel, bestNode from the frontier best is shortest label
    bestlabel should be distance and bestNode the nodename
    """
    bestLabel = 9999999  ## Classic find the smallest, set start to huge
    bestNode = None   ## set name of smallest to none (empty bucket)
    for node in frontier:
        #print('\nspd[node]',spd[node])
        if spd[node][0] < bestLabel:  ## if better than best so far, update
            bestLabel = spd[node][0]
            bestNode = node
    return( bestLabel, bestNode)
    
def findFinishLabel(finish, spd):  ## Hint I added spd to arg list, you will need it.
    """
    Your comment here.  Describe what this fucntion should do
    """
    total = 0				## totalLabel
    currentLetter = 'f'		## sets current letter to use in loop

    for x in range(4):
    	nodeValue = spd[currentLetter] 	## gets the value to the key node (returns a list with 3 items)
    	predecessor = nodeValue[-1]    	## gets last item in that list (the predecessor node)
    	weight = nodeValue[0] 			## the weight of the node
    	total = total + weight 	        ## adds weight to total label
    	currentLetter = predecessor   	## updates current letter to predecessor to continue path traceback
    return(total) # None is not right
            
def calculatePathStartToFinish(finish, spd):
    """
    This function will traceback all nodes and adds them to a final path list
    BTW   What might you add (or did I already add)
    to our structures so we can find this path?
    """
    ## spd [last index of spd >> last index of the key >> add to list]
    finalPath = ['f'] 		## a list containing the final path
    currentLetter = 'f'		## sets current letter to use in loop

    for x in range(4):
    	nodeValue = spd[currentLetter] 	## gets the value to the key node (returns a list with 3 items)
    	predecessor = nodeValue[-1]    	## gets last item in that list (the predecessor node)
    	finalPath.insert(0,predecessor) 	## appends that letter to the final path list 
    	currentLetter = predecessor   	## updates current letter to predecessor to continue path traceback

    return(finalPath) # None is not right
           
  
def shortestPath(graph, start,finish):
    """Takes a graph, a weighted graph, represented as a dictionary,
    {node: [(neighborNode, edgeWeight), ...], node: ...} and satrt node,
    and finish node.  Returns three things,
    a dictionary {node: length of path start to node, ...}
    length of shortest path to finish,
    shortest path to finish, that is a list [start, node, node, ..., finish]"""
    spd = {}  ## an empty dictionary which will hold our estimates of distances
    ## as we go 
    ## someestimates will be marked True meaning permanent
    ## we can also keep track of predecessors here
    ## so what doesspd look like?  Ir is a dictionary.
    ## keys inspd are node Names, (e.g spd[start]  or spd['a'] or spd['Paris'])
    ## so a value in spd looks like 
    ## a list [distanceSoFar, PermanentTrueOrFalse, predecessorNodeNameorNone ]
    
    for node in graph.keys():
        spd[node]  = [999999, False, None]  ## init all estimates to infinity
        ## and no predecessors
    spd[start] = [0, True, None]  ## mark the start node as distance 0 
    ## and mark it True (i.e. permanent,not temprorary), 
    ## and set the predecessor of start to None
    lastAdded = start  ## lastAdded is the one maerked True most recently
    frontier = {start}  ## the frontier set holds all nodes one edge
    ## away from our marked set (this start will get removed at next step)
    while notAllTrue(spd):  ## keep going until all are marked True
        frontier.remove(lastAdded)  ## now that lastAdded is True, 
        ## remove it from frontier
        #print('\ngraph[lastAdded]', graph[lastAdded])
        newlyAddedToFrontier = set()
        for nodePair in graph[lastAdded]:  ## graph[lastAdded] is a list of 
            ## [edgeLength, endNode] for nodes one edge away from lastAdded
            ## if that node is False in our spd we should add it to the frontier
            if spd[nodePair[0]][1] == False:
                frontier.add(nodePair[0])
                newlyAddedToFrontier.add(nodePair[0])
        #print('\nnewlyAddedToFrontier', newlyAddedToFrontier)
        for node in newlyAddedToFrontier:
            ## for each node in newlyAddedToFrontier, check if there is now a 
            ## shorter temp label (dist fromlastAdded to node)
            ## this only matters for nodes one edge from lastAdded
            newLabel, currentPredecessor  = calcTempLabel(node, lastAdded, spd, graph)
            spd[node] = [newLabel, False, currentPredecessor]
        bestLabel, bestNode = findShortest(frontier, spd) ## best label
        #print('\nbestLabel, bestNode', bestLabel, bestNode)
        spd[bestNode][0] = bestLabel
        spd[bestNode][1] =  True  ## gets promoted to True
        
        lastAdded = bestNode  ## and that nodebecomes lastAdded
    #print('spd now', spd)
    #print('\n')
    finishLabel = findFinishLabel(finish, spd)
    path = calculatePathStartToFinish(finish, spd)
    print('\nspd:\n', spd)
    print('\nfinishLabel:\n', finishLabel)
    print('\n path:\n', path)
    
    return(spd, finishLabel, path)
               
if __name__ == '__main__':
    shortestPath(testD,'a', 'f')
    
    