---
title: Panoply Connection Issues
keywords: troubleshooting, destination, trouble, issue, help, error, errors, panoply
permalink: /troubleshooting/destinations/panoply-connection-issues
tags: [troubleshooting_destinations, troubleshooting_errors]

summary: "If you’re having trouble with setting up or connecting to your Panoply data warehouse in Stitch, try these troubleshooting steps before reaching out to support."
type: "panoply-destination, connection, error"
category: "connection-errors"
promote: "false"
---
{% include misc/data-files.html %}

{{ page.summary }}

---

## Invalid Panoply Credentials

If you’ve recently reset your password in Panoply, you’ll also need to update it in Stitch. Try entering your new password in the **{{ app.page-names.dw-settings }}** page to see if this resolves any invalid credentials / connection failure errors.

1. On the {{ app.page-names.dashboard }} page, click the {{ app.menu-paths.destination-settings }}.
2. Click the **Set a New Password** link under the **Password** field.
3. Enter your new Panoply password.
4. Click the {{ app.buttons.update-dw-settings | flatify }} button.

---

## Contact Support

If you’re still running into problems with Panoply in Stitch, reach out to [Stitch support](mailto:{{ site.support }}).

If you’re experiencing issues inside of Panoply, [reach out to Panoply support](https://panoply.io){:target="new"}.