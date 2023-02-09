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

title: TikTok Ads (v1)
permalink: /integrations/saas/tiktok-ads ## Add if there are multiple versions: /v1
keywords: tiktok ads, integration, schema, etl tiktok ads, tiktok ads etl, tiktok ads schema
layout: coming-soon
input: false

key: "tiktok-ads-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "tiktok-ads"
display_name: "TikTok Ads"

singer: true
status-url: ""

tap-name: "" ## Ex: Intercom, not intercom
repo-url: https://github.com/singer-io/tap-tiktok-ads

this-version: "1"
---
{% assign integration = page %}
{% include misc/data-files.html %}