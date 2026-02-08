# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import sys
import tracklib as tkl
import unittest
from netmatcher import (createNetwork, filtreNoeudSimple, deleteSmallEdge)



class TestUtilNetwork1(unittest.TestCase):
    

    
    def setUp (self):

        tkl.NetworkReader.counter = 1

        self.collection = tkl.TrackCollection()
        wkt1 = 'LineString (949464.54181289207190275 6511189.01651289127767086, 949465.41049999999813735 6511188.81468277052044868)'
        wkt2 = 'LineString (949465.41049999999813735 6511187.94359373487532139, 949465.41049999999813735 6511188.81468277052044868)'
        wkt3 = 'LineString (949465.62881248281337321 6511189.69476869702339172, 949465.41049999999813735 6511188.81468277052044868)'
        wkt4 = 'LineString (949465.62881248281337321 6511189.69476869702339172, 949468.1601792813744396 6511191.25851298123598099)'
        wkt5 = 'LineString (949468.37692472361959517 6511192.10310463793575764, 949468.1601792813744396 6511191.25851298123598099)'
        wkt6 = 'LineString (949468.37692472361959517 6511192.10310463793575764, 949466.86878196173347533 6511194.67706254497170448)'
        wkt7 = 'LineString (949466.86878196173347533 6511194.67706254497170448, 949467.20845044264569879 6511196.06949897296726704)'
        wkt8 = 'LineString (949465.03866808395832777 6511196.55419210344552994, 949467.20845044264569879 6511196.06949897296726704)'
        wkt9 = 'LineString (949467.20845044264569879 6511196.06949897296726704, 949467.61479663848876953 6511196.07794086635112762)'
        wkt10 = 'LineString (949467.61479663848876953 6511196.07794086635112762, 949469.45157357701100409 6511197.91671759262681007)'
        wkt11 = 'LineString (949469.45157357701100409 6511197.91671759262681007, 949469.94407232687808573 6511199.69164014235138893)'
        wkt12 = 'LineString (949469.6469706620555371 6511202.0275160800665617, 949469.69944186392240226 6511199.91917888820171356)'

        wkt13 = 'LineString (949480.12939887423999608 6511199.19875026308000088, 949475.91746515338309109 6511200.24975066632032394)'
        wkt14 = 'LineString (949478.5082995411939919 6511202.83872656710445881, 949479.32515376713126898 6511202.84751619212329388)'
        wkt15 = 'LineString (949479.30492988810874522 6511205.52914131432771683, 949479.32515376713126898 6511202.84751619212329388)'
        wkt16 = 'LineString (949483.76547800260595977 6511202.86597826145589352, 949479.32515376713126898 6511202.84751619212329388)'
        wkt17 = 'LineString (949475.17201779293827713 6511199.78719203174114227, 949469.94407232687808573 6511199.69164014235138893)'
        wkt18 = 'LineString (949475.91746515338309109 6511200.24975066632032394, 949475.17201779293827713 6511199.78719203174114227)'
        wkt19 = 'LineString (949478.5082995411939919 6511202.83872656710445881, 949475.91746515338309109 6511200.24975066632032394)'
        wkt20 = 'LineString (949482.44749729475006461 6511208.84750906005501747, 949479.30492988810874522 6511205.52914131432771683)'
        wkt21 = 'LineString (949482.42193457367829978 6511210.86011874303221703, 949482.44749729475006461 6511208.84750906005501747)'
        wkt22 = 'LineString (949484.19817507360130548 6511201.10387634672224522, 949483.76547800260595977 6511202.86597826145589352)'
        wkt23 = 'LineString (949487.29527037218213081 6511203.72070884145796299, 949483.76547800260595977 6511202.86597826145589352)'
        wkt24 = 'LineString (949489.46468488150276244 6511205.86012941598892212, 949487.29527037218213081 6511203.72070884145796299)'
        wkt25 = 'LineString (949491.84050031285732985 6511205.87000762857496738, 949489.46468488150276244 6511205.86012941598892212)'
        wkt26 = 'LineString (949491.84050031285732985 6511205.87000762857496738, 949494.08009398635476828 6511207.2453936580568552)'
        wkt27 = 'LineString (949494.08009398635476828 6511207.2453936580568552, 949494.76566181192174554 6511208.57294407859444618)'
        wkt28 = 'LineString (949496.71090080286376178 6511209.78778613172471523, 949494.76566181192174554 6511208.57294407859444618)'
        wkt29 = 'LineString (949497.53016577800735831 6511209.84840254299342632, 949496.71090080286376178 6511209.78778613172471523)'
        wkt30 = 'LineString (949497.53016577800735831 6511209.84840254299342632, 949498.41724877315573394 6511210.84553961642086506)'
        wkt31 = 'LineString (949500.33019306417554617 6511210.96740047261118889, 949498.41724877315573394 6511210.84553961642086506)'
        wkt32 = 'LineString (949500.68271779990755022 6511212.46355483122169971, 949500.33019306417554617 6511210.96740047261118889)'
        wkt33 = 'LineString (949503.20755883702076972 6511210.47432378120720387, 949500.33019306417554617 6511210.96740047261118889)'
        wkt34 = 'LineString (949503.20755883702076972 6511210.47432378120720387, 949507.4713976455386728 6511213.46039757318794727)'
        wkt35 = 'LineString (949509.20874382252804935 6511213.58894168958067894, 949507.4713976455386728 6511213.46039757318794727)'
        wkt36 = 'LineString (949510.51752759772352874 6511214.8745622169226408, 949509.20874382252804935 6511213.58894168958067894)'
        wkt37 = 'LineString (949510.51752759772352874 6511214.8745622169226408, 949510.52185361413285136 6511215.05153173394501209)'
        wkt38 = 'LineString (949510.52185361413285136 6511215.05153173394501209, 949511.72446891199797392 6511215.95276325196027756)'
        wkt39 = 'LineString (949512.5510817221365869 6511216.8414676021784544, 949511.72446891199797392 6511215.95276325196027756)'
        wkt40 = 'LineString (949512.51182067231275141 6511218.74059210158884525, 949512.5510817221365869 6511216.8414676021784544)'
        wkt41 = 'LineString (949513.22191673144698143 6511214.52859342657029629, 949511.72446891199797392 6511215.95276325196027756)'
        wkt42 = 'LineString (949513.22191673144698143 6511214.52859342657029629, 949518.94621406449005008 6511215.91137302108108997)'
        
        wkt43 = 'LineString (949469.05290992837399244 6511223.69493918865919113, 949468.26808145293034613 6511211.18771177344024181)'
        wkt44 = 'LineString (949468.26808145293034613 6511211.18771177344024181, 949469.204160928260535 6511210.07154473103582859)'
        wkt45 = 'LineString (949469.204160928260535 6511210.07154473103582859, 949468.93606799142435193 6511205.77977732382714748)'
        wkt46 = 'LineString (949468.93606799142435193 6511205.77977732382714748, 949468.4117087172344327 6511205.23369199223816395)'
        wkt47 = 'LineString (949468.4117087172344327 6511205.23369199223816395, 949468.41183437709696591 6511203.31365993060171604)'
        wkt48 = 'LineString (949468.41183437709696591 6511203.31365993060171604, 949469.6469706620555371 6511202.0275160800665617)'
        wkt49 = 'LineString (949470.40296131605282426 6511225.08713433146476746, 949469.05290992837399244 6511223.69493918865919113)'
        wkt50 = 'LineString (949470.40729040070436895 6511229.07259419746696949, 949470.40296131605282426 6511225.08713433146476746)'

        WKTs = [wkt1, wkt2, wkt3, wkt4, wkt5, wkt6, wkt7, wkt8, wkt9, wkt10,
                wkt11, wkt12,wkt13, wkt14, wkt15, wkt16, wkt17,
                wkt18, wkt19, wkt20, wkt21, wkt22, wkt23, wkt24,
                wkt25, wkt26, wkt27, wkt28, wkt29, wkt30, wkt31, wkt32, wkt33,
                wkt34, wkt35, wkt36, wkt37, wkt38, wkt39, wkt40, wkt41, wkt42,
                wkt43, wkt44, wkt45, wkt46, wkt47, wkt48, wkt49, wkt50]
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
        
        tolerance = 0.5
        network = createNetwork(self.collection, tolerance)

        self.plotNet(network, False)

        self.assertEqual(len(network.EDGES), 50, "Number of edges")
        self.assertEqual(len(network.NODES), 51, "Number of nodes")
        self.assertLessEqual(abs(125.01 - network.totalLength()), 0.01, "Total length of all edges")

        # Arc 1
        e1 = network.EDGES[1]
        self.assertIsInstance(e1, tkl.Edge)
        self.assertIsInstance(e1.source, tkl.Node)
        self.assertIsInstance(e1.target, tkl.Node)
        # Noeud 1
        n1 = e1.source
        self.assertEqual(n1.id, 1)
        self.assertEqual(len(network.getNextEdges(n1.id)), 1)
        self.assertEqual(network.getNextEdges(n1.id)[0], 1)
        self.assertEqual(len(network.getPrevEdges(n1.id)), 1)
        self.assertEqual(network.getPrevEdges(n1.id)[0], 1)
        self.assertEqual(len(network.getIncidentEdges(n1.id)), 1)
        self.assertEqual(network.getIncidentEdges(n1.id)[0], 1)
        # Noeud 2
        n2 = e1.target
        self.assertEqual(n2.id, 2)
        self.assertEqual(len(network.getPrevEdges(e1.target.id)), 3)
        self.assertEqual(len(network.getNextEdges(e1.target.id)), 3)
        self.assertEqual(network.getPrevEdges(n2.id)[0], 1)
        self.assertEqual(network.getPrevEdges(n2.id)[1], 2)
        self.assertEqual(network.getPrevEdges(n2.id)[2], 3)
        self.assertEqual(network.getNextEdges(n2.id)[0], 1)
        self.assertEqual(network.getNextEdges(n2.id)[1], 2)
        self.assertEqual(network.getNextEdges(n2.id)[2], 3)
        self.assertEqual(network.getIncidentEdges(n2.id)[0], 1)
        self.assertEqual(network.getIncidentEdges(n2.id)[1], 2)
        self.assertEqual(network.getIncidentEdges(n2.id)[2], 3)

        # Arc 2
        e2 = network.EDGES[2]
        self.assertEqual(e2.source.id, 3)
        self.assertEqual(e2.target.id, n2.id)
        # Noeud 3
        n3 = e2.source
        self.assertEqual(len(network.getNextEdges(n3.id)), 1)
        self.assertEqual(len(network.getPrevEdges(n3.id)), 1)
        self.assertEqual(len(network.getIncidentEdges(n3.id)), 1)

        # Arc 3
        e3 = network.EDGES[3]
        self.assertEqual(e3.source.id, 4)
        self.assertEqual(e3.target.id, n2.id)
        self.assertEqual(len(network.getNextEdges(n2.id)), 3)


        # Arc 32
        e32 = network.EDGES[32]
        self.assertEqual(e32.source.id, 33)
        self.assertEqual(e32.target.id, 32)

        self.assertEqual(len(network.getNextEdges(33)), 1)
        self.assertEqual(len(network.getPrevEdges(33)), 1)
        self.assertEqual(len(network.getIncidentEdges(33)), 1)

        self.assertEqual(len(network.getNextEdges(32)), 3)
        self.assertEqual(len(network.getPrevEdges(32)), 3)
        self.assertEqual(len(network.getIncidentEdges(32)), 3)


    def testFiltre(self):

        tolerance = 0.5
        network = createNetwork(self.collection, tolerance)
        filtreNoeudSimple(network)

        self.plotNet(network)

        self.assertEqual(len(network.EDGES), 17, "Number of edges")
        self.assertEqual(len(network.NODES), 18, "Number of nodes")

        # Arc 32
        e32 = network.EDGES[32]
        self.assertEqual(e32.source.id, 33)
        self.assertEqual(e32.target.id, 32)

        self.assertEqual(len(network.getNextEdges(33)), 1)
        self.assertEqual(len(network.getPrevEdges(33)), 1)
        self.assertEqual(len(network.getIncidentEdges(33)), 1)

        # Les arcs de 32
        self.assertEqual(len(network.getNextEdges(32)), 3)
        self.assertEqual(len(network.getPrevEdges(32)), 3)
        self.assertEqual(len(network.getIncidentEdges(32)), 3)
        # Les noeuds de 32
        self.assertEqual(len(network.getNextNodes(32)), 3)
        self.assertEqual(len(network.getPrevNodes(32)), 3)
        self.assertEqual(len(network.getAdjacentNodes(32)), 3)


    def testDeleteSmallEdges(self):

        tolerance = 0.5
        network = createNetwork(self.collection, tolerance)
        filtreNoeudSimple(network)

        threshold = 10
        nb = deleteSmallEdge(network, threshold)

        self.assertEqual(nb, 6, "edges deleted")

        filtreNoeudSimple(network)
        self.assertEqual(len(network.EDGES), 5, "Number of edges")
        self.assertEqual(len(network.NODES), 6, "Number of nodes")

        self.plotNet(network)







if __name__ == '__main__':
    suite = unittest.TestSuite()

    suite.addTest(TestUtilNetwork1("testCreation"))
    suite.addTest(TestUtilNetwork1("testFiltre"))
    suite.addTest(TestUtilNetwork1("testDeleteSmallEdges"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
