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

title: Migrating from a Google BigQuery v1 destination to Google BigQuery v2
keywords: bigquery, google bigquery data warehouse, bigquery data warehouse, bigquery etl, etl to bigquery, bigquery destination
summary: "Migrate from using Stitch's Google BigQuery v1 destination to the new version, v2."

permalink: /destinations/google-bigquery/v2/migrating-from-google-bigquery-v1

content-type: "destination-setup"
key: "bigquery-v1-migration"

order: 1

toc: true
layout: general


# -------------------------- #
#     Destination Details    #
# -------------------------- #

display_name: "Google BigQuery"
name: "google-bigquery"

type: "bigquery"

this-version: "2"


# -------------------------- #
#        Introduction        #
# -------------------------- #

intro: |
  {% capture migration-callout %}
  **Important**: This guide is applicable if:

  1. You're migrating from an existing {{ destination.display_name }} v1 destination to v2 in the same Stitch account
  2. You previously used your {{ destination.display_name }} instance as a Stitch destination and it contains integration datasets (schemas). This instance may have been connected to your current account or a previous account. 

  If you're new to Stitch or haven't used Stitch's {{ destination.display_name }} destination before, refer to the [Connecting a {{ destination.display_name }} v2 destination guide]({{ link.destinations.setup.bigquery-v2 | prepend: site.baseurl }}).
  {% endcapture %}

  {% include important.html content=migration-callout %}


# -------------------------- #
#        Requirements        #
# -------------------------- #

requirements:
  - item: |
      **An existing Google Cloud Platform (GCP) project with the following setup:**

      - **Enabled billing for the GCP project**. The project must have [billing enabled and an attached credit card]({{ site.data.destinations.bigquery.resource-links.enable-billing }}). This is required for Stitch to successfully load data.

      - **An existing Google {{ destination.display_name }} instance in the GCP project.** Stitch will not create an instance for you.

  - item: |
      **Permissions in the GCP project that allow you to create Identity Access Management (IAM) service accounts.** Stitch uses a service account during the replication process to load data into {{ destination.display_name }}. Refer to [Google's documentation]({{ site.data.destinations.bigquery.resource-links.service-accounts }}){:target="new"} for more info about service accounts and the permissions required to create them.


# -------------------------- #
#         Instructions       #
# -------------------------- #

sections:
  - title: "Considerations"
    anchor: "considerations"
    content: |
      {% include destinations/switching-destination-steps.html type="considerations" %}

  - title: "Step 1: Delete your existing {{ destination.display_name }} destination in Stitch"
    anchor: "delete-existing-destination"
    content: |
      In this step, you'll delete the current {{ destination.display_name }} v1 destination configuration in Stitch:

      {% for subsection in section.subsections %}
      - [{{ subsection.title | flatify }}](#{{ subsection.anchor }})
      {% endfor %}
    subsections:
      - title: "Step 1.1: Select a historical data setting"
        anchor: "select-historical-data-setting"
        content: |
          {% include destinations/switching-destination-steps.html type="select-historical-data-setting" %}

      - title: "Step 1.2: Delete the existing {{ page.display_name }} destination in Stitch"
        anchor: "delete-current-destination"
        content: |
          {% include destinations/switching-destination-steps.html type="delete-current-destination" %}

  - title: "Step 2: Delete existing Stitch integration datasets in {{ page.display_name }}"
    anchor: "delete-existing-integration-datasets"
    content: |
      {% include important.html type="single-line" content="This step must be completed before you connect the new destination in Stitch or replication issues will occur." %}

      Next, you'll need to prep your {{ destination.display_name }} instance for the migration. To continue replicating data from your existing integrations, you'll need to delete the integration datasets (schemas) and tables in {{ destination.display_name }} and allow Stitch to re-create them using {{ destination.display_name }} v2.

      For example: Using {{ destination.display_name }} v1, data was replicated to an integration dataset named `facebook_ads`. You want to continue replicating data from this integration to the `facebook_ads` dataset. To do so, you need to delete the entire `facebook_ads` dataset and allow Stitch to re-create it using {{ destination.display_name }} v2. This is to ensure data is loaded correctly.

      **Note**: This must be completed for every integration dataset created using a {{ destination.display_name }} v1 destination where you want to continue replicating data to the same dataset name. Additionally, this is applicable even if another Stitch account was used with {{ destination.display_name }} v1. If not completed, Stitch will encounter issues when attempting to load data.

      **If you want to retain any historical webhook data**, create a backup of the data before deleting datasets from your {{ destination.display_name }} instance. If you have the ability to replay webhook data, you may not need to do this.

      Refer to [Google's documentation]({{ site.data.destinations.bigquery.resource-links.delete-dataset }}){:target="new"} for instructions on deleting datasets.

  - title: "Step 3: Set up {{ destination.display_name }} v2"
    anchor: "set-up-v2-in-stitch"
    content: |
      Next, you'll configure the new {{ destination.display_name }} v2 destination in Stitch:

      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}
    subsections:
      - title: "Step 3.1: Create a GCP IAM service account"
        anchor: "create-gcp-iam-service-account"
        content: |
          {% for sub-subsection in subsection.sub-subsections %}
          - [{{ sub-subsection.title }}](#{{ sub-subsection.anchor }})
          {% endfor %}
        sub-subsections:
          - title: "Step 3.1.1: Define the service account details"
            anchor: "define-service-account-details"
            content: |
              {% include destinations/google-bigquery/create-iam-service-account.html type="define-service-account-details" %}

          - title: "Step 3.1.2: Assign BigQuery Admin permissions"
            anchor: "assign-bigquery-admin-permissions"
            content: |
              {% include destinations/google-bigquery/create-iam-service-account.html type="assign-bq-admin" %}

          - title: "Step 3.1.3: Create a JSON project key"
            anchor: "create-json-project-key"
            content: |
              {% include destinations/google-bigquery/create-iam-service-account.html type="create-json-project-key" %}

      - title: "Step 3.2: Connect Stitch"
        anchor: "connect-stitch"
        content: |
          To complete the setup, you'll upload the GCP project key file to Stitch and define settings for your {{ destination.display_name }} destination:

          {% for sub-subsection in subsection.sub-subsections %}
          - [{{ sub-subsection.title }}](#{{ sub-subsection.anchor }})
          {% endfor %}
        sub-subsections:
          - title: "Step 3.2.1: Upload the JSON project key file to Stitch"
            anchor: "upload-json-project-key-file"
            content: |
              {% include destinations/google-bigquery/define-stitch-settings.html type="upload-project-file" version-migration=true %}

          - title: "Step 3.2.2: Select a Google Storage Location"
            anchor: "select-gcp-storage-location"
            content: |
              {% include destinations/google-bigquery/define-stitch-settings.html type="select-gcs-location" %}

          - title: "Step 3.2.3: Define loading behavior"
            anchor: "define-loading-behavior"
            content: |
              {% include destinations/google-bigquery/define-stitch-settings.html type="define-loading-behavior" %}

          - title: "Step 3.2.4: Save the destination"
            anchor: "save-destination"
            content: |
              {% include shared/database-connection-settings.html type="finish-up" %}

  - title: "Step 4: Unpause your integrations"
    anchor: "unpause-your-integrations"
    content: |
      {% include destinations/switching-destination-steps.html type="unpause-integrations" %}
---
{% include misc/data-files.html %}
{% assign destination = page %}