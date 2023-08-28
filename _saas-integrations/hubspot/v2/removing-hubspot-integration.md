---
title: Removing the HubSpot integration
keywords: hubspot, integration, schema, etl hubspot, hubspot etl
permalink: /integrations/saas/hubspot/removing-hubspot-integration
summary: "Instructions on how to delete your {{ page.display_name }} integration in Stitch and uninstall Stitch in the HubSpot platform."
input: false

layout: general
toc: false
content-type: "guide"

name: "hubspot"
display_name: "HubSpot"

this-version: "2"

intro: |
  {% include misc/data-files.html %}

  To completely disconnect Stitch from your {{ page.display_name }} account, you need to delete the integration from Stitch, and uninstall the Stitch app from {{ page.display_name }}.
  
  Disconnecting {{ page.display_name }} from Stitch will stop the replication of {{ page.display_name }} data to your Stitch destination. There will be no impact to the {{ page.display_name }} data, as Stitch is a read-only integration with {{ page.display_name }}. All data that has already replicated to your Stitch destination will be maintained and under your control.


sections:
  - title: "Deleting your {{ page.display_name }} integration"
    anchor: "delete-hubspot-integration"
    content: |
      To delete your {{ page.display_name }} integration from your Stitch account:
      1. Log in to your Stitch account and open the **Integrations** tab.
      2. Click your HubSpot integration and click **Settings**.
      3. Scroll down to the bottom of the page and click **Delete**.
      4. Click **Delete** to confirm.

  - title: "Uninstalling Stitch in your {{ page.display_name }} account"
    anchor: "uninstall-stitch-in-hubspot"
    content: |
      To uninstall Stitch in your {{ page.display_name }} account:
      1. Log in to your {{ page.display_name }} account and click the **Marketplaces** account in the navigation bar.
      2. Under **Manage**, click **Connected apps**.
      3. Click the **Actions** drop-down menu in the **Stitch** app, and click **Uninstall**.
      4. In the dialog box that appears, enter `uninstall` in the text field and click **Uninstall** to confirm."
---