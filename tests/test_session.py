import os

import pytest

import lpdb

KEY = os.getenv("API_KEY")


@pytest.fixture
def session() -> lpdb.LpdbSession:
    return lpdb.LpdbSession(KEY)


def test_get_wikis(session: lpdb.LpdbSession):
    wikis = session.get_wikis()
    assert isinstance(wikis, set)
    # Test with top 5 wikis
    assert {
        "dota2",
        "counterstrike",
        "valorant",
        "mobilelegends",
        "leagueoflegends",
    }.issubset(wikis)


def test_make_request_invalid_key():
    session = lpdb.LpdbSession("some_random_gibberish")
    with pytest.raises(lpdb.LpdbError):
        session.make_request(
            "match",
            "leagueoflegends",
            conditions="[[parent::World_Championship/2025]]",
            streamurls="true",
        )


def test_make_request_invalid_type(session: lpdb.LpdbSession):
    with pytest.raises(ValueError):
        session.make_request("match2", "leagueoflegends")


def test_make_request(session: lpdb.LpdbSession):
    responses = session.make_request(
        "match",
        "leagueoflegends",
        conditions="[[parent::World_Championship/2025]]",
        streamurls="true",
    )

    for response in responses:
        assert response["parent"] == "World_Championship/2025"


def test_get_team_template(session: lpdb.LpdbSession):
    template = session.get_team_template("leagueoflegends", "t1")
    assert template["page"] == "T1"


def test_get_team_templates(session: lpdb.LpdbSession):
    templates = session.get_team_template_list("leagueoflegends")
    assert isinstance(templates, list)
    for template in templates:
        assert isinstance(template["page"], str)
