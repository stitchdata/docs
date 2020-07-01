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

title: Impact
permalink: /integrations/saas/impact
keywords: impact, integration, schema, etl impact, impact etl, impact schema
layout: coming-soon
input: false

key: "impact-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "impact"
display_name: "Impact"

singer: true
status-url: ""

tap-name: "Impact"
repo-url: https://github.com/singer-io/tap-impact

this-version: "1"
---
{% assign integration = page %}
{% include misc/data-files.html %}