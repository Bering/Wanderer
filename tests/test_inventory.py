import unittest
from inventory import WouldOverflowError, ItemNotInStockError, WouldUnderflowError, Inventory
import config

class Test_Inventory(unittest.TestCase):
    def test_max_size(self):
        i = Inventory(100)
        self.assertEqual(i.size_max, 100)
        self.assertEqual(i.size, 0)


    def test_add_InventoryEntry(self):
        inventory = Inventory(100)
        inventory.add("gold", 1, 1)
        self.assertTrue("gold" in inventory.items)
        self.assertEqual(inventory.size, 1)


    def test_add_cant_overstock(self):
        inventory = Inventory(100)
        self.assertRaises(WouldOverflowError, inventory.add, "Ship", 20000, 1)


    def test_cant_remove_inexisting_items(self):
        inventory = Inventory(100)
        self.assertRaises(ItemNotInStockError, inventory.remove, "Ship", 1)
    

    def test_can_remove_some_of_one_item(self):
        inventory = Inventory(100)
        inventory.add("Food", 1, 10)
        inventory.remove("Food", 1)
        self.assertTrue("Food" in inventory.items)
        self.assertEqual(inventory.items["Food"].quantity, 9)
        self.assertEqual(inventory.size, 9)


    def test_can_remove_all_of_one_item(self):
        inventory = Inventory(100)
        inventory.add("Food", 1, 10)
        inventory.remove("Food", 10)
        self.assertTrue("Food" not in inventory.items)


    def test_cant_remove_too_much(self):
        inventory = Inventory(100)
        inventory.add("Food", 1, 10)
        self.assertRaises(WouldUnderflowError, inventory.remove, "Food", 100)


if __name__ == '__main__':
    unittest.main()
