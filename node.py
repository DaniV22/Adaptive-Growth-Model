class Node():

    '''Class to store the nodes instances

    ATTRIBUTES:

        position :          a tuple containing the x and y coordinates in a lattice
        parent :            a node-object used to assign a parent to a newly added node
        score :             an integer to track the score of a node

    METHODS:

        shortest_path :    returns a list of nodes forming the shortest path (node to seed)
        update_score :     it updates the score of the node
    
    '''


    def __init__(self, position, parent, score):

        self.position = position
        self.parent = parent
        self.score = score

    def shortest_path(self):

        '''
        Method to get the list of nodes forming the shortest path,
        from the current node to the seed. It follows the nodes
        parents to arrive to the seed
        '''

        i = 0

        #Initial path
        next_node = self.parent
        path = [self, next_node]

        #Iterating over the parents until we find the seed
        while True:

            #Checking if next node is the seed
            if next_node.parent == None:
                return path
        
            #Next node
            else:
                next_node = next_node.parent
                path.append(next_node)

    def update_score(self, delta):

        '''
        A method to add (or substract) "delta"
        to the current score. It can be positive or 
        negative.
        '''
        self.score += delta