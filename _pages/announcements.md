---
title: "Integration Upgrades"
permalink: /announcements/
layout: page
feedback: false

## ADDING INTEGRATIONS TO THE DEPRECATION LIST
# To add an integration version to the deprecation list on this page, you need to
# add a deprecation date to the appropriate version in the integration's version
# file.

# Version files are located in /_data/taps/versions/

# 1. Find the file with the same name as the integration & open it.
# 2. In the released-versions list in the file, locate the version being deprecated. For example:

# released-versions:
#  - number: "0.11"
#    date-released: "October 1, 2015"
#    deprecated: true
#    # deprecation-date: ""

# 3. Uncomment the deprecation-date line.
# 4. Add the date the version is being deprecated in MONTH, DAY, YEAR format. For example: "November 22, 2017" Don't forget the double quotes, stuff won't work.
# 5. Save!

# That's it. Any version with a deprecation date will be added to the list on this page.
---
{% include misc/data-files.html %}

Over the coming months, we'll be converting our integrations to use the [Singer open source project]({{ site.singer }}){:target="_blank"}. Powering the Stitch platform with Singer means that there are no limits to the types of data sources that Stitch can integrate with, and since the code is open source, users have complete visibility into and control of how their data is collected.

Check out the [Singer organization on GitHub]({{ site.singer-github }}){:target="new"}.

---

## Upgrade Your Integrations

To upgrade to the latest version of an integration, you'll need to do the following:

1. **Re-create all affected integrations in your account**. New connections will use the latest version of the integration. See the next section for deprecation info for affected integrations.

   Note that:

   - Historical data will need to be re-synced for new connections. You can do this during setup by [changing the integration's start date]({{ link.replication.saas-historical | prepend: site.baseurl }}).

    - Row usage for the newly created integrations will be exempt for two weeks so that you may re-sync historical data free of charge. Note that it may take up to one business day for this to take effect.
2. **Delete the old versions of the integration from your account**.

If you need a refresher on setting up an integration, refer to the [SaaS Integration docs]({{ site.baseurl }}/integrations/saas).

---

## Version Deprecation Dates {#deprecation-dates}

Below is a list of integration versions currently scheduled for deprecation. These versions will continue to run after their deprecation date, however, they will no longer receive support.

As we prepare to convert integrations, we'll add them to this list. We'll also announce updates on our [status page]({{ site.status }}){:target="_blank"}, which you can subscribe to.

{% include notifications/integration-version-deprecation-list.html %}

---

## More Info & Support

If you have questions about these changes, [reach out to support](mailto:{{ site.support }}) - we'll be happy to help!

To stay up-to-date on the latest and be notified of upcoming integration releases, subscribe to our [changelog]({{ site.changelog }}){:target="_blank"} and [status page]({{ site.status }}){:target="_blank"}.
