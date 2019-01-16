---
title: Connecting a Google BigQuery Data Warehouse to Stitch
permalink: /destinations/bigquery/connecting-google-bigquery-to-stitch
tags: [bigquery_destination]
keywords: bigquery, google bigquery data warehouse, bigquery data warehouse, bigquery etl, etl to bigquery, bigquery destination
summary: "Connect a Google BigQuery destination to your Stitch account."

content-type: "destination-setup"

toc: true
layout: destination-setup-guide
display_name: "BigQuery"
type: "bigquery"

# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements-list:
  - item: |
      **A user with full access to an existing [Google Cloud Platform (GCP) project within {{ destination.display_name }}]({{ destination.setup-project }}){:target="_blank"}**. Stitch won't be able to create one for you.
  - item: |
      **Admin permissions for BigQuery and Google Cloud Storage (GCS)**. This includes the BigQuery Admin and Storage Admin permissions. Stitch requires these permissions to [create and use a GCS bucket](https://cloud.google.com/storage/docs/access-control/bucket-level-iam){:target="_blank"} to load replicated data into BigQuery.
  - item: |
      **Access to a project where [billing is enabled]({{ destination.enable-billing }}){:target="_blank"} and a credit card is attached**. Even if you're using BigQuery's free trial, billing must still be enabled for Stitch to load data.

# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

setup-steps:
  - title: "Create a GCP account"
    anchor: "create-gcp-account"
    content: |
      This one's easy. Simply [sign up here]({{ destination.sign-up }}) and you'll receive a $300 credit.

  - title: "Create a GCP project and enable billing"
    anchor: "create-gcp-project-enable-billing"
    content: |
      Next, create a new GCP project to house your BigQuery data warehouse by following [these instructions]({{ destination.setup-project }}).

      **Be sure to enable billing for the account and attach a credit card, even if you're using the free trial option.** If billing isn't enabled, Stitch will encounter issues when loading data into your data warehouse.

  - title: "Grant user permissions"
    anchor: "grant-user-permissions"
    content: |
      {% include layout/inline_image.html type="right" file="destinations/bigquery-dashboard-project-info.png" alt="The project Info box on the GCP Platform Dashboard page." max-width="250px" %}After the project has been created, open the project in the GCP console. You can do this by either:

      - Clicking **Manage Project Settings** in the **Project Info** box on the dashboard page, as seen to the right.

      - Toggling between Projects by clicking the drop-down menu next to the Google Cloud Platform logo in the upper-left corner.

      Then, follow the instructions in the tab below. **Note**: Even if the user has Owner permissions, the permissions outlined below must still be granted to the user. Stitch will encounter loading errors otherwise.

      {% include destinations/templates/destination-user-setup.html %}

  - title: "Authenticate with Google"
    anchor: "authenticate-with-google"
    content: |
      The last step is to complete Google's authorization process and grant Stitch access to the BigQuery project you created in Step 2.

      1. Sign into your Stitch account, if you haven't already.
      2. Click the {{ app.menu-paths.destination-settings }}, then the **{{ destination.display_name }}** icon.
      3. Click **Sign in with Google.**
      4. If you aren't already signed into your Google account, you'll be prompted for your credentials. **Sign in as the same user you granted BigQuery and Storage Admin permissions to in [Step 3](#grant-user-permissions).**
      5. After you sign in, you'll see a list of the permissions requested by Stitch:
         - **Read/Write Access to Google Cloud Storage** - Stitch requires Read/Write access to create and use a GCS bucket to load replicated data into BigQuery.
         - **Full Access to BigQuery** - Stitch requires full access to be able to create datasets and load data into BigQuery.
         - **Read-Only Access to Projects** - Stitch requires read-only access to projects to allow you to select a project to use during the BigQuery setup process.
         - **Basic Profile Information** - Stitch uses your basic profile info to retrieve your user ID.
         - **Offline Access** - To continuously load data, Stitch requires offline access. This allows the authorization token generated during setup process to be used for more than an hour after the initial authentication takes place.
      6. To grant access, click the **Authorize** button.
      7. After you sign into Google and grant Stitch access, you'll be redirected back to Stitch.
         Fill in the fields that display: 
            - **Google Cloud Project**: From the dropdown, select the project you created in [Step 2](#create-gcp-project-enable-billing).
            - **Google Cloud Storage Location**: From the dropdown, select the location where data should be stored:
                - **US**: Data will be stored in the United States
                - **EU**: Data will be stored in Europe
      8. Click **Finish Setup**.
---
{% include misc/data-files.html %}
{% assign destination = site.destinations | where:"type","bigquery" | first %}

{{ destination.description }}

For detailed info on how Stitch works with BigQuery, check out the [Stitch Google BigQuery Destination Overview]({{ link.destinations.overviews.bigquery | prepend: site.baseurl }}).