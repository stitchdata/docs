---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: GitHub ## Find/replace SAAS-INTEGRATION with the display name (ex: Intercom)
permalink: /integrations/saas/github ## Find/replace saas-integration with the key name (ex: intercom)
tags: [saas_integrations]
keywords: github, integration, schema, etl github, github etl, github schema
layout: singer

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "github"
display_name: "GitHub"
singer: true
author: "Stitch"
author-url: https://www.stitchdata.com
repo-url: https://github.com/singer-io/tap-github


# If there's more than 1 version available:
#   1. Uncomment the line below,
#   2. Create a version file in _data/taps/versions for the integration, using the template in the folder.

# this-version: ""

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: false # Community-supported integration

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
status-url: https://status.github.com/messages
icon: /images/integrations/icons/github.svg
whitelist:
  tables: true
  columns: true


# -------------------------- #
#        API Details         #
# -------------------------- #

## Info about the integration's API that may affect either the speed of
## replication or the ability to replicate data at all.

## For example: Salesforce enforces a daily quota - once it's reached,
## Stitch is unable to replicate data until more quota is available.

## Details about the limitations go in the replication-notes content block.

enforces-api-limits: true/false


## If Stitch queries for X days each time due to attribution windows, enter the
## # of days here
## If it's the past day or 1 day, use "day"

attribution-window: "# days"

# -------------------------- #
#      Incompatiblities      #
# -------------------------- #

## uncomment section below if integration is compatible with any Stitch destinations
## if incompatible with multiple destinations, create a section for each destination

## incompatible:
  ## [redshift]: "always,sometimes,never"
  ## reason: "copy"

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **A valid Access Token which allows access to any projects you want to replicate data from.** Stitch will only be able to access the same projects as the user who creates the access token.

requirements-info:

setup-steps:
  - title: "Create a {{ integration.display_name }} token"
    anchor: "create-access-token"
    content: |
      1. Sign into your GitLab account.
      2. Click the **user menu (your icon) > Settings**.
      3. Click the **Developer settings** tab.
      4. Click the **Personal access tokens** tab.
      5. Click the **Generate new token** button.
      6. Input your password again if prompted.
      7. In the **Description** field, enter `stitch`. This will allow you to easily idenfiy what application is using the token.
      8. FIXME
      9. Click the **Generate token** button.
      10. The new Access Token will display on the next page. **Copy the token before navigating away from the page** - GitHub won't display it again.
  - title: "add integration"
    content: |
      4. In the **GitHub Access Token** field, paste the **Access Token** you created in the previous section.
      5. In the **GitHub Repository Name** field, enter the repository you want to track.
  - title: "historical sync"
  - title: "replication frequency"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/saas-integration

schema-sections:
  - title: ""
    anchor: ""
    content: |

---
{% assign integration = page %}
{% include misc/data-files.html %}
