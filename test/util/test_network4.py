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

class TestUtilNetwork4(unittest.TestCase):
    '''

    '''

    def setUp (self):

        tkl.NetworkReader.counter = 1

        self.collection = tkl.TrackCollection()


        #wkt1 = 'LineString (949441.71472716750577092 6511610.61251389048993587, 949436.46487163472920656 6511613.90067949332296848)'
        #wkt2 = 'LineString (949441.71472716750577092 6511610.61251389048993587, 949442.13998358394019306 6511608.95274663716554642)'
        #wkt3 = 'LineString (949447.12526071863248944 6511605.82945351861417294, 949442.13998358394019306 6511608.95274663716554642)'
        #wkt4 = 'LineString (949447.12526071863248944 6511605.82945351861417294, 949447.54179937392473221 6511604.17029798589646816)'
        
        wkt5 = 'LineString (949451.39797509158961475 6511601.34049021638929844, 949447.54179937392473221 6511604.17029798589646816)'
        wkt6 = 'LineString (949451.40333068161271513 6511599.92092489264905453, 949451.39797509158961475 6511601.34049021638929844)'
        wkt7 = 'LineString (949451.85614544944837689 6511601.44218096323311329, 949451.39797509158961475 6511601.34049021638929844)'
        wkt8 = 'LineString (949451.39797509158961475 6511601.34049021638929844, 949451.85614544944837689 6511601.44218096323311329)'
        wkt9 = 'LineString (949452.99435993283987045 6511600.73960983008146286, 949451.85614544944837689 6511601.44218096323311329)'
        wkt10 = 'LineString (949452.99435993283987045 6511600.73960983008146286, 949455.88972671213559806 6511601.44481853395700455)'

        #wkt11 = 'LineString (949456.37146829348057508 6511600.97635867074131966, 949455.88972671213559806 6511601.44481853395700455)'
        #wkt12 = 'LineString (949456.3749611908569932 6511600.84966119192540646, 949456.37146829348057508 6511600.97635867074131966)'
        #wkt13 = 'LineString (949456.3749611908569932 6511600.84966119192540646, 949457.37883411906659603 6511599.8709693755954504)'
        #wkt14 = 'LineString (949457.37883411906659603 6511599.8709693755954504, 949458.11131992377340794 6511599.85417966917157173)'

        #wkt15 = 'LineString (949458.94675049907527864 6511599.32599695399403572, 949458.11131992377340794 6511599.85417966917157173)'
        #wkt16 = 'LineString (949458.94675049907527864 6511599.32599695399403572, 949459.708413100335747 6511596.18736542202532291)'
        #wkt17 = 'LineString (949460.1401951543521136 6511595.9236504789441824, 949459.708413100335747 6511596.18736542202532291)'
        #wkt18 = 'LineString (949460.19637063844129443 6511595.92336206696927547, 949460.1401951543521136 6511595.9236504789441824)'

        WKTs = [#wkt1, wkt2, wkt3, wkt4,
                 wkt5, wkt6, wkt7, wkt8, wkt9, wkt10#,
                #wkt11, wkt12, wkt13, wkt14, wkt15, wkt16, wkt17, wkt18
                ]
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
        self.plotNet(network, False)

        threshold = 10
        nb = deleteSmallEdge(network, threshold)
        print ('nombre de suppression : ', nb)
        print ('Number of edges = ', len(network.EDGES))

        filtreNoeudSimple(network)
        self.plotNet(network, False)

        print ('Number of edges = ', len(network.EDGES))


if __name__ == '__main__':
    suite = unittest.TestSuite()

    suite.addTest(TestUtilNetwork4("testCreation"))


    runner = unittest.TextTestRunner()
    runner.run(suite)




