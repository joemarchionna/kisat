from enum import Enum
import logging


class DOCSTRING_STYLE(Enum):
    RESTRUCTXT = 1
    GOOGLE = 2
    NUMPY = 3
    OTHER = 100


_DS_DESC_END = {
    DOCSTRING_STYLE.RESTRUCTXT: [":"],
    DOCSTRING_STYLE.GOOGLE: ["arg", "argument", "attribute", "raise", "return", "example", "----"],
    DOCSTRING_STYLE.NUMPY: ["parameter", "raise", "return", "example", "----"],
}

_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())

FIRST_LINE_TERMS_MSG = "The First Line Of The DOC String For Method '{}' Starts With A Terminating String, This May Be Unintentional"


def methodDesc(method, docStrType: DOCSTRING_STYLE = DOCSTRING_STYLE.GOOGLE, terminatingStrs: list[str] = []) -> str:
    """
    returns a single-line string based on evaluating the __doc__ field of the method provided

    Args:
        method (callable): the callable method to evaluate the docstring of
        docStrType (DOCSTRING_STYLE, optional): the style the docstring is authored in. Defaults to DOCSTRING_STYLE.GOOGLE
        terminatingStrs (list[str], optional): terminating strings used if DOCSTRING_STYLE.OTHER is specified, when evaluating the docstring, the evaluation of the docstring ends when it comes across a line that begins with any of these strings. Defaults to an empty list

    Returns:
        str: single line string
    """
    if not method.__doc__:
        _logger.debug("No Doc String Found For {}".format(method.__name__))
        return ""
    lines = method.__doc__.split("\n")
    endPatterns = _DS_DESC_END.get(docStrType, terminatingStrs)
    # print("EP: {}; LINES: {}".format(endPatterns,lines))
    desc = []
    for i, s in enumerate(lines):
        ss = s.strip()
        if ss:
            sl = ss.lower()
            if any([sl.startswith(x) for x in endPatterns]):
                if i == 0:
                    _logger.debug(FIRST_LINE_TERMS_MSG.format(method.__name__))
                break
            desc.append(ss)
    ds = " ".join(desc)
    _logger.debug("Doc String For {}: {}".format(method.__name__, ds))
    return ds
