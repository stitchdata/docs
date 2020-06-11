---
title: Re-authorizing Integrations
keywords: troubleshooting, integration, trouble, issue, help, error, errors, reauthorize, re-auth, credentials, authorization
permalink: /troubleshooting/integrations/reauthorizing-integrations
tags: [troubleshooting_integrations, troubleshooting_errors]

summary: "If you see a message that asks you to re-authorize an integration, it means that Stitch's permissions to that service have been revoked."
type: "all-integrations, error"
category: "connection-errors"
---
{% include misc/data-files.html %}

When you create an integration in Stitch, the credentials you provide authorize Stitch - meaning we're granted the necessary permissions - to pull data from that particular service.

If you see a message that asks you to "re-authorize" an integration, it means that Stitch's permissions to that service have been revoked:

> We're having some trouble connecting to your integration. Please verify that your credentials are correct and up-to-date.

Authorization errors can occur for a few reasons:

- **The credentials used to authorize Stitch have changed.** This can be the username, password, API credentials, or even the permissions themselves. For example: the password associated with the user Stitch uses to access your Postgres database has been changed in the database, but not in the Stitch app.
- **A third party service is experiencing an issue**. For example: if Salesforce is reporting downtime, Stitch may not be able to connect and thus interpret the reason as a lack of permissions.
- **Stitch is experiencing an internal issue.**. Our goal is to be up *at least* 99% of the time, but Stitch does occasionally encounter downtime.

If you receive the error mentioned above, we recommend trying these simple checks before reaching out to support.

---

## Verify Credentials & Re-authorize Integrations {#verifying-creds-reauthorizing}

First, check that the credentials entered into Stitch are correct. This includes user credentials (such as a username or password) and API credentials (such as a Key or Token).

In some cases, you may need to generate new API credentials to resolve the issue. Check out the [connection instructions for your SaaS integration]({{ site.baseurl }}/integrations/saas/) for guidance on how to do this.

---

## Check Permission Settings {#check-permissions}

- **For database integrations,** check the *Creating a Stitch Database User* section of the [connection instructions for your database]({{ site.baseurl }}/integrations/databases). That section contains all the permissions Stitch requires to connect to your particular database.
- **For SaaS integrations,** check the [connection instructions for your SaaS integration]({{ site.baseurl }}/integrations/saas/) to see if that particular integration has any permission requirements. Some integrations - such as NetSuite or Marketo - require certain permissions or roles to access data.

---

## Check for Reported Downtime {#check-for-downtime}

- **For SaaS integrations,** check out the Status Page for the problem integration to see if any issues have been reported. You can find a list of all our integrations' status pages in the [Third-Party Downtime article]({{ link.troubleshooting.third-party-downtime | prepend: site.baseurl }}).
- **If the third party hasn't reported any issues,** check out [Stitch's Status Page]({{ site.status }}) to see if we're currently reporting an outage.

---

## Re-authorize Integrations

1. From the {{ app.page-names.dashboard }}, click into the integration.
2. Click the {{ app.buttons.update-int-settings }} button.
   - **For databases and SaaS integrations**, you can manually re-enter the credentials. Click {{ app.buttons.save-int-settings }} to update and save.
   - **For some SaaS integrations** - like Facebook Ads, for example - you'll see a **Re-authorize** button. Click this button to go through the re-authorization process.

Note that in some cases, the error may continue to display even after inputting and saving the correct credentials. Stitch may continue to "believe" that an authorization issue is present until the next replication job (which is dependent upon that integration's Replication Frequency) completes.

---

## Contact Support

If you've done all of the above and are still having trouble, please reach out to support.