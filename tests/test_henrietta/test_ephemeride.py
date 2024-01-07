"""
unit tests for henrietta ephemeride classe
"""
import numpy as np

from henrietta.ephemeride import Ephemeride

ADDRESS = "Pl. Champollion 46100 Figeac"


def test_get_planet_info():
    """
    check venus is visible and mercury is invisible
    """

    ephem = Ephemeride(ADDRESS)

    start_time = "2023-09-02 05:00:00"
    target_times = np.arange(
        np.datetime64(start_time),
        np.datetime64(start_time) + np.timedelta64(1, "h"),
        np.timedelta64(1, "h"),
    ).tolist()

    venus_info = ephem.get_planet_info("venus", target_times)

    assert venus_info["venus.alt"].iloc[0] > 0

    venus_info = ephem.get_planet_info("mercury", target_times)

    assert venus_info["mercury.alt"].iloc[0] < 0


def test_get_planets_info():
    """
    check venus is visible and mercury is invisible
    """

    ephem = Ephemeride(ADDRESS)

    start_time = "2023-09-02 05:00:00"
    target_times = np.arange(
        np.datetime64(start_time),
        np.datetime64(start_time) + np.timedelta64(1, "h"),
        np.timedelta64(1, "h"),
    ).tolist()

    venus_info = ephem.get_planets_info(target_times)

    assert venus_info["venus.alt"].iloc[0] > 0

    assert venus_info["mercury.alt"].iloc[0] < 0
