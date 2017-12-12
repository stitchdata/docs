---
title: SaaS Integration Connection Errors
keywords: troubleshooting, connection issue, connection error, trouble, saas integration
tags: [troubleshooting_integrations, troubleshooting_errors]

permalink: /troubleshooting/integrations/saas-integration-connection-errors
redirect_from: /troubleshooting/integrations/integration-connection-errors
## Some users may experience a blip while the redirect works - it's normal. 

summary: "If Stitch is unable to connect to one of your SaaS integrations, the issue may be a security setting on the integration provider's side."
type: "saas-integrations, connection, error"
---
{% include misc/data-files.html %}

> We're unable to connect to your [name] integration. Please verify that our IP is whitelisted and we're not blocked by a firewall.

If you've received the above error for a SaaS integration, the issue may be a security setting on the integration provider's side.

{% capture db-connection-errors %}
**Need help troubleshooting connection issues for a database integration?** [Click here]({{ link.troubleshooting.db-connection-errors | prepend: site.baseurl }}).
{% endcapture %}

{% include tip.html content=db-connection-errors %}

---

## Verify Integration Whitelist Settings

Some SaaS integrations offer an IP restriction feature that restricts access only to the IP addresses that are whitelisted, or given access.

If you're having connection issues with one of the following SaaS integrations, IP restriction may be enabled. If this is the case, you'll need to whitelist Stitch's IP addresses to ensure the connection is successful.

**Click the links below to view instructions specific to that integration**.

{% include integrations/saas/saas-integrations-whitelisting.html %}

---

## Check for Reported Issues

If the troubleshooting steps detailed above don’t resolve the issue or if the errors persist, we recommend checking for reported issues:

1. **On the SaaS integration provider's Status Page**. All the SaaS integrations that have Status Pages can be found here: [Third-Party Downtime]({{ link.troubleshooting.third-party-downtime | prepend: site.baseurl }}).
2. **On Stitch's Status Page**, which can be found here: [Stitch Status Page]({{ site.status }}).

---

## Contact Support

If the errors persist even after you've checked the integration's whitelist settings and no issues have been reported, please reach out to support for assistance.