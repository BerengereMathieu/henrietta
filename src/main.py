"""
Script to use Henrietta library
"""
import argparse
from datetime import datetime

import numpy as np

from henrietta.ephemeride import Ephemeride


def get_args():
    """
    parser for script parameters
    """

    parser = argparse.ArgumentParser(
        prog="henrietta",
        description="Give location of a planet in Altitude-Azimuth system ",
    )

    parser.add_argument("address", help="Observer location, as an address")

    parser.add_argument("json_res_file", help="Json file were to save result")

    parser.add_argument(
        "--planet",
        "-p",
        required=False,
        help="Name of specific planet.If this parameter is not set, \
            results are returned for all planets in the solar system.",
    )

    parser.add_argument(
        "--start_time",
        "-s",
        required=False,
        help="Start of observation period. One observation by hour. \
            If this parameter is not set, observation start at current time.",
    )

    parser.add_argument(
        "--end_time",
        "-e",
        required=False,
        help="End of observation period. One observation by hour. \
            If this parameter is not set, observation end after start time.",
    )

    return parser.parse_args()


def main():
    """
    script entrypoint
    """
    args = get_args()

    ephem = Ephemeride(args.address)

    if args.start_time:
        start_time = args.start_time
    else:
        # use current time
        start_time = str(datetime.now())

    if args.end_time:
        target_times = np.arange(
            np.datetime64(start_time),
            np.datetime64(args.end_time),
            np.timedelta64(1, "h"),
        ).tolist()
    else:
        target_times = np.arange(
            np.datetime64(start_time),
            np.datetime64(start_time) + np.timedelta64(1, "h"),
            np.timedelta64(1, "h"),
        ).tolist()

    if args.planet:
        observations = ephem.get_planet_info(args.planet, target_times)
    else:
        observations = ephem.get_planets_info(target_times)

    observations.to_json(args.json_res_file)


if __name__ == "__main__":
    main()
