import unittest
import war

class TestWvsW(unittest.TestCase):
	def setUp (self):
		self.war1 = war.Konnica()
		self.war2 = war.Warrior()
		
	def test_is_alive(self):
		self.assertTrue(self.war1.is_alive())
		self.assertTrue(self.war2.is_alive())
		
	def test_kick(self):
		self.assertEqual(self.war1.health, 50)
		self.assertEqual(self.war2.health, 50)
		
	def test_after_kick(self):
		self.war1.kick(self.war2)
		self.assertEqual(self.war1.health, 50)
		self.assertEqual(self.war2.health, 35)
		
		
if __name__ == '__main__':
	unittest.main()