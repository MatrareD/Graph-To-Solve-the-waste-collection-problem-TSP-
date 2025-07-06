# Python TSP solver for waste collection 
In a bid to entrance into a french engineer school, I had to work on the theme "Transition, Transformation, Conversion". Therefore, I decided to focus on the waste collection probleme in Bordeaux (French City).
First, I wanted to work on household daily waste, but there were too much difficulties (and in the real life, the optimisation depends on on-field agents' experience).
This is why I wanted to study the situation for the voluntary drop-off points (glass columns or alimentary waste) whose informatic optimisation is used by private companies or municipalities.

Thanks to openstreetmap contributors : 
https://www.openstreetmap.org/#map=13/44.84133/-0.5805
you can have access to all data that you need. Indeed, the name of the differents roads, the properties of the ways and the direction of traffic being extrated, I was able to build a graph of Bordeaux from scratch. 
https://github.com/user-attachments/assets/580a785a-8576-4683-ae72-9578e8f0ab2b

The algorithm the most important of this project is the shortest path between two vertices : Dijkstra algorithm. It provides the real distance in my neighborhood between two intersections. This is how it works: 
0°) Every neighbor is at an infinite distance from the initial vertex
1°) At each step, every distance between a visited vertex and the initial one is actualised to be the sortest.
2°) The final vertex is visited, we take the sortest path between this and the initial one. 
There is a clear exemple : https://github.com/user-attachments/assets/12e1c11a-aeaf-4de0-ab2b-cbdbcb25b198

Lets now focus on the waste collection : 
