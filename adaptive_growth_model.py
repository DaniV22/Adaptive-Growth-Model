from random import choice
from node import Node
from cluster import Cluster

def create_cluster(max_iterations, Nm, eta):

    '''
    Function to create a Cluster using the adaptive growth model,
    for a given parameters Nm and eta, and max_iterations steps

    Parameters:
        
        max_iterations :    an integer number (number of particles/nodes added)
        Nm :                a (positive) real number that determines the substracted score (it affects the steady size of the cluster)
        eta :               a (positive) real number that modifies the score of particles (it modifies the structure of the cluster)
    '''

    #File to store the cluster
    f = open(f'time_size_{Nm}_change.txt', 'w')

    #Creating the seed
    seed = Node(position=(0,0), parent=None, score=1)

    #Creating cluster
    cluster = Cluster(seed)
    cluster.empty_sites.extend(cluster.get_available_neighbors(seed))
    cluster.sites.append(seed.position)

    iter = 1

    while iter < max_iterations:

        #Next position
        while True:

            position = choice(cluster.empty_sites)
            a = cluster.get_parent(position)

            if a == 9999:
                pass
                
            else:
                parent = a
                break


        #Creating and adding next node of the cluster 
        next_node = Node(position, parent, 0)
        cluster.add_node(next_node)

        #Path from node to seed
        path = next_node.shortest_path()

        #Updating score to every node in path
        for node in path:
            node.update_score( (1 / (1 + len(path))**eta ))
           
        #We iterate over a copy of the cluster because
        #we have to remove some nodes
        cluster_copy = cluster

        for i, node in enumerate(cluster_copy.cluster):

            #Updating score
            cluster.cluster[i].update_score(-1/(Nm))

            #Removing nodes with score < 0
            if cluster.cluster[i].score < 0:

                cluster.remove_node(cluster.cluster[i])

                for n in cluster.get_neighbors_to_remove(node.position):
                    cluster.empty_sites.remove(n)

        #Writing in file the time and size
        if iter % 100 == 0:
            f.write(str(iter))
            f.write('   ')
            f.write(str(cluster.size))
            f.write('\n')

        if iter % 1000 == 0:
            print(f'Iterations = {iter} :  Size = ' + str(cluster.size))

        iter += 1

    f.close()

    return cluster


#Parameters of the model
max_iterations = 250000
eta = 1
Nm = 102400

cluster = create_cluster(max_iterations, Nm, eta)

print(f'Cluster size :  {cluster.size} nodes')

#Saving cluster in file
f = open(f'cluster_Nm_{Nm}_change.txt', 'w')
for node in cluster.cluster:
        
    f.write(str(node.position[0]))
    f.write('   ')
    f.write(str(node.position[1]))
    f.write('   ')
    f.write(str(node.score))
    f.write('\n')

f.close()
