# henrietta

Get horizontal coordinate of observable planets from a reference point. 

Project is on [NU AFFERO GENERAL PUBLIC LICENSE Version 3] licence

## Initialize project

1. Create Python virtualenv: `python -m venv .venv`
2. [Activate it](https://docs.python.org/3/tutorial/venv.html)
3. Install henrietta project: `pip install .`
4. Install devops dependancies: `pip install -r requirements.txt`
5. Run tox: `tox`

## Usage

Use the script `src/main.py`

```
python src/main.py --help
usage: henrietta [-h] [--planet PLANET] [--start_time START_TIME] [--end_time END_TIME] adress json_res_file

Give location of a planet in Altitude-Azimuth system

positional arguments:
  adress                Observer location, as an address
  json_res_file         Json file were to save result

options:
  -h, --help            show this help message and exit
  --planet PLANET, -p PLANET
                        Name of specific planet.If this parameter is not set, results are returned for all planets in the solar system.
  --start_time START_TIME, -s START_TIME
                        Start of observation period. One observation by hour. If this parameter is not set, observation start at current time.
  --end_time END_TIME, -e END_TIME
                        End of observation period. One observation by hour. If this parameter is not set, observation end after start time.
```

**Examples:**

+ python src/main.py "Pl. Champollion 46100 Figeac" observartion.json 
+ python src/main.py "Pl. Champollion 46100 Figeac" observartion.json -s "2023-09-01 20:00:00"  
+ python src/main.py "Pl. Champollion 46100 Figeac" observartion.json  -e "2024-09-02 20:00:00" (the end date must be later than the current date)
+ python src/main.py "Pl. Champollion 46100 Figeac" observartion.json -s "2023-09-01 20:00:00"  -e "2023-09-02 20:00:00"
+ python src/main.py "Pl. Champollion 46100 Figeac" observartion.json -p jupiter
  
