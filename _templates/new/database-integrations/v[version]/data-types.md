---
# --------------------------------------- #
#  [DB-TYPE] v[VERSION] SUPPORTED DATA TYPES #
# --------------------------------------- #

## This file contains info about support for various data types for
## [DB-TYPE] integrations.


# -------------------------- #
#       ABOUT THIS FILE      #
# -------------------------- #

content-type: "integration-metadata"
key: "[DB-TYPE]-data-types"
this-version: "[VERSION]"

integration-name: "[db-type]"         


# --------------------------------- #
#  INTEGRATION-SPECIFIC DATA TYPES  #
# --------------------------------- #

## The following data types are specific to [DB-TYPE]:

specific-types:
  - "[type]"

## Each data type in this list should also be in the section below,
## in the following format:

## [type]:                        The name of the data type. It must match exactly
##                                what's listed in the specific-types list.
##   stitch-type: "[type]"        The Stitch type the data type will map to
##   format: "[formatted-type]"   The type Stitch will format the data as - typically
##                                used for date and timestamp data


# --------------------------------- #
#          ALL DATA TYPES           #
# --------------------------------- #

bigint:
  stitch-type: "integer"

bit:
  stitch-type: "boolean"

boolean:
  stitch-type: "boolean"

char:
  stitch-type: "string"
      
date:
  stitch-type: "string"
  format: "date-time"
      
decimal:
  stitch-type: "number"

double:
  stitch-type: "number"

float:
  stitch-type: "number"  
      
integer:
  stitch-type: "integer"

longvarchar:
  stitch-type: "string"

longnvarchar:
  stitch-type: "string"

nchar:
  stitch-type: "string"

numeric:
  stitch-type: "number"
      
nvarchar:
  stitch-type: "string"

real:
  stitch-type: "number"

smallint:
  stitch-type: "integer"

time:
  stitch-type: "string"
  format: "date-time"

timestamp:
  stitch-type: "string"
  format: "date-time"

tinyint:
  stitch-type: "integer"

varchar:
  stitch-type: "string"
---