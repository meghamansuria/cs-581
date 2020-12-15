# Name:  Megha Mansuria

# Assignment 5: Graphs

# I pledge my honor that I have abided by the Stevens Honor System.

# Sources: I started by referencing the first assingment for working with csv files,
# but I have written additional code to supplement the assignment requirements.
# I referenced the documentation of NetworkX a lot to understand graphs in Python:
# https://networkx.org/documentation/latest/tutorial.html#accessing-edges-and-neighbors

# graphs.py processes an input file and identifies all of the triads in the graph. 
# Distinguishes the value of the edges in the triangle formed by the three nodes in 
# the triad. For each triad, identify which of the four triad types it represents, 
# and add to the appropriate count. Expected and Actual Distributions are displayed.

# To run from terminal window:   python3 graphs.py 

import networkx as nx
import csv

# graph of all the required stats to collect
def graph(filename):
    # create the graph for all the reviewer, reviewee, relationship
    G = nx.Graph()

    # declare variables for the count of stats
    edges = 0
    selfLoops = 0
    trusts = 0
    distrusts = 0

    with open(filename, mode='r', newline='') as csv_file:
        # open and read the file
        # read each line and assign values for reviewer, reviewee, weight
        for row in csv_file:
            # data = [tuple(row)] I DONT THINK I NEED THIS
            reviewer, reviewee, weight = tuple(map(int, row.split(",")))
            edges += 1
            # if reviewer == reviewee -> it's a self loop
            if (reviewer == reviewee):
                selfLoops += 1
            # if relationship between reviewer and reviewee is 1 -> count trust
            if (reviewer != reviewee) and (weight == 1):
                trusts += 1
            # if relationship between reviewer and reviewee is -1 -> count distrust
            if (reviewer != reviewee) and (weight == -1):
                distrusts += 1
            # add edge to the graph G
            G.add_edge(reviewer, reviewee, weight=weight)
    return edges, selfLoops, trusts, distrusts, G

def expected_dist(posProb, negProb):
    # calculates the probabilities of each triad type using the probabilities
    # that an edge will be positive or negative
    ttt = posProb * posProb * posProb * 100
    ttd = 3 * (posProb * posProb * negProb) * 100
    tdd = 3 * (posProb * negProb * negProb) * 100
    ddd = negProb * negProb * negProb * 100
    return ttt, ttd, tdd, ddd

def main():
    # get input file from user
    name = input("Enter a file: ")

    # call method graph to get data
    edges, selfLoops, trusts, distrusts, G = graph(name)
    totEdges = edges - selfLoops
    posProb = trusts / totEdges
    negProb = 1 - posProb

    # get all the triads formed and add to list all_triads
    all_triads = []
    for n in nx.enumerate_all_cliques(G):
        if len(n) == 3:
            all_triads.append(n)

    # find number of triangles in the graph
    numTriangles = len(all_triads)
    
    # print 1) num of edges, 2) num of self loops, 3) num of totEdges
    #       4) num of trusts, 5) num of distrusts, 6) posProb
    #       7) negProb
    print("\n************************* Statistics *************************")
    print("Edges in network: " + str(edges))
    print("Self-loops: " + str(selfLoops))
    print("Edges used - TotEdges: " + str(totEdges))
    print("Trust edges:    " + str(trusts) + "        probability p: " + str(round(posProb, 2)))
    print("Distrust edges: " + str(distrusts) + "        probability 1-p: " + str(round(negProb, 2)))
    print("Triangles: " + str(numTriangles))

    # calculate number of expected distributions of triads
    ttt, ttd, tdd, ddd = expected_dist(posProb, negProb)
    tttNum = ttt * numTriangles * 0.01
    ttdNum = ttd * numTriangles * 0.01
    tddNum = tdd * numTriangles * 0.01
    dddNum = ddd * numTriangles * 0.01

    # calculate totals -percent and numbers- of  expected triads
    exptot = round(ttt + ttd + tdd + ddd)
    exptotNum = round(tttNum + ttdNum + tddNum + dddNum)

    # calculate numbers and percents of actual distributions of triads
    # initiliaze all numbers count for actual dist
    tttNumAct = 0
    ttdNumAct = 0
    tddNumAct = 0
    dddNumAct = 0

    # goes through all the triads and finds the type. keeps track of totals of that type
    for t in all_triads:
        # get values for each edge between nodes (the reviewer & reviewee)
        first_node = t[0]
        second_node = t[1]
        third_node = t[2]
        # gets the weight of the edges in a triad and adds them to a total
        first_edge = G[first_node][second_node]['weight']
        second_edge = G[first_node][third_node]['weight']
        third_edge =  G[second_node][third_node]['weight']
        totalWeight = first_edge + second_edge + third_edge

        # the totalWeight determines what type of triad it is and keeps count
        if (totalWeight == 3):
            tttNumAct += 1
        if (totalWeight == 1):
            ttdNumAct += 1
        if (totalWeight == -1):
            tddNumAct += 1
        if (totalWeight == -3):
            dddNumAct += 1

    # calculate percents of actual distributions
    tttAct = tttNumAct / numTriangles * 100
    ttdAct = ttdNumAct / numTriangles * 100
    tddAct = tddNumAct / numTriangles * 100
    dddAct = dddNumAct / numTriangles * 100

    # calculate totals -percent and numbers- of actual triads
    acttot = round(tttAct + ttdAct + tddAct + dddAct)
    acttotNum = round(tttNumAct + ttdNumAct + tddNumAct + dddNumAct)

    # print all the expected and actual distributions
    print("\nExpected Distribution    Actual Distribution")
    print("Type percent number      Type percent number")
    print("TTT   " + str(round(ttt, 1)).rjust(4) + "    " + str(round(tttNum, 1)).rjust(4) + "       " + "TTT   " + str(round(tttAct)).rjust(4) + "    " + str(round(tttNumAct)).rjust(4))
    print("TTD   " + str(round(ttd, 1)).rjust(4) + "    " + str(round(ttdNum, 1)).rjust(4) + "       " + "TTD   " + str(round(ttdAct)).rjust(4) + "    " + str(round(ttdNumAct)).rjust(4))
    print("TDD   " + str(round(tdd, 1)).rjust(4) + "    " + str(round(tddNum, 1)).rjust(4) + "       " + "TDD   " + str(round(tddAct)).rjust(4) + "    " + str(round(tddNumAct)).rjust(4))
    print("DDD   " + str(round(ddd, 1)).rjust(4) + "    " + str(round(dddNum, 1)).rjust(4) + "       " + "DDD   " + str(round(dddAct)).rjust(4) + "    " + str(round(dddNumAct)).rjust(4))
    print("Total " + str(exptot).rjust(4) + "    " + str(exptotNum).rjust(4) + "       " + "Total " + str(acttot).rjust(4) + "    " + str(acttotNum).rjust(4))
    print()

if __name__ == "__main__":
    main()