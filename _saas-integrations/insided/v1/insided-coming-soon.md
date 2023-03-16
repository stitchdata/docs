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

title: inSided (v1)
permalink: /integrations/saas/insided
keywords: insided, integration, schema, etl insided, insided etl, insided schema
layout: coming-soon
input: false

key: "insided-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "insided"
display_name: "inSided"

singer: true
status-url: ""

tap-name: "inSided"
repo-url: https://github.com/singer-io/tap-insided

this-version: "1"
---
{% assign integration = page %}
{% include misc/data-files.html %}