---
title: Change the Location of a Google BigQuery Destination
permalink: /destinations/bigquery/changing-google-bigquery-destination-data-locations
tags: [bigquery_destination]
keywords: bigquery, google bigquery data warehouse, bigquery data warehouse, bigquery etl, etl to bigquery, bigquery destination
summary: "Change the location of your Google BigQuery destination."
toc: true
layout: destination
display_name: "BigQuery"
type: "bigquery"
---
{% assign destination = site.destinations | where:"type","bigquery" | first %}
{% assign page-settings = site.data.ui.change-destinations-page %}
{% include misc/data-files.html %}

{% capture only-for-existing-destinations %}
This guide is only for changing **existing** {{ destination.display_name }} destinations, or those already connected to Stitch. To connect a new {{ destination.display_name }} destination, [refer to these instructions]({{ link.destinations.setup.bigquery | prepend: site.baseurl }}).
{% endcapture %}


{% include important.html content=only-for-existing-destinations %}

Need to change the location in which {{ destination.display_name }} stores your data? Using Stitch's Destination Change feature, you can delete the current destination and connect a new one with the desired data storage location.

---

## Considerations

Here's what you need to know to ensure a smooth switch:

- **Your integrations will be paused.** After the switch is complete, you'll need to manually unpause the integrations you'd like to resume.

- **Some webhook data may be lost during this process**. Due to their continuous, real-time nature, some webhook data may be lost during the switch.

- **Historical data from webhook-based integrations must be either manually backfilled or replayed**. Some webhook providers - such as Segment - allow customers on certain plans to ‘replay’ their historical data. This feature varies from provider to provider and may not always be available.

   If you don’t have the ability to replay historical webhook data, then it must be manually backfilled after the switch is complete.

- **We won’t delete or transfer any data from your current {{ destination.display_name }} destination**. Depending on your needs, how historical data is imported into the new instance may vary. See the next section for details.

---

## Step 1: Select a historical data setting {#select-historical-data-setting}

If you need historical data in the new destination, you’ll need to either manually transfer your historical data or queue a historical replication job.

- **Manually transfer historical data**: To accomplish this, you can use Google's UI to import the existing datasets into the new {{ destination.display_name }} instance. Ensure that all dataset names remain the same during the transfer, or loading errors may occur.

   **Complete the historical transfer before continuing.**

- **Queue a historical replication job**: Initializing a historical replication will re-replicate all historical data from your integrations. For SaaS integrations, Stitch will replicate data beginning with the **Start Date** currently in the integration's settings.

### Define the setting

1. From the {{ app.page-names.dashboard }}, click the {{ app.menu-paths.destination-settings }}.
2. At the bottom of the page, click the {{ app.buttons.change-destination }} button.
3. In the **Historical Data** section, select how you want data to be replicated to the new destination: 
   {% for field in page-settings.bigquery-historical-data %}
   - {{ field.field }}: {{ field.copy | flatify }}
   {% endfor %}

---

## Step 2: Delete the current destination {#delete-current-bigquery-destination}

1. Click **Continue**. A message will display asking you to confirm the removal of the current destination's settings.
2. To complete the switch, Stitch must delete your current destination configuration. **Note**: This will not delete data in the destination itself - it only clears this destination's settings from Stitch.

   To continue with the switch, click **OK** to delete the current destination settings.

---

## Step 3: Connect the new {{ destination.display_name }} destination {#connect-new-bigquery-destination}

{% capture permissions %}
**Requirements for connecting {{ destination.display_name }}**<br><br>

1. **A user with full access to an existing [Google Cloud Platform (GCP) project within {{ destination.display_name }}]({{ destination.setup-project }}){:target="_blank"}**.<br>

2. **Admin permissions for BigQuery and Google Cloud Storage (GCS)**. This includes the BigQuery Admin and Storage Admin permissions. Stitch requires these permissions to [create and use a GCS bucket](https://cloud.google.com/storage/docs/access-control/bucket-level-iam){:target="_blank"} to load replicated data into BigQuery.<br>

3. **Access to a project where [billing is enabled]({{ destination.enable-billing }}){:target="_blank"} and a credit card is attached**. Even if you're using BigQuery's free trial, billing must still be enabled for Stitch to load data.
{% endcapture %}

{% include important.html content=permissions %}

1. On the next page in Stitch, click the **{{ destination.display_name }}** icon.
2. Click **Sign in with Google**.
3. If you aren't already signed into your Google account, you'll be prompted for your credentials.
4. After you sign in, you'll see a list of the permissions requested by Stitch:
     - **Read/Write Access to Google Cloud Storage** - Stitch requires Read/Write access to create and use a GCS bucket to load replicated data into BigQuery.
     - **Full Access to BigQuery** - Stitch requires full access to be able to create datasets and load data into BigQuery.
     - **Read-Only Access to Projects** - Stitch requires read-only access to projects to allow you to select a project to use during the BigQuery setup process.
     - **Basic Profile Information** - Stitch uses your basic profile info to retrieve your user ID.
     - **Offline Access** - To continuously load data, Stitch requires offline access. This allows the authorization token generated during setup process to be used for more than an hour after the initial authentication takes place.
5. To grant access, click the **Authorize** button.
6. After you sign into Google and grant Stitch access, you'll be redirected back to Stitch.
   Fill in the fields that display:
      - **Google Cloud Project**: From the dropdown, select the project you want to connect to Stitch.
      - **Google Cloud Storage Location**: From the dropdown, select the new location you want to use.
7. Click **Finish Setup**.

---

## Step 4: Delete the existing Google Cloud Storage bucket {#delete-current-bucket}

To ensure Stitch can load data into the new BigQuery instance, you'll need to delete the Google Cloud Storage (GCS) bucket that's attached to the project.

{% include important.html content="Before completing this step, verify that all data you want to retain has been transferred. Google permanently deletes objects within buckets, and they cannot be recovered after this process completes." %}

1. In another browser tab, [log into the Google console](https://console.cloud.google.com/).
2. Use [Google's instructions](https://cloud.google.com/storage/docs/deleting-buckets) to locate the bucket in Google's UI.
3. Locate the Stitch bucket, which is named `com-stitchdata-staging-[xxxxxx]`.
4. Delete the bucket.

---

## Step 5: Unpause integrations {#unpause-integrations}

After you've successfully connected the new {{ destination.display_name }} destination and deleted the original Stitch GCS bucket, un-pause your integrations in Stitch.

Your data will begin replicating according to the historical data option selected in [Step 1](#select-historical-data-setting).