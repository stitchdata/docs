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

title: Amazon DSP (v1)
permalink: /integrations/saas/amazon-ads-dsp
keywords: amazon-dsp, integration, schema, etl amazon-dsp, amazon-dsp etl, amazon-dsp schema
layout: coming-soon
input: false

key: "amazon-dsp-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "amazon-dsp"
display_name: "Amazon DSP"

singer: true
status-url: ""

tap-name: "Amazon DSP"
repo-url: https://github.com/singer-io/tap-amazon-ads-dsp

this-version: "1"
---
{% assign integration = page %}
{% include misc/data-files.html %}