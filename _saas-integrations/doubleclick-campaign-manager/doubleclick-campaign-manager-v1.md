---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: DoubleClick Campaign Manager
permalink: /integrations/saas/doubleclick-campaign-manager
tags: [saas_integrations]
keywords: doubleclick campaign manager, integration, schema, etl doubleclick campaign manager, doubleclick campaign manager etl, doubleclick campaign manager schema
layout: singer
# input: false

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "doubleclick-campaign-manager"
display_name: "DoubleClick Campaign Manager"

singer: true 
tap-name: "doubleclick-campaign-manager"
repo-url: https://github.com/singer-io/tap-doubleclick-campaign-manager

# this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: false

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
status-url: "https://ads.google.com/status#hl=en&v=status"

anchor-scheduling: true
extraction-logs: true
loading-reports: true

table-selection: true
column-selection: false

# attribution-window: "# days"
# attribution-is-configurable: 

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **A Campaign Manager account**. Refer to [Google's website](https://www.google.com/doubleclick/advertisers/){:target="new"} for signup information.
  - item: |
      **API access.** Most Campaign Manager accounts have this enabled by default. If you're not sure, contact your DoubleClick representative or the [Campaign Manager support team](mailto: dcm-support@google.com).
  - item: |
      **Access to the reports you want to replicate.** Stitch will only have access to the reports that the user who authorizes the integration has access to.

setup-steps:
  - title: "Verify report access"
    anchor: "verify-report-access"
    content: |
      Before you connect {{ integration.display_name }} to Stitch, you should verify that you have access to the reports you want to replicate. Stitch will only be able to replicate data for the same reports that you have access to in {{ integration.display_name }}.

      1. [Sign into your {{ integration.display_name }} account and navigate to the **Report Builder** page](https://www.google.com/analytics/dfa/){:target="new"}.
      2. Under **Reports**, click **My Reports**.
      3. A list of all the reports you have access to will display:

         ![]({{ site.baseurl }}/images/integrations/doubleclick-campaign-manager-all-reports.png)

  - title: "Locate your {{ integration.display_name }} profile ID"
    anchor: "locate-your-profile-id"
    content: |
      {%- capture multiple-profiles -%}
      **Need to connect multiple profiles?** To connect more than one {{ integration.display_name }} profile, you'll need to create additional {{ integration.display_name }} integrations in your Stitch account.
      {%- endcapture -%}
      {% include note.html type="single-line" content=multiple-profiles %}

      {% include layout/inline_image.html type="right" file="integrations/doubleclick-campaign-manager-profile-id.png" max-width="250px" alt="" %}
      1. [Sign into your {{ integration.display_name }} account](https://www.google.com/dfa/trafficking){:target="new"}.
      2. Click the user menu (your icon) in the top right corner.
      3. In the dropdown beneath the **Sign out** button will be a list of the profiles you have access to.
      4. Locate the ID of the profile you want to connect. This will be a seven digit number next to the name of the profile. For example: `9999999`

         An example is highlighted in the image to the right.
      5. Copy the profile ID.

      Keep this handy - you'll need it in the next step.

  - title: "add integration"
    content: |
      4. In the **Profile ID** field, paste the ID of the {{ integration.display_name }} profile from [Step 2](#locate-your-profile-id). This value should be a seven digit number such as `9999999`.
  - title: "replication frequency"
  - title: "Authorize Stitch to access {{ integration.display_name }}"
    anchor: "grant-stitch-authorization"
    content: |
      1. If you aren't already signed into your Google account, you'll be prompted for your credentials.
      2. After you sign in, you'll see a list of the permissions requested by Stitch:
         - **View and manage DoubleClick for Advertisers reports** - This is required to allow Stitch to view and run reports. **Note**: Stitch will not alter report settings, and will only ever read data. Refer to the [Replication section](#replication) below for more info.
      3. To grant access, click the **Allow** button.
      4. After you've granted access, you'll be redirected back to Stitch to finish setting up the integration.
  - title: "track data"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/doubleclick-campaign-manager

# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |

---
{% assign integration = page %}
{% include misc/data-files.html %}