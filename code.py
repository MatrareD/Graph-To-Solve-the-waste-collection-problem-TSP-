import heapq as heapq
import copy
from collections import deque
from math import *
import numpy as np
import random as random

# Initiation of the city : Le Triangle D'Or in Bordeaux, with each point of intersection

Points = {"exutoire":[[0,44.843316, -0.570308]],
"Place Jean Jaurès":[[0,44.843316, -0.570308],[1,44.843298, -0.570498],[2,44.843241, -0.571072],[3,44.842607, -0.570913]],
"Cours du Chapeau Rouge":[[3,44.842607, -0.570913],[4,44.842342, -0.571097],[5,44.842219, -0.572990],[8,44.842145, -0.574291]],
"Rue Louis":[[5,44.842219, -0.572990],[6,44.843000, -0.573135]],
"Rue Esprit des Lois":[[2,44.843241, -0.571072],[6,44.843000, -0.573135],[7,44.843196, -0.571790],[73,44.842913, -0.574363]],
"Cours de l'Intendance": [[8,44.842145, -0.574291],[9,44.842066, -0.575949],[10,44.841963, -0.577377],[11,44.841906, -0.578166],[19,44.841753, -0.578622],[12,44.841777, -0.579321], [13,44.841703, -0.579939]],
"Cours Georges Clémenceau": [[13,44.841703, -0.579939],[34,44.842811, -0.579378],[35,44.845175, -0.577943],[79,44.843514, -0.578832]],
"Place Gambetta":[[13,44.841703, -0.579939],[14,44.841634, -0.581084],[20,44.841183, -0.581098],[15,44.840589, -0.580861],[16,44.840643, -0.580082]],
"Rue de la Porte Dijeaux":[[16,44.840643, -0.580082],[17,44.840687, -0.579686],[18,44.840780, -0.578476]],
"Rue de la Vielle Tour":[[12,44.841777, -0.579321],[17,44.840687, -0.579686]],
"Rue Vital Carles":[[18,44.840780, -0.578476],[19,44.841753, -0.578622]],
"Rue du Palais Gallien": [[14,44.841634, -0.581084],[41,44.842661, -0.581445],[42,44.843212, -0.581533],[43,44.844359, -0.581729],[44,44.845848, -0.581880],[45,44.846843, -0.581764],[46,44.847458, -0.581253]],
"Rue Fondaugège": [[35,44.845175, -0.577943],[46,44.847458, -0.581253],[47,44.846119, -0.579307],[48,44.846781, -0.580470]],
"Place Tourny":[[35,44.845175, -0.577943]],
"Place des Grands Hommes":[[25,44.843233, -0.577994],[26,44.842867, -0.577915],[27,44.842760, -0.577524],[28,44.843307, -0.577242],[29,44.843417, -0.577659],[65,44.843099, -0.577123]],
"Rue Voltaire":[[10,44.841963, -0.577377],[27,44.842760, -0.577524]],
"Rue Franklin":[[11,44.841906, -0.578166],[22,44.842659, -0.578277]],
"Rue Montesquieu":[[21,44.842212, -0.579026],[22,44.842659, -0.578277],[26,44.842867, -0.577915]],
"Rue Condillac":[[12,44.841777, -0.579321],[21,44.842212, -0.579026],[23,44.842863, -0.578784],[24,44.843387, -0.578467],[30,44.844491, -0.577828],[36,44.844763, -0.577481]],
"Rue Fénelon":[[22,44.842659, -0.578277],[23,44.842863, -0.578784]],
"Rue Buffon":[[24,44.843387, -0.578467],[25,44.843233, -0.577994],[79,44.843514, -0.578832]],
"Rue Jean Jacques Rousseau":[[29,44.843417, -0.577659],[30,44.844491, -0.577828],[40,44.844103, -0.577752]],
"Allées de Tourny":[[35,44.845175, -0.577943],[36,44.844763, -0.577481],[37,44.843914, -0.576322],[38,44.843288, -0.575422],[39,44.842845, -0.574705],[58,44.845180, -0.577025],[61,44.844966, -0.576977],[63,44.844527, -0.576296],[64,44.844220, -0.575852],[71,44.843734, -0.575134],[72,44.843188, -0.574450]],
"Rue Michel Montaigne":[[28,44.843307, -0.577242],[31,44.843528, -0.576920],[37,44.843914, -0.576322]],
"Rue Mably":[[31,44.843528, -0.576920],[32,44.842781, -0.576102],[40,44.844103, -0.577752],[66,44.843233, -0.576534]],
"Rue Diderot":[[65,44.843099, -0.577123],[66,44.843233, -0.576534]],
"Place du Chapelet":[[32,44.842781, -0.576102],[33,44.842550, -0.575989]],
"Rue Martignac":[[9,44.842066, -0.575949],[33,44.842550, -0.575989]],
"Rue Mautrec":[[33,44.842550, -0.575989],[39,44.842845, -0.574705]],
"Rue Jean Jacques Bel":[[32,44.842781, -0.576102],[38,44.843288, -0.575422]],
"Rue Rolland":[[41,44.842661, -0.581445],[34,44.842811, -0.579378]],
"Rue de Lurbe":[[42,44.843212, -0.581533],[51,44.843359, -0.579571]],
"Rue Huguerie":[[35,44.845175, -0.577943],[43,44.844359, -0.581729],[50,44.844599, -0.579894]],
"Rue Turenne":[[44,44.845848, -0.581880],[49,44.846180, -0.580173]],
"Rue Lafaurie de Monbadon":[[34,44.842811, -0.579378],[49,44.846180, -0.580173],[50,44.844599, -0.579894],[51,44.843359, -0.579571]],
"Place Charles Gruet":[[48,44.846781, -0.580470],[49,44.846180, -0.580173]],
"Rue du Professeur Demons":[[47,44.846119, -0.579307],[80,44.846870, -0.578954]],
"Rue Hustin":[[52,44.846561, -0.578227],[53,44.846233, -0.577262],[80,44.846870, -0.578954]],
"Rue Victoire Américaine":[[47,44.846119, -0.579307],[52,44.846561, -0.578227]],
"Cours de Verdun":[[35,44.845175, -0.577943],[53,44.846233, -0.577262],[54,44.846618, -0.576989],[85,44.847157, -0.576678]],
"Rue d'Enghien":[[53,44.846233, -0.577262],[57,44.846006, -0.576672],[59,44.845732, -0.575859]],
"Rue Blanc Dutrouilh":[[54,44.846618, -0.576989],[55,44.846392, -0.576404],[56,44.846070, -0.575519]],
"Rue Boudet":[[58,44.845180, -0.577025],[55,44.846392, -0.576404],[57,44.846006, -0.576672],[84,44.846953, -0.576106]],
"Cours de Gourgue":[[83,44.846736, -0.575211],[84,44.846953, -0.576106],[85,44.847157, -0.576678]],
"Cours du Maréchal Foch":[[82,44.846189, -0.575092],[83,44.846736, -0.575211]],
"Cours de Tournon":[[35,44.845175, -0.577943],[58,44.845180, -0.577025],[60,44.845279, -0.575959]],
"Place des Quinconces":[[56,44.846070, -0.575519],[59,44.845732, -0.575859],[60,44.845279, -0.575959],[62,44.844859, -0.575738],[67,44.844622, -0.575255],[68,44.844593, -0.574761]],
"Rue de Sèze":[[62,44.844859, -0.575738],[63,44.844527, -0.576296]],
"Rue du Château Trompette":[[64,44.844220, -0.575852],[67,44.844622, -0.575255]],
"Allées de Munich":[[68,44.844593, -0.574761],[69,44.844984, -0.570648],[78,44.844917, -0.570942]],
"Allées de Bristol":[[81,44.846559, -0.570891],[82,44.846189, -0.575092]],
"Petit Quai Louis XVIII":[[0,44.843316, -0.570308],[77,44.844135, -0.570768],[78,44.844917, -0.570942]],
"Grand Quai Louis XVIII":[[0,44.843316, -0.570308],[69,44.844984, -0.570648],[81,44.846559, -0.570891]],
"Allées d'Orléans":[[70,44.843780, -0.574561],[74,44.843876, -0.573341],[75,44.843996, -0.571932],[76,44.844094, -0.571207],[77,44.844135, -0.570768]],
"Rue Lafayette":[[2,44.843241, -0.571072],[76,44.844094, -0.571207]],
"Charles Lamoureux":[[7,44.843196, -0.571790],[75,44.843996, -0.571932]],
"Rue de Condé":[[6,44.843000, -0.573135],[74,44.843876, -0.573341]],
"Rue Gobineau":[[70,44.843780, -0.574561],[71,44.843734, -0.575134]],
"Cours du 30 juillet":[[68,44.844593, -0.574761],[70,44.843780, -0.574561],[72,44.843188, -0.574450],[73,44.842913, -0.574363]],
"Place de la Comédie":[[8,44.842145, -0.574291],[39,44.842845, -0.574705],[73,44.842913, -0.574363]]}

