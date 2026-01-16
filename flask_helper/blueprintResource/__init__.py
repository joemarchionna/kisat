from flask_helper.blueprintResource.bpResourceMetaCls import PREFIX_ATTRIBUTE, _API_BP_RESOURCE_METACLASS


class BLUEPRINT_RESOURCE(metaclass=_API_BP_RESOURCE_METACLASS):
    """
    base or parent class of a url endpoint specification\n
    the sub-class can then be used as a reference for clients and the server specification

    server usage:
    ```python
        from client import STATUS_RESOURCE
        from flask import Flask
        app = Flask(__name__)
        bp = Blueprint("status", __name__, url_prefix=STATUS_RESOURCE._PREFIX)
        app.register_blueprint(bp)

        @app.route(STATUS_RESOURCE.INDEX.rule)
        @app.route(STATUS_RESOURCE.HEARTBEAT.rule)
        def hb():
            return "I'm Alive"

        @app.route(STATUS_RESOURCE.VERSION.rule)
        def ver():
            return "1.0.0"
    ```

    client usage:
    ```python
        import requests

        class STATUS_RESOURCE(BLUEPRINT_RESOURCE):
            _PREFIX = "/status"
            INDEX = ""
            HEARTBEAT = "/hb"
            VERSION = "/version"

        requests.get(baseUrl + STATUS_RESOURCE.VERSION)
        >>> 1.0.0
    ```
    """

    @classmethod
    def prefix(cls, prefixAttr: str = PREFIX_ATTRIBUTE) -> str:
        return getattr(cls, prefixAttr)
