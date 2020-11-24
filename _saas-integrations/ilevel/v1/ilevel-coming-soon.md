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

title: iLevel (v1)
permalink: /integrations/saas/ilevel
keywords: ilevel, integration, schema, etl ilevel, ilevel etl, ilevel schema
layout: coming-soon
input: false

key: "ilevel-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "ilevel"
display_name: "iLevel"

singer: true
status-url: ""

tap-name: "iLevel"
repo-url: https://github.com/singer-io/tap-ilevel

this-version: "1"
---
{% assign integration = page %}
{% include misc/data-files.html %}