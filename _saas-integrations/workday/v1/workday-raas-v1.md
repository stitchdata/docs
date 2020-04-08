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

title: Workday RaaS (v1)
permalink: /integrations/saas/workday-raas
keywords: workday-raas, integration, schema, etl workday-raas, workday-raas etl, workday-raas schema
layout: singer
# input: false
enterprise: true
enterprise-cta:
  feature: "Workday RaaS integrations "
  title: "{{ site.data.strings.enterprise.title.are-an | prepend: page.enterprise-cta.feature }}"
  copy: "{{ site.data.strings.enterprise.copy.are-an | prepend: page.enterprise-cta.feature | flatify }}"

key: "workday-raas-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "workday-raas"
display_name: "Workday RaaS"

singer: true
status-url: ""

tap-name: "Workday RaaS"
repo-url: https://github.com/singer-io/tap-workday-raas

this-version: "1"

api: |
  [{{ integration.display_name }} Public Web Services API](https://community.workday.com/api){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true

api-type: "platform.workday-raas" 

historical: "1 year"
frequency: "1 hour"
tier: "Enterprise"

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true


# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data from your defined  reports using the {{ integration.api | flatify | strip }}. For more information on this integration's table creation, refer to the [Schema](#schema) section.


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

setup-steps:
  - title: "Retrieve your report URL"
    anchor: "retrieve-report-url"
    content: |
      1. Login to your {{ integration.display_name }} account.
      2. Navigate to your reports.
      3. Select the report you want to replicate and ensure that the **Enable As Web Service** box is checked.
      4. Copy the **Workday XML** REST link and keep it available for the next step.

         ![Workday XML REST link highlighted on the URLs Web Service page in {{ integration.display_name }}]({{ site.baseurl }}/images/integrations/workday-report-url.jpg){:style="max-width: 415px"}

      To replicate multiple reports, repeat steps 3 and 4 as needed.

  - title: "add integration"
    content: |
      4. In the **Username** field, enter the username for your {{ integration.display_name }} account.
      5. In the **Password** field, enter the password for your {{ integration.display_name }} account.
      6. In the **Report Name** field, enter a name for the report. **Note**: This will be used to create the name of the corresponding destination table.
      7. In the **Report URL** field, enter the report URL you obtained in [step 1](#retrieve-report-url).

      To replicate additional reports, click **Configure another report** and repeat steps 6 and 7.

  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data"


# -------------------------- #
#  Integration Replication   #
# -------------------------- #

replication-sections:
  - content: |
      Stitch uses Full Table Replication to replicate report data from {{ integration.display_name }}. This means that during every replication job, every report configured in the integration's settings will be replicated in full.


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# This tells the Singer layout not to run the /integrations/templates/schemas/table-schemas.html include.
exclude-table-schemas: true

schema-sections:
  - content: |
      Stitch's {{ integration.display_name }} integration replicates data from existing reports in your {{ integration.display_name }} account. For every report you configure while setting up the integration, Stitch will create a corresponding table in your destination.

      The fields available for selection are dependent on the data points that exist in the report in {{ integration.display_name }}. If you don't see a field you want to select in Stitch, verify that the report in {{ integration.display_name }} contains the field.
---
{% assign integration = page %}
{% include misc/data-files.html %}