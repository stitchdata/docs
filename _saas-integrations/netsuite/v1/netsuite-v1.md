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


# https://975200-sb2.app.netsuite.com/app/help/helpcenter.nl?fid=section_4502013915.html
# If the user has a SuiteCloud Plus license and has been designated a concurrent web services user,
# Then the user can have 10 concurrent requests at a time.
# Otherwise, it's just 1 request (session) at a time.

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
#     Replication Details    #
# -------------------------- #

replication-sections:
  - content: |
      In this section:

      {% for section in page.replication-sections %}
      - [{{ section.title | flatify }}](#{{ section.anchor }})
      {% endfor %}

  - title: "Custom records"
    anchor: "custom-records"
    content: |
      For each custom record type in {{ integration.display_name }}, a table for that custom record type will be available for selection in Stitch.

    subsections:
      - title: "Table names for custom record types"
        anchor: "custom-record-types-table-names"
        content: |
          Custom record tables are named `customrecord_[custom_record_type]`, where `[custom_record_type]` is the name of the custom record in {{ integration.display_name }}. For example: If a custom record were named `promo discount` in {{ integration.display_name }}, the corresponding table for those records would be named `customrecord_promo_discount`.

      - title: "Replication methods for custom record types"
        anchor: "custom-record-type-replication"
        content: |
          {% include layout/image.html type="right" file="/integrations/netsuite-custom-record-bookmarks.png" alt="Highlighted Show Creation Date and Show Last Modified fields in NetSuite's Custom Record Type page" max-width="350" %}
          The Replication Method Stitch uses to replicate data for a custom record type depends on two custom record settings in {{ integration.display_name }}: **Show Last Modified** and **Show Creation Date**. These settings determine whether the {{ integration.display_name }} SuiteTalk API will return timestamp columns to use as [Replication Keys]({{ link.replication.rep-keys | prepend: site.baseurl }}).

          - **If the record definition has either setting enabled**, Stitch will use [Key-based Incremental Replication]({{ link.replication.key-based-incremental | prepend: site.baseurl }}). This means that only new and updated records for the record type will be replicated during each job.
          - **If the record definition doesn't have either setting enabled**, Stitch will use [Full Table Replication]({{ link.replication.full-table | prepend: site.baseurl }}). This means that all records for the record type will be replicated in full during each job.

          To check the configuration of these settings for a custom record type in {{ integration.display_name }}:

          1. Type `page: record types` into global search and click the **Page: Record Types** result.
          2. Locate and click the custom record type in the list. This will open the **Custom Record Type** page.
          3. Locate the **Show Creation Date** and **Show Last Modified** settings.

          In the example to the right, both of these settings are enabled for the `Stitch Example` custom record type.

  - title: "Deleted records"
    anchor: "deleted-records"
    content: |
      Accounting for deleted records is especially important if you’re performing any sort of aggregate function - for example, totaling invoices or balancing your books.

      To account for deletes in {{ integration.display_name }}, Stitch's {{ integration.display_name }} integration offers a table named [`Deleted`](#deleted). Once set to replicate, this table acts as a log for records deleted in {{ integration.display_name }} for [supported record types](#record-types-with-delete-support).

      In this section:

      {% for subsection in section.subsections %}
      - [{{ subsection.title | flatify }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "Identify deleted records in other tables"
        anchor: "identify-deleted-records-other-tables"
        content: |
          {% include note.html type="single-line" content="**Note**: The SQL queries in this section are only examples. As SQL syntax varies by database type, you may have to modify or rewrite these queries to allow them to run in your destination." %}

          To account for deleted records, you can use a `LEFT JOIN` to tie deleted records back to the appropriate table.

          For example: The following query would return all invoice records that exist in the `Transaction` and `Deleted` tables:

          ```sql
             SELECT * 
               FROM netsuite.Transaction tran 
          LEFT JOIN netsuite.Deleted del
                 ON tran.internalId = del.internalId 
                AND tran.type = 'invoice'
                AND del.type = 'invoice'
          ```

          If you're using a destination that is case-insensitive, some queries may result in errors. If this occurs, try using `LOWER` to resolve the issue:

          ```sql
             SELECT *
               FROM netsuite.Transaction tran 
          LEFT JOIN netsuite.Deleted del 
                 ON tran.internalId = del.internalId 
          AND LOWER(tran.type) = LOWER(del.type)
          ```

          To filter out deleted records from other data, you can run a query like this one:

          ```sql
             SELECT *
               FROM netsuite.Transaction tran 
          LEFT JOIN netsuite.Deleted del
                 ON tran.internalId = del.internalId 
          AND LOWER(tran.type) = LOWER(del.type) 
              WHERE del.deletedDate is null;
          ```

          Refer to the [`Deleted` table schema](#deleted) for more info about the available fields in the `Deleted` table.

      - title: "Record types with delete support"
        anchor: "record-types-with-delete-support"
        content: |
          According to [{{ integration.display_name }}'s documentation](https://975200-sb2.app.netsuite.com/app/help/helpcenter.nl?fid=section_N3497592.html){:target="new"}, only certain record types support the `getDeleted` API operation Stitch uses to retrieve deleted record data from the SuiteTalk API.

          In the table below are the record types that have delete support and the name of the Stitch table that contains the data for that record  type. If a record type is listed, records of this type will be logged in the `Deleted` table when they are deleted in {{ integration.display_name }}.

          **Note**: If a record type isn't in this list, it doesn't have delete support. Records not listed here will not be included in the `Deleted` table even if they are deleted in {{ integration.display_name }}.

          <table class="attribute-list">
          <tr>
          <td width="40%; fixed" align="right">
          <strong>
          {{ integration.display_name }} record type
          </strong>
          </td>
          <td class="attribute-description">
          <strong>
          Stitch table name
          </strong>
          </td>
          </tr>
          {% for object in site.data.taps.extraction.netsuite.objects-with-delete-support %}
          <tr>
          <td width="40%; fixed" align="right">
          {{ object.name }}
          </td>
          <td class="attribute-description">
          {% if object.anchor %}
          <a href="#{{ object.anchor }}">{{ object.table | default: object.name }}</a>
          {% else %}
          {{ object.table | default: object.name }}
          {% endif %}
          </td>
          </tr>
          {% endfor %}
          </table>

  - title: "Supported {{ integration.display_name }} transaction types"
    anchor: "supported-transaction-types"
    content: |
      Stitch supports replicating the transaction types listed below. Data for these records can be found in the `Transaction` table:

      {% for transaction-type in site.data.taps.extraction.netsuite.multi-search-objects.transactions %}
      - {{ transaction-type.name }}
      {% endfor %}

  - title: "Supported {{ integration.display_name }} item types"
    anchor: "supported-item-types"
    content: |
      Stitch supports replicating the item types listed below. Data for these records can be found in the `Item` table:

      {% for item-type in site.data.taps.extraction.netsuite.multi-search-objects.items %}
      - {{ item-type.name }}
      {% endfor %}

  - title: "Unsupported {{ integration.display_name }} record types"
    anchor: "unsupported-objects"
    content: |
      Stitch supports replicating all record types from {{ integration.display_name }}'s 2018.1 WSDL, with the exception of the following:

      {% assign blacklisted-objects = site.data.taps.extraction.netsuite.blacklisted-objects.all | sort:"name" %}

      {% for blacklisted-object in blacklisted-objects %}
      - {{ blacklisted-object.name }}
      {% endfor %}

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/netsuite

schema-sections:
  - content: |
      To ensure we can provide you with up-to-date documentation, this section will only cover a few of the most popular tables Stitch's {{ integration.display_name }} integration offers.

      Refer to the [{{ integration.display_name }} SuiteTalk Schema Browser](https://975200-sb2.app.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2018_2/schema/index.html){:target="new"} for info on objects not listed here, including the fields available in each object.

      **Note**: Stitch currently supports the replication of the majority of {{ integration.display_name }} objects, with the exception of those listed in the [Unsupported Objects section](#unsupported-objects).
---
{% assign integration = page %}
{% include misc/data-files.html %}