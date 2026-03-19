from kisat.blueprintResource.bpResource import _API_BP_RESOURCE
from kisat.exceptions import ResourceException
import logging

PREFIX_ATTRIBUTE = "_PREFIX"

_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())


class _API_BP_RESOURCE_METACLASS(type):
    def __new__(cls, name: str, bases: tuple[type], attDict: dict):
        # only validate if not base class
        if name != "BLUEPRINT_RESOURCE":
            # validate prefix is defined
            if not PREFIX_ATTRIBUTE in attDict:
                msg = "Types Using The 'BLUEPRINT_RESOURCE' As A MetaClass Require The {} Attribute To Be Defined".format(PREFIX_ATTRIBUTE)
                _logger.debug(msg)
                raise ResourceException(msg)
            # validate prefix is formatted correctly
            if not attDict[PREFIX_ATTRIBUTE].startswith("/"):
                msg = "{}.{} Should Be Formatted With A Leading Forward Slash ('/')".format(name, PREFIX_ATTRIBUTE)
                _logger.debug(msg)
                raise ResourceException(msg)
            # create the resource objects
            for k, v in attDict.items():
                if str(k).startswith("_"):
                    continue
                attDict[k] = _API_BP_RESOURCE(prefix=attDict[PREFIX_ATTRIBUTE], rule=v)
        return super().__new__(cls, name, bases, attDict)
