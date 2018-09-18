---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/destination-templates/destination-overview/
## FOR INSTRUCTIONS & REFERENCE INFO


# -------------------------- #
#        Page Controls       #
# -------------------------- #
title: DESTINATION-NAME Destination
permalink: /destinations/destination-type/
layout: destination-overview
tags: [bigquery_destination]
keywords: destination-type, destination-type, destination-type data warehouse, destination-type etl, etl to destination-type
summary: ""
toc: true
destination: true


# -------------------------- #
#    Destination Details     #
# -------------------------- #
display_name: "DESTINATION-NAME"
type: "destination-type"
db-type: ""
pricing_tier: "standard" ## for Stitch
status: ""
description: ""
pricing_model: "" ## provider model
free_option: ""
fully-managed: true/false
pricing_notes: "" ## ex: "BigQuery's pricing isn't based on a fixed rate, meaning your bill can vary over time."
icon: /images/destinations/icons/destination-type.svg


# -------------------------- #
#           Support          #
# -------------------------- #
replication-methods: ""
connection-methods: "SSH, SSL"
supported-versions: "n/a"

nested-structures: true ## if true, natively supports nested structures
case: "Case Insensitive"
table-name-limit: "" ## max # of characters
column-name-limit: "" ## max # of characters
column-limit: "" ## max # of columns allowed in tables
timestamp-range: ""
timezones:
  supported: false
  storage: ""
varchar-limit: "" ## max width for varchars
decimal-limit: ""
decimal-range: ""
reserved-words: ""


# -------------------------- #
#    Incompatible Sources    #
# -------------------------- #
incompatible-with: 0



# -------------------------- #
#            Links           #
# -------------------------- #
status-url: 
sign-up: 
documentation: 
pricing: 
price-calculator: 

# -------------------------- #
#      Overview Content      #
# -------------------------- #

introduction: |
  {{ destination.description | flatify | markdownify }}

sections:
  - title: "pricing"
    content: |

  - title: "setup"
    content: |

  - title: "limitations"
    include: |
      {% include destinations/overview-limitations.html %}

  - title: "replication"
    include: |
      {% include destinations/overview-replication-process.html %}

  - title: "schema"
    include: |
      {% include destinations/overview-integration-schemas.html %}
---
{% assign destination = page %}
{% include misc/data-files.html %}