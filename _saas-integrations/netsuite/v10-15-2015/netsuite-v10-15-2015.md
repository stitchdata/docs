---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: NetSuite (v10-15-2015)
permalink: /integrations/saas/netsuite-suitetalk/v10-15-2015

keywords: netsuite, integration, schema, etl netsuite, netsuite etl, netsuite schema
summary: "Connection instructions and schema details for Stitch's NetSuite integration."
layout: singer
input: false

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "netsuite"
display_name: "NetSuite"
singer: false

this-version: "10-15-2015"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Deprecated"
certified: true

historical: "1 year"
frequency: "30 minutes"
tier: "Paid"

table-selection: true
column-selection: false

anchor-scheduling: true
extraction-logs: false
loading-reports: true

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

## Info about permissions is kept in: _data/taps/extraction/netsuite/netsuite-permissions.yml

requirements-list:
  - item: "**Administrator permissions in {{ integration.display_name }}**. This is required to complete the setup steps in {{ integration.display_name }}."
  - item: "**To enable Web Services for your {{ integration.display_name }} account.** This is necessary to access {{ integration.display_name }}'s API."

setup-steps:
  - title: "Enable Web Services in your {{ integration.display_name }} account"
    anchor: "enable-web-services"
    content: |
      {% include note.html type="single-line" content="**Note:**This step is only required if Web Services isn't already enabled in your NetSuite account." %}

      1. In your {{ integration.display_name }} account, click **Setup > Company > Enable Features**.
      2. Click the **SuiteCloud** subtab.
      3. Locate the **SuiteTalk (Web Services)** section.
      4. Check the **Web Services** box:
         ![The SuiteTalk (Web Services) section in NetSuite's SuiteCloud subtab.]({{ site.baseurl }}/images/integrations/netsuite-suitecloud-webservices.png)
      5. Scroll to the bottom of the page and click **Save**.

  - title: "Whitelist Stitch's IP addresses"
    anchor: "whitelist-stitch-ips"
    content: |
      {% include note.html type="single-line" content="**Note**: This step is required only if IP whitelisting is enforced for your NetSuite account." %}

      {% include layout/inline_image.html type="right" file="integrations/netsuite-ip-addresses.png" alt="" max-width="400px" %}
      1. In your {{ integration.display_name }} account, click **Setup > Company > Company Information**.
      2. In the **Allowed IP addresses** field, enter a comma-separated list of the following IP addresses:

         {% for ip-address in ip-addresses %}
         - {{ ip-address.ip }}
         {% endfor %}
      3. Click **Save**.

  - title: "Create a Stitch {{ integration.display_name }} role"
    anchor: "create-stitch-netsuite-role"
    content: |
      To connect {{ integration.display_name }} to Stitch, we recommend that you create a Stitch-specific role and user for us. We suggest this to ensure that:

      1. Stitch is easily distinguishable in any logs or audits.

      2. Stitch doesn't encounter issues with replication due to {{ integration.display_name }}'s API limitations. Currently, a single {{ integration.display_name }} user is allowed to only have a single open API session at a time. If the user connected to Stitch has another connection elsewhere, replication problems will arise.

      3. Stitch can successfully authenticate to {{ integration.display_name }}.

    substeps:
      - title: "Create the new role"
        anchor: "create-the-new-role"
        content: |
          1. Using the global search, type `page: new role` and click the **Page: New Role** result.
          2. On the Role page, enter a name for the role in the **Name** field. For example: `Stitch`
          3. In the **Authentication** section, check the **Web Services Only Role** box.

      - title: "Grant permissions to the role"
        anchor: "grant-permissions-to-role"
        content: |
          Next, you'll grant permissions to the role. In the tabs below, you'll find the following:

          - **Adding permissions** - Step-by-step instructions for adding permissions to the role on the **Create Role** page.
          - **Required permissions** - The minimum permissions required to successfully connect Stitch to {{ integration.display_name }}.
          - **Object permissions** - The permissions required to access and replicate data for specific objects in {{ integration.display_name }}. Stitch recommends granting only the permissions required for the objects you want to replicate.

          {% include integrations/saas/netsuite-permission-list.html %}

      - title: "Save the role and retrieve its internal ID"
        anchor: "save-role-retrieve-id"
        content: |
          After you've finished granting permissions to the role, click **Save** to create  it.

          Next, you'll retrieve the role's internal ID. Stitch requires this ID to successfully create your {{ integration.display_name }} integration.

          If you've just saved the role, you should automatically be redirected to the **Manage Roles** page. If not, you can access this page by clicking **Setup > Users/Roles > Manage Roles**.

          Locate the role you just created. The ID is located in a column called **Internal ID**:

          ![The Internal ID column contains the user's Role ID.]({{ site.baseurl }}/images/integrations/netsuite-locate-role-id.png)

          If you don't see the Internal ID column in the list, you may need to add it:

          1. Click the **Edit View** button.
          2. Click the drop-down menu and select **Internal ID**.
          3. Click **Add**.
          4. Click **Save**.

          After you add the column to the Roles list, locate the ID for the role. Keep this handy - you'll need it to complete the setup in Stitch.
        
  - title: "Create the Stitch {{ integration.display_name }} user"
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

  - title: "Locate your {{ integration.display_name }} Account ID"
    anchor: "locate-netsuite-account-id"
    content: |
      {% include layout/inline_image.html type="right" file="integrations/netsuite-account-id.png" alt="" max-width="250px" %}
      Click **Setup > Integration Web Services Preferences**.
      
      In the Primary Information section, locate the **Account ID** field as shown in the image on the right.
      
      **Note**: If your Account ID contains a suffix - `1234567_SB2`, for example - it should be included when entering the ID into Stitch.

  - title: "add integration"
    content: |
      4. Enter the email address and password associated with the Stitch {{ integration.display_name }} user.
      5. Enter the **Role ID** you retrieved in [Step 3.3](#save-role-retrieve-id). **Note**: This must be the numerical ID, not the name of the role. See [Step 3.3](#save-role-retrieve-id) if you need help locating the user's Role ID.
      6. In the **Account ID** field, enter the Account ID you retrieved in [Step 5](#locate-netsuite-account-id).
      6. Select the **Account Type** - Production or Sandbox.
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data"

# -------------------------- #
#     Integration Tables     #
# --------------------------#

schema-sections:
  - title: "Deleted records"
    anchor: "using-netsuite-deleted"
    content: |
      Stitch's NetSuite integration includes a table called `netsuite_deleted`; this table contains a row for **every deleted record that supports deletes**. Accounting for deleted records is especially important if you’re performing any sort of aggregate function - for example, totaling invoices or balancing your books.

      For this reason, we recommend setting this table to replicate.
    subsections:
      - title: "netsuite_deleted Table Schema"
        anchor: "netsuite-deleted-table-schema"
        content: |
          The attributes of the `netsuite_deleted` table include:

          - **type**: This indicates the **type** of record. For example: invoice.
          - **name**: This is the name of the record. For example: `Invoice #INV197`
          - **deletedDate:** The date the record was deleted.
          - **customRecord:** This indicates if the record was a custom record.
          - **internalId:** This is the numerical ID of the record.

          Custom records will look a little different than other records. In this case, you'll see the following:

          - **type**: This column will contain a **numerical ID**.
          - **name** and **internalId**: The `internalId` of the record will display in **both** columns.
          - **customRecord**: This column will contain a `true` value.

          For example: The first two records in this table are "normal" records, while the third is a custom record:

          | type         | internalId | name             | customRecord | deletedDate                   |
          |--------------+------------+------------------+--------------+-------------------------------|
          | invoice      | 124831     | Invoice #INV197  | false        | 2016-08-02T09:33:07.000-07:00 |
          | journalEntry | 111366     | Journal #JV13526 | false        | 2016-08-04T12:01:22.000-07:00 |
          | 19           | 128        | 128              | true         | 2016-07-21T12:05:26.000-07:00 |

      - title: "Accounting for deleted records"
        anchor: "accounting-record-deletes"
        content: |
          To account for deleted records, you can use a `LEFT JOIN` to tie deleted records back to the appropriate table.

          For example: The following query would return all invoice records that exist in the `netsuite_transaction` and `netsuite_deleted` tables:

          ```sql
             SELECT * 
               FROM netsuite_transactions tran 
          LEFT JOIN netsuite_deleted del
                 ON tran.internalId = del.internalId 
                AND tran.type = 'invoice'
                AND del.type = 'invoice'
          ```

          If you're using a data warehouse that is **case-insensitive** (like Redshift), some queries may result in errors. If this occurs, try using `LOWER` to resolve the issue:

          ```sql
             SELECT *
               FROM netsuite_transactions tran 
          LEFT JOIN netsuite_deleted del 
                 ON tran.internalId = del.internalId 
          AND LOWER(tran.type) = LOWER(del.type)
          ```

          To filter out deleted records from other data, you can run a query like this one:

          ```sql
             SELECT *
               FROM netsuite_transactions tran 
          LEFT JOIN netsuite_deleted del
                 ON tran.internalId = del.internalId 
          AND LOWER(tran.type) = LOWER(del.type) 
              WHERE del.deletedDate is null;
          ```
  - title: "Supported transaction types"
    anchor: "transaction-types"
    content: |
      The following table contains the transaction types Stitch's NetSuite integration currently supports.

      {% assign all-tables = site.integration-schemas | where:"tap",integration.name %}
      {% assign transaction-table = all-tables | where:"name","netsuite_transaction" %}

      <table class="attribute-list">
      {% for table in transaction-table %}
      {% for transaction-type in table.supported-types %}
      {% cycle 'before': '<tr>', '', '', '' %}
      <td>
      {{ transaction-type.name }}
      </td>
      {% if forloop.last %}
      <td>
      </td>
      <td>
      </td>
      </tr>
      {% else %}
      {% cycle 'after': '', '', '', '</tr>' %}
      {% endif %}
      {% endfor %}
      {% endfor %}
      </table>
---
{% assign integration = page %}
{% include misc/data-files.html %}