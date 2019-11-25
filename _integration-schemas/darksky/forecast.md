---
tap: "darksky"
version: "1.0"

name: "forecast"
doc-link: "https://darksky.net/dev/docs#overview"
singer-schema: "https://github.com/singer-io/tap-darksky/blob/master/tap_darksky/schemas/forecast.json"
description: "This table contains information about the forcasts."

replication-method: "Key-based Incremental"

api-method:
  name: "Time Machine Request"
  doc-link: "https://darksky.net/dev/docs#time-machine-request"

attributes:
  - name: "forecast_date"
    type: "date-time"
    primary-key: true
    description: ""
    replication-key: true

  - name: "latitude"
    type: "number"
    primary-key: true
    description: "The requested latitude."
    
  - name: "longitude"
    type: "number"
    primary-key: true
    description: "The requested longitude."

  - name: "daily"
    type: "object"
    description: "A data block containing the weather conditions day-by-day for the next week."
    subattributes:
      - name: "apparent_temperature_high"
        type: "number"
        description: "The daytime high apparent temperature."

      - name: "apparent_temperature_high_time"
        type: "date-time"
        description: "The UNIX time representing when the daytime high apparent temperature occurs."

      - name: "apparent_temperature_low"
        type: "number"
        description: "The overnight low apparent temperature."

      - name: "apparent_temperature_low_time"
        type: "date-time"
        description: "The UNIX time representing when the overnight low apparent temperature occurs."

      - name: "apparent_temperature_max"
        type: "number"
        description: "The maximum apparent temperature during a given date."

      - name: "apparent_temperature_max_time"
        type: "date-time"
        description: "The UNIX time representing when the maximum apparent temperature during a given date occurs."

      - name: "apparent_temperature_min"
        type: "number"
        description: "The minimum apparent temperature during a given date."

      - name: "apparent_temperature_min_time"
        type: "date-time"
        description: "The UNIX time representing when the minimum apparent temperature during a given date occurs."

      - &cloud-cover
        name: "cloud_cover"
        type: "number"
        description: "The percentage of sky occluded by clouds, between 0 and 1, inclusive."
      - &dew-point
        name: "dew_point"
        type: "number"
        description: "The dew point in degrees Fahrenheit."

      - &humidity
        name: "humidity"
        type: "number"
        description: "The relative humidity, between 0 and 1, inclusive."

      - &icon
        name: "icon"
        type: "string"
        description: "A machine-readable text summary of this data point, suitable for selecting an icon for display. If defined, this property will have one of the following values: clear-day, clear-night, rain, snow, sleet, wind, fog, cloudy, partly-cloudy-day, or partly-cloudy-night."

      - name: "moon_phase"
        type: "number"
        description: "The fractional part of the lunation number during the given day: a value of 0 corresponds to a new moon, 0.25 to a first quarter moon, 0.5 to a full moon, and 0.75 to a last quarter moon."

      - name: "precip_accumululation"
        type: "number"
        description: "The amount of snowfall accumulation expected to occur - over the hour or day, respectively - in inches. If no snowfall is expected, this property will not be defined."

      - &precip-intensity
        name: "precip_intensity"
        type: "number"
        description: "The intensity, in inches of liquid water per hour, of precipitation occurring at the given time. This value is conditional on probability."

      - name: "precip_intensity_max"
        type: "number"
        description: ""

      - name: "precip_intensity_max_time"
        type: "date-time"
        description: "The maximum value of `precipIntensity` during a given day."

      - &precip-probability
        name: "precip_probability"
        type: "number"
        description: "The probability of precipitation occurring, between 0 and 1, inclusive."

      - &precip-type
        name: "precip_type"
        type: "string"
        description: "The type of precipitation occurring at the given time. If defined, this property will have one of the following values: rain, snow, or sleet."

      - &pressure
        name: "pressure"
        type: "number"
        description: "The sea-level air pressure in millibars."

      - name: "summary"
        type: "string"
        description: "A human-readable text summary of this data point."

      - name: "sunrise_time"
        type: "date-time"
        description: "The UNIX time of when the sun will rise during a given day."

      - name: "sunset_time"
        type: "date-time"
        description: "The UNIX time of when the sun will set during a given day."

      - name: "temperature_high"
        type: "number"
        description: "The daytime high temperature."

      - name: "temperature_high_time"
        type: "date-time"
        description: "The UNIX time representing when the daytime high temperature occurs."

      - name: "temperature_low"
        type: "number"
        description: "The overnight low temperature."

      - name: "temperature_low_time"
        type: "date-time"
        description: "The UNIX time representing when the overnight low temperature occurs."

      - name: "temperature_max"
        type: "number"
        description: "The maximum temperature during a given date."

      - name: "temperature_max_time"
        type: "date-time"
        description: "The UNIX time representing when the maximum temperature during a given date occurs."

      - name: "temperature_min"
        type: "number"
        description: "The minimum temperature during a given date."

      - name: "temperature_min_time"
        type: "date-time"
        description: "The UNIX time representing when the minimum temperature during a given date occurs."

      - &time
        name: "time"
        type: "date-time"
        description: "The UNIX time at which this data point begins."

      - &uv-index
        name: "uv_index"
        type: "integer"
        description: "The UV index."

      - name: "uv_index_time"
        type: "date-time"
        description: "The UNIX time of when the maximum `uvIndex` occurs during a given day."

      - &visibility
        name: "visibility"
        type: "number"
        description: "The average visibility in miles, capped at 10 miles."

      - &wind-bearing
        name: "wind_bearing"
        type: "integer"
        description: "The direction that the wind is coming from in degrees, with true north at 0° and progressing clockwise."

      - &wind-speed
        name: "wind_speed"
        type: "number"
        description: "The wind speed in miles per hour."
  
  - name: "end_time"
    type: "date-time"
    description: ""
  
  - name: "flags"
    type: "object"
    description: "Various metadata information related to the request."
    subattributes:
      - name: "nearest_station"
        type: "number"
        description: "The distance to the nearest weather station that contributed data to this response."
      - name: "sources"
        type: "array"
        description: "An array of IDs for each data source utilized in servicing this request."
      - name: "units"
        type: "string"
        description: "Indicates the units which were used for the data in this request."
  
  - name: "hourly"
    type: "object"
    description: "The various weather phenomena occurring over an hour."
    subattributes:
      - name: "data"
        type: "array"
        description: "The weather conditions at the requested location over time."
        subattributes:
          - name: "apparent_temperature"
            type: "string"
            description: "The apparent (or 'feels like') temperature in degrees Fahrenheit."

          - *cloud-cover

          - *dew-point

          - *humidity

          - *icon

          - *precip-intensity

          - *precip-probability
            
          - *precip-type

          - *pressure

          - name: "ozone"
            type: "number"
            description: "The columnar density of total atmospheric ozone at the given time in Dobson units."

          - name: "summary"
            type: "string"
            description: "A human-readable text summary of this data point."

          - name: "temperature"
            type: "number"
            description: "The air temperature in degrees Fahrenheit."

          - *time

          - *uv-index

          - *visibility

          - *wind-bearing

          - name: "wind_gust"
            type: "number"
            description: "The wind gust speed in miles per hour."

          - *wind-speed

      - name: "icon"
        type: "string"
        description: "A machine-readable text summary of this data block."

      - name: "summary"
        type: "string"
        description: "A human-readable summary of this data block."
  
  - name: "local_date"
    type: "string"
    description: ""
  
  - name: "offset"
    type: "number"
    description: "The current timezone offset in hours."
  
  - name: "start_time"
    type: "date-time"
    description: ""
  
  - name: "timezone"
    type: "string"
    description: "The IANA timezone name for the requested location. This is used for text summaries and for determining when hourly and daily data block objects begin."
---