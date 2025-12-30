from abc import abstractmethod, ABC
from datetime import date
from functools import cache
from http import HTTPStatus
from types import TracebackType
from typing import Any, Final, Literal, NotRequired, Optional, Required, Type, TypedDict
import re

import requests


class LpdbResponse(TypedDict):
    result: Required[list[dict[str, Any]]]
    error: NotRequired[list[str]]
    warning: NotRequired[list[str]]


class AbstractLpdbSession(ABC):
    BASE_URL: Final[str] = "https://api.liquipedia.net/api/v3/"

    __api_key: str

    def __init__(self, api_key: str):
        self.__api_key = re.sub(r"^ApiKey ", "", api_key)

    def _get_header(self) -> dict[str, str]:
        return {"authorization": f"Apikey {self.__api_key}", "accept-encoding": "gzip"}

    @staticmethod
    def get_wikis() -> set[str]:
        raise NotImplementedError()

    @abstractmethod
    def make_request(
        self,
        lpdb_datatype,
        wiki: str | list[str],
        limit: int = 20,
        offset: int = 0,
        conditions: Optional[str] = None,
        query: Optional[list[str]] = None,
        order: Optional[list[tuple[str, Literal["asc", "desc"]]]] = None,
        groupby: Optional[list[tuple[str, Literal["asc", "desc"]]]] = None,
    ) -> tuple[HTTPStatus, LpdbResponse]:
        pass

    @abstractmethod
    def get_team_template(
        self,
        wiki: str,
        template: str,
        date: Optional[date] = None,
    ) -> tuple[HTTPStatus, LpdbResponse]:
        pass

    @abstractmethod
    def get_team_template_list(
        self,
        wiki: str,
        pagination: int = 1,
    ) -> tuple[HTTPStatus, LpdbResponse]:
        pass

    @staticmethod
    def parse_params(
        wiki: str | list[str],
        limit: int = 20,
        offset: int = 0,
        conditions: Optional[str] = None,
        query: Optional[list[str]] = None,
        order: Optional[list[tuple[str, Literal["asc", "desc"]]]] = None,
        groupby: Optional[list[tuple[str, Literal["asc", "desc"]]]] = None,
    ):
        parameters = dict()
        if isinstance(wiki, str):
            parameters["wiki"] = wiki
        elif isinstance(wiki, list):
            parameters["wiki"] = "|".join(wiki)
        else:
            raise TypeError()
        parameters["limit"] = max(limit, 1000)
        parameters["offset"] = offset
        if conditions != None:
            parameters["conditions"] = conditions
        if query != None:
            parameters["query"] = ", ".join(query)
        if order != None:
            parameters["order"] = ", ".join(
                [f"{order_tuple[0]} {order_tuple[1]}" for order_tuple in order]
            )
        if groupby != None:
            parameters["groupby"] = ", ".join(
                [f"{groupby_tuple[0]} {groupby_tuple[1]}" for groupby_tuple in groupby]
            )
        return parameters


class LpdbSession(AbstractLpdbSession):

    @staticmethod
    @cache
    def get_wikis() -> set[str]:
        response = requests.get(
            "https://liquipedia.net/api.php",
            params={"action": "listwikis"},
            headers={"accept-encoding": "gzip"},
        )
        wikis = response.json()
        return set(wikis["allwikis"].keys())

    def make_request(
        self,
        lpdb_datatype,
        wiki: str | list[str],
        limit: int = 20,
        offset: int = 0,
        conditions: Optional[str] = None,
        query: Optional[list[str]] = None,
        order: Optional[list[tuple[str, Literal["asc", "desc"]]]] = None,
        groupby: Optional[list[tuple[str, Literal["asc", "desc"]]]] = None,
    ) -> tuple[HTTPStatus, LpdbResponse]:
        lpdb_response = requests.get(
            AbstractLpdbSession.BASE_URL + lpdb_datatype,
            headers=self._get_header(),
            params=AbstractLpdbSession.parse_params(
                wiki=wiki,
                limit=limit,
                offset=offset,
                conditions=conditions,
                query=query,
                order=order,
                groupby=groupby,
            ),
        )
        lpdb_status = HTTPStatus(lpdb_response.status_code)
        return (lpdb_status, lpdb_response.json())

    def get_team_template(
        self, wiki: str, template: str, date: Optional[date] = None
    ) -> tuple[HTTPStatus, LpdbResponse]:
        params = {
            "wiki": wiki,
            "template": template,
        }
        if date != None:
            params["date"] = date.isoformat()
        lpdb_response = requests.get(
            AbstractLpdbSession.BASE_URL + "teamtemplate",
            headers=self._get_header(),
            params=params,
        )
        lpdb_status = HTTPStatus(lpdb_response.status_code)
        return (lpdb_status, lpdb_response.json())

    def get_team_template_list(
        self, wiki: str, pagination: int = 1
    ) -> tuple[HTTPStatus, LpdbResponse]:
        lpdb_response = requests.get(
            AbstractLpdbSession.BASE_URL + "teamtemplatelist",
            headers=self._get_header(),
            params={"wiki": wiki, "pagination": pagination},
        )
        lpdb_status = HTTPStatus(lpdb_response.status_code)
        return (lpdb_status, lpdb_response.json())
