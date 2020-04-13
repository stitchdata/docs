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

title: Mambu (v1)
permalink: /integrations/saas/mambu
keywords: mambu, integration, schema, etl mambu, mambu etl, mambu schema
layout: singer
# input: false

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "mambu"
display_name: "Mambu"

singer: true 
tap-name: "Mambu"
repo-url: https://github.com/singer-io/tap-mambu

this-version: "1"

api: |
  [{{ integration.display_name }} v2.0](https://api.mambu.com/?shell#Welcome){:target="new"} and [v1.0 APIs](https://support.mambu.com/docs/rest-apis-overview){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true 

historical: "1 year"
frequency: "1 hour"
tier: "Free"
status-url: "https://status.mambu.com/"

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true


# -------------------------- #
#      Incompatibilities     #
# -------------------------- #

## uncomment section below if integration is compatible with any Stitch destinations
## if incompatible with multiple destinations, create a section for each destination

## incompatible:
  ## [redshift]: "always,sometimes,never"
  ## reason: "copy" 


# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: "**A {{ integration.display_name }} account with API access**. The {{ integration.display_name }} integration requires an account login with API access. In {{ integration.display_name }}'s app, API access can be granted to any existing user."

setup-steps:
  - title: "add integration"
    content: |
      5. In the **Subdomain** field, enter your {{ integration.display_name }} subdomain. For example: If the subdomain were `stitch.{{ integration.name }}.com`, only `stitch` would be entered into this field.
      6. In the **Username** and **Password** fields, enter the username and password of the {{ integration.display_name }} user with {{ integration.display_name }} API access.
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/mambu
---
{% assign integration = page %}
{% include misc/data-files.html %}
