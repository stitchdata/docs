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

title: Connecting a Google BigQuery (v1) Destination to Stitch
permalink: /destinations/google-bigquery/v1/connecting-google-bigquery-to-stitch

keywords: bigquery, google bigquery data warehouse, bigquery data warehouse, bigquery etl, etl to bigquery, bigquery destination
summary: "Connect a Google BigQuery database to your Stitch account as a destination."

content-type: "destination-setup"
key: "bigquery-setup"

order: 2

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

this-version: "1.0"


# -------------------------- #
#        Requirements        #
# -------------------------- #

requirements:
  - item: |
      **A user with full access to an existing [Google Cloud Platform (GCP) project within {{ destination.display_name }}]({{ site.data.destinations.resource-links[destination.type]setup-project }}){:target="_blank"}**. Stitch won't be able to create one for you.
  - item: |
      **Admin permissions for {{ destination.display_name }} and Google Cloud Storage (GCS)**. This includes the {{ destination.display_name }} Admin and Storage Admin permissions. Stitch requires these permissions to [create and use a GCS bucket](https://cloud.google.com/storage/docs/access-control/bucket-level-iam){:target="_blank"} to load replicated data into {{ destination.display_name }}.
  - item: |
      **Access to a project where [billing is enabled]({{ site.data.destinations.resource-links[destination.type]enable-billing }}){:target="_blank"} and a credit card is attached**. Even if you're using {{ destination.display_name }}'s free trial, billing must still be enabled for Stitch to load data.


# -------------------------- #
#         Instructions       #
# -------------------------- #

steps:
  - title: "Create a GCP account"
    anchor: "create-gcp-account"
    content: |
      [Sign up here]({{ site.data.destinations.resource-links[destination.type]sign-up }}){:target="new"} to get started.

  - title: "Create a GCP project and enable billing"
    anchor: "create-gcp-project-enable-billing"
    content: |
      Next, create a new GCP project to house your {{ destination.display_name }} destination by following [these instructions]({{ site.data.destinations.resource-links[destination.type]setup-project }}){:target="new"}.

      **Be sure to enable billing for the account and attach a credit card, even if you're using the free trial option.** If billing isn't enabled, Stitch will encounter issues when loading data into your data warehouse.

  - title: "Grant user permissions"
    anchor: "grant-user-permissions"
    content: |
      {% include note.html type="single-line" content="**Note**: Granting permissions to a user in Google Cloud Platform requires the `resourcemanager.projects.setIamPolicy` privilege." %}
      
      {% include layout/inline_image.html type="right" file="destinations/bigquery-dashboard-project-info.png" alt="The project Info box on the GCP Platform Dashboard page." max-width="300px" %}After the project has been created, open the project in the GCP console. You can do this by either:

      - Clicking **Go to project settings** in the **Project Info** box on the dashboard page, as seen to the right.

      - Toggling between Projects by clicking the drop-down menu next to the Google Cloud Platform logo in the upper-left corner.

      Then, follow the instructions in the tab below. **Note**: Even if the user has Owner permissions, the permissions outlined below must still be granted to the user. Stitch will encounter loading errors otherwise.

      {% include destinations/templates/destination-user-setup.html %}

  - title: "Authenticate with Google"
    anchor: "authenticate-with-google"
    content: |
      Next, you'll complete Google's authorization process and grant Stitch access to the {{ destination.display_name }} project you created in [Step 2](#create-gcp-project-enable-billing).

      1. Sign into your Stitch account, if you haven't already.
      2. Click the {{ app.menu-paths.destination-settings }}, then the **{{ destination.display_name }}** icon.
      3. Click **Sign in with Google.**
      4. If you aren't already signed into your Google account, you'll be prompted for your credentials. **Sign in as the same user you granted {{ destination.display_name }} and Storage Admin permissions to in [Step 3](#grant-user-permissions).**
      5. After you sign in, you'll see a list of the permissions requested by Stitch:
         - **Read/Write Access to Google Cloud Storage** - Stitch requires Read/Write access to create and use a GCS bucket to load replicated data into BigQuery.
         - **Full Access to BigQuery** - Stitch requires full access to be able to create datasets and load data into BigQuery.
         - **Read-Only Access to Projects** - Stitch requires read-only access to projects to allow you to select a project to use during the BigQuery setup process.
         - **Basic Profile Information** - Stitch uses your basic profile info to retrieve your user ID.
         - **Offline Access** - To continuously load data, Stitch requires offline access. This allows the authorization token generated during setup process to be used for more than an hour after the initial authentication takes place.
      6. To grant access, click the **Authorize** button.

  - title: "Select a Google Cloud Project and Storage Location"
    anchor: "select-gcp-project-storage-location"
    content: |
      After you sign into Google and grant Stitch access, you'll be redirected back to Stitch. The last step is to select the select a project and define a storage location for your destination.

      Fill in the fields as follows:
     
      1. From the **Google Cloud Project** dropdown, select the project you created in [Step 2](#create-gcp-project-enable-billing).

      2. From the **Google Cloud Storage Location**, select the location where data should be stored:

         {% for region in site.data.destinations.reference.bigquery.v1.region-list %}
         - {{ region.name | markdownify }}
         {% endfor %}
      3. Click **Finish Setup**.
---
{% include misc/data-files.html %}
{% assign destination = page %}