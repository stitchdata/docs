---
# -------------------------- #
#       ABOUT THIS FILE      #
# -------------------------- #

content-type: "integration-metadata"
key: "[integration]-details-v[version]"
name: "[integration]"
type: "saas"

version: &version-number "[version]"


# -------------------------- #
#       Version Details      #
# -------------------------- #

version:
  number: *version-number
  status: ""
  is-latest: true/false
  release-date: ""
  # date-last-connection: ""
  # deprecation-date: ""
  # sunset-date: ""


# -------------------------- #
#         Tap Details        #
# -------------------------- #

tap:
  name: ""
  repo-url: ""
  api: ""

  is-file-system: true/false


# -------------------------- #
#      Stitch Details        #
# -------------------------- #

stitch-details:
  certified: true/false
  subscription-plan: "Standard/Enterprise"

  api-property-type: ""
  override-api-property-type: true/false


# -------------------------- #
#   Replication Scheduling   #
# -------------------------- #

replication-scheduling:
  default-frequency: ""
  anchor: true
  cron: true


# -------------------------- #
#      Object Selection      #
# -------------------------- #

object-selection:
  tables: true
  columns: true
  table-reset: true

  select-all: ""
  select-all-reason: ""


# -------------------------- #
#    Replication Methods     #
# -------------------------- #

replication-methods:
  are-configurable: true/false
  set-default: true/false


# -------------------------- #
#   Replication Monitoring   #
# -------------------------- #

transparency:
  extraction-logs: true
  loading-reports: true


# -------------------------- #
#        Data Types          #
# -------------------------- #

## Refer to this file for data type info for this version:
## _integrations/saas/[integration]/v<[version]/data-types.md

## NOTE: This won't be applicable to all SaaS integrations.

# ----------------------------- #
#   READ ME BEFORE CONTINUING!  #
# ----------------------------- #

## TODO


# -------------------------- #
#        UI Fields           #
# -------------------------- #

## TODO

ui-fields:
  - "integration-name"
---