"""
compute location of planets for a given period
"""
import pandas as pd
from astropy.coordinates import (AltAz, EarthLocation, get_body,
                                 solar_system_ephemeris)
from astropy.table import QTable
from astropy.time import Time


class Ephemeride:
    """
    Compute location of planets relative to a given place
    """

    DATE = "date"
    PLANETS = ["mercury", "venus", "mars", "jupiter", "saturn", "uranus", "neptune"]

    def __init__(self, address):
        """
        initialize location
        """
        self.location = EarthLocation.of_address(address)
        solar_system_ephemeris.set("de430")

    def get_planet_info(self, planet_name, target_times):
        """
        return alt az information for a given planet and
        a given period
        :param planet_name: english lower case planet name
        :param target_times: time of observations
        """

        time_scale = Time(target_times)
        frame = AltAz(obstime=time_scale, location=self.location)

        planet = get_body(planet_name, time_scale)
        platnet_altazs = planet.transform_to(frame)

        planet_df = QTable([platnet_altazs], names=[planet_name]).to_pandas()
        planet_df["time"] = [str(obs_time) for obs_time in target_times]

        return planet_df

    def get_planets_info(self, target_times):
        """
        get location of planets for a given period
        :param start_datetime: beginning of the period
        :param end_datetime: end of the period
        """

        res = None
        for planet_name in self.PLANETS:
            planet_df = self.get_planet_info(planet_name, target_times)

            if res is None:
                res = planet_df.copy()
            else:
                res = pd.merge(res, planet_df, on=["time"])

        return res
