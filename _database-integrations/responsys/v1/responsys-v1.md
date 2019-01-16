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

title: Responsys
permalink: /integrations/databases/responsys
tags: [database_integrations]
keywords: responsys, etl responsys, responsys etl
layout: singer
# input: false
snapshot-type: "databases"
show-in-menus: true
no-schema: true

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "responsys"
display_name: "Responsys"

singer: true 
tap-name: "Responsys"
repo-url: https://github.com/singer-io/tap-responsys
status-url: "https://community.oracle.com/docs/DOC-1011262"

# this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Open Beta"
certified: true 

historical: "1 year"
frequency: "1 hour"
tier: "Paid"
port: 22
db-type: "responsys"

icon: /images/integrations/icons/responsys.svg

## Stitch features

versions: "n/a"
ssh: true
ssl: false

## General replication features

anchor-scheduling: true
extraction-logs: true
loading-reports: true

table-selection: true
column-selection: false
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
#         Requirements       #
# -------------------------- #

file-requirements:
  - name: "File to be created"
    description: |
      We recommend using a **date/time prefix OR suffix** for file names, which will result in {{ integration.display_name }} creating multiple files.

      If a prefix or suffix isn't used, the export will only ever create a single file. Every new export will replace the entire file, overwriting the data it contains. If this occurs before Stitch runs an extraction job, the overwritten data would be lost and unable to be replicated.

  - name: "File extension"
    description: |
      **.csv** or **.txt**

      Stitch's {{ integration.display_name }} integration doesn't currently support replicating other file types.

  - name: "Character set"
    description: |
      Unicode (UTF-8)

  - name: "File delimiter"
    description: |
      Comma

      Stitch's {{ integration.display_name }} integration doesn't currently support other file delimiters.

  - name: "Field enclosure"
    description: |
      Double quotes (`"`)

  - name: "Insert column header as first line"
    description: |
      **Box must be checked**

      Stitch's {{ integration.display_name }} integration requires that the first row of every export file be a column header.

  - name: "Encryption/compression"
    description: |
      **Do not encrypt or compress file**

      Stitch's {{ integration.display_name }} does not currently support replicating encrypted or compressed files.

  - name: "Additional ready file at completion of download"
    description: |
      Select **Create file with record count**.

      In the **File extension** field, enter `ready`


