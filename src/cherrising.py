"""
Henrietta Web API 
"""
import json
from datetime import datetime

import cherrypy
import numpy as np

from henrietta.ephemeride import Ephemeride


def to_valuable_json(raw_json_observation):
    """
    convert DataFrame json conversion to a more
    usable json object by spliting column name
    in different keys.
    """
    valuable_json = {}
    for column_name, cell_value in raw_json_observation.items():
        print(column_name, cell_value)
        new_keys = column_name.split(".")

        current_dict = valuable_json
        for num_key, key_name in enumerate(new_keys):
            if key_name not in current_dict:
                current_dict[key_name] = {}

            if num_key == len(new_keys) - 1:
                current_dict[key_name] = cell_value["0"]

            current_dict = current_dict[key_name]

    return json.dumps(valuable_json)


@cherrypy.expose
class HenriettaAPI:
    """
    For a given place and and a given time
    get location of solar system planets
    in Altitude-Azimuth system
    """

    @cherrypy.tools.accept(media="application/json")
    def GET(
        self, address="Pl. Champollion 46100 Figeac", local_time=None
    ):  # pylint: disable=invalid-name
        """
        single API entry point to get information about locations of solar planets
        for a given observer
        """

        ephem = Ephemeride(address)

        if local_time is None:
            local_time = str(datetime.now())

        target_times = np.arange(
            np.datetime64(local_time),
            np.datetime64(local_time) + np.timedelta64(1, "h"),
            np.timedelta64(1, "h"),
        ).tolist()

        observations = ephem.get_planets_info(target_times)

        observations_raw_json = json.loads(observations.to_json())

        return to_valuable_json(observations_raw_json)


if __name__ == "__main__":
    conf = {
        "/": {
            "request.dispatch": cherrypy.dispatch.MethodDispatcher(),
            "tools.sessions.on": True,
            "tools.response_headers.on": True,
            "tools.response_headers.headers": [("Content-Type", "application/json")],
            "tools.encode.text_only": False,
        }
    }
    cherrypy.quickstart(HenriettaAPI(), "/", conf)
