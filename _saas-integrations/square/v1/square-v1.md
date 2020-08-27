---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas/
## FOR INSTRUCTIONS & REFERENCE INFO


# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Square (v1)
permalink: /integrations/saas/square ## Add if there are multiple versions: /vVERSION
keywords: square, integration, schema, etl square, square etl, square schema
layout: singer
# input: false

key: "square-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "square"
display_name: "Square"

singer: true
status-url: "http://issquareup.com/"

tap-name: "Square" ## Ex: Intercom, not intercom
repo-url: https://github.com/singer-io/tap-square

this-version: "1"

api: |
  [{{ integration.display_name }} REST API v2](https://developer.squareup.com/reference/square){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true 

historical: "1 year"
frequency: "1 hour"
tier: "Free"

api-type: "platform.square"

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true

# attribution-window: "# days"
# attribution-is-configurable: 

# setup-name: ""


# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.


# -------------------------- #
#      Incompatibilities     #
# -------------------------- #

## uncomment section below if integration is compatible with any Stitch destinations
## if incompatible with multiple destinations, create a section for each destination

## incompatible:
  ## [redshift]: "always,sometimes,never"
  ## reason: "copy" 

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: ""
  - item: ""

requirements-info:

setup-steps:
  - title: "add integration"
    content: |
      4. Check the **Connect to a sandbox environment** if choosing to connect to your {{ integration.display_name }} sandbox.
  - title: "historical sync"
  - title: "replication frequency"
  - title: "Authorizing Stitch to Access Square"
    anchor: "authorize-stitch"
    content: |
      Lastly, you'll be directed to Square's website to complete the setup.

      1. Enter your Square credentials and click **Login**.
      2. After the authorization process successfully completes, you'll be redirected back to Stitch.
      3. Click {{ app.buttons.finish-int-setup }}.
  - title: "track data" ## remove this if the integration doesn't support at least table selection


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/square


# Remove this if you don't need it:
# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |
---
{% assign integration = page %}
{% include misc/data-files.html %}