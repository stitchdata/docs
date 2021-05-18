---
# -------------------------- #
#       ABOUT THIS FILE      #
# -------------------------- #

content-type: "integration-metadata"
key: "[name]-details-v[version]"
name: "[name]"
type: "database"

db-type: "[db-type]"


# -------------------------- #
#       Version Details      #
# -------------------------- #

version: &version-number "[version]"

## Refer to the generic details file for this version's info,
## such as status, release date, etc:
## _integrations/databases/[db-type]/v[version]/generic-details.md


# -------------------------- #
#         Tap Details        #
# -------------------------- #

tap:
  name: ""
  repo-url: ""
  driver: ""

  is-file-system: true/false


# -------------------------- #
#      Stitch Details        #
# -------------------------- #

stitch-details:
  certified: true/false
  subscription-plan: "Standard/Enterprise"

  default-port: 
  supported-database-versions: ""

  api-property-type: ""
  override-api-property-type: true/false


# -------------------------- #
#    Connection Support      #
# -------------------------- #

connection-methods:
  ssh: true/false
  ssl: true/false


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
  database-views: true/false
  table-reset: true

  select-all: ""
  select-all-reason: ""


# -------------------------- #
#    Replication Methods     #
# -------------------------- #

replication-methods:
  are-configurable: true/false
  set-default: true/false

  key-based: true/false
  full-table: true/false
  view-replication: true/false

  log-based: true/false

  log-based-minimum-version: ""
  log-based-read-replica: true/false
  log-based-read-replica-doc-link: ""
  log-based-read-replica-reason: ""


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
## _integrations/databases/[db-type]/v<[version]/data-types.md


# ----------------------------- #
#   READ ME BEFORE CONTINUING!  #
# ----------------------------- #

## TODO


# -------------------------- #
#      User Privileges       #
# -------------------------- #

## NOTE: User privilege data lives in here:
## _integrations/databases/[db-type]/common/user-privileges.md

user-privileges:
  - "<privilege-name>"


# -------------------------- #
#      Server Settings       #
# -------------------------- #

## NOTE: Server settings data lives in here:
## _integrations/databases/[db-type]/common/server-settings.md

server-settings:
  - "<server-setting-name>"


# -------------------------- #
#        UI Fields           #
# -------------------------- #

## NOTE: Server settings data lives in here:
## _integrations/databases/[db-type]/common/ui-connection-fields.md

ui-fields:
  - "integration-name"
  - "host"
  - "port"
  - "password"
  - "database"
---