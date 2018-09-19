---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: NetSuite
permalink: /integrations/saas/netsuite
tags: [saas_integrations]
keywords: netsuite, integration, schema, etl netsuite, netsuite etl, netsuite schema
summary: "Connection instructions and schema details for Stitch's NetSuite integration."
layout: singer

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "netsuite"
display_name: "NetSuite"
singer: false
author: "Stitch"
author-url: "https://www.stitchdata.com"
status-url: "https://status.netsuite.com/"

# this-version: "10-15-2015"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

historical: "1 year"
frequency: "30 minutes"
tier: "Premium"
icon: /images/integrations/icons/netsuite.svg
whitelist:
  tables: true
  columns: false

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

## Info about permissions is kept in: _data/taps/extraction/netsuite/netsuite-permissions.yml

requirements-list:
  - item: "**Administrator permissions in NetSuite**. This is required to complete parts of the setup process."
  - item: "**To enable Web Services for your NetSuite account.** This is necessary to access NetSuite's API."

setup-steps:
  - title: "Enable Web Services in Your NetSuite Account"
    anchor: "enable-web-services"
    content: |
      {% include note.html content="If Web Services is already enabled for your account, skip this step." %}

      1. In your NetSuite account, click **Setup > Company > Enable Features**.
      2. Click the **SuiteCloud** subtab.
      3. Locate the **SuiteTalk (Web Services)** section.
      4. Check the **Web Services** box:
         ![The SuiteTalk (Web Services) section in NetSuite's SuiteCloud subtab.]({{ site.baseurl }}/images/integrations/netsuite-suitecloud-webservices.png)
      5. Scroll to the bottom of the page and click **Save**.

  - title: "Create a Stitch NetSuite Admin User"
    anchor: "create-netsuite-admin-user"
    content: |
      To connect NetSuite to Stitch, we recommend that you create a Stitch-specific Admin user for us. We suggest this approach for a few reasons:

      1. This will ensure that Stitch is easily distinguishable in any logs or audits.

      2. NetSuite's API has some limitations that could make it difficult or impossible for Stitch to replicate data. For example: a single NetSuite user is only allowed to have **one** open API session at a time. If there's another connection elsewhere, Stitch will run into problems replicating data.

      After you've created the Admin user, move onto the next step.

## Info about permissions is kept in: _data/taps/extraction/netsuite/netsuite-permissions.yml

  - title: "Retrieve the NetSuite User's Role ID"
    anchor: "retrieve-netsuite-role-id"
    content: |
      All Roles in NetSuite have a `Name` - for example, Accountant - and `Role ID`, or Internal ID number. Stitch requires this ID to successfully create a NetSuite integration.

      Role IDs can be found on the **Manage Roles** page in NetSuite. From your dashboard, click **Setup > Users/Roles > Manage Roles*.

      Locate the Role of the user in the Roles list. The ID is located in a column called **Internal ID**:

      ![The Internal ID column contains the user's Role ID.]({{ site.baseurl }}/images/integrations/netsuite-locate-role-id.png)

      If you don't see the Internal ID column in the list, you may need to add it:

      1. Click the **Edit View** button.
      2. Click the drop-down menu and select **Internal ID**.
      3. Click **Add**.
      4. Click **Save**.

      After you add the column to the Roles list, locate the ID for the user and move onto the next step.

  - title: "add integration"
    content: |
      4. Enter the email address and password associated with the Stitch NetSuite user.
      5. Enter the **Role ID** - the numerical ID, not the name of the Role - associated with the user entered above. See [Step 3](#retrieve-netsuite-role-id) if you need help locating the user's Role ID.

         **Note:** If this field is left blank, Stitch will use NetSuite's default role ID for Admin roles (`3`). If you receive an error when trying to save the integration, enter a `3` in this field and try saving again.
      6. Select the **Account Type** - Production or Sandbox.
  - title: "historical sync"
  - title: "replication frequency"


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
          - **name**: This is the name of the record. For example: Invoice #INV197
          - **deletedDate:** The date the record was deleted.
          - **customRecord:** This indicates if the record was a custom record.
          - **internalId:** This is the numerical ID of the record.

          Custom records will look a little different than other records. In this case, you'll see the following:

          - **type**: This column will contain a **numerical ID**.
          - **name** and **internalId**: The `internalId` of the record will display in **both** columns.
          - **customRecord**: This column will contain a `true` value.

          For example: the first two records in this table are "normal" records, while the third is a custom record:

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

      {% assign transaction-table = integration.tables | where:"name","netsuite_transaction" %}

      {% for transaction-type in transaction-table.supported-types %}
        {{ transaction-type.name }}
        {{ transaction-table.name }}
      {% endfor %}

---
{% assign integration = page %}
{% include misc/data-files.html %}