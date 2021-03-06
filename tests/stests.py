"""
module with unittests
for testing serialization methods
"""
import unittest
from model.user import User
from model.accounting import Accounting
from serialization.sjson import UserEncoder, encode_dict
import yaml
import json
import pickle
import datetime


class TestSerialization(unittest.TestCase):

    def create_user(self):
        """
        :return: User object
        """
        acc = Accounting()
        acc.set_datetime(datetime.datetime(2016, 3, 27, 0, 0))
        acc.set_description('desc')
        acc.set_sum(17.00)
        usr = User()
        usr.add_payment(acc)
        return usr

    def test_yaml(self):
        """
        test yaml serialization
        :return: nothing
        """

        obj = self.create_user()
        stringIO = yaml.dump(obj)
        obj1 = yaml.load(stringIO)
        for p1, p2 in zip(obj.get_payment_list(), obj1.get_payment_list()):
            self.assertEqual(p1.get_sum(), p2.get_sum())
            self.assertEqual(p1.get_description(), p2.get_description())
        self.assertEqual(obj.get_money(), obj1.get_money())

    def test_json(self):
        """
        test json serialization
        :return: nothing
        """
        obj = self.create_user()
        stringIO = json.dumps(obj, cls=UserEncoder)
        obj1 = encode_dict(json.loads(stringIO))
        for p1, p2 in zip(obj.get_payment_list(), obj1.get_payment_list()):
            self.assertEqual(p1.get_sum(), p2.get_sum())
            self.assertEqual(p1.get_description(), p2.get_description())
        self.assertEqual(obj.get_money(), obj1.get_money())

    def test_pickle(self):
        """
        test pickle serialization
        :return: nothing
        """
        obj = self.create_user()
        stringIO = pickle.dumps(obj)
        obj1 = pickle.loads(stringIO)
        for p1, p2 in zip(obj.get_payment_list(), obj1.get_payment_list()):
            self.assertEqual(p1.get_sum(), p2.get_sum())
            self.assertEqual(p1.get_description(), p2.get_description())
        self.assertEqual(obj.get_money(), obj1.get_money())
        # self.assertEqual(obj, obj1)

if __name__ == '__main__':
    unittest.main()
