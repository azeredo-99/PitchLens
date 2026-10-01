from pitchlens.config import MVP_COMPETITIONS


def test_mvp_competitions_match_adr_0006() -> None:
    ids = {(c.competition_id, c.season_id) for c in MVP_COMPETITIONS}
    assert ids == {(55, 282), (53, 315), (2, 27)}


def test_competition_keys_are_unique() -> None:
    keys = [c.key for c in MVP_COMPETITIONS]
    assert len(keys) == len(set(keys))


def test_xg_v2_needs_at_least_two_competitions_with_360() -> None:
    assert sum(c.has_360 for c in MVP_COMPETITIONS) >= 2
