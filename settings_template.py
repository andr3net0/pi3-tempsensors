# settings for getTemps.py

# getTemps script switches
APIPOST = True # change to enable/disable api posting
VERBOSE = True # change to enable/disable verbose output
TEMPWARN = True # change to enable/disable Siren/Beacon output

# API Settings
URL = 'your api endpoint url'
URL_LIMTS = 'your api endpoint url - get temperature limits'
API_KEY = 'your api key'
PI_KEY = 'your pi serial'

# DB Settings
DB_NAME = "database.db" # DB name for measures and params
SQL_FILE_NAME = "db_init.sql" # sql name to DB init

# DHT Info
DHT_V = 11      # DHT version '11': Adafruit_DHT.DHT11, '22': Adafruit_DHT.DHT22, '2302': Adafruit_DHT.AM2302 
DHT_PINS = [17,27]

# CT / ADC Info
ADC_CHANNELS = [0,1]

# Software SPI configuration - MCP3008 ADC:
CLK  = 6
MISO = 13
MOSI = 19
CS   = 26

# Door sensors 
DOOR_PINS = [22,5]

# Siren/Beacon
WARN_PIN = 21
SIGNAL_TIME = 5