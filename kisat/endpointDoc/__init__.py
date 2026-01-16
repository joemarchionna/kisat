from enum import Enum


class DOCSTRING_STYLE(Enum):
    RESTRUCTXT = 1
    GOOGLE = 2
    NUMPY = 3
    OTHER = 100


_DS_DESC_END = {DOCSTRING_STYLE.RESTRUCTXT: [":"], DOCSTRING_STYLE.GOOGLE: ["args", "return"], DOCSTRING_STYLE.NUMPY: ["parameters", "return"]}


def methodDesc(method, docStrType: DOCSTRING_STYLE = DOCSTRING_STYLE.RESTRUCTXT, terminatingStrs: list[str] = None) -> str:
    """
    returns a single-line string based on evaluating the __doc__ field of the method provided

    :param method: the callable method to evaluate the docstring of
    :type method: callable
    :param docStrType: the style the docstring is authored in
    :type docStrType: DOCSTRING_STYLE
    :param terminatingStrs: terminating strings used if DOCSTRING_STYLE.OTHER is specified, when evaluating the docstring, the evaluation of the docstring ends when it comes across a line that begins with any of these strings
    :type terminatingStrs: list[str]
    :return: single line string
    :rtype: str
    """
    if not method.__doc__:
        return ""
    lines = method.__doc__.split("\n")
    endPatterns = _DS_DESC_END.get(docStrType, terminatingStrs)
    desc = []
    for s in lines:
        s = s.strip()
        if s:
            sl = s.lower()
            if any([sl.startswith(x) for x in endPatterns]):
                break
            desc.append(s)
    return " ".join(desc)
