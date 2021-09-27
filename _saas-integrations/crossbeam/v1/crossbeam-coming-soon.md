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

title: Crossbeam (v1)
permalink: /integrations/saas/crossbeam ## Add if there are multiple versions: /vVERSION
keywords: crossbeam, integration, schema, etl crossbeam, crossbeam etl, crossbeam schema
layout: coming-soon
input: false

key: "crossbeam-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "crossbeam"
display_name: "Crossbeam"

singer: true
status-url: ""

tap-name: "Crossbeam" ## Ex: Intercom, not intercom
repo-url: https://github.com/singer-io/tap-crossbeam

this-version: "1"
---
{% assign integration = page %}
{% include misc/data-files.html %}