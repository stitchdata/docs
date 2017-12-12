---
title: Missing Tables & Columns
keywords: troubleshooting, integration, trouble, issue, help,
permalink: /troubleshooting/replication/missing-tables-and-columns
tags: [replication]
summary: "If Stitch can't detect databases or tables, you may need to double-check your user's permission settings."

---

> Stitch cannot detect any objects (databases, tables, etc.) at or below this level.

If you receive this message or you can't find an object (database, table, column, etc.), it's typically a **permissions** issue.

---

## Database Integrations
Verify that the Stitch user has all the required permissions as outlined in the **Setup** instructions for the database. Docs for database integrations [can be found here]({{ site.baseurl }}/integrations/databases).

---

## SaaS Integrations

Some SaaS integrations - like [Salesforce]({{ site.baseurl }}/integrations/saas/salesforce) and [Facebook Ads]({{ site.baseurl }}/integrations/saas/facebook-ads) - allow specific permissions to be granted to users. **Stitch will only be able to detect and replicate the objects that the user who authorized (created) the integration in Stitch can access.**

Verify the authorizing user's permissions. If the user's permissions can't be changed, a different person with the correct permissions may have to re-authorize the integration. Docs for SaaS integrations [can be found here]({{ site.baseurl }}/integrations/saas).

---

## Contacting Support

If you verify that all the correct permissions are in place and you still encounter issues, please [reach out to support](mailto: {{ site.support }}).