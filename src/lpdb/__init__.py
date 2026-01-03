"""
Python interface for Liquipedia Database (LPDB) API
"""

import importlib.metadata as _metadata

from .defs import *
from .session import *

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

__version__ = _metadata.version("LPDB_python")
