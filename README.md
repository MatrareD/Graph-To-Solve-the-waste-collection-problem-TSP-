# Python TSP solver for waste collection 
In a bid to entrance into a french engineer school, I had to work on the theme "Transition, Transformation, Conversion". Therefore, I decided to focus on the waste collection probleme in Bordeaux (French City).
First, I wanted to work on household daily waste, but there were too much difficulties (and in the real life, the optimisation depends on on-field agents' experience).
This is why I wanted to study the situation for the voluntary drop-off points (VDP) (glass columns or alimentary waste) whose informatic optimisation is used by private companies or municipalities.

Thanks to openstreetmap contributors : 
https://www.openstreetmap.org/#map=13/44.84133/-0.5805
you can have access to all data that you need. Indeed, the name of the differents roads, the properties of the ways and the direction of traffic being extrated, I was able to build a graph of Bordeaux from scratch. The following work will be done on a specif neighborhood : the Golden Triangle of Bordeaux, but it will work the same way for the others. 

![Ville](https://github.com/user-attachments/assets/580a785a-8576-4683-ae72-9578e8f0ab2b)

The algorithm the most important of this project is the shortest path between two vertices : Dijkstra algorithm. It provides the real distance in my neighborhood between two intersections. This is how it works: 
0°) Every neighbor is at an infinite distance from the initial vertex
1°) At each step, every distance between a visited vertex and the initial one is actualised to be the sortest.
2°) The final vertex is visited, we take the sortest path between this and the initial one. 
There is a clear example : 

![Dijkstra](https://github.com/user-attachments/assets/12e1c11a-aeaf-4de0-ab2b-cbdbcb25b198)

Let's now focus on the waste collection : 
There are several points that have to be collected in Bordeaux, and I will put these specific vertices in a list called VDP (voluntary drop-off points). The idea is to find the shortest path to join them all and to go back to my initial vertex 0 (called the outlet). This is an example of what we call " Travelling Salesman Problem" (TSP).
To find them, you can search to the municipality that gives every information. Bordeaux' one is the following adress: 
https://www.bordeaux-metropole.fr/a-votre-service/services-aux-particuliers/gerer-reduire-mes-dechets/je-trie-mes-dechets/bornes-a (glass) and https://geo.bordeaux-metropole.fr/composteurs/index.html?context=QQHv (alimentary)

![VDP](https://github.com/user-attachments/assets/dbc08f17-d8be-4683-94b0-216eae970251)4329-8ed9-d6a63313ea31)


<> A naive idea could be to see where is the closest VDP, with a distance as the crow flies, and to reach it the fastest than you can, and do it again until every point is collected. The issue is that such a method can not work in a tiny neighborhood where most of the roads have a single traffic direction, the closest as the crow flies is not really the closest of the initial vertex in such a city. 
Here is an example : 

![Naive algorithm](https://github.com/user-attachments/assets/de2fb36a-5a39-4329-8ed9-d6a63313ea31)

<> This is why you must use the 'real' distance given by Dijkstra algorithm, in order to consider the geometry of the city. However, this is still unefficient, because there are some points that you are collecting twice: I invite you to look at the following exemple. In green, there is the beggining of the path and the end in blue : the 62 vertex is collected at the start ( green ) and at the end of the algorithm ( blue ). This shows that this simple idea is not enough to solve the TSP. 

![First relevant method](https://github.com/user-attachments/assets/8fccaefb-bc0a-4074-bc47-e11b8a5abcb3)

<> Therefore I had to think about a better method. The one I found the most relevant was the Ant Colony Optimization. To go further, I found the work of Strikingloo very interesting : https://strikingloo.github.io/ant-colony-optimization-tsp, but I will try to explain how it works and to give a first idea of algorithm. The idea is to send a group of several ants, and to let them travelling around my city. They have a transition probability of going through one road or an other, linked to the distance between the nodes. Every time an ant travel from one vertex to an other, it releases pheromones, that will influence the behaviour of the future population of ants. Then, for a given number n, we send n groups of ants, one after the other, and we actualise both the list of pheromones and the probability of transition. At the end, we obtain a path, generated 'randomly', that often is better than the previous ones. Here is the best one I obtained with this algorithm. 
