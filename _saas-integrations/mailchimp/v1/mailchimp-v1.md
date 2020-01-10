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

title: MailChimp
permalink: /integrations/saas/mailchimp
keywords: mailchimp, integration, schema, etl mailchimp, mailchimp etl, mailchimp schema
layout: singer
# input: false

key: "mailchimp-setup"

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "mailchimp"
display_name: "MailChimp"

singer: true 
tap-name: "MailChimp"
repo-url: https://github.com/singer-io/tap-mailchimp

this-version: "1.0"

api: |
  [{{ integration.display_name }} API 3.0](https://developer.mailchimp.com/documentation/mailchimp/reference/overview/){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true 

historical: "1 year"
frequency: "1 hour"
tier: "Free"
status-url: "https://status.mailchimp.com/"

anchor-scheduling: true
cron-scheduling: true

table-selection: true
column-selection: true

extraction-logs: true
loading-reports: true


# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **To verify your access in {{ integration.display_name }}.** Stitch will only be able to replicate the same data as the user who authorizes the integration.

      If this user has restricted permissions - meaning the user doesn't have access to all campaigns or lists, for example - Stitch may encounter issues replicating data. 

setup-steps:
  - title: "add integration"
  - title: "historical sync"
  - title: "replication frequency"
  - title: "Authorize Stitch to access {{ integration.display_name }}"
    anchor: "grant-stitch-authorization"
    content: |
      1. When finished in the **Integration Settings** page, click the **Authorize** button. You'll be prompted to sign into your {{ integration.display_name }} account.
      2. Sign into your {{ integration.display_name }} account.
      3. After the authorization process is successfully completed, you'll be directed back to Stitch.
      4. Click {{ app.buttons.finish-int-setup }}.
  - title: "track data"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/mailchimp
---
{% assign integration = page %}
{% include misc/data-files.html %}