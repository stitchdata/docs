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

title: Mambu (v4)
permalink: /integrations/saas/mambu ## Add if there are multiple versions: /vVERSION
keywords: mambu, integration, schema, etl mambu, mambu etl, mambu schema
layout: coming-soon
input: false

key: "mambu-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "mambu"
display_name: "Mambu"

singer: true
status-url: "https://status.mambu.com/"

tap-name: "Mambu" ## Ex: Intercom, not intercom
repo-url: https://github.com/singer-io/tap-mambu

this-version: "4"
---
{% assign integration = page %}
{% include misc/data-files.html %}