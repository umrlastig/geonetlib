# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import sys
from shapely import wkt

import tracklib as tkl
import unittest
from netmatcher import (createNetwork,
                        removeDuplicateGeometries,
                        filtreNoeudSimple,
                        deleteSmallEdge)

class TestUtilNetwork5(unittest.TestCase):

    def setUp (self):

        tkl.NetworkReader.counter = 1

        self.collection = tkl.TrackCollection()

        # edge 1326
        wkt1 = 'LineString (949711.07996507245115936 6511691.77532575279474258, 949710.37035837769508362 6511694.73132603242993355)'
        wkt2 = 'LineString (949710.37035837769508362 6511694.73132603242993355, 949711.18996185949072242 6511695.9543120451271534)'
        wkt3 = 'LineString (949711.18996185949072242 6511695.9543120451271534, 949711.17723053647205234 6511695.95437376759946346)'
        wkt4 = 'LineString (949714.32271942729130387 6511698.92591316998004913, 949711.18996185949072242 6511695.9543120451271534)'
        wkt5 = 'LineString (949712.4092491464689374 6511698.10504418797791004, 949711.18996185949072242 6511695.9543120451271534)'
        wkt6 = 'LineString (949716.3774175476282835 6511698.89760604500770569, 949714.32271942729130387 6511698.92591316998004913)'
        wkt7 = 'LineString (949712.4092491464689374 6511698.10504418797791004, 949712.41322237649001181 6511710.69397122226655483)'
        #wkt8 = 'LineString (949712.41516225738450885 6511716.69546669535338879, 949712.41322237649001181 6511710.69397122226655483)'
        #wkt9 = 'LineString (949714.31332738231867552 6511708.87142911553382874, 949712.41322237649001181 6511710.69397122226655483)'
        #wkt10='LineString (949716.37786863720975816 6511708.88101750425994396, 949714.31332738231867552 6511708.87142911553382874)'

        WKTs = [wkt1, wkt2, wkt3, wkt4, wkt5, wkt6, wkt7]#, wkt8, wkt9, wkt10
        for wkt in WKTs:
            track = tkl.TrackReader().parseWkt(wkt)
            if track.size() < 2 :
                continue
            self.collection.addTrack(track)


    def plotNet(self, network, vnode=True):

        network.plot()

        for eid in network.getIndexEdges():
            edge = network.EDGES[eid]
            x1 = edge.geom.getFirstObs().position.getX()
            y1 = edge.geom.getFirstObs().position.getY()
            x2 = edge.geom.getLastObs().position.getX()
            y2 = edge.geom.getLastObs().position.getY()
            plt.text((x1+x2)/2, (y1+y2)/2, str(eid), fontsize=14)

        for nid in network.getIndexNodes():
            node = network.NODES[nid]
            x = node.coord.getX()
            y = node.coord.getY()
            if vnode:
                plt.text(x, y, str(nid), fontsize=14, color='C1')

        # ax.set_xlim([949490, 949510])
        # ax.set_ylim([6511200, 6511220])
        plt.show()

        # print ('Number of edges = ', len(network.EDGES))
        # print ('Number of nodes = ', len(network.NODES))
        # print ('Total length of all edges = ', network.totalLength())


    def testCreation(self):

        tolerance = 0.05
        network = createNetwork(self.collection, tolerance)
        self.plotNet(network, True)


        seuil_doublon = 0.1
        removeDuplicateGeometries(network, seuil_doublon)
        self.plotNet(network, False)


        filtreNoeudSimple(network)
        self.plotNet(network, True)


        threshold = 10
        nb = deleteSmallEdge(network, threshold)
        print ('nombre de suppression : ', nb)
        print ('Number of edges = ', len(network.EDGES))
        filtreNoeudSimple(network)
        print ('Number of edges = ', len(network.EDGES))
        self.plotNet(network, False)




if __name__ == '__main__':
    suite = unittest.TestSuite()

    suite.addTest(TestUtilNetwork5("testCreation"))


    runner = unittest.TextTestRunner()
    runner.run(suite)




