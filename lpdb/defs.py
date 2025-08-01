from datetime import date, datetime, UTC
from typing import Any, Optional


class LpdbBaseData:
    """
    Base class of all LPDB response data
    """

    _raw: dict[str, Any]
    """
    Raw response from LPDB in Python dict form
    """

    def __init__(self, raw: dict[str, Any]):
        self._raw = raw

    @property
    def pageid(self) -> int:
        return self._raw["pageid"]

    @property
    def pagename(self) -> str:
        return self._raw["pagename"]

    @property
    def namespace(self) -> int:
        return self._raw["namespace"]

    @property
    def objectname(self) -> str:
        return self._raw["objectname"]

    @property
    def extradata(self) -> Optional[dict[str, Any]]:
        return self._raw["extradata"]

    @property
    def wiki(self) -> str:
        return self._raw["wiki"]

    def __repr__(self):
        return repr(self._raw)

    @staticmethod
    def _parseIsoDate(date_str: str) -> Optional[date]:
        try:
            return date.fromisoformat(date_str)
        except ValueError:
            return None

    @staticmethod
    def _parseIsoDateTime(datetime_str: str) -> Optional[datetime]:
        try:
            return datetime.fromisoformat(datetime_str).replace(tzinfo=UTC)
        except ValueError:
            return None


class Broadcasters(LpdbBaseData):

    def __init__(self, raw):
        super().__init__(raw)

    @property
    def id(self) -> str:
        return self._raw["id"]

    @property
    def name(self) -> str:
        return self._raw["name"]

    @property
    def page(self) -> str:
        return self._raw["page"]

    @property
    def position(self) -> str:
        return self._raw["position"]

    @property
    def language(self) -> str:
        return self._raw["language"]

    @property
    def flag(self) -> str:
        return self._raw["flag"]

    @property
    def weight(self) -> float:
        return self._raw["weight"]

    @property
    def date(self) -> Optional[date]:
        return LpdbBaseData._parseIsoDate(self._raw["date"])

    @property
    def parent(self) -> str:
        return self._raw["parent"]


class Company(LpdbBaseData):

    def __init__(self, raw):
        super().__init__(raw)

    @property
    def name(self) -> str:
        return self._raw["name"]

    @property
    def image(self) -> str:
        return self._raw["image"]

    @property
    def imageurl(self) -> str:
        return self._raw["imageurl"]

    @property
    def imagedark(self) -> str:
        return self._raw["imagedark"]

    @property
    def imagedarkurl(self) -> str:
        return self._raw["imagedarkurl"]

    @property
    def locations(self) -> list:
        return self._raw["locations"]

    @property
    def parentcompany(self) -> str:
        return self._raw["parentcompany"]

    @property
    def sistercompany(self) -> str:
        return self._raw["sistercompany"]

    @property
    def industry(self) -> str:
        return self._raw["industry"]

    @property
    def foundeddate(self) -> Optional[datetime]:
        return LpdbBaseData._parseIsoDateTime(self._raw["foundeddate"])

    @property
    def defunctdate(self) -> Optional[datetime]:
        return LpdbBaseData._parseIsoDateTime(self._raw["defunctdate"])

    @property
    def defunctfate(self) -> str:
        return self._raw["defunctfate"]

    @property
    def links(self) -> dict[str, Any]:
        return self._raw['links']


class Datapoint(LpdbBaseData):

    def __init__(self, raw):
        super().__init__(raw)

    @property
    def type(self) -> str:
        return self._raw["type"]

    @property
    def name(self) -> str:
        return self._raw["name"]

    @property
    def information(self) -> str:
        return self._raw["information"]

    @property
    def imageurl(self) -> str:
        return self._raw["imageurl"]

    @property
    def imagedark(self) -> str:
        return self._raw["imagedark"]

    @property
    def imagedarkurl(self) -> str:
        return self._raw["imagedarkurl"]

    @property
    def date(self) -> Optional[datetime]:
        return LpdbBaseData._parseIsoDateTime(self._raw["date"])


def x() -> Broadcasters:
    b = Broadcasters()
    pass
