class Cluster():

    '''
    A Class to store the cluster instances

    ATTRIBUTES:

        cluster :                   a list to store the nodes in the cluster
        sites :                     a list to store the positions of the cluster
        empty_sites :               a list to store the empty sites in the border of the cluster
        size :                      an integer to store the size (number of nodes) of the cluster

    METHODS:

        get_available_neighbors :   returns a list of available neighbors of a node
        get_neighbors_to_remove :   returns a list of neighbors to remove from empty_sites
        get_neighbors :             returns a list of neighbors of a given position
        get_parent :                returns the parent node of a new added node
        add_node :                  adds a node to the cluster
        remove_node :               removes a node from the cluster 

    '''

    def __init__(self, seed):
        
        self.cluster = [seed]
        self.sites = []
        self.empty_sites = []
        self.size = len(self.cluster)

    def get_available_neighbors(self, node):

        '''
        Method to get a list of empty neighbors for a given node. We 
        consider that a site is available if it has not a node (from cluster)
        and it is not already in the list of empty sites
        
        '''

        #List of all neighbors for a given node
        site_neighbors = self.get_neighbors(node.position)

        #Choosing available neighbors
        empty_neighbors = [n for n in site_neighbors if n not in self.sites]

        return empty_neighbors

    def get_neighbors_to_remove(self, site):

        '''
        A function to get the neighbors of a site that are empty (to remove them).

        '''
        #List of neighbors
        neighbors = self.get_neighbors(site)

        #List of empty neighbors
        empty_neighbors = [n for n in neighbors if n in self.empty_sites]

        return empty_neighbors

    def get_neighbors(self, node_pos):

        '''
        Method to get all neighbors for a given position
        '''

        site_neighbors = [
            (node_pos[0] + 1, node_pos[1]),
            (node_pos[0] - 1, node_pos[1]),
            (node_pos[0], node_pos[1] + 1),
            (node_pos[0], node_pos[1] - 1)]

        return site_neighbors

    def get_parent(self, node_pos):

        '''
        A method to find the parent for a given position. It is used
        when adding a new node to cluster, to assign a parent to the
        newly added node.

        If the position has two possible parents, we assign the first.
        An improvement could be to assign the parent that leads to
        the shortest path. 
        '''

        #Iterating over every node in cluster
        for node in self.cluster:

            #Neighbors of the current node
            node_neighbors = self.get_neighbors(node.position)

            #If the new node is in the neighbors of a 
            # node, we assign it to that
            if node_pos in node_neighbors:
                return node

        #If we do not find a parent (error)
        return 9999

    def add_node(self, node):

        '''
        A method to add a node to the cluster. It updates
        also other attributes (size, sites, empty sites...)
        '''

        #Adding nodes and updating attributes
        self.cluster.append(node)
        self.size += 1
        self.empty_sites.extend(self.get_available_neighbors(node))
        self.empty_sites.remove(node.position)
        self.sites.append(node.position)

    def remove_node(self, node):

        '''
        A method to remove a node from the cluster. It updates
        also other attributes (size, sites, empty sites...)
        
        '''

        #Removing node from cluster and updating attributes
        self.cluster.remove(node)
        self.size += -1
        self.sites.remove(node.position)
        self.empty_sites.append(node.position)