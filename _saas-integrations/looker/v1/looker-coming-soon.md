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

title: Looker (v1)
permalink: /integrations/saas/looker
keywords: looker, integration, schema, etl looker, looker etl, looker schema
layout: coming-soon
input: false

key: "looker-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "looker"
display_name: "Looker"

singer: true
status-url: ""

tap-name: "Looker"
repo-url: https://github.com/singer-io/tap-looker

this-version: "1"
---
{% assign integration = page %}
{% include misc/data-files.html %}