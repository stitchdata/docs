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

title: Slack (v1)
permalink: /integrations/saas/slack
keywords: slack, integration, schema, etl slack, slack etl, slack schema
layout: coming-soon
input: false

key: "slack-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "slack"
display_name: "Slack"

singer: true
status-url: ""

tap-name: "Slack"
repo-url: https://github.com/singer-io/tap-slack

this-version: "1"
---
{% assign integration = page %}
{% include misc/data-files.html %}