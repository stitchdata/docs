---
title: "Updated feature: Post-Load Webhooks API change"
content-type: "changelog-entry"
date: 2021-08-09
entry-type: "updated-feature"
entry-category: "app, connect-api"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

The Stitch Connect API and Application now require that you have a destination to create a post-load webhook.

In the Stitch Connect API, you now need to provide a **Destination ID** in the `POST` body. The `destination_id` parameter value should be the destination that will trigger the webhook. For more information, take a look at our docs on [how to create a post-load webhook]({{ link.connect.api | prepend: site.baseurl | append: "#create-hook-notification" }}).

Use one of the following ways to find your Destination ID:

**via the Connect API:**
Call `GET /v4/destinations`

**via the Web Application:**
1. Log into your Stitch account.
2. Navigate to **Destinations**.
3. Your ID is part of the web URL. Look for `/v2/destinations/<destination_id>/edit`.

If you need additional help retrieving your Destination ID, please reach out to Stitch Support.