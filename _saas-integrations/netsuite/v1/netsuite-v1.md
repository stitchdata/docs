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

title: NetSuite (SuiteTalk)
permalink: /integrations/saas/netsuite-suitetalk
redirect_from: /integrations/saas/netsuite
keywords: netsuite, integration, schema, etl netsuite, netsuite etl, netsuite schema
layout: singer
# input: false

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "netsuite"
display_name: "NetSuite"

singer: true 
tap-name: "NetSuite"
repo-url: https://github.com/singer-io/tap-netsuite

# this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Closed Beta"
certified: true 

historical: "1 year"
frequency: "1 hour"
tier: "Paid"

anchor-scheduling: true
extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: "**Administrator permissions in {{ integration.display_name }}**. This is required to complete the setup steps in {{ integration.display_name }}."

setup-steps:
  - title: "Whitelist Stitch's IP addresses"
    anchor: "whitelist-stitch-ips"
    content: |
      {% include note.html type="single-line" content="**Note**: This step is required only if IP address rules (**Setup > Company > Enable Features > Company > Access**) are enabled for your NetSuite account. Otherwise, skip to [Step 2](#configure-web-services-and-authentication-settings). " %}

      {% capture ip-addresses %}
      {% for ip-address in ip-addresses %}
      {{ ip-address.ip }}{% unless forloop.last == true %},{% endunless %}
      {% endfor %}
      {% endcapture %}

      {% include layout/inline_image.html type="right" file="integrations/netsuite-ip-addresses.png" alt="" max-width="400px" %}
      1. In your {{ integration.display_name }} account, click **Setup > Company > Company Information**.
      2. In the **Allowed IP addresses** field, add the following comma-separated list of Stitch's IP addresses:

         ```
         {{ ip-addresses | strip_newlines }}
         ```

         **Note**: Make sure you don't overwrite or change any existing IP addresses in this field - doing so could cause access issues for you and other {{ integration.display_name }} users in your account.
      3. Click **Save**.

  - title: "Configure Web Services and authentication settings"
    anchor: "configure-web-services-and-authentication-settings"
    content: |
      To use Stitch's {{ integration.display_name }} integration, you'll need to enable Web Services and token-based authentication in your {{ integration.display_name }} account.
    substeps:
      - title: "Enable Web Services"
        anchor: "enable-web-services"
        content: |
          In this step, you'll enable Web Services for your {{ integration.display_name }} account. This is required to use {{ integration.display_name }}'s SuiteTalk API, which is what Stitch will use to extract data.

          1. Sign into your {{ integration.display_name }} account as an administrator.
          2. Using the global search, type `page: enable` and click the **Page: Enable Features** result. For example:

             ![]({{ site.baseurl }}/images/integrations/netsuite-v1-global-search-example.png)
          3. On the **Enable Features** page, click the **SuiteCloud** subtab.
          4. Locate the **SuiteTalk (Web Services)** section.
          5. Check the **Web Services** box.

      - title: "Enable token-based authentication"
        anchor: "enable-token-based-authentication"
        content: |
          Next, you'll enable token-based authentication for your {{ integration.display_name }} account. This is required to generate tokens and authenticate to the SuiteTalk API.

          1. On the **Enable Features** page, locate the **Manage Authentication** section. This should be after the **SuiteTalk** section.
          2. Check the **Token-based Authentication** box. Your settings should look like this when finished:

             ![]({{ site.baseurl }}/images/integrations/netsuite-v1-enable-features.png)

          5. Scroll to the bottom of the page and click **Save**.

  - title: "Create an integration record for Stitch"
    anchor: "create-stitch-integration-record"
    content: |
      Next, you'll create an integration record for Stitch. This will uniquely identify Stitch in your {{ integration.display_name }} account.

      1. Using the global search, type `page: integrations` and click the **Page: Manage Integrations** result.
      2. On the **Integrations** page, click the **New** button.
      3. On the **New Integration** pgae, fill in the following fields:
         - **Name**: Enter a name for the integration. For example: `Stitch`
         - **State**: Select **Enabled**.
      4. In the **Authentication** tab, select the **Token-based Authentication** option.
      5. Click the **Save** button. The confirmation page will display a **Consumer key/secret** section.
      6. **Copy the Consumer Key and Secret somewhere handy.** You'll need these credentials to complete the setup in Stitch.

  - title: "Create a Stitch {{ destination.display_name }} and configure permissions"
    anchor: "create-configure-stitch-user"
    content: |
      todo
    substeps:
      - title: "Create a Stitch {{ integration.display_name }} role"
        anchor: "create-stitch-netsuite-role"
        content: |
          todo
      - title: "Grant role permissions"
        anchor: "grant-role-permissions"
        content: |
          todo
      - title: "Save the role"
        anchor: "save-role"
        content: ""

      - title: "Create a Stitch {{ integration.display_name }} user"
        anchor: "create-stitch-netsuite-user"
        content: |
          Next, you'll create a dedicated {{ integration.display_name }} user for Stitch and assign the Stitch role to it.

          1. In your NetSuite account, click **Lists > Employees > Employees > New**.
          2. In the Employee page, fill in the **Name** and **Email** fields.
          3. Next, click the **Access** tab.
          4. In the **Access** tab:

             1. Create a password for the Stitch user. Enter it in the **Password** field, then again in the **Confirm Password** field.
             2. In the **Roles** section, search the dropdown menu to locate the Stitch role you created in [Step 3](#create-stitch-netsuite-role).
             3. Click **Add** once you've located the role.
          5. When finished, click **Save**.

  - title: "Create access tokens"
    anchor: "create-access-tokens"
    content: |
      In this step, you'll generate access tokens for the Stitch integration record (application) and user role.

      1. Using the global search, type `page: tokens` and click the **Page: Access Tokens** result.
      2. Click the **New Access Token** button.
      3. On the **Access Token** page, fill in the following fields:
         - **Application Name**: Select the integration record you created in [Step 3](#reate-stitch-integration-record).
         - **User**: Select the [user TODO]().
         - **Role**: Select the role you created in [Step 4.1](#create-stitch-netsuite-role).
         - **Token Name**: Enter a name for the token. For example: `Stitch`
      4. Click the **Save** button. The confirmation page will display a **Token ID and Secret**.
      5. **Copy the Token ID and Secret somewhere handy.** You'll need these credentials to complete the setup in Stitch.

  - title: "Locate your {{ integration.display_name }} Account ID"
    anchor: "locate-netsuite-account-id"
    content: |
      {% include layout/inline_image.html type="right" file="integrations/netsuite-account-id.png" alt="" max-width="250px" %}
      
      1. Using the global search, type `page: web services` and click the **Page: Web Services Preferences** result.
      2. In the Primary Information section, locate the **Account ID** field as shown in the image on the right.
      
      **Note**: If your Account ID contains a suffix - `1234567_SB2`, for example - it should be included when entering the ID into Stitch.

  - title: "add integration"
    content: |
      4. In the **Account** field, enter the {{ integration.display_name }} account ID you retrieved in [Step 6](#locate-netsuite-account-id).
      5. In the **Consumer Key** field, paste the Consumer Key you generated when you [created Stitch's integration record](#create-stitch-integration-record).
      6. In the **Token ID** field, paste the Token ID you generated when you [created Stitch's access tokens](#create-access-tokens).
      7. In the **Consumer Secret** field, paste the Consumer Secret you generated when you [created Stitch's integration record](#create-stitch-integration-record).
      8. In the **Token Secret** field, paste the Token Secret you generated when you [created Stitch's access tokens](#create-access-tokens).
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data"


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/netsuite

# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |

---
{% assign integration = page %}
{% include misc/data-files.html %}