import unittest

from thursday_homework_walkthru import Cart

class testCart(unittest.TestCase):
    def test_add_item(self):
        test_cart = Cart()
        self.assertEqual(test_cart.add('jean'== {'quantity': 2, 'price': 20.0}), {{'jean': {'quantity': 2, 'price': 20.0}}})

    def test_remove_item(self):
        test_cart = Cart()
        test_cart.add('jean')
        test_cart.add('shirt')
        test_cart.add('pant')

        test_cart.remove('shirt')

        assert test_cart.grocery_dict == {'jean', 'pant'}

if __name__ == '__main__':
    unittest.main()