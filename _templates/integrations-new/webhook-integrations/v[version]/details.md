---
# -------------------------- #
#       ABOUT THIS FILE      #
# -------------------------- #

content-type: "integration-metadata"
key: "[integration]-details-v[version]"
name: "[integration]"
type: "webhook"

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

## Webhooks aren't taps.


# -------------------------- #
#      Stitch Details        #
# -------------------------- #

stitch-details:
  certified: true
  subscription-plan: "Standard"


# -------------------------- #
#   Replication Scheduling   #
# -------------------------- #

replication-scheduling:
  default-frequency: "Continuous"
  anchor: false
  cron: false


# -------------------------- #
#      Object Selection      #
# -------------------------- #

object-selection:
  tables: false
  columns: false
  table-reset: false


# -------------------------- #
#    Replication Methods     #
# -------------------------- #

replication-methods:
  are-configurable: false
  set-default: false


# -------------------------- #
#   Replication Monitoring   #
# -------------------------- #

transparency:
  extraction-logs: false
  loading-reports: false


# -------------------------- #
#        UI Fields           #
# -------------------------- #

## TODO

ui-fields:
  - "integration-name"
---