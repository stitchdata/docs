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

this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Open Beta"
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

             ![NetSuite global search field]({{ site.baseurl }}/images/integrations/netsuite-v1-global-search-example.png)
          3. On the **Enable Features** page, click the **SuiteCloud** subtab.
          4. Locate the **SuiteTalk (Web Services)** section.
          5. Check the **Web Services** box.

      - title: "Enable token-based authentication"
        anchor: "enable-token-based-authentication"
        content: |
          Next, you'll enable token-based authentication for your {{ integration.display_name }} account. This is required to generate tokens and authenticate to the SuiteTalk API.

          1. On the **Enable Features** page, locate the **Manage Authentication** section. This should be after the **SuiteTalk** section.
          2. Check the **Token-based Authentication** box. Your settings should look like this when finished:

             ![Highlighted Web Services and Token-based Authentication fields on the NetSuite Enable features page]({{ site.baseurl }}/images/integrations/netsuite-v1-enable-features.png)

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

  - title: "Create a Stitch {{ destination.display_name }} role and configure permissions"
    anchor: "create-configure-stitch-role"
    content: |
      To connect {{ integration.display_name }} to Stitch, we recommend that you create a Stitch-specific role and user for us. We suggest this to ensure that:

      1. Stitch is easily distinguishable in any logs or audits.

      2. Stitch doesn't encounter issues with replication due to {{ integration.display_name }}'s API limitations. Currently, a single {{ integration.display_name }} user is allowed to only have a single open API session at a time. If the user connected to Stitch has another connection elsewhere, replication problems will arise.

      3. Stitch can successfully authenticate to {{ integration.display_name }}. This will require creating a role that mirrors the standard {{ integration.display_name }} [Full Access Role](https://system.netsuite.com/app/help/helpcenter.nl?fid=section_N295396.html){:target="new"}.

         **Note**: Using the Full Access role requires two-factor authentication, which Stitch's integration doesn't currently support. For this reason, **do not assign the actual Full Access role to the Stitch user.**
    substeps:
      - title: "Create a Stitch {{ integration.display_name }} role"
        anchor: "create-stitch-netsuite-role"
        content: |
          {% capture two-factor-auth-roles %}
          {{ integration.display_name }} enforces two-factor authentication for Full Access and Administrator roles as of {{ integration.display_name }} 2018.1.

          Stitch's {{ integration.display_name }} integration doesn't support authenticating with this method. Connection errors will arise if either the Full Access or Administrator role is assigned to the Stitch user.
          {% endcapture %}

          {% include important.html first-line="**Do not assign the Full Access or Administrator role to Stitch**" content=two-factor-auth-roles %}

          To ensure Stitch can access and replicate all NetSuite objects supported for replication, you'll need to create a role to assign to the Stitch user.

          1. Using the global search, type `page: new role` and click the **Page: New Role** result.
          2. On the Role page, enter a name for the role in the **Name** field. For example: `Stitch`
          3. In the **Authentication** section, check the **Web Services Only Role** box.
          
      - title: "Configure permissions and save the Stitch role"
        anchor: "configure-permissions-save-stitch-role"
        content: |
          Next, you'll grant permissions to the role. Below are instructions for adding permissions to the role, the permissions required, and where to find them in {{ integration.display_name }}.

          In {{ integration.display_name }}, the Create Role **Permissions** section contains several subsections. In this guide is a tab that corresponds to the permissions you need to add in each {{ integration.display_name }} subsection. For example: In the **Permissions > Transactions** subsection, you'll add the permissions outlined in the **Transactions** tab of this guide.

          {% capture adding-permission-instructions %}
          **Refer to the other tabs in this section of the guide for the permissions you need to add**. 

          To add a permission to the role:

          1. In the **Permissions** tab, click a subtab. For example: **Transactions**
          2. Using the **Permission** dropdown, search for the permission you want to add.

             For example: If adding permissions in the **Transactions** subtab of {{ integration.display_name }}, you'll use the checklist in the **Transactions** tab of this guide.
          3. Using the **Level** dropdown, set the permission level to the corresponding level outlined in this guide:

             ![The Transactions subsection in the Permissions section of the NetSuite Create Role page]({{ site.baseurl }}/images/integrations/netsuite-role-permissions-tab.png)
          4. Click **Add**.
          5. Repeat these steps until all permissions in the tabs of this guide have been added.

          **Note**: If you don't see a permission in {{ integration.display_name }} that is listed here, skip it. Some permissions are dependent on specific products being enabled in your {{ integration.display_name }} account.
          {% endcapture %}

          {% include integrations/saas/netsuite-permission-list.html %}

      - title: "Save the role"
        anchor: "save-role"
        content: |
          After you've finished granting permissions to the role, click **Save** to create it.

  - title: "Create a Stitch {{ integration.display_name }} user"
    anchor: "create-stitch-netsuite-user"
    content: |
      {% include layout/image.html type="right" file="/integrations/netsuite-new-employee-page.png" alt="The Name, Email, Access tab, Password, and Role tabs highlighted in the NetSuite " max-width="450" enlarge=true %}
      Next, you'll create a dedicated {{ integration.display_name }} user for Stitch and assign the Stitch role to it.

      1. Using the global search, type `page: new role` and click the **Page: New Employees** result.
      2. In the Employee page, fill in the **Name**, **Email**, and any other required fields.
      3. Click the **Access** tab, located in the bottom half of the page.
      4. In the **Access** tab:

         1. Check the **Manually assign or change password** box to create a password for the Stitch user.
         2. Enter a password in the **Password** field, then again in the **Confirm Password** field.
         3. In the **Roles** section, search the dropdown menu to locate the Stitch role you created in [Step 4](#create-configure-stitch-role).
         3. Click **Add** once you've located the role.
      5. When finished, click **Save** to create the user.

  - title: "Create access tokens for Stitch"
    anchor: "create-access-tokens"
    content: |
      In this step, you'll generate access tokens for the Stitch integration record (application) and user role.

      1. Using the global search, type `page: tokens` and click the **Page: Access Tokens** result.
      2. Click the **New Access Token** button.
      3. On the **Access Token** page, fill in the following fields:
         - **Application Name**: Select the integration record you created in [Step 3](#reate-stitch-integration-record).
         - **User**: Select the Stitch user you created in [Step 5](#create-stitch-netsuite-user).
         - **Role**: Select the Stitch role you created in [Step 4](#create-stitch-netsuite-role).
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
      4. In the **Account** field, enter the {{ integration.display_name }} account ID you retrieved in [Step 7](#locate-netsuite-account-id).
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