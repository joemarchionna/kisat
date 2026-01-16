from kisat.endpointDoc import methodDesc, DOCSTRING_STYLE
import unittest


def nd(a: int, b: int) -> int:
    return a + b


def eds(a: int, b: int) -> int:
    """"""
    return a + b


def sd(a: int, b: int) -> int:
    """
    docstring for method

    :param a: Description
    :type a: int
    """
    return a + b


def dd(a: int, b: int) -> int:
    """
    docstring for method,
    this does crazy stuff

    :param a: Description
    :type a: int
    """
    return a + b


def sg(a: int, b: int) -> int:
    """
    docstring for method

    Args:
        a (int): Description
    """
    return a + b


def sn(a: int, b: int) -> int:
    """
    docstring for method

    Parameters
    ----------
        a : int
            Description
    """
    return a + b


def snnp() -> int:
    """
    docstring for method

    Returns
    -------
    int
        It's Always 8
    """
    return 8


class TestEndpointDoc(unittest.TestCase):
    def test_a_nd(self):
        md = methodDesc(nd)
        self.assertEqual("", md)

    def test_a_eds(self):
        md = methodDesc(eds)
        self.assertEqual("", md)

    def test_b_sd(self):
        md = methodDesc(sd)
        # print("Method Description: '{}'".format(md))
        self.assertEqual("docstring for method", md)

    def test_c_dd(self):
        md = methodDesc(dd)
        # print("Method Description: '{}'".format(md))
        self.assertEqual("docstring for method, this does crazy stuff", md)

    def test_d_sg(self):
        md = methodDesc(sg, DOCSTRING_STYLE.GOOGLE)
        # print("Method Description: '{}'".format(md))
        self.assertEqual("docstring for method", md)

    def test_e_sn(self):
        md = methodDesc(sn, DOCSTRING_STYLE.NUMPY)
        # print("Method Description: '{}'".format(md))
        self.assertEqual("docstring for method", md)

    def test_e_snnp(self):
        md = methodDesc(snnp, DOCSTRING_STYLE.NUMPY)
        # print("Method Description: '{}'".format(md))
        self.assertEqual("docstring for method", md)
