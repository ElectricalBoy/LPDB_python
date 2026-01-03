import os

import pytest
import pytest_asyncio

import lpdb
from lpdb.async_session import AsyncLpdbSession


KEY = os.getenv("API_KEY")


@pytest_asyncio.fixture
async def async_session() -> AsyncLpdbSession:
    return AsyncLpdbSession(KEY)


@pytest.mark.asyncio
async def test_get_wikis(async_session: AsyncLpdbSession):
    wikis = await async_session.get_wikis()
    assert isinstance(wikis, set)
    # Test with top 5 wikis
    assert {
        "dota2",
        "counterstrike",
        "valorant",
        "mobilelegends",
        "leagueoflegends",
    }.issubset(wikis)


@pytest.mark.asyncio
async def test_make_request_invalid_key():
    with pytest.raises(lpdb.LpdbError):
        async with AsyncLpdbSession("some_random_gibberish") as async_session:
            await async_session.make_request(
                "match",
                "valorant",
                conditions="[[parent::VCT/2025/Stage_1/Masters]]",
                streamurls="true",
            )


@pytest.mark.asyncio
async def test_make_request_invalid_type(async_session: AsyncLpdbSession):
    with pytest.raises(ValueError):
        await async_session.make_request("match2", "valorant")


@pytest.mark.asyncio
async def test_make_request(async_session: AsyncLpdbSession):
    responses = await async_session.make_request(
        "match",
        "valorant",
        conditions="[[parent::VCT/2025/Stage_1/Masters]]",
        streamurls="true",
    )

    for response in responses:
        assert response["parent"] == "VCT/2025/Stage_1/Masters"


@pytest.mark.asyncio
async def test_get_team_template(async_session: AsyncLpdbSession):
    template = await async_session.get_team_template("valorant", "t1")
    assert template["page"] == "T1"


@pytest.mark.asyncio
async def test_get_team_templates(async_session: AsyncLpdbSession):
    templates = await async_session.get_team_template_list("valorant")
    assert isinstance(templates, list)
    for template in templates:
        assert isinstance(template["page"], str)