City = {0:[1,69], 1:[0,2], 2:[1,3,7,76], 3:[2,4], 4:[3], 5:[4], 6:[5,7,73],
7:[2,6,75], 8:[5,9,73], 9:[8,10,33], 10:[9,11], 11:[10,19], 12:[13,19,21],
13:[12,14,16,34], 14:[13,20,41], 15:[16,20], 16:[13,17], 17:[12,16,18],
18:[17,19], 19:[11,12,18], 20:[14,15], 21:[12,22], 22:[11,26], 23:[21,22],
24:[23,25], 25:[26], 26:[27], 27:[10,65], 28:[29,31], 29:[40],
30:[24,36], 31:[40,37], 32:[66], 33:[32], 34:[13,35,79],35:[34,36,47,50,53,58],
36:[30,35,37], 37:[38], 38:[32,39], 39:[8,33,71,73], 40:[30], 41:[34,42],
42:[43,51], 43:[44,50], 44:[45,49], 45:[44], 46:[45,48], 47:[35,48,80],
48:[46,47], 49:[48, 50], 50:[51], 51:[34], 52:[47,53], 53:[35,54,57],
54:[53,85], 55:[54,56,84], 56:[59], 57:[55,59], 58:[57,60], 59:[60],
60:[62], 61:[36,58], 62:[67], 63:[61,62], 64:[63], 65:[28],
66:[31,65], 67:[64,68], 68:[78], 69:[0,81], 70:[68,71], 71:[64],
72:[70,71], 73:[6,8,72], 74:[6,70], 75:[74], 76:[75], 77:[1,76],
78:[69,77], 79:[24,35], 80:[52], 81:[69,82], 82:[56,83], 83:[84], 84:[83,85], 85:[54,84]}
# Points to collect : Voluntary drop-off points VDP

