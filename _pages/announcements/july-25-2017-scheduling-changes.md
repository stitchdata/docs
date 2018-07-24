---
title: "Announcements: Integration Scheduling Changes on July 25"
permalink: /announcements/integration-scheduling-changes-july-25
layout: page
feedback: false

rollout-date: "July 25th"
rollout-time: "6PM Eastern Time"
---

{% capture rollout %}**On {{ page.rollout-date }} at {{ page.rollout-time }}**, we'll be modifying the scheduling mechanism for [a subset of our integrations](#affected-integrations) to establish scheduling consistency across the board. The nature of this change may result in more frequent replication for some integrations.<br><br>

To avoid inflating your row counts as a result, **we will proactively change the replication frequency for affected integrations using a 30 minute schedule to 60 minutes.**
{% endcapture %}

{% include important.html type="single-line" content=rollout %}

To be notified when this change is released, subscribe to our [changelog]({{ site.changelog }}){:target="_blank"} - and feel free to bump those frequencies afterward if they don't fit your needs.

---

## Job Scheduling Now & in the Future

This change provides more predictability in the scheduled replication jobs for your integrations. Below is a summary of how job scheduling works now and how scheduling will work after {{ page.rollout-date }}.

#### Scheduling Now

Currently, scheduling for [the integrations listed below](#affected-integrations) is based on the completion, or **ending** time of the previous sync.

For example: A Facebook Ads integration has a Replication Frequency of 30 minutes. The Start and End Times for this integration's syncs might look like this:

| Sync # | Start Time | End Time | Duration (minutes) |
|--------+------------+----------+--------------------|
| Sync 1 | 12:00:00   | 12:42:00 | 42                 |
| Sync 2 | 13:12:00   | 13:41:00 | 29                 |
| Sync 3 | 13:42:00   | 14:15:00 | 33                 |
| Sync 4 | 14:15:00   | ...      | ...                |


#### Scheduling After {{ page.rollout-date }}

On {{ page.rollout-date }}, Stitch will begin scheduling syncs based on the **start time** of the previous sync.

Additionally, if the previous sync is still in progress when it would be time to start the next sync, Stitch will wait until the next recurrence of the Replication Frequency to begin. In the past, the next sync would be scheduled immediately upon the previous sync's completion.

Using the new scheduling process, the Start and End times for same Facebook Ads integration with a Replication Frequency of 30 minutes might look like this:

| Sync # | Start Time | End Time | Duration (minutes) |
|--------+------------+----------+--------------------|
| Sync 1 | 12:00:00   | 12:42:00 | 42                 |
| Sync 2 | 13:00:00   | 13:29:00 | 29                 |
| Sync 3 | 13:30:00   | 14:03:00 | 33                 |
| Sync 4 | 14:30:00   | ...      | ...                |

To avoid inflating your row counts as a result of the potential increase in replication, we will proactively change the Replication Frequency for affected integrations using a 30 minute schedule to 60 minutes. Feel free to bump those frequencies afterward to better suit your needs.

---

## Affected Integrations {#affected-integrations}

On {{ page.rollout-date }}, the following integrations will be switched over to the new scheduling mechanism:

{% assign scheduling-integrations = site.saas-integrations | where:"singer",false %}

<ul class="tiles">
{% for integration in scheduling-integrations %}
	<li>
		<a href="{{ integration.url | prepend: site.baseurl }}">
			<img src="{{ integration.icon | prepend: site.baseurl }}" alt="{{ integration.display_name }}">
		</a>
		<strong>{{ integration.title }}</strong>
 	</li>
{% endfor %}
</ul>

---

## Questions? Concerns?

If you have questions about these changes, [reach out to support](mailto:{{ site.support }}) - we'll be happy to help!

You can also subscribe to our [changelog]({{ site.changelog }}){:target="_blank"} to be notified when this change is released.