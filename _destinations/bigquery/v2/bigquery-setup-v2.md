---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/destination-templates/destination-setup/
## FOR INSTRUCTIONS & REFERENCE INFO


# -------------------------- #
#        Page Controls       #
# -------------------------- #

title: Connecting a Google BigQuery (v2) Destination to Stitch
keywords: bigquery, google bigquery data warehouse, bigquery data warehouse, bigquery etl, etl to bigquery, bigquery destination
summary: "Connect a Google BigQuery database to your Stitch account as a destination."

permalink:  /destinations/google-bigquery/connecting-google-bigquery-to-stitch
redirect_from: /destinations/bigquery/connecting-google-bigquery-to-stitch

content-type: "destination-setup"
key: "bigquery-setup"

order: 1

toc: true
layout: tutorial
use-tutorial-sidebar: false


# -------------------------- #
#     Destination Details    #
# -------------------------- #

display_name: "BigQuery"
type: "bigquery"

ssh: false
ssl: false

this-version: "2.0"

# -------------------------- #
#        Requirements        #
# -------------------------- #

requirements:
  - item: |
      **An existing Google Cloud Platform (GCP) project with the following setup:**

      - **Enabled billing for the GCP project**. The project must have [billing enabled and an attached credit card]({{ site.data.destinations.resource-links[destination.type]enable-billing }}). This is required for Stitch to successfully load data.

      - **An existing Google {{ destination.display_name }} instance in the GCP project.** Stitch will not create an instance for you.

  - item: |
      **Permissions in the GCP project that allow you to create Identity Access Management (IAM) service accounts.** Stitch uses a service account during the replication process to load data into {{ destination.display_name }}. Refer to [Google's documentation]({{ site.data.destinations.resource-links.bigquery.service-accounts }}){:target="new"} for more info about service accounts and the permissions required to create them.


# -------------------------- #
#         Instructions       #
# -------------------------- #

steps:
  - title: "Create a GCP IAM service account"
    anchor: "create-gcp-iam-service-account"
    content: |
      {% for substep in step.substeps %}
      - [Step 1.{{ forloop.index }}: {{ substep.title }}]({{ substep.anchor }})
      {% endfor %}

    substeps:
      - title: "Define the service account details"
        anchor: "define-service-account-details"
        content: |
          1. Navigate to the [IAM Service Accounts page](https://console.cloud.google.com/iam-admin/serviceaccounts){:target="new"} in the GCP console.
          2. Select the project you want to use by using the project dropdown menu, located near the top left corner of the page:

             ![Highlighted project selection menu in the Google Cloud Platform console]({{ site.baseurl }}/images/destinations/bigquery-gcp-project-menu.png){:style="max-width: 450px;"}
          3. Click **+ Create Service Account**.
          4. On the **Service account details** page, fill in the field as follows:
             - **Service account name**: Enter a name for the service account. For example: `Stitch`
             - **Serivce account description**: Enter a description for the service account. For example: `Loading Stitch data`
          5. Click **Create**.

      - title: "Assign BigQuery Admin permissions"
        anchor: "assign-bigquery-admin-permissions"
        content: |
          Next, you'll assign the {{ destination.display_name }} Admin role to the service account. This is required to successfully load data into {{ destination.display_name }}.

          1. On the **Service account permissions** page, click the **Role** field.
          2. In the window that displays, type `bigquery` into the filter/search field:
             ![The service account role field with BigQuery Admin selected]({{ site.baseurl }}/images/destinations/bigquery-service-account-role.png){:style="max-width: 450px;"}

          3. Select **BigQuery Admin**.
          4. Click **Continue**.

      - title: "Create a JSON project key"
        anchor: "create-json-project-key"
        content: |
          The last step is to create and download a JSON project key. The project key file contains information about the project, which Stitch will use to complete the setup.

          ![]({{ site.baseurl }}/images/destinations/bigquery-create-project-key-file.png){:style="max-width: 350px; margin-left: 15px;" align="right"}
          1. On the **Grant users access to this service account** page, scroll to the **Create key** section.
          2. Click **+ Create Key**.
          3. When prompted, click the **JSON** option.
          4. Click **Create**.
          5. Save the JSON project key file to your computer. The file will be downloaded to the location you specify (if prompted), or the default download location defined for the web browser you're currently using.

  - title: "Connect Stitch"
    anchor: "connect-stitch"
    content: |
      To complete the setup, you'll upload the GCP project key file to Stitch and define settings for your {{ destination.display_name }} destination:

      {% for substep in step.substeps %}
      - [Step 2.{{ forloop.index }}: {{ substep.title }}]({{ substep.anchor }})
      {% endfor %}

    substeps:
      - title: "Upload the JSON project key file"
        anchor: "upload-json-project-key-file"
        content: |
          1. Click the {{ app.menu-paths.destination-settings }}.
          2. Click the **{{ destination.display_name }}** icon.
          3. On the page that opens, scroll to the **Your service account** section.
          4. In the **Your Key File** field, click the [todo- upload icon] and locate the JSON project key file you created in [Step 1.3](#create-json-project-key).
          
          Once uploaded, the **BigQuery Project Name** field will automatically populate with the name of the GCP project in the JSON project key file.

      - title: "Select a Google Storage Location"
        anchor: "select-gcp-storage-location"
        content: |
          Next, you'll select the region used by your Google Cloud Storage (GCS) [todo]. This setting determines the region of the internal [Google Storage Bucket](https://cloud.google.com/storage/docs/key-terms#buckets){:target="new"} Stitch uses during the replication process.

          Using the **Google Cloud Storage Location** dropdown, select your GCS region. Refer to [todo]() for the list of regions this version of the {{ destination.display_name }} destination supports.

          **Note**: Changing this setting will result in replication issues if data migration isn't completed correctly. Refer to [todo]() for more info.

      - title: "Define loading behavior"
        anchor: "define-loading-behavior"
        content: |
          {% capture loading-setting-note %}
          **Note**: The Loading behavior setting can't be changed after the destination is created. To change {{ destination.display_name }} loading behavior, you'll need to [delete and re-create the destination]({{ link.destinations.switch-destinations | prepend: site.baseurl }}).
          {% endcapture %}

          {% include note.html type="single-line" content=loading-setting-note %}

          The last step is to define how Stitch will handle changes to existing records in your {{ destination.display_name }} destination:

          - **Upsert**: Existing rows will be updated with the most recent version of the record from the source. With this option, only the most recent version of a record will exist in {{ destination.display_name }}. 

          - **Append**: Existing rows aren't updated. Newer versions of existing records are added as new rows to the end of tables. With this option, many versions of the record will exist in {{ destination.display_name }}, capturing how a record changed over time.

          [todo - add sentence about costs?] Refer to [todo]() for more info and examples.

      - title: "Save the destination"
        anchor: "save-destination"
        content: |
          {% include shared/database-connection-settings.html type="finish-up" %}
---
{% include misc/data-files.html %}
{% assign destination = page %}