VDP = { 0:["exutoire"], 4:["Glass"], 10:["Glass","Food"],
11:["Glass"], 20:["Glass","Food"],
22:["Glass"], 25:["Glass"], 37:["Glass"], 45:["Food"],
49:["Glass"], 54:["Food"], 62:["Glass"],
70:["Glass","Food"], 77:["Glass","Food"] }

def fusion(liste1,liste2): # will help for next algorithms
    liste=[]
    i,j=0,0
    while i<len(liste1)and j<len(liste2):
        if liste1[i][1]<=liste2[j][1]:
            liste.append(liste1[i])
            i+=1
        else:
            liste.append(liste2[j])
            j+=1
    while i<len(liste1):
        liste.append(liste1[i])
        i+=1
    while j<len(liste2):
        liste.append(liste2[j])
        j+=1
    return liste

def sort_fusion(liste):
    if len(liste)<2:
        return liste
    else:
        milieu=len(liste)//2
        liste1=sort_fusion(liste[:milieu])
        liste2=sort_fusion(liste[milieu:])
        return fusion(liste1,liste2)
def tri_graph_croissant(g):
    for x in g:
        L=g[x]
        g[x]= tri_fusion(L)
    return g
  
def distance(a,b):
    lat1,lon1,lat2,lon2 = a[1]*pi/180, a[2]*pi/180,b[1]*pi/180,b[2]*pi/180
    r = 6378.137
    dlat = (lat2 - lat1)
    dlon = (lon2 - lon1)
    a = sin(dlat/2)*sin(dlat/2) + cos(lat1)*cos(lat2)*sin(dlon/2)*sin(dlon/2)
    c = 2*r*atan2(sqrt(a), sqrt(1-a))
    return(c)

