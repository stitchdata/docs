---
title: Zuora
permalink: /integrations/saas/zuora
tags: [saas_integrations]
keywords: zuora, integration, schema, etl zuora, zuora etl, zuora schema
summary: "Connection instructions and schema details for Stitch's Zuora integration."
layout: singer

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "zuora"
display_name: "Zuora"
singer: true
author: "Stitch"
author-url: "https://www.stitchdata.com"
repo-url: https://github.com/singer-io/tap-zuora

# this-version: 

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

historical: "1 year"
frequency: "30 minutes"
tier: "Premium"
status-url: "http://trust.zuora.com/"
icon: /images/integrations/icons/zuora.svg
whitelist:
  tables: true
  columns: false

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: "**Administrator permissions in Zuora.** These permissions are required to create a Zuora user for Stitch."

setup-steps:
  - title: "Create a Stitch Zuora User"
    anchor: "#create-stitch-zuora-user"
    content: |

      In this step, you'll create a Zuora user for Stitch. Creating a Stitch-specific user will ensure that Stitch is distinguishable in any logs or audits.

      #### Zuora User Requirements

      To replicate your Zuora data, Stitch requires a user that:

      1. **Has Standard user permissions.** While Stitch will only ever read your data, these permissions are required to access certain objects in Zuora.
      2. **Has two-factor authentication disabled.** If this is enabled, connection and replication issues will occur after setup. Refer to the **Disable or Reset Two-Factor Authentication** section [in this Zuora documentation](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/Two-Factor_Authentication) for help disabling this setting.
      3. **Has credentials that don't expire.** This is applicable only if your company enforces Password Expiration rules. If Stitch's Zuora credentials expire, connection issues may arise. [Refer to this Zuora support article for a workaround](https://knowledgecenter.zuora.com/kb/How_do_I_prevent_my_API_user_login_from_expiring%3F).

      #### Create the Zuora User

      {% include layout/inline_image.html type="right" file="integrations/zuora-user-setup.png" alt="Zuora user permissions" max-width="400px" %}1. Sign into your Zuora account, if you haven't already.
      2. Click your username in the top-right corner.
      3. Click **Administration**, then **Manage Users**.
      4. Click **Add Single User**.
      5. Enter a first and last name for the user.
      6. Enter an email address in the **Work Email** field.
      7. Enter an email address in the **Login Field**.
      8. In the **Zuora Platform Role** field, select **Standard User**.
      9. For the remaining **Role** fields, select the **Standard User** option.
      10. There aren't any requirements for the **Locale** and **Language** fields - leave them as the defaults.
      11. Click **Save** to create the user.

      After the user is created, Zuora will send a verification email to the email address in the **Work Email** field. Complete the verification and set a password for the Stitch user before moving on to the next step.

  - title: "add integration"
    content: |
      4. If the Zuora instance you want to connect to Stitch is a sandbox, check the **Connect to a Sandbox Environment** checkbox.
      5. In the **Username** field, enter the Stitch Zuora user's username. This is the email address that was in the **Login Name** field when you created the user.
      6. In the **Password** field, enter the password associated with the Stitch Zuora user.
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data"


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

schema-sections:
  - content: |
      To get a better understanding of how Zuora objects relate to each other, check out [Zuora's Entity Relationship Diagram](http://knowledgecenter.zuora.com/BC_Developers/SOAP_API/E0_API_Object_Relationships). 

      Understanding the relationships between different data sets will allow you to perform more in-depth and complex analyses.
---
{% assign integration = page %}
{% include misc/data-files.html %}