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

title: SAAS-INTEGRATION (vVERSION)
permalink: /integrations/saas/saas-integration ## Add if there are multiple versions: /vVERSION
keywords: saas-integration, integration, schema, etl saas-integration, saas-integration etl, saas-integration schema
layout: coming-soon
input: false

key: "saas-integration-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "saas-integration"
display_name: "SAAS-INTEGRATION"

singer: true
status-url: ""

tap-name: "" ## Ex: Intercom, not intercom
repo-url: https://github.com/singer-io/tap-saas-integration

this-version: ""
---
{% assign integration = page %}
{% include misc/data-files.html %}