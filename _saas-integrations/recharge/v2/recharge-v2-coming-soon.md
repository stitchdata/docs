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

title: ReCharge (v2)
permalink: /integrations/saas/recharge ## Add if there are multiple versions: /vVERSION
keywords: recharge, integration, schema, etl recharge, recharge etl, recharge schema
layout: coming-soon
input: false

key: "recharge-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "recharge"
display_name: "ReCharge"

singer: true
status-url: ""

tap-name: "ReCharge" ## Ex: Intercom, not intercom
repo-url: https://github.com/singer-io/tap-recharge

this-version: "2"
---
{% assign integration = page %}
{% include misc/data-files.html %}