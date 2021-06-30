#!/usr/bin/python3
"""This module tests the BaseModel class"""
import os
import pep8
import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """Tests various functions of the BaseModel class"""

    def test_pep8(self):
        """Tests pep8"""

        style = pep8.StyleGuide(quiet=True)
        file_base_model = "models/base_model.py"
        file_test_base_model = "tests/test_base_model.py"
        check = style.check_files([file_base_model, file_test_base_model])
        self.assertEqual(check.total_errors, 0,
                         "Found code style errors (and warning).")

    @classmethod
    def setUpClass(cls):
        """Sets up the class"""
        cls.ins = BaseModel()

    @classmethod
    def teardown(cls):
        """Cleans everything up"""
        del cls.ins
        try:
            os.remove("file.json")
        except:
            pass

    def test_BaseModeldoc(self):
        """Test documentation"""
        self.assertNotEqual(len(BaseModel.__doc__), 0)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_BaseModelAttr(self):
        """Test BaseModel attributes"""
        self.assertEqual(hasattr(self.ins, "id"), True)
        self.assertEqual(hasattr(self.ins, "created_at"), True)
        self.assertEqual(hasattr(self.ins, "updated_at"), True)

    def test_isinstance(self):
        """Test instance"""
        self.assertTrue(isinstance(self.ins, BaseModel))

    def test_save_updated_at_created_at(self):
        """Tests save"""
        self.ins.save()
        self.assertNotEqual(self.ins.created_at, self.ins.updated_at)
        dummy = BaseModel()
        my_id = dummy.id
        dummy.name = "Holby"
        dummy.save()
        storage.reload()
        my_objs = storage.all()["BaseModel.{}".format(my_id)]
        self.assertTrue(hasattr(my_objs, "name"))
        self.assertTrue(my_objs.name == "Holby")
        self.assertTrue(os.path.exists('file.json'))

    def test_dict(self):
        """Tests dictionary"""
        a_dict = self.ins.to_dict()
        self.assertTrue(a_dict.get("__class__"))
        self.assertTrue(type(a_dict) is dict)
        self.assertTrue("to_dict" in dir(self.ins))

    def test_var_storage(self):
        """Tests storage"""
        my_objs = storage.all()

        self.assertTrue(type(my_objs) is dict)
        self.assertTrue(isinstance(storage, FileStorage))

    def test_reload(self):
        """Tests reload"""
        self.ins.save()
        storage.reload()
        my_dict = storage.all()
        self.assertTrue(len(my_dict) != 0)

if __name__ == '__main__':
    unittest.main()
