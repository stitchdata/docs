---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/destination-templates/destination-setup/
## FOR INSTRUCTIONS & REFERENCE INFO

title: Connecting a DESTINATION-NAME Data Warehouse to Stitch
permalink: /destinations/destination-type/connecting-destination-type-to-stitch
tags: [destination-type_destination]
keywords: destination-type, destination-type data warehouse, destination-type data warehouse, destination-type etl, etl to destination-type, destination-type destination
summary: "Connect a DESTINATION-NAME destination to your Stitch account."
toc: true
layout: destination-setup-guide

type: "destination-type"
display_name: "DESTINATION-NAME"

# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements-list:
  - item: |

# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

setup-steps:
  - title: ""
    anchor: ""
    content: ""

---
{% include misc/data-files.html %}
{% assign destination = site.destinations | where:"type","destination-type" | first %}