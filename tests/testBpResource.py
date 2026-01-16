from flask_helper.blueprintResource import BLUEPRINT_RESOURCE
from flask_helper.exceptions import ResourceException
import unittest


class TEST_RESOURCE(BLUEPRINT_RESOURCE):
    _PREFIX = "/base"
    INDEX = "/"
    HEARTBEAT = ""
    VERSION = "/version"


class TestBlueprintResource(unittest.TestCase):
    def test_a_base(self):
        v = TEST_RESOURCE._PREFIX
        # print("a: '{}' ({})".format(v, type(v).__name__))
        self.assertEqual("/base", v)

    def test_b_hb(self):
        v = TEST_RESOURCE.HEARTBEAT
        # print("b: '{}' ({})".format(v, type(v).__name__))
        self.assertEqual("/base", str(v))

        v = TEST_RESOURCE.HEARTBEAT.rule
        # print("b: '{}' ({})".format(v, type(v).__name__))
        self.assertEqual("", v)

    def test_c_ver(self):
        v = TEST_RESOURCE.VERSION
        # print("c: '{}' ({})".format(v, type(v).__name__))
        self.assertEqual("/base/version", str(v))

        v = TEST_RESOURCE.VERSION.rule
        # print("c: '{}' ({})".format(v, type(v).__name__))
        self.assertEqual("/version", v)

    def test_d_idx(self):
        v = TEST_RESOURCE.INDEX.rule
        # print("d: '{}' ({})".format(v, type(v).__name__))
        self.assertEqual("/", v)

    def test_e_addition(self):
        baseUrl = "http://localhost:5000"
        self.assertTrue(isinstance(baseUrl + TEST_RESOURCE.VERSION, str))

    def test_f_failPfx(self):
        def ibr():
            from tests.badResourcePfx import BAD_RESOURCE

        self.assertRaises(ResourceException, ibr)

    def test_f_failSlash(self):
        def ibr():
            from tests.badResourceSlash import BAD_RESOURCE

        self.assertRaises(ResourceException, ibr)
