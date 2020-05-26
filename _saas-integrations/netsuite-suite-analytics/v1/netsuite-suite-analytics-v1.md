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

title: NetSuite Suite Analytics
permalink: /integrations/saas/netsuite-suite-analytics
keywords: netsuite suite analytics, integration, schema, etl netsuite suite analytics, netsuite suite analytics etl, netsuite suite analytics schema
layout: singer
# input: false

key: "netsuite-analytics-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "netsuite-suite-analytics"
display_name: "NetSuite Suite Analytics"

singer: true
status-url: ""

tap-name: "NetSuite Suite Analytics"
# repo-url: ## this is currently private

this-version: "1"

api: |
  SuiteAnalytics Connect JDBC driver


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true 

historical: "1 year"
frequency: "1 hour"
tier: "Standard"

api-type: "platform.netsuite-suite-analytics"

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true
define-replication-methods: true

table-selection: true
column-selection: true
table-level-reset: true


# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Using this integration requires that the [SuiteAnalytics feature](#setup-requirements) be enabled in your NetSuite account.

  Refer to the [Schema](#schema) section for a list of objects available for replication.

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: "**Administrator permissions in NetSuite.**. This is required to complete the setup steps in NetSuite."
  - item: "**Access to the SuiteAnalytics feature in NetSuite.** Suite Analytics is a premium NetSuite feature. Contact your NetSuite administrator if you have questions about this feature."

setup-steps:
  - title: "Create a Stitch NetSuite role and configure permissions"
    anchor: "create-configure-stitch-role"
    content: |
      To connect {{ integration.display_name }} to Stitch, we recommend that you create a Stitch-specific role and user for us.

      1. Using the global search, type `page: new role` and click the **Page: New Role** result.
      2. In the **General** section, enter a name for the role in the **Name** field. For example: `Stitch SuiteAnalytics`
      3. Scroll down to the **Permissions** tab and click the **Setup** subtab, if it isn't already open.
      4. Using the **Permission** dropdown, search for `SuiteAnalytics Connect`:

         ![The SuiteAnalytics Connect permission in the Create Role screen in NetSuite]({{ site.baseurl }}/images/integrations/netsuite-suite-analytics-role-permissions.png)
      5. Click **Add** to add the permission to the role.
      6. When finished, click **Save** to create the role.

# SuiteAnalytics Connect permissions documentation:
# https://1796361.app.netsuite.com/app/help/helpcenter.nl?fid=section_3998867068.html

  - title: "Get the role's internal ID"
    anchor: "get-role-internal-id"
    content: |
      1. Using the global search, type `page: manage roles` and click the **Page: Manage Roles** result.
      2. Locate the role you created [in the previous step](#create-configure-stitch-role).
      3. Locate the role's **Internal ID**:

         ![The role's internal ID in the Manage Roles screen in NetSuite]({{ site.baseurl }}/images/integrations/netsuite-suite-analytics-role-id.png)

         **Note**: If you don't see the **Internal ID** column, click the **Edit View** button to add it.

      Keep this info handy - you'll need it to complete the setup in Stitch.

  - title: "Create a Stitch NetSuite user and assign the role"
    anchor: "create-stitch-netsuite-user"
    content: |
      {% include integrations/saas/netsuite-create-user.html step-number="1" step-anchor="create-configure-stitch-role" %}

  - title: "Retrieve SuiteAnalytics Connect details"
    anchor: "retrieve-suite-analytics-connect"
    content: |
      In this step, you'll retrieve the details required to connect to {{ integration.display_name }} from NetSuite.

      1. On the home page of your NetSuite account, click **Settings > Set Up SuiteAnalytics Connect**:

         ![The NetSuite homepage with the Set Up SuiteAnalytics Connect option highlighted]({{ site.baseurl }}/images/integrations/netsuite-suite-analytics-home-settings.png)
      2. The next page will display the connection details in the **Your Configuration** section:

         ![The Your Configuration section of the Set Up SuiteAnalytics Connect page in NetSuite]({{ site.baseurl }}/images/integrations/netsuite-suiteanalytics-connect-page.png)

      Keep this page open - you'll need it in the next step.

  - title: "add integration"
    content: |
      1. In the **Host** field, paste the host value from [Step 4](#retrieve-suite-analytics-connect).
      2. In the **Port** field, paste the port value from [Step 4](#retrieve-suite-analytics-connect).
      3. In the **Account ID** field, paste the account ID field from [Step 4](#retrieve-suite-analytics-connect).
      4. In the **Role ID** field, enter the role's internal ID from [Step 2](#get-role-internal-id).
      5. In the **Username** and **Password** fields, enter the Stitch user's username and password from [Step 1](#create-configure-stitch-role).
      
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data"


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/netsuite-analytics


# Remove this if you don't need it:
# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |
---
{% assign integration = page %}
{% include misc/data-files.html %}