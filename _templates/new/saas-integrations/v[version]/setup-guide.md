---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: "Connecting [TODO: a/an] [display-name] (v[version]) integration to Stitch"
permalink: /integrations/saas/[integration]/v[version]/connecting-[integration]
keywords: [integration], integration, schema, etl [integration], [integration] etl, [integration] setup

layout: tutorial
content-type: "integration-setup"
key: "[integration]-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

this-version: "[version]"

name: "[integration]"
display_name: "[display-name]"



# ------------------------- #
#           Intro            #
# -------------------------- #

# REMOVE IF NOT USED.
# `intro` displays a single paragraph. Use `intro-sections` if you need headings.

# intro:
# intro-sections: 


# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements:
  - item: ""


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

## REMOVE ANY STEPS IF THEY'RE NOT NEEDED.

steps:
  - title: ""
    anchor: ""
    content: |
      [TODO]

  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      4. Enter the information you requested from [Step 1](#request-api) into the corresponding fields in Stitch.

  - title: "Define the historical replication start date"
    anchor: "define-historical-sync"
    content: |
      {% include integrations/saas/setup/historical-sync.html %}
  
  - title: "Create a replication schedule"
    anchor: "define-rep-frequency"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}

  - title: "Set objects to replicate"
    anchor: "setting-data-to-replicate"
    content: |
      {% include integrations/shared-setup/data-selection/object-selection.html %}
---
{% assign integration = page %}
{% include misc/data-files.html %}