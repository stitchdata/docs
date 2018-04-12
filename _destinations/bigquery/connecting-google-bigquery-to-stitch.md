---
title: Connecting a Google BigQuery Data Warehouse to Stitch
permalink: /destinations/bigquery/connecting-google-bigquery-to-stitch
tags: [bigquery_destination]
keywords: bigquery, google bigquery data warehouse, bigquery data warehouse, bigquery etl, etl to bigquery, bigquery destination
summary: "Connect a Google BigQuery destination to your Stitch account."
toc: true
layout: destination-setup-guide
display_name: "BigQuery"
type: "bigquery"

# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements-list:
  - item: |
      **To have full access to a GCP project.** Stitch requires this permission to create datasets and load data into BigQuery.
  - item: |
      **Admin permissions to a BigQuery instance that:**

      - **Is based in the United States (US).** Currently, Stitch can only create US-based Google Cloud Storage (GCS) buckets, which are required for the replication process. US-based buckets are only compatible with US-based BigQuery instances.

        This means that instances based in other regions - for example, the EU - will not currently work with Stitch's {{ destination.display_name }} destination. If you're interested in Stitch supporting this feature, [please let us know](mailto:{{ site.support }}).

      - **Has billing info (a credit card) attached to it.** Note that even if you're using BigQuery's free trial option, billing must still be enabled or Stitch will encounter issues with loading data into your data warehouse. [Instructions for setting up and connecting a billing account to a BigQuery instance can be found here.]({{ destination.enable-billing }}){:target="_blank"}
  - item: |
      **Storage Admin permissions for GCS**. Stitch requires these permissions to [create and use a GCS bucket](https://cloud.google.com/storage/docs/access-control/bucket-level-iam){:target="_blank"} to load replicated data into BigQuery.

# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

setup-steps:
  - title: "Create a GCP Account"
    anchor: "create-gcp-account"
    content: |
      This one's easy. Simply [sign up here]({{ destination.sign-up }}) and you'll receive a $300 credit.

  - title: "Create a GCP Project & Enable Billing"
    anchor: "create-gcp-project-enable-billing"
    content: |
      Next, create a new Project to house your BigQuery data warehouse by following [these instructions]({{ destination.setup-project }}).

      **Be sure to enable billing for the account, even if you're using the free trial option.** If billing isn't enabled, Stitch will encounter issues when loading data into your data warehouse.

  - title: "Grant User Permissions"
    anchor: "grant-user-permissions"
    content: |
      {% include layout/inline_image.html type="right" file="destinations/bigquery-dashboard-project-info.png" alt="The Project Info box on the GCP Platform Dashboard page." max-width="250px" %}After the Project has been created, **open the Project in the GCP console**. You can do this by either:

      - Clicking **Manage Project Settings** in the **Project Info** box on the dashboard page, as seen to the right.

      - Toggling between Projects by clicking the drop-down menu next to the Google Cloud Platform logo in the upper-left corner.

      {% include layout/inline_image.html type="right" file="destinations/bigquery-user-permissions.gif" alt="Assigning BigQuery Admin & Storage Admin permissions to a GCP user." max-width="425px" %}

      In the page that displays, click the **IAM** option in the menu on the left side of the page. This will display a page of all the members that have access to the Project.

      1. In the list, locate the user you want to use to connect BigQuery to Stitch.
      2. Click the **Role(s)** drop-down in the row for that user.
      3. Select the **BigQuery** option and click **BigQuery Admin**.
      4. Next, select the **Storage** option and click **Storage Admin**.
      5. Click **Save.**

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
         - **Offline Access** - To continuously load data, Stitch requires offline access. This is so the authorization token generated during setup process can be used for more than an hour after the initial auth.
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
