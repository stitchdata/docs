---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Amazon S3 CSV
keywords: amazon-s3-csv, database integration, etl amazon-s3-csv, amazon-s3-csv etl
permalink: /integrations/databases/amazon-s3-csv
summary: "Connect and replicate data from CSV files in your Amazon S3 bucket using Stitch's Amazon S3 CSV integration."
snapshot-type: "databases"
show-in-menus: true
no-schema: true

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "amazon-s3-csv"
display_name: "Amazon S3 CSV"
setup-name: "S3 CSV"

singer: true
repo-url: "https://github.com/singer-io/tap-s3-csv"
status-url: "https://status.aws.amazon.com/"

# this-version: "1.0"

# -------------------------- #
#       Stitch Supports      #
# -------------------------- #

status: "Released"
certified: true
setup-name: "Amazon S3"

frequency: "1 hour"
historical: "1 year"
tier: "Free"
db-type: "s3"

## Stitch features

versions: "n/a"
ssh: false
ssl: false

## General replication features

anchor-scheduling: true
extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true
table-level-reset: false

## Replication methods

define-replication-methods: false

log-based-replication-minimum-version: "n/a"
log-based-replication-master-instance: false
log-based-replication-read-replica: false

## Other Replication Methods

key-based-incremental-replication: true
full-table-replication: false

view-replication: false



# -------------------------- #
#    Table search patterns   #
# -------------------------- #

search-pattern-examples:
  - example: "Single file, periodically updated"
    file-name: "`customers.csv`"
    updates: "A single CSV file is periodically updated with new and updated customer data."
    description: "Because there will only ever be one file, you could enter the exact name of the file in your S3 bucket:"
    pattern: |
      customers\.csv
    matches: "`customer.csv`, exactly"

  - example: "Multiple files, generated daily"
    file-name: "`customers-<string>.csv`, where `<string>` is a unique, random string"
    updates: "A new CSV file is created every day that contains new and updated customer data. Old files are never updated after they're created."
    description: "To ensure new and updated files are identified, you'd want to enter a search pattern that would match all files beginning with `customers`, regardless of the string in the file name:"
    pattern: |
      (customers-).*\.csv
    matches: |
      - `customers-reQDSwNG6U.csv`
      - `customers-xaPTXfN4tD.csv`
      - `customers-MBJMhCbNCp.csv`
      - etc.

# -------------------------- #
#   Data types for loading   #
# -------------------------- #

loading-data-types:
  - name: "datetime"
    note: |
      If a value can't be parsed as a date, Stitch will load the column as a nullable `string`. To ensure dates are typed properly, [specify them during setup](#specify-datetime-fields).
  - name: "integer"
  - name: "number"
  - name: "string"

# -------------------------- #
#          Sample data       #
# -------------------------- #

## Sample data for Append-only explanation

sample-data:
  - name: "Finn"
    type: "human"
    magic: false
    primary-key: "b6c0fd8c-7dec-4e34-be93-2b774fde32cc"
    job: 1

  - name: "Finn"
    type: "human"
    magic: false
    primary-key: "0acd439b-cefe-436c-b8ba-285bd956057b"
    job: 2

  - name: "Jake"
    type: "dog"
    magic: true
    primary-key: "4b5c413c-1adf-4720-8ccc-48579d6b4e58"
    job: 1

  - name: "Jake"
    type: "dog"
    magic: true
    primary-key: "7e9fa5cf-1739-45a2-9a89-caa6f393efc9"
    job: 2

  - name: "Beamo"
    type: "robot"
    magic: true
    primary-key: "634d6945-1762-4049-b997-cd9240d4592b"
    job: 2

  - name: "Bubblegum"
    type: "princess"
    magic: true
    primary-key: "c5fb32b8-a16d-455d-96c9-b62fff22fe4b"
    job: 2



# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements-list:
  - item: |
      **An Amazon Web Services (AWS) account.** Signing up is free - [click here](https://aws.amazon.com){:target="new"} or go to `https://aws.amazon.com` to create an account if you don't have one already.
  - item: |
      **Permissions in AWS Identity Access Management (IAM) that allow you to create policies, create roles, and attach policies to roles**. This is required to grant Stitch authorization to your S3 bucket.
  - item: |
      **To verify that column names in CSV files adhere to your destination's length limit for column names**. If a column name exceeds the destination's limit, the [destination will reject the column]({{ link.destinations.storage.rejected-records | prepend: site.baseurl }}). Compliant columns will persist to the destination.

      Column name limits vary by destination:

      {% capture destination-column-name-limits %}
      {% assign all-destinations = site.destinations | where:"destination",true | sort:display_name %}
      {% assign destinations = all-destinations | where_exp:"destination","destination.type != 'data-world'" %}

      {% for destination in destinations %}

      {% case site.data.destinations.reference[destination.type]object-name-limit-info.columns %}

      {% when 'n/a' %}
      {% capture column-name-limit %}
      Not applicable to this destination
      {% endcapture %}

      {% else %}
      {% capture column-name-limit %}
      Limited to **{{ site.data.destinations.reference[destination.type]object-name-limit-info.columns }} characters**
      {% endcapture %}
      {% endcase %}
      - **{{ destination.display_name }}** - {{ column-name-limit }}
      {% endfor %}
      {% endcapture %}

      {{ destination-column-name-limits }}

# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

setup-steps:
  - title: "Retrieve your Amazon Web Services account ID"
    anchor: "retrieve-aws-account-id"
    content: |
      {% include integrations/shared-setup/aws-s3-iam-setup.html type="retrieve-account-id" %}
      
  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include shared/database-connection-settings.html type="general" %}

  - title: "Configure tables"
    anchor: "configure-tables"
    content: |
      Next, you'll indicate which CSV file(s) you want to include for replication. You can include a single CSV file, or map several CSV files to a table.

      In the following sections, we'll walk you through how to configure a table in Stitch.

      {% capture best-table-results %}
      For the best results:

      - **Each file should have a header row with names that adhere to your destination's limits for column names.** If a column name exceeds the destination's limit, the [destination will reject the column]({{ link.destinations.storage.rejected-records | prepend: site.baseurl }}).

      - **If including multiple files in a table, each file should have the same header row.** Including multiple files in a single table depends on the search pattern you define in the next step.

        **Note**: This is not the same as configuring multiple tables. See the [search pattern](#define-table-search-pattern-and-name) section below for examples.
      {% endcapture %}

      {% include note.html first-line="**Tips for setting up CSV files**" content=best-table-results %}

    substeps:

## If a user is including a single file inside of a folder, do they need to escape backslashes and periods?
## Is there anything that will *not* work in this field?
## Does the first backslash for a directory need to be included? (Ex: /analytics/file.csv vs analytics/file.csv)
      - title: "Define the table's search settings"
        anchor: "define-table-search-settings"
        content: |
          In this step, you'll tell Stitch which files in your S3 bucket you want to replicate data from. To do this, you'll use the **Search Pattern** and **Directory** fields.

        sub-substeps:
          - title: "Define the Search Pattern"
            anchor: "define-search-pattern"
            content: |
              The **Search Pattern** field defines the search criteria Stitch should use for selecting and replicating CSV files. This field accepts regular expressions, which can be used to include a single file or multiple CSV files. 

              The search pattern you use depends on how data for a particular entity is updated. Consider these examples:

              <table class="attribute-list">
              <tr>
              <td align="right" width="18%; fixed">
              <strong>Scenario</strong>
              </td>
              {% for example in integration.search-pattern-examples %}
              <td width="42%; fixed">
              {{ example.example }}
              </td>
              {% endfor %}
              </tr>

              <tr>
              <td align="right" width="18%; fixed">
              <strong>How updates are made</strong>
              </td>
              {% for example in integration.search-pattern-examples %}
              <td width="42%; fixed">
              {{ example.updates | markdownify }}
              </td>
              {% endfor %}
              </tr>

              <tr>
              <td align="right" width="18%; fixed">
              <strong>File name</strong>
              </td>
              {% for example in integration.search-pattern-examples %}
              <td width="42%; fixed">
              {{ example.file-name | markdownify }}
              </td>
              {% endfor %}
              </tr>

              <tr>
              <td align="right" width="18%; fixed">
              <strong>Search pattern</strong>
              </td>
              {% for example in integration.search-pattern-examples %}
              <td width="42%; fixed">
              {{ example.description | markdownify }}

              {% highlight text %}
              {{ example.pattern | strip }}
              {% endhighlight %}
              </td>
              {% endfor %}
              </tr>

              <tr>
              <td align="right" width="18%; fixed">
              <strong>Matches</strong>
              </td>
              {% for example in integration.search-pattern-examples %}
              <td width="42%; fixed">
              {{ example.matches | markdownify }}
              </td>
              {% endfor %}
              </tr>
              </table>

              When creating a search pattern, keep the following in mind:

              - Special characters such as periods (`.`) have special meaning in regular expressions. To match exactly, they'll need to be escaped. For example: `.\`
              - Stitch uses Python for regular expressions, which may vary in syntax from other varieties. Try using [PyRegex](http://www.pyregex.com/){:target="new"} to test your expressions before saving the integration in Stitch.

          - title: "Limit file search to a specific directory"
            anchor: "limit-search-to-directory"
            content: |
              {% include note.html type="single-line" content="**Note**: This step is optional." %}

              The **Directory** field limits the location of the file search Stitch performs during replication jobs. When defined, Stitch will only search for files in this location and select the ones that match the [search pattern](#define-search-pattern).

              To define a specific location in the S3 bucket, enter the directory path into the **Directory** field. For example: `data-exports/lists`. **Note**: This field is not a regular expression.

              While using this field is optional, limiting the search to a single location may make extraction more efficient.

      - title: "Define the table's name"
        anchor: "define-table-name"
        content: |
          In the **Table Name** field, enter a name for the table. Keep in mind that each destination has its own rules for how tables can be named. For example: Amazon Redshift table names can't exceed {{ site.data.destinations.reference.redshift.object-name-limit-info.tables }}.

          If the table name exceeds the destination's character limit, the [destination will reject the table entirely]({{ link.destinations.storage.rejected-records | prepend: site.baseurl }}). Refer to the [documentation for your destination]({{ link.destinations.overview | prepend: site.baseurl }}) for more info about table naming rules.

      - title: "Define the table's Primary Key"
        anchor: "define-table-primary-key"
        content: |
          {% include note.html type="single-line" content="**Note**: This step is optional." %}

          In the **Primary Key** field, enter one or more header fields (separated by commas) Stitch can use to identify unique rows. For example:

          ```
          account_id,date
          ```

          If undefined, Stitch will load data into the table in an append-only fashion. This means that existing rows in the destination won't be updated, but will be appended to the end of the table. Refer to the [Primary Keys and Append-Only Replication](#primary-keys-append-only) section below for more info and examples.

      - title: "Specify datetime fields"
        anchor: "specify-datetime-fields"
        content: |
          {% include note.html type="single-line" content="**Note**: This step is optional." %}

          In the **Specify datetime fields** field, enter one or more header fields (separated by commas) that should appear in the destination table as `datetime` fields instead of strings. For example:

          ```
          created_at,updated_at
          ```

          If columns are not specified and values cannot be parsed as dates, Stitch will load them as nullable strings. Refer to the [Determining data types section](#determining-data-types) for more info on how Stitch identifies data types.

      - title: "Configure additional tables"
        anchor: "configure-additional-tables"
        content: |
          If you want to add another table, click the **Configure another table?** link below the **Specify datetime fields** field. Otherwise, move onto the [Sync historical data](#define-historical-sync) section.

           Stitch doesn't enforce a limit on the number of tables that you can configure for a single integration.

  - title: "Define the historical sync"
    anchor: "define-historical-sync"
    content: |
      {% include integrations/saas/setup/historical-sync.html %}
    content: |
      For example: You've added a `customers.*\csv` search pattern and set the integration's historical **Start Date** to 1 year. During the initial replication job, Stitch will fully replicate the contents of all files that match the search pattern that have been modified in the past year.

      During subsequent replication jobs, Stitch will only replicate the files that have been modified since the last job ran.

      As files included in a replication job are replicated in full during each job, how data is added to updated files can impact your row count. Refer to the [Incremental Replication for {{ integration.display_name }}](#incremental-replication-for-amazon-s3-csv) section for more info on initial and subsequent replication jobs for {{ integration.display_name }}.

  - title: "Create a replication schedule"
    anchor: "create-replication-schedule"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}

  - title: "Grant access to your bucket using AWS IAM"
    anchor: "grant-access-bucket-iam"
    content: |
      {% include integrations/shared-setup/aws-s3-iam-setup.html type="aws-iam-access-intro" %}

    substeps:
      - title: "Create an IAM policy"
        anchor: "create-iam-policy"
        content: |
          {% include integrations/shared-setup/aws-s3-iam-setup.html type="create-iam-policy" %}
          
      - title: "Create an IAM role for Stitch"
        anchor: "create-stitch-iam-role"
        content: |
          {% include integrations/shared-setup/aws-s3-iam-setup.html type="create-stitch-iam-role" %}

      - title: "Check and save the connection in Stitch"
        anchor: "check-save-stitch-connection"
        content: |
          {% include integrations/shared-setup/aws-s3-iam-setup.html type="check-and-save" %}

  - title: "Select data to replicate"
    anchor: "setting-data-to-replicate"
    content: |
      {% include integrations/databases/setup/syncing.html %}

# -------------------------- #
#      Replication Info      #
# -------------------------- #

replication-sections:
  - content: |
      In this section:
        - [How data types are determined](#determining-data-types)
        - [How new and updated data is identified and replicated](#incremental-replication-for-amazon-s3-csv)
        - [How Primary Keys affect loading data](#primary-keys-append-only)

  # - title: "Table schema detection"
  #   anchor: "table-schema-detection"
  #   content: |
  #     Stitch's {{ integration.display_name }} integration expects the structure of a given CSV file to be stable. This means that header rows should be the same for every file included in a table's configuration.

  #     To determine a table's structure, Stitch will analyze the first **five** files returned by the table's [Search Pattern](#define-table-search-pattern). Stitch will use the header rows in these five files to determine the schema of the destination table. **Note**: If the header rows change after the fifth file, Stitch will not detect the differences.

  #     For example: The first five files for a configured table contain the following header rows:

  #     <table class="attribute-list">
  #     <tr>
  #     <td><strong>id</strong></td>
  #     <td><strong>name</strong></td>
  #     <td><strong>age</strong></td>
  #     <td><strong>location</strong></td>
  #     </tr>
  #     </table>

  #     In the sixth CSV file, a new column named `active` is added, changing the schema to the following:

  #     <table class="attribute-list">
  #     <tr>
  #     <td><strong>id</strong></td>
  #     <td><strong>name</strong></td>
  #     <td><strong>age</strong></td>
  #     <td><strong>location</strong></td>
  #     <td><strong>active</strong></td>
  #     </tr>
  #     </table>

  #   subsections:
  #     - title: "Handling schema changes"
  #       anchor: "handling-schema-changes"
  #       content: |
  #         Stitch's {{ integration.display_name }} works best when the header rows are consistent across the files for a given table. If the structure of the files used for a given table changes, this is what Stitch recommends:

  #         1. **Nest files in folders in {{ integration.display_name }}.** For example: `/old-files/customers.csv` and `/new-files/customers.csv`
  #         2. **Add a new table configuration to the integration in Stitch.** You can add a new table in the {{ app.page-names.int-settings }} page. The new table's **Search Pattern** should match only the folder containing the updated files for the table.
  #         3. **Update the old table's Search Pattern**.

  - title: "Determining data types"
    anchor: "determining-data-types"
    content: |
      To determine a column's data type, Stitch will analyze the first 1,000 lines of (up to) the first **five** files included for a given table.

      Stitch's {{ integration.display_name }} integration will load data from CSV files and type it as one of the following data types:

      {% for item in integration.loading-data-types %}
      - `{{ item.name | upcase }}`{% if item.note %} - {{ item.note }}{% endif%}
      {% endfor %}

  - title: "Incremental Replication for {{ integration.display_name }}"
    anchor: "incremental-replication-for-amazon-s3-csv"
    content: |
      {% include replication/extraction/file-modification-replication-keys.html %}

    subsections:
      - title: "Frequently updated files and impact on row usage"
        anchor: "frequently-updated-files-row-usage-impact"
        content: |
          Because modified files are replicated in full during each replication job, large, frequently updated files can quickly use up a large number of rows.

          To reduce row usage, you could create new files that only include updated records that match the table's [search pattern](#define-table-search-pattern). This will ensure that only updated records are replicated and counted towards your usage.

  - title: "Primary Keys and Append-Only Replication"
    anchor: "primary-keys-append-only"
    content: |
      {% include note.html type="single-line" content="**For BigQuery and Amazon S3 (CSV) destinations**: Replication will function in an append-only manner regardless of whether a Primary Key is specified during setup. Refer to the [Querying Append-Only tables section](#querying-append-only-tables) for more info." %}

      For destinations that support upserts (that is, updating existing rows), Stitch uses Primary Keys to de-dupe data during loading. {{ site.data.tooltips.primary-key }}

      **If Primary Keys aren't specified during setup**, Stitch will load data using [Append-Only Replication]({{ link.replication.append-only | prepend: site.baseurl }}). This means that existing rows in the destination won't be updated, but instead appended to the end of the table.

      Additionally, Stitch will append a column (`{{ system-column.primary-key }}`) to the table to function as a Primary Key. **Note**: Appending this column will not enable Stitch to de-dupe data, as a unique value will be inserted every time a row is loaded, regardless of whether it's ever been replicated before. This means that a record can have multiple `{{ system-column.primary-key }}` values, each of them unique.

    subsections:
      - title: "Example: Append-Only with {{ system-column.primary-key }}"
        anchor: "append-only-example"
        content: |
          For example: The following rows are replicated during the initial replication job:

          {% assign initial-job = integration.sample-data | where:"job","1" %}

          <table class="attribute-list">
            <tr>
              <td width="45%; fixed">
                <strong>{{ system-column.primary-key }}</strong>
              </td>
              <td>
                <strong>name</strong>
              </td>
              <td>
                <strong>type</strong>
              </td>
              <td>
                <strong>magic</strong>
              </td>
            </tr>
            {% for record in initial-job %}
            <tr>
              <td>
                {{ record.primary-key }}
              </td>
              <td>
                {{ record.name }}
              </td>
              <td>
                {{ record.type }}
              </td>
              <td>
                {{ record.magic }}
              </td>
            </tr>
            {% endfor %}
          </table>

          Before the next job, the CSV file containing these rows is modified. This means that Stitch will replicate the contents of the entire file, including the rows for `Finn` and `Jake` even if they haven't been updated.

          In the destination, the table might now look like the table below. Notice that records for `Finn` and `Jake` have been appended to the end of the table with new `{{ system-column.primary-key }}` values:

          {% assign second-job = integration.sample-data %}

          <table class="attribute-list">
            <tr>
              <td width="45%; fixed">
                <strong>{{ system-column.primary-key }}</strong>
              </td>
              <td>
                <strong>name</strong>
              </td>
              <td>
                <strong>type</strong>
              </td>
              <td>
                <strong>magic</strong>
              </td>
            </tr>
            {% for record in second-job %}
            <tr>
              <td>
                {{ record.primary-key }}
              </td>
              <td>
                {{ record.name }}
              </td>
              <td>
                {{ record.type }}
              </td>
              <td>
                {{ record.magic }}
              </td>
            </tr>
            {% endfor %}
          </table>

      - title: "Querying Append-Only tables"
        anchor: "querying-append-only-tables"
        content: |
          Querying Append-Only tables requires a different strategy than you might normally use. For instructions and a sample query, check out the [Querying Append-Only tables guide]({{ link.replication.append-only-querying | prepend: site.baseurl }}).

          {% capture append-only-destinations %}
          The answer depends on your destination:

          - **BigQuery and Amazon S3 CSV** - These destinations are Append-Only regardless of whether Primary Keys are specified.

             If you specified Primary Keys during setup, use the column(s) specified (ex: `id`). Otherwise, use `{{ system-column.primary-key }}`.
          - **All other destinations** - Use `{{ system-column.primary-key }}` when querying Append-Only tables.
          {% endcapture %}

          {% include note.html first-line="**What column do I use as a Primary Key when querying?**" content=append-only-destinations %}


# -------------------------- #
#         Schema Info        #
# -------------------------- #

other-sections:
  - title: "{{ integration.display_name }} table schemas"
    anchor: "table-schemas"
    content: |
      In this section:

      - [Why column names may be transformed](#column-name-transformations)
    subsections:
      - title: "Column name transformations"
        anchor: "column-name-transformations"
        content: |
          When loading data, Stitch may perform some light transformation on column names to ensure the names follow the destination's rules for column names. This might include removing or replacing spaces or illegal characters such as `!#*`.

          **Note**: Stitch will not truncate column names to make them adhere to a destination's length limit. If a column's name is too long, the destination will reject the column. Compliant columns will persist to the table.

          For info on and examples of column name transformations, refer to the documentation for your destination type:

          {% assign destinations = site.destinations | where:"destination",true | sort:"title" %}

          {% for destination in destinations %}
          {% unless destination.type == "data-world" or destination.type == "amazon-s3" %}
          - [{{ destination.title | remove:" Destination" }}]({{ destination.url | prepend: site.baseurl | append: "#column-naming" }})
          {% endunless %}
          {% endfor %}
---
{% assign integration = page %}
{% include misc/data-files.html %}
{% include misc/icons.html %}