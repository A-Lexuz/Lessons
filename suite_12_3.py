import unittest
import tests_12_1_v1_1 as t1
import tests_12_2_v1_1 as t2

test_all = unittest.TestSuite()
test_all.addTest(unittest.TestLoader().loadTestsFromTestCase(t1.RunnerTest))
test_all.addTest(unittest.TestLoader().loadTestsFromTestCase(t2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_all)