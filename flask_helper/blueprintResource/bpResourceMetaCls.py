from flask_helper.blueprintResource.bpResource import _API_BP_RESOURCE
from flask_helper.exceptions import ResourceException

PREFIX_ATTRIBUTE = "_PREFIX"


class _API_BP_RESOURCE_METACLASS(type):
    def __new__(cls, name: str, bases: tuple[type], attDict: dict):
        # only validate if not base class
        if name != "BLUEPRINT_RESOURCE":
            # validate prefix is defined
            if not PREFIX_ATTRIBUTE in attDict:
                raise ResourceException(
                    "Types Using The 'BLUEPRINT_RESOURCE' As A MetaClass Require The {} Attribute To Be Defined".format(PREFIX_ATTRIBUTE)
                )
            # validate prefix is formatted correctly
            if not attDict[PREFIX_ATTRIBUTE].startswith("/"):
                raise ResourceException("{}.{} Should Be Formatted With A Leading Forward Slash ('/')".format(name, PREFIX_ATTRIBUTE))
            # create the resource objects
            for k, v in attDict.items():
                if str(k).startswith("_"):
                    continue
                attDict[k] = _API_BP_RESOURCE(prefix=attDict[PREFIX_ATTRIBUTE], rule=v)
        return super().__new__(cls, name, bases, attDict)
