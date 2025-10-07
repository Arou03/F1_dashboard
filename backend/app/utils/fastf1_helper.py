# f1_cache_helpers.py
import fastf1
import logging
from app.services.cache_service import CacheService

fastf1.set_log_level(logging.ERROR)
cache = CacheService()

def get_session_cached(season: int, gp_name: str):
    cache_key = f"session_{season}_{gp_name}_R"
    cached = cache.get(cache_key)
    if cached is not None:
        return cached

    session = fastf1.get_session(season, gp_name, 'R')
    session.load()
    cache.set(cache_key, session)
    return session


def get_race_results_by_driver(season: int, gp_name: str):
    session = get_session_cached(season, gp_name)
    return session.results.loc[:, ['FullName', 'Points']]


def get_race_results_by_team(season: int, gp_name: str):
    session = get_session_cached(season, gp_name)
    return session.results.loc[:, ['TeamName', 'Points']].groupby(['TeamName'], as_index=False).sum()
