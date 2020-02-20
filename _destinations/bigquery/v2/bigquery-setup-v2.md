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

permalink: /destinations/google-bigquery/v2/connecting-google-bigquery-to-stitch
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

display_name: "Google BigQuery"
name: "google-bigquery"

type: "bigquery"

ssh: false
ssl: false

this-version: "2"


# -------------------------- #
#        Introduction        #
# -------------------------- #

intro: |
  {% capture migration-callout %}
  **{{ destination.display_name }} v1 migration**: If migrating from {{ destination.display_name }} v1, there are additional steps that must be completed. Refer to the [Migrating from {{ destination.display_name }} v1 guide]({{ link.destinations.setup.bigquery-v1-migration | prepend: site.baseurl }}) for instructions.
  {% endcapture %}

  {% include important.html type="single-line" content=migration-callout %}


# -------------------------- #
#        Requirements        #
# -------------------------- #

requirements:
  - item: |
      **An existing Google Cloud Platform (GCP) project with the following setup:**

      - **Enabled billing for the GCP project**. The project must have [billing enabled and an attached credit card]({{ site.data.destinations.bigquery.resource-links.enable-billing }}). This is required for Stitch to successfully load data.

      - **An existing {{ destination.display_name }} instance in the GCP project.** Stitch will not create an instance for you.

  - item: |
      **Permissions in the GCP project that allow you to create Identity Access Management (IAM) service accounts.** Stitch uses a service account during the replication process to load data into {{ destination.display_name }}. Refer to [Google's documentation]({{ site.data.destinations.bigquery.resource-links.service-accounts }}){:target="new"} for more info about service accounts and the permissions required to create them.


# -------------------------- #
#         Instructions       #
# -------------------------- #

steps:
  - title: "Create a GCP IAM service account"
    anchor: "create-gcp-iam-service-account"
    content: |
      {% for substep in step.substeps %}
      - [Step 1.{{ forloop.index }}: {{ substep.title }}](#{{ substep.anchor }})
      {% endfor %}

    substeps:
      - title: "Define the service account details"
        anchor: "define-service-account-details"
        content: |
          {% include destinations/google-bigquery/create-iam-service-account.html type="define-service-account-details" %}

      - title: "Assign BigQuery Admin permissions"
        anchor: "assign-bigquery-admin-permissions"
        content: |
          {% include destinations/google-bigquery/create-iam-service-account.html type="assign-bq-admin" %}

      - title: "Create a JSON project key"
        anchor: "create-json-project-key"
        content: |
          {% include destinations/google-bigquery/create-iam-service-account.html type="create-json-project-key" %}

  - title: "Connect Stitch"
    anchor: "connect-stitch"
    content: |
      To complete the setup, you'll upload the GCP project key file to Stitch and define settings for your {{ destination.display_name }} destination:

      {% for substep in step.substeps %}
      - [Step 2.{{ forloop.index }}: {{ substep.title }}](#{{ substep.anchor }})
      {% endfor %}

    substeps:
      - title: "Upload the JSON project key file to Stitch"
        anchor: "upload-json-project-key-file"
        content: |
          {% include destinations/google-bigquery/define-stitch-settings.html type="upload-project-file" %}

      - title: "Select a Google Storage Location"
        anchor: "select-gcp-storage-location"
        content: |
          {% include destinations/google-bigquery/define-stitch-settings.html type="select-gcs-location" %}

      - title: "Define loading behavior"
        anchor: "define-loading-behavior"
        content: |
          {% include destinations/google-bigquery/define-stitch-settings.html type="define-loading-behavior" %}

      - title: "Save the destination"
        anchor: "save-destination"
        content: |
          {% include shared/database-connection-settings.html type="finish-up" %}
---
{% include misc/data-files.html %}
{% assign destination = page %}