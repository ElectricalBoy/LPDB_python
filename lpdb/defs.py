from datetime import date, datetime, timedelta, timezone, UTC
from enum import StrEnum
from typing import Any, Optional


class OpponentType(StrEnum):
    team = "team"
    solo = "solo"
    duo = "duo"
    trio = "trio"
    quad = "quad"
    literal = "literal"


class LpdbBaseData:
    """
    Base class of all LPDB data
    """

    _raw: dict[str, Any]
    """
    Raw data from LPDB in Python dict form
    """

    def __init__(self, raw: dict[str, Any]):
        self._raw = raw

    def _rawGet(self, key: str):
        value = self._raw.get(key)
        if value == '':
            return None
        return value

    @property
    def extradata(self) -> Optional[dict[str, Any]]:
        return self._rawGet("extradata")

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


class LpdbBaseResponseData(LpdbBaseData):
    """
    Base class of all LPDB response data
    """

    def __init__(self, raw):
        super().__init__(raw)

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


class Broadcasters(LpdbBaseResponseData):

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


class Company(LpdbBaseResponseData):

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


class Datapoint(LpdbBaseResponseData):

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


class ExternalMediaLink(LpdbBaseResponseData):

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


class Match(LpdbBaseResponseData):

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
            return LpdbBaseData._parseIsoDate(self._rawGet("date"))
        parsed = LpdbBaseData._parseIsoDateTime(self._rawGet("date"))
        return parsed.astimezone(tz=self.timezone)

    @property
    def dateexact(self) -> bool:
        return bool(self._rawGet("dateexact"))

    @property
    def timezone(self) -> Optional[timezone]:
        if not self.dateexact:
            return None
        offset: str = self.extradata.get("timezoneoffset")
        if offset == None:
            return None
        sliced_offset = offset.split(":")
        offset_delta = timedelta(
            hours=int(sliced_offset[0]), minutes=int(sliced_offset[1])
        )
        return timezone(offset_delta, name=self.extradata.get("timezoneid"))

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
    def match2games(self) -> list["MatchGame"]:
        return [
            MatchGame(self, match2game) for match2game in self._rawGet("match2games")
        ]

    @property
    def match2opponents(self) -> list["MatchOpponent"]:
        return [
            MatchOpponent(match2opponent)
            for match2opponent in self._rawGet("match2opponents")
        ]


class MatchGame(LpdbBaseData):
    _parent: "Match"

    def __init__(self, parent: "Match", raw: dict[str, Any]):
        super().__init__(raw)
        self._parent = parent

    @property
    def map(self) -> str:
        return self._rawGet("map")

    @property
    def subgroup(self) -> str:
        return self._rawGet("subgroup")

    @property
    def match2gameid(self) -> int:
        return self._rawGet("match2gameid")

    @property
    def scores(self) -> list[int | float]:
        return self._rawGet("scores")

    @property
    def opponents(self) -> list[dict]:
        return self._rawGet("opponents")

    @property
    def status(self) -> str:
        return self._rawGet("status")

    @property
    def winner(self) -> str:
        return self._rawGet("winner")

    @property
    def walkover(self):
        return self._rawGet("walkover")

    @property
    def resulttype(self) -> str:
        return self._rawGet("resulttype")

    @property
    def date(self) -> datetime:
        parsed = LpdbBaseData._parseIsoDateTime(self._rawGet("date"))
        if not self.dateexact:
            return parsed
        return parsed.astimezone(self._parent.timezone)

    @property
    def dateexact(self) -> bool:
        return self.extradata.get("dateexact")

    @property
    def mode(self) -> str:
        return self._rawGet("mode")

    @property
    def type(self) -> str:
        return self._rawGet("type")

    @property
    def game(self) -> str:
        return self._rawGet("game")

    @property
    def patch(self) -> str:
        return self._rawGet("patch")

    @property
    def vod(self) -> str:
        return self._rawGet("vod")

    @property
    def length(self) -> str:
        return self._rawGet("length")


class MatchOpponent(LpdbBaseData):
    _raw: dict[str, Any]

    def __init__(self, raw: dict[str, Any]):
        self._raw = raw

    @property
    def id(self) -> int:
        return self._rawGet("id")

    @property
    def type(self) -> OpponentType:
        return OpponentType(self._rawGet("type"))

    @property
    def name(self) -> str:
        return self._rawGet("name")

    @property
    def template(self) -> Optional[str]:
        return self._rawGet("template")

    @property
    def icon(self) -> str:
        return self._rawGet("icon")

    @property
    def score(self) -> int | float:
        return self._rawGet("score")

    @property
    def status(self) -> str:
        return self._rawGet("status")

    @property
    def placement(self) -> int:
        return self._rawGet("placement")

    @property
    def match2players(self) -> list[dict]:
        return self._rawGet("match2players")

    @property
    def extradata(self) -> dict:
        return self._rawGet("extradata")

    @property
    def teamtemplate(self) -> dict:
        return self._rawGet("teamtemplate")


class Placement(LpdbBaseResponseData):
    def __init__(self, raw):
        super().__init__(raw)

    @property
    def tournament(self) -> str:
        return self._rawGet("tournament")

    @property
    def series(self) -> str:
        return self._rawGet("series")

    @property
    def parent(self) -> str:
        return self._rawGet("parent")

    @property
    def imageurl(self) -> str:
        return self._rawGet("imageurl")

    @property
    def imagedarkurl(self) -> str:
        return self._rawGet("imagedarkurl")

    @property
    def startdate(self) -> Optional[datetime]:
        return LpdbBaseData._parseIsoDateTime(self._rawGet("startdate"))

    @property
    def date(self) -> Optional[datetime]:
        return LpdbBaseData._parseIsoDateTime(self._rawGet("date"))

    @property
    def prizemoney(self) -> int | float:
        return self._rawGet("placement")

    @property
    def weight(self) -> int | float:
        return self._rawGet("weight")

    @property
    def mode(self) -> str:
        return self._rawGet("mode")

    @property
    def type(self) -> str:
        return self._rawGet("type")

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
    def game(self) -> str:
        return self._rawGet("game")

    @property
    def lastvsdata(self) -> dict:
        return self._rawGet("lastvsdata")

    @property
    def opponentname(self) -> str:
        return self._rawGet("opponentname")

    @property
    def opponenttemplate(self) -> Optional[str]:
        return self._rawGet("opponenttemplate")

    @property
    def opponenttype(self) -> OpponentType:
        return OpponentType(self._rawGet("opponenttype"))

    @property
    def opponentplayers(self) -> dict:
        return self._rawGet("opponentplayers")

    @property
    def qualifier(self) -> str:
        return self._rawGet("qualifier")

    @property
    def qualifierpage(self) -> str:
        return self._rawGet("qualifierpage")

    @property
    def qualifierurl(self) -> str:
        return self._rawGet("qualifierurl")


def x() -> Broadcasters:
    b = Broadcasters()
    pass
