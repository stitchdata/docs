---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-coming-soon
## FOR INSTRUCTIONS & REFERENCE INFO


# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Sailthru (v1)
permalink: /integrations/saas/sailthru ## Add if there are multiple versions: /vVERSION
keywords: sailthru, integration, schema, etl sailthru, sailthru etl, sailthru schema
layout: coming-soon
input: false

key: "sailthru-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "sailthru"
display_name: "Sailthru"

singer: true
status-url: "https://status.sailthru.com/#!/"

tap-name: "Sailthru" ## Ex: Intercom, not intercom
repo-url: https://github.com/singer-io/tap-sailthru

this-version: "1"
---
{% assign integration = page %}
{% include misc/data-files.html %}