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
        return self._raw.get("pageid")

    @property
    def pagename(self) -> str:
        return self._raw.get("pagename")

    @property
    def namespace(self) -> int:
        return self._raw.get("namespace")

    @property
    def objectname(self) -> str:
        return self._raw.get("objectname")

    @property
    def extradata(self) -> Optional[dict[str, Any]]:
        return self._raw.get("extradata")

    @property
    def wiki(self) -> str:
        return self._raw.get("wiki")

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
        return self._raw.get("id")

    @property
    def name(self) -> str:
        return self._raw.get("name")

    @property
    def page(self) -> str:
        return self._raw.get("page")

    @property
    def position(self) -> str:
        return self._raw.get("position")

    @property
    def language(self) -> str:
        return self._raw.get("language")

    @property
    def flag(self) -> str:
        return self._raw.get("flag")

    @property
    def weight(self) -> float:
        return self._raw.get("weight")

    @property
    def date(self) -> Optional[date]:
        return LpdbBaseData._parseIsoDate(self._raw.get("date"))

    @property
    def parent(self) -> str:
        return self._raw.get("parent")


class Company(LpdbBaseData):

    def __init__(self, raw):
        super().__init__(raw)

    @property
    def name(self) -> str:
        return self._raw.get("name")

    @property
    def image(self) -> str:
        return self._raw.get("image")

    @property
    def imageurl(self) -> str:
        return self._raw.get("imageurl")

    @property
    def imagedark(self) -> str:
        return self._raw.get("imagedark")

    @property
    def imagedarkurl(self) -> str:
        return self._raw.get("imagedarkurl")

    @property
    def locations(self) -> list:
        return self._raw.get("locations")

    @property
    def parentcompany(self) -> str:
        return self._raw.get("parentcompany")

    @property
    def sistercompany(self) -> str:
        return self._raw.get("sistercompany")

    @property
    def industry(self) -> str:
        return self._raw.get("industry")

    @property
    def foundeddate(self) -> Optional[datetime]:
        return LpdbBaseData._parseIsoDateTime(self._raw.get("foundeddate"))

    @property
    def defunctdate(self) -> Optional[datetime]:
        return LpdbBaseData._parseIsoDateTime(self._raw.get("defunctdate"))

    @property
    def defunctfate(self) -> str:
        return self._raw.get("defunctfate")

    @property
    def links(self) -> dict[str, Any]:
        return self._raw.get("links")


class Datapoint(LpdbBaseData):

    def __init__(self, raw):
        super().__init__(raw)

    @property
    def type(self) -> str:
        return self._raw.get("type")

    @property
    def name(self) -> str:
        return self._raw.get("name")

    @property
    def information(self) -> str:
        return self._raw.get("information")

    @property
    def imageurl(self) -> str:
        return self._raw.get("imageurl")

    @property
    def imagedark(self) -> str:
        return self._raw.get("imagedark")

    @property
    def imagedarkurl(self) -> str:
        return self._raw.get("imagedarkurl")

    @property
    def date(self) -> Optional[datetime]:
        return LpdbBaseData._parseIsoDateTime(self._raw.get("date"))


class ExternalMediaLink(LpdbBaseData):

    def __init__(self, raw):
        super().__init__(raw)

    @property
    def title(self) -> str:
        return self._raw.get("title")

    @property
    def translatedtitle(self) -> str:
        return self._raw.get("translatedtitle")

    @property
    def link(self) -> str:
        return self._raw.get("link")

    @property
    def date(self) -> Optional[date]:
        return LpdbBaseData._parseIsoDate(self._raw.get("date"))

    @property
    def authors(self) -> dict[str, str]:
        return self._raw.get("authors")

    @property
    def language(self) -> str:
        return self._raw.get("language")

    @property
    def publisher(self) -> str:
        return self._raw.get("publisher")

    @property
    def type(self) -> str:
        return self._raw.get("type")


def x() -> Broadcasters:
    b = Broadcasters()
    pass
