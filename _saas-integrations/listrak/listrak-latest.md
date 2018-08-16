---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Listrak
permalink: /integrations/saas/listrak
tags: [saas_integrations]
keywords: listrak, integration, schema, etl listrak, listrak etl, listrak schema
layout: singer

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "listrak"
display_name: "Listrak"
singer: true 
repo-url: https://github.com/singer-io/tap-listrak

# this-version: ""

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: false

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
status-url: 
icon: /images/integrations/icons/listrak.svg
whitelist:
  tables: true
  columns: false

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

setup-steps:
  - title: "Create a {{ integration.display_name }} Stitch user"
    anchor: "create-stitch-listrak-user"
    content: |
      {% capture user-limit %}
      While we recommend doing creating a user for Stitch to ensure we're visible in any logs or audits, it may not be feasible as Listrak limits each account to five users.

      **Should you choose not to create a user for us**, you should verify that the user who creates the integration in Stitch has:

      1. Access to the Listrak lists you want to replicate, and
      2. The permissions listed in **Step 8** of this section.
      {% endcapture %}
      {% include note.html first-line="**Listrak user limits**" content=user-limit %}

      1. Sign into your Listrak account.
      2. From the home page, click **Manage**.
      3. Click **Accounts > User Manager**.
      4. Scroll to the bottom of the page and click **Create New User**.
      5. Fill in the **User Information** fields.
      6. In the **Lists** section, select the lists you want the Stitch user to have access to. **Note**: Stitch will only be able to replicate data for lists that it is able to access.
      7. For **Granted Access**, select **Role Based Access**.
      8. In the section below this field, select check the boxes for the following permissions:
         - **Analytics Access** - This allows the Stitch user to view analytics for messages, contacts, and lists for available lists.
         - **API Access** - This allows the Stitch user to replicate data from your {{ integration.display_name }} using the {{ integration.display_name }} API.
      9. Click **Add User** when finished.
  - title: "add integration"
    content: |
      4. In the **Username** field, enter the Stitch {{ integration.display_name }} user's username.
      5. In the **Password** field, enter the Stitch {{ integration.display_name }} user's password.
  - title: "historical sync"
  - title: "replication frequency"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/listrak

# replication-sections:
#   - name: ""
#     anchor: ""
#     content: |

---
{% assign integration = page %}
{% include misc/data-files.html %}

