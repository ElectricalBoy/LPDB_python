from datetime import date
from http import HTTPStatus
from types import TracebackType
from typing import Any, Literal, Optional, Type

import aiohttp

from ..session import AbstractLpdbSession, LpdbError

__all__ = ["AsyncLpdbSession"]


class AsyncLpdbSession(AbstractLpdbSession):
    __session: aiohttp.ClientSession

    def __init__(self, api_key):
        super().__init__(api_key)
        self.__session = aiohttp.ClientSession(AbstractLpdbSession.BASE_URL)

    def __enter__(self) -> None:
        raise TypeError("Use async with instead")

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        pass

    async def __aenter__(self) -> "AsyncLpdbSession":
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        await self.__session.close()

    @staticmethod
    async def get_wikis() -> set[str]:
        async with aiohttp.ClientSession("https://liquipedia.net/") as session:
            async with session.get(
                "api.php",
                params={"action": "listwikis"},
                headers={"accept-encoding": "gzip"},
            ) as response:
                wikis = await response.json()
                return set(wikis["allwikis"].keys())

    @staticmethod
    async def __handle_response(
        response: aiohttp.ClientResponse,
    ) -> list[dict[str, Any]]:
        try:
            return AbstractLpdbSession.parse_results(await response.json())
        except Exception as e:
            if isinstance(e, LpdbError):
                raise e
            status = HTTPStatus(response.status)
            raise LpdbError(status.description) from e

    async def make_request(
        self,
        lpdb_datatype,
        wiki: str | list[str],
        limit: int = 20,
        offset: int = 0,
        conditions: Optional[str] = None,
        query: Optional[list[str]] = None,
        order: Optional[list[tuple[str, Literal["asc", "desc"]]]] = None,
        groupby: Optional[list[tuple[str, Literal["asc", "desc"]]]] = None,
    ) -> list[dict[str, Any]]:
        async with self.__session.get(
            lpdb_datatype,
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
        ) as response:
            return await AsyncLpdbSession.__handle_response(response)

    async def get_team_template(
        self, wiki: str, template: str, date: Optional[date] = None
    ) -> Optional[dict[str, Any]]:
        params = {
            "wiki": wiki,
            "template": template,
        }
        if date != None:
            params["date"] = date.isoformat()
        async with self.__session.get(
            "teamtemplate", headers=self._get_header(), params=params
        ) as response:
            parsed_response = await AsyncLpdbSession.__handle_response(response)
            return parsed_response[0]

    async def get_team_template_list(
        self, wiki: str, pagination: int = 1
    ) -> list[dict[str, Any]]:
        async with self.__session.get(
            "teamtemplatelist",
            headers=self._get_header(),
            params={"wiki": wiki, "pagination": pagination},
        ) as response:
            return await AsyncLpdbSession.__handle_response(response)