requirements-list:
  - item: |
      **Export files that adhere to [Stitch's requirements](#verify-connect-data-export-file-configuration).** Files that aren't set up correctly may not be replicated successfully, or may cause issues during extraction.


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

setup-steps:
  - title: "Add Stitch's Public Key to your {{ integration.display_name }} SFTP server"
    anchor: "add-stitch-public-key-to-sftp-server"
    content: |
      Stitch uses an SSH tunnel to securely connect to your {{ integration.display_name }} SFTP server. This means that to connect successfully, you'll need to add Stitch's Public Key to your server.

    substeps:
      - title: "Retrieve the Stitch Public Key"
        anchor: "retrieve-stitch-public-key"
        content: |
          1. {{ app.menu-paths.add-integration | flatify }}
          2. Click the **{{ integration.display_name }}** icon.
          3. The Stitch Public Key will be at the top of the page that opens:

             ![The Stitch Public Key in the {{ integration.display_name }} settings page]({{ site.baseurl }}/images/integrations/responsys-public-key.png)

      - title: "Determine your SFTP server hosting"
        anchor: "sftp-server-hosting"
        content: |
          Next, you'll need to add the Public Key to your SFTP server. The steps for doing this depend on how your SFTP server is hosted:

          {% capture oracle-hosted %}
          Contact Oracle and provide them with the Public Key to complete this step.

          {% endcapture %}
          {% include layout/expandable-heading.html title="My server is hosted by Oracle. (This is the default)" content=oracle-hosted anchor="oracle-hosted" %}

          {% capture self-hosted %}
          If your SFTP server is self-hosted, or not hosted by Oracle, you'll need to add the Public Key to the `authorized_keys` file. This will allow Stitch to conntect to the server using a trusted user.

          In this step, you'll create a dedicated SSH user for Stitch and then import the Stitch Public Key into the `authorized_keys` file.

          {% include shared/create-linux-user.html no-notification=true %}

          {% endcapture %}
          {% include layout/expandable-heading.html title="My server is self-hosted." content=self-hosted anchor="self-hosted" %}

          If you skip this step or the Public Key is added incorrectly, the following error will surface when you save the integration in Stitch:

          ```
          "Message from SFTP server: Authentication failed. - Please ensure that the server is configured to accept the public key for this integration."
          ```

  - title: "Verify {{ integration.display_name }} Connect data export configuration"
    anchor: "verify-connect-data-export-file-configuration"
    content: |
      {% include layout/inline_image.html type="right" file="integrations/responsys-data-export-file-settings.png" alt="Connect Data Export Destination Specification page" max-width="450px" %}

      Stitch's {{ integration.display_name }} integration replicates `.csv` or `.txt` files created as part of a [Connect data export job](https://interact2.responsys.net/interact/help/rifh/en/Content/Connect_WizardDownload.htm){:target="new"}. In the {{ integration.display_name }} app, jobs are created and managed in the **Manage Connect** page, accessed via **Data > Connect**.

      File settings are defined in the **Destination Specification** step of the Connect data export process, which can be seen in the image to the right.

      The settings in the **Destination Specification** page must match the required values listed in the table below. This will ensure that data is replicated successfully from {{ integration.display_name }}.

      <table class="attribute-list">
      <tr>
      <td class="attribute-name">
      <strong>Setting in {{ integration.display_name }}</strong>
      </td>
      <td class="attribute-description">
      <strong>Required value</strong>
      </td>
      </tr>
      {% for requirement in integration.file-requirements %}
      <tr>
      <td class="attribute-name">
      <strong>{{ requirement.name }}</strong>
      </td>
      <td class="attribute-description">
      {{ requirement.description | flatify | markdownify }}
      </td>
      </tr>
      {% endfor %}
      </table>

  - title: "add integration"
    content: |
      The info you need to complete the remaining fields depends on how your SFTP server is hosted:

      {% capture fields-for-oracle-hosted %}
      If your server is hosted by Oracle, you can find its connection details in the {{ integration.display_name }} app by navigating to **Data > Connect > Destination Connectivity**. If you have multiple file locations, click the one you want to connect to Stitch.

      {% include layout/inline_image.html type="right" file="integrations/responsys-oracle-hosted-example.png" alt="Oracle-hosted SFTP server connection details" max-width="500px" %}
      The image on the right shows an example of the connection details in {{ integration.display_name }}.

      Fill in the remaining fields in Stitch as follows:

      - **Host**: In Stitch, enter the value from the {{ integration.display_name }} **Server** field. This will likely be `files.responsys.net`
      - **Port**: Leave this as `22`.
      - **Username**: In Stitch, enter the value from the {{ integration.display_name }} **User name** field. In the example, this is `demo_scp`
      - **Path**: In Stitch, enter the value of the {{ integration.display_name }} **Directory path** field, or the file server path where completed {{ integration.display_name }} export files are stored. In the example, this is `download`
      {% endcapture %}
      {% include layout/expandable-heading.html title="My server is hosted by Oracle. (This is the default)" content=fields-for-oracle-hosted anchor="fields-for-oracle-hosted" %}

      {% capture fields-for-self-hosted %}
      If your server is hosted by Oracle, you can find its connection details in the {{ integration.display_name }} app by navigating to **Data > Connect > Destination Connectivity**. If you have multiple file locations, click the one you want to connect to Stitch.

      {% include layout/inline_image.html type="right" file="integrations/responsys-self-hosted-example.png" alt="Self-hosted SFTP server connection details" max-width="500px" %}
      The image on the right shows an example of the connection details in {{ integration.display_name }}.

      Fill in the remaining fields in Stitch as follows:

      - **Host**: Enter the host address (endpoint) used by the SFTP server.
      - **Port**: Enter the SSH port used by the SFTP server. This is usually `22`.
      - **Username**: Enter the name of the user you created in [Step 1.2](#sftp-server-hosting). In the example, this is `stitch_user`
      - **Path**: Enter the file server path where completed {{ integration.display_name }} export files are stored.
      {% endcapture %}
      {% include layout/expandable-heading.html title="My server is self-hosted." content=fields-for-self-hosted anchor="fields-for-self-hosted" %}

  - title: "historical sync"

  - title: "replication frequency"

  - title: "track data"


# -------------------------- #
#      Replication Info      #
# -------------------------- #

replication-sections:
  - content: |
      While data from {{ integration.display_name }} integrations is replicated using [Key-based Incremental Replication]({{ link.replication.key-based-incremental | prepend: site.baseurl }}), the behavior for this integration differs subtly from other integrations.

      The table below compares Key-based Incremental Replication and [Replication Key]({{ link.replication.rep-keys | prepend: site.baseurl }}) behavior for {{ integration.display_name }} to that of other integrations.

      <table class="attribute-list">
      <tr>
      <td>
      </td>
      <td>
      <strong>{{ integration.display_name }}</strong>
      </td>
      <td>
      <strong>Other integrations</strong>
      </td>
      </tr>
      {% for comparison in site.data.taps.extraction.replication-methods.key-based-incremental.database-file-integrations %}
      <tr>
      <td align="right" width="35%; fixed">
      <strong>{{ comparison.item | flatify }}</strong>
      </td>
      <td>
      {{ comparison.this-integration | markdownify }}
      </td>
      <td>
      {{ comparison.other-integrations | markdownify }}
      </td>
      </tr>
      {% endfor %}
      </table>

# -------------------------- #
#         Schema Info        #
# -------------------------- #

other-sections:
  - title: "{{ integration.display_name }} Schema"
    anchor: "schema"
    content: |
      {{ integration.display_name }} tables will contain the same columns that the source files contains. These tables will also contain [common system columns]({{ link.destinations.storage.sdc-columns | prepend: site.baseurl }}), as well as columns specific to {{ integration.display_name }} integrations:

      <table class="attribute-list">
      <tr>
      <td class="attribute-name">
      <strong>{{ system-column.source-file }}</strong>
      </td>
      <td class="attribute-description">
      {{ system-column.source-file-description | replace: "**Applicable only to Responsys integrations**, this column contains t", "T" | markdownify }}
      </td>
      </tr>
      <tr>
      <td class="attribute-name">
      <strong>{{ system-column.source-lineno }}</strong>
      </td>
      <td class="attribute-description">
      {{ system-column.source-lineno-description | replace: "**Applicable only to Responsys integrations**, this column contains t", "T" | markdownify }}
      </td>
      </tr>
      </table>
---
{% assign integration = page %}
{% include misc/data-files.html %}