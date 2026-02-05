"""
Python interface for Liquipedia Database (LPDB) API
"""

import importlib.metadata as _metadata

from .defs import (
    OpponentType,
    Broadcasters,
    Company,
    Datapoint,
    ExternalMediaLink,
    Match,
    MatchGame,
    MatchOpponent,
    Placement,
    Player,
    Series,
    SquadPlayer,
    StandingsEntry,
    StandingsTable,
    Team,
    Tournament,
    Transfer,
    TeamTemplate,
)
from .session import LpdbError, LpdbWarning, LpdbSession

__all__ = [
    "OpponentType",
    "Broadcasters",
    "Company",
    "Datapoint",
    "ExternalMediaLink",
    "LpdbError",
    "LpdbWarning",
    "LpdbSession",
    "Match",
    "MatchGame",
    "MatchOpponent",
    "Placement",
    "Player",
    "Series",
    "SquadPlayer",
    "StandingsEntry",
    "StandingsTable",
    "Team",
    "Tournament",
    "Transfer",
    "TeamTemplate",
]

try:
    __version__ = _metadata.version(__name__)
except _metadata.PackageNotFoundError:
    __version__ = "0.0.0"
