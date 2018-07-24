---
title: Connecting a data.world Data Warehouse to Stitch
permalink: /destinations/data-world/connecting-a-data-world-data-warehouse-to-stitch
keywords: data-world, data-world, data-world data warehouse, etl to s3, s3 etl, data-world etl, amazon s3
summary: "Connect your data.world destination to Stitch."
toc: true
layout: destination-setup-guide

display_name: "data.world"
type: "data-world"
---
{% include misc/data-files.html %}
{% assign destination = site.destinations | where:"type",page.type | first %}

{% capture account-management %}
Stitch is not involved with the management of {{ destination.display_name }} data warehouses. If you have billing questions or need help regarding your {{ destination.display_name }} data warehouse, [reach out to {{ destination.display_name }}]({{ destination.documentation }}).
{% endcapture %}

{% include note.html first-line="**data.world account management**" content=account-management %}

{{ destination.description | flatify }} With just a few clicks, you can connect your {{ destination.display_name }} account to Stitch and get the data flowing.

1. Click the {{ app.menu-paths.destination-settings }}.
2. Click the **{{ destination.display_name }}** icon.
3. Click the **Sign in with {{ destination.display_name }}** button.
4. At the prompt, sign into your {{ destination.display_name }} account.
5. Next, you'll be asked to authorize Stitch to access your {{ destination.display_name }} account. Stitch will request permission to perform the following:
   - **Access your profile information**: This is required to identify and connect to your account.
   - **Read datasets and projects**: This is required to load replicated data into your destination.
   - **Write to datasets and projects**: This is required to load replicated data into your destination.
6. Click **Authorize Stitch**.
7. After the authorization process is successfully completed, you'll be directed back to Stitch to verify your {{ destination.display_name }} account ID.

   Stitch will use your {{ destination.display_name }} Account ID by default, but you can use a different ID if desired. For example: For a user named `stitch-data-world`, Stitch would default to using `stitch-data-world` as the Account ID.

   To use a different ID, click the link and enter the ID in the **Use This Account ID** field:

   ![Changing the data.world Account ID in Stitch]({{ site.baseurl }}/images/destinations/data-world-s3-change-account-id.gif)
8. When finished, click **Save Settings** to save and test the connection.