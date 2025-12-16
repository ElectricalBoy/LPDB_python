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


class Match(LpdbBaseData):
    def __init__(self, raw):
        super().__init__(raw)

    @property
    def match2id(self) -> str:
        return self._raw.get("match2id")

    @property
    def match2bracketid(self) -> str:
        return self._raw.get("match2bracketid")

    @property
    def status(self) -> str:
        return self._raw.get("status")

    @property
    def winner(self) -> str:
        return self._raw.get("winner")

    @property
    def walkover(self) -> str:
        return self._raw.get("walkover")

    @property
    def resulttype(self) -> str:
        return self._raw.get("resulttype")

    @property
    def finished(self) -> bool:
        return self._raw.get("finished")

    @property
    def mode(self) -> str:
        return self._raw.get("mode")

    @property
    def type(self) -> str:
        return self._raw.get("type")

    @property
    def section(self) -> str:
        return self._raw.get("section")

    @property
    def game(self) -> str:
        return self._raw.get("game")

    @property
    def patch(self) -> str:
        return self._raw.get("patch")

    @property
    def links(self) -> dict[str, Any]:
        return self._raw.get("links")

    @property
    def bestof(self) -> Optional[int]:
        return self._raw.get("bestof")

    @property
    def date(self) -> Optional[datetime]:
        return LpdbBaseData._parseIsoDateTime(self._raw.get("date"))

    @property
    def dateexact(self) -> bool:
        return self._raw.get("dateexact")

    @property
    def stream(self) -> dict[str, Any]:
        return self._raw.get("stream")

    @property
    def vod(self) -> str:
        return self._raw.get("vod")

    @property
    def tournament(self) -> str:
        return self._raw.get("tournament")

    @property
    def parent(self) -> str:
        return self._raw.get("parent")

    @property
    def tickername(self) -> str:
        return self._raw.get("tickername")

    @property
    def shortname(self) -> str:
        return self._raw.get("shortname")

    @property
    def series(self) -> str:
        return self._raw.get("series")

    @property
    def icon(self) -> str:
        return self._raw.get("icon")

    @property
    def iconurl(self) -> str:
        return self._raw.get("iconurl")

    @property
    def icondark(self) -> str:
        return self._raw.get("icondark")

    @property
    def icondarkurl(self) -> str:
        return self._raw.get("icondarkurl")

    @property
    def liquipediatier(self) -> str:
        return self._raw.get("liquipediatier")

    @property
    def liquipediatiertype(self) -> str:
        return self._raw.get("liquipediatiertype")

    @property
    def publishertier(self) -> str:
        return self._raw.get("publishertier")

    @property
    def match2bracketdata(self) -> str:
        return self._raw.get("match2bracketdata")

    @property
    def tickername(self) -> str:
        return self._raw.get("tickername")

    @property
    def match2games(self) -> str:
        return self._raw.get("match2games")

    @property
    def match2opponents(self) -> str:
        return self._raw.get("match2opponents")


def x() -> Broadcasters:
    b = Broadcasters()
    pass