def reverse_graph_city():
    Vertices = {x:[] for x in range(86)}
    for rue in Points:
        try :
            for (p,lat,long) in Points[rue]:
                if not (rue in Vertices[p]):
                   Vertices[p].append(rue)
        except:
            print(f"'{rue}' not found.")
    return Vertices

Sommets = inversion_graphe_ville()

def coordonnees(s:int)->list:
    rue_de_s = Vertices[s][0]
    coord=[]
    for p in Points[rue_de_s]:
        if p[0]==s:
            coord=p
    return coord

def weights():
    Weighted_city = {s:[] for s in Ville}
    for s in City :
        for v in City[s]:
            Weighted_city[s].append((v,distance(coordonnees(s),coordonnees(v))))
    return Weighted_city

Weighted_city = weights()

def dijkstra(g, v_init,v_fin):
    visited = {x : False for x in g}
    pred = {x : None for x in g}
    dist = {x : float('inf') for x in g}
    dist[v_init] = 0
    hq = [(0, v_init)]
    heapq.heapify(hq)
    while len(hq) > 0 and not(visited[v_fin]):
        dv, v = heapq.heappop(hq)
        if not visited[v]:
            visited[v] = True
            for w, dvw in g[v]:
                if not visited[w]:
                    dw = dv + dvw
                    if dw < dist[w]:
                        dist[w] = dw
                        pred[w] = v
                        heapq.heappush(hq, (dw, w))
    C = [v_fin]
    while C[0] != v_init:
        w = pred[C[0]]
        C = [w] + C
    end = ""
    for x in C:
        end += "->" + str(x)
    return (end, dist[v_fin])
  # O[(|A|+|S|)log(|S|)] complexity

def naive_algo_closest_neighbor(vdp,v_init):
    l = [0]
    city_bacs = {x:[] for x in vdp}
    for bac in vdp :
        for end in vdp :
            if bac == end :
                None
            else :
                d = dijkstra(Weighted_city,bac,end)
                city_bacs[bac].append((end,d[1]))
    visited = {x : False for x in vdp}
    stack = [(0,0)]
    last = 0
    km = 0
    path = ""
    total_path = ""
    ordered_vdp = sort_graph_increasing(city_bacs)
    while len(stack) > 0:
        v, dv = stack.pop()
        total_path += "->" + dijkstra(Weighted_city,last,v)[0]
        last = v
        if not visited[v]:
            visited[v] = True
            l.append(0)
            path += "->" + str(v)
            km+=dv
        c = 0
        for w, dw in ordered_vdp[v]:
            if not visited[w] and c == 0:
                stack.append((w, dw))
                c = 1
        d = dijkstra(Weighted_city, last, v_init)
    print("le chemin des bacs est " + path + d[0] + "-> 0")
    print("et le trajet complet dans la ville est \n" + total_path)
    return km + d[1] # the length of the path


