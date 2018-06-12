---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Quick Base
permalink: /integrations/saas/quick-base
tags: [saas_integrations]
keywords: quick-base, integration, schema, etl quick-base, quick-base etl, quick-base schema
layout: singer

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "quick-base"
display_name: "Quick Base"
singer: true
repo-url: https://github.com/singer-io/tap-quickbase

# this-version: ""

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: false

historical: "1 year"
frequency: "1 hour"
tier: "Free"
status-url: https://service.quickbase.com/#!/
icon: /images/integrations/icons/quick-base.svg
whitelist:
  tables: true
  columns: false

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: ""
  - item: ""

requirements-info:

setup-steps:
  - title: "add integration"
    content: |
      4. In the **Quick Base API URL** field, enter your Quick Base API URL.
      5. In the **Quick Base APP ID** field, enter your Quick Base APP ID.
      6. In the **Quick Base User Token** field, paste your Quick Base User Token.
  - title: "historical sync"
  - title: "replication frequency"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/quick-base

schema-sections:
  - title: "Milliseconds"
    anchor: ""
    content: |
      https://github.com/singer-io/tap-quickbase/blob/master/tap_quickbase/__init__.py#L89

---
{% assign integration = page %}
{% include misc/data-files.html %}

