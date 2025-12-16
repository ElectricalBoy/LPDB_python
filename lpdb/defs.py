from datetime import date, datetime, timedelta, timezone, UTC
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

    def _rawGet(self, key: str):
        return self._raw.get(key)

    @property
    def pageid(self) -> int:
        return self._rawGet("pageid")

    @property
    def pagename(self) -> str:
        return self._rawGet("pagename")

    @property
    def namespace(self) -> int:
        return self._rawGet("namespace")

    @property
    def objectname(self) -> str:
        return self._rawGet("objectname")

    @property
    def extradata(self) -> Optional[dict[str, Any]]:
        return self._rawGet("extradata")

    @property
    def wiki(self) -> str:
        return self._rawGet("wiki")

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
        return self._rawGet("id")

    @property
    def name(self) -> str:
        return self._rawGet("name")

    @property
    def page(self) -> str:
        return self._rawGet("page")

    @property
    def position(self) -> str:
        return self._rawGet("position")

    @property
    def language(self) -> str:
        return self._rawGet("language")

    @property
    def flag(self) -> str:
        return self._rawGet("flag")

    @property
    def weight(self) -> float:
        return self._rawGet("weight")

    @property
    def date(self) -> Optional[date]:
        return LpdbBaseData._parseIsoDate(self._rawGet("date"))

    @property
    def parent(self) -> str:
        return self._rawGet("parent")


class Company(LpdbBaseData):

    def __init__(self, raw):
        super().__init__(raw)

    @property
    def name(self) -> str:
        return self._rawGet("name")

    @property
    def image(self) -> str:
        return self._rawGet("image")

    @property
    def imageurl(self) -> str:
        return self._rawGet("imageurl")

    @property
    def imagedark(self) -> str:
        return self._rawGet("imagedark")

    @property
    def imagedarkurl(self) -> str:
        return self._rawGet("imagedarkurl")

    @property
    def locations(self) -> list:
        return self._rawGet("locations")

    @property
    def parentcompany(self) -> str:
        return self._rawGet("parentcompany")

    @property
    def sistercompany(self) -> str:
        return self._rawGet("sistercompany")

    @property
    def industry(self) -> str:
        return self._rawGet("industry")

    @property
    def foundeddate(self) -> Optional[datetime]:
        return LpdbBaseData._parseIsoDateTime(self._rawGet("foundeddate"))

    @property
    def defunctdate(self) -> Optional[datetime]:
        return LpdbBaseData._parseIsoDateTime(self._rawGet("defunctdate"))

    @property
    def defunctfate(self) -> str:
        return self._rawGet("defunctfate")

    @property
    def links(self) -> dict[str, Any]:
        return self._rawGet("links")


class Datapoint(LpdbBaseData):

    def __init__(self, raw):
        super().__init__(raw)

    @property
    def type(self) -> str:
        return self._rawGet("type")

    @property
    def name(self) -> str:
        return self._rawGet("name")

    @property
    def information(self) -> str:
        return self._rawGet("information")

    @property
    def imageurl(self) -> str:
        return self._rawGet("imageurl")

    @property
    def imagedark(self) -> str:
        return self._rawGet("imagedark")

    @property
    def imagedarkurl(self) -> str:
        return self._rawGet("imagedarkurl")

    @property
    def date(self) -> Optional[datetime]:
        return LpdbBaseData._parseIsoDateTime(self._rawGet("date"))


class ExternalMediaLink(LpdbBaseData):

    def __init__(self, raw):
        super().__init__(raw)

    @property
    def title(self) -> str:
        return self._rawGet("title")

    @property
    def translatedtitle(self) -> str:
        return self._rawGet("translatedtitle")

    @property
    def link(self) -> str:
        return self._rawGet("link")

    @property
    def date(self) -> Optional[date]:
        return LpdbBaseData._parseIsoDate(self._rawGet("date"))

    @property
    def authors(self) -> dict[str, str]:
        return self._rawGet("authors")

    @property
    def language(self) -> str:
        return self._rawGet("language")

    @property
    def publisher(self) -> str:
        return self._rawGet("publisher")

    @property
    def type(self) -> str:
        return self._rawGet("type")


class Match(LpdbBaseData):
    def __init__(self, raw):
        super().__init__(raw)

    @property
    def match2id(self) -> str:
        return self._rawGet("match2id")

    @property
    def match2bracketid(self) -> str:
        return self._rawGet("match2bracketid")

    @property
    def status(self) -> str:
        return self._rawGet("status")

    @property
    def winner(self) -> str:
        return self._rawGet("winner")

    @property
    def walkover(self) -> str:
        return self._rawGet("walkover")

    @property
    def resulttype(self) -> str:
        return self._rawGet("resulttype")

    @property
    def finished(self) -> bool:
        return bool(self._rawGet("finished"))

    @property
    def mode(self) -> str:
        return self._rawGet("mode")

    @property
    def type(self) -> str:
        return self._rawGet("type")

    @property
    def section(self) -> str:
        return self._rawGet("section")

    @property
    def game(self) -> str:
        return self._rawGet("game")

    @property
    def patch(self) -> str:
        return self._rawGet("patch")

    @property
    def links(self) -> dict[str, Any]:
        return self._rawGet("links")

    @property
    def bestof(self) -> Optional[int]:
        return self._rawGet("bestof")

    @property
    def date(self) -> Optional[date | datetime]:
        if not self.dateexact:
            return  LpdbBaseData._parseIsoDate(self._rawGet("date"))
        parsed = LpdbBaseData._parseIsoDateTime(self._rawGet("date"))
        offset: str = self.extradata.get('timezoneoffset')
        if offset == None:
            return parsed
        sliced_offset = offset.split(':')
        offset_delta = timedelta(hours=int(sliced_offset[0]), minutes=int(sliced_offset[1]))
        return parsed.astimezone(tz=timezone(offset_delta, name=self.extradata.get('timezoneid')))

    @property
    def dateexact(self) -> bool:
        return bool(self._rawGet("dateexact"))

    @property
    def stream(self) -> dict[str, Any]:
        return self._rawGet("stream")

    @property
    def vod(self) -> str:
        return self._rawGet("vod")

    @property
    def tournament(self) -> str:
        return self._rawGet("tournament")

    @property
    def parent(self) -> str:
        return self._rawGet("parent")

    @property
    def tickername(self) -> str:
        return self._rawGet("tickername")

    @property
    def shortname(self) -> str:
        return self._rawGet("shortname")

    @property
    def series(self) -> str:
        return self._rawGet("series")

    @property
    def icon(self) -> str:
        return self._rawGet("icon")

    @property
    def iconurl(self) -> str:
        return self._rawGet("iconurl")

    @property
    def icondark(self) -> str:
        return self._rawGet("icondark")

    @property
    def icondarkurl(self) -> str:
        return self._rawGet("icondarkurl")

    @property
    def liquipediatier(self) -> str:
        return self._rawGet("liquipediatier")

    @property
    def liquipediatiertype(self) -> str:
        return self._rawGet("liquipediatiertype")

    @property
    def publishertier(self) -> str:
        return self._rawGet("publishertier")

    @property
    def match2bracketdata(self) -> dict:
        return self._rawGet("match2bracketdata")

    @property
    def tickername(self) -> str:
        return self._rawGet("tickername")

    @property
    def match2games(self) -> list:
        return self._rawGet("match2games")

    @property
    def match2opponents(self) -> list:
        return self._rawGet("match2opponents")


def x() -> Broadcasters:
    b = Broadcasters()
    pass
