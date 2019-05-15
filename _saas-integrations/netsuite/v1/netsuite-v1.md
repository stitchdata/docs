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

title: NetSuite (v1.0)
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

this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
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

permission-for-table: |
  {% assign object = site.data.taps.extraction.netsuite.netsuite-permissions[table.key] %}

  {% capture permission-copy %}
  **{% if object.permission.tab %}{{ object.permission.tab | append: " > " }}{% endif %}{{ object.permission.name }} ({{ object.permission.level | default: "View" }})**
  {% endcapture %}

  #### {{ table.name }} table replication requirements {#{{ table.name | slugify }}-table--replication-requirements}
  {% if object.feature-requirements %}
  Replicating this table requires that the following feature(s) be enabled in your {{ integration.display_name }} account:

  {% for feature in object.feature-requirements %}
  - **{% if feature.tab %}{{ feature.tab }} > {% endif %}{{ feature.name | flatify }}**{% if feature.description %} {{ feature.description | flatify }}{% endif %}
  {% endfor %}

  You will also need the {{ permission-copy | flatify }} permission. If you have the above feature(s) enabled, refer to the [Configure the Stitch role](#configure-permissions-save-stitch-role) section for instructions on adding this permission.

  {% else %}
  Replicating this table requires the {{ permission-copy | flatify }} permission{% if object.permission.description %}{{ object.permission.description | flatify }}{% endif %} in {{ integration.display_name }}. Refer to the [Configure the Stitch role](#configure-permissions-save-stitch-role) section for instructions on adding this permission.
  {% endif %}

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
      1. Sign into your {{ integration.display_name }} account as an administrator.
      2. In your {{ integration.display_name }} account, click **Setup > Company > Company Information**.
      3. In the **Allowed IP addresses** field, add the following comma-separated list of Stitch's IP addresses:

         ```
         {{ ip-addresses | strip_newlines }}
         ```

         **Note**: Make sure you don't overwrite or change any existing IP addresses in this field - doing so could cause access issues for you and other {{ integration.display_name }} users in your account.
      4. Click **Save**.

  - title: "Configure Web Services and authentication settings"
    anchor: "configure-web-services-and-authentication-settings"
    content: |
      To use Stitch's {{ integration.display_name }} integration, you'll need to enable Web Services and token-based authentication in your {{ integration.display_name }} account.
    substeps:
      - title: "Enable Web Services"
        anchor: "enable-web-services"
        content: |
          In this step, you'll enable Web Services for your {{ integration.display_name }} account. This is required to use {{ integration.display_name }}'s SuiteTalk API, which is what Stitch will use to extract data.

          1. Sign into your {{ integration.display_name }} account as an administrator, if you aren't already signed in.
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
      3. On the **New Integration** page, fill in the following fields:
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

      3. Stitch can successfully authenticate to {{ integration.display_name }}.
    substeps:
      - title: "Create a Stitch {{ integration.display_name }} role"
        anchor: "create-stitch-netsuite-role"
        content: |
          1. Using the global search, type `page: new role` and click the **Page: New Role** result.
          2. On the Role page, enter a name for the role in the **Name** field. For example: `Stitch`
          3. In the **Authentication** section, check the **Web Services Only Role** box.
          
      - title: "Configure permissions and save the Stitch role"
        anchor: "configure-permissions-save-stitch-role"
        content: |
          Next, you'll grant permissions to the role. In the tabs below, you'll find the following:

          - **Adding permissions** - Step-by-step instructions for adding permissions to the role on the **Create Role** page.
          - **Required permissions** - The minimum permissions required to successfully connect Stitch to {{ integration.display_name }}.
          - **Object permissions** - The permissions required to access and replicate data for specific objects in {{ integration.display_name }}. Stitch recommends granting only the permissions required for the objects you want to replicate.

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

      1. Using the global search, type `page: new employee` and click the **Page: New Employees** result.
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
      {% include note.html type="single-line" content="**Note**: This requires the **Setup > Access Token Management** permission in NetSuite." %}
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
          Custom record tables are named `customrecord_[custom_record_name]`, where `[custom_record_name]` is the value of the ID field in the Custom Record Setup page in {{ integration.display_name }}.

          For example: If a custom record were named `promo discount` in {{ integration.display_name }}, the corresponding table for those records would be named `customrecord_promo_discount`.

          If the ID field in the Custom Record Setup page is left blank, {{ integration.display_name }} will auto-assign a numerical ID to the record. In Stitch, the table for the custom record would then be something like `customrecord_123`, where `123` is the ID auto-assigned by {{ integration.display_name }}.

      - title: "Replication methods for custom record types"
        anchor: "custom-record-type-replication"
        content: |
          {% include layout/image.html type="right" file="/integrations/netsuite-custom-record-bookmarks.png" alt="Highlighted  Show Last Modified field in NetSuite's Custom Record Type page" max-width="350" %}
          The Replication Method Stitch uses to replicate data for a custom record type depends on whether the **Show Last Modified** setting is checked in {{ integration.display_name }} for the custom record. This determines whether the {{ integration.display_name }} SuiteTalk API will return a timestamp column to use as a [Replication Key]({{ link.replication.rep-keys | prepend: site.baseurl }}).

          - **If the record definition has the Show Last Modified setting enabled**, Stitch will use [Key-based Incremental Replication]({{ link.replication.key-based-incremental | prepend: site.baseurl }}). This means that only new and updated records for the record type will be replicated during each job.

          - **If the record definition doesn't have this setting enabled**, Stitch will use [Full Table Replication]({{ link.replication.full-table | prepend: site.baseurl }}). This means that all records for the record type will be replicated in full during each job.

          To check the configuration of this setting for a custom record type in {{ integration.display_name }}:

          1. Type `page: record types` into global search and click the **Page: Record Types** result.
          2. Locate and click the custom record type in the list. This will open the **Custom Record Type** page.
          3. Locate the **Show Last Modified** setting.

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
      Stitch supports replicating all record types from {{ integration.display_name }}'s 2017.2 WSDL, with the exception of the following:

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