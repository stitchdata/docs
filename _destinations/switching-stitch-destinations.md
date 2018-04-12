---
title: Changing Stitch Destinations
tags: [destinations]
keywords: destinations, compatibility, switch destination, switch redshift, switch, change redshift, change bigquery, change postgresql, change destination
permalink: /destinations/switching-destinations
summary: "In this guide, we'll show you how to change your Stitch destination."

toc: true
type: "all"
destination: "false"
---
{% assign page-settings = site.data.ui.change-destinations-page %}
{% include misc/data-files.html %}

Sometimes, you may want to replicate data to a different location than what you initially connected to Stitch. 

For example: you now want to replicate data from your integrations to a different database in your Redshift cluster, or you simply decide that Redshift isn't the data warehouse for you.

---

## Prerequisites

The only prerequisite to changing destinations is that the **new** destination is ready to be connected to Stitch. This will minimize any downtime you may experience.

If you need a refresher on how to spin up a destination for Stitch, check out the [destination setup guides]({{ site.baseurl }}/destinations#current-destinations).

---

## Considerations

Here's what you need to know to ensure a smooth switch:

- **Some destinations may structure data differently than your current destination.** For example: if you're changing from Redshift to BigQuery, there will be some differences in how your data is stored. Detailed info about how Stitch loads data can be found in the [Data Loading Guide]({{ link.destinations.storage.loading-data | prepend: site.baseurl }}) for each destination.

- **Your integrations will be paused.** After the switch is complete, you’ll need to manually unpause the integrations you’d like to resume.

- **We won’t delete or transfer any data from your current destination.** To get historical data into your new destination, you'll need to queue a full re-sync of all your integrations. 

   Re-syncing historical data will count towards your row usage and may take some time, depending on the volume of data and API limitations imposed by the provider.

- **Some webhook data may be lost during this process.** Due to their continuous, real-time nature, some webhook data may be lost during the switch.

- **Historical data from webhook-based integrations must be either manually backfilled or replayed.** Some webhook providers - such as Segment - allow customers on certain plans to 'replay' their historical data. This feature varies from provider to provider and may not always be available.

   If you don't have the ability to replay historical webhook data, then it must be manually backfilled after the switch is complete.

---

## Switch Destinations

1. From the {{ app.page-names.dashboard }}, click the {{ app.menu-paths.destination-settings }}.
2. At the bottom of the page, click the {{ app.buttons.change-destination }} button.
3. In the **Historical Data** section, select how you want data to be replicated to the new destination:
   {% for field in page-settings.default-historical-data %}
   - {{ field.field }}: {{ field.copy | flatify }}
   {% endfor %}
4. Click **Continue**. A message will display asking you to confirm the removal of the current destination's settings.
5. To complete the switch, Stitch must delete your current destination configuration. **Note**: This will not delete data in the destination itself - it only clears this destination's settings from Stitch.

   To continue with the switch, click **OK** to delete the current destination settings.
6. On the next page, click the icon of the destination type you want to switch to.
7. Follow the instructions for that destination type to complete the setup. If you need some help, refer to the destination's setup guide:
   {% for destination in site.destinations %}
   {% if destination.destination == true %}
   - [{{ destination.display_name }} Setup]({{ destination.url | prepend: site.baseurl | append:"#setup" }})
   {% endif %}
   {% endfor %}
8. After you've successfully connected the new destination, un-pause your integrations. Your data will begin replicating according to the historical data option selected in Step 3.

---

## Troubleshooting

If you encounter connection issues, check out the [Destination Connection Errors guide]({{ link.troubleshooting.dw-connection-errors | prepend: site.baseurl }}) for common problems and solutions.
