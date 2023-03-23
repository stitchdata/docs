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

title: Twilio (v1)
permalink: /integrations/saas/twilio ## Add if there are multiple versions: /vVERSION
keywords: twilio, integration, schema, etl twilio, twilio etl, twilio schema
layout: coming-soon
input: false

key: "twilio-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "twilio"
display_name: "Twilio"

singer: true
status-url: "https://status.twilio.com/"

tap-name: "Twilio" ## Ex: Intercom, not intercom
repo-url: https://github.com/singer-io/tap-twilio

this-version: "1"
---
{% assign integration = page %}
{% include misc/data-files.html %}