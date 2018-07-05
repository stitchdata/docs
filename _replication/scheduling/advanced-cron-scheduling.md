---
title: Advanced Replication Scheduling Using Cron Expressions
permalink: /replication/replication-scheduling/advanced-cron-scheduling
keywords: replicate, replication, replication frequency, frequency, anchor time, scheduling, schedule, interval, change replication time
tags: [replication]

summary: "[TODO]"
type: "settings"
toc: true
weight: 2

enterprise-cta:
  title: "Need advanced scheduling?"
  url: "?utm_medium=docs&utm_campaign=cron-scheduling"
  copy: |
    **Advanced replication scheduling is only available on an Enterprise plan**. Cron scheduling allows you to fine-tune an integration's replication schedule, ensuring you have the data you need when you need it. [Contact Stitch Sales for more info]({{ site.sales | append: page.enterprise-cta.url }}).

---

{% include enterprise-cta.html %}

{{ page.summary }}

- We use Vixie and Quartz

### Uses for advanced scheduling

1. "Blackout" hours
2. Time extraction with 
3. Reduce Stitch usage
4. Avoid re-replicating 

---

## Cron expression basics

A cron expression in Stitch is made up of five field, or subexpressions, that describe the details of the schedule, separated by spaces. When combined, the expression translates to the schedule Stitch will use to replicate data from the integration.

The fields are as follows:

```conf
[minute] [hour] [day of month] [month] [day of week]
```

### Field formatting

{% assign cron = site.data.ui.cron-scheduling %}

The fields in a cron expression can contain any of the following values, along with the allowed special characters for that field.

<ul id="profileTabs" class="nav nav-tabs">
    <li class="active"><a href="#required-fields" data-toggle="tab">Required fields</a></li>
    <li><a href="#special-characters" data-toggle="tab">Special characters</a></li>
</ul>
<div class="tab-content">
    <div role="tabpanel" class="tab-pane active" id="required-fields">
        <table class="attribute-list">
            <tr>
                <td>
                    <strong>Field name</strong>
                </td>
                <td>
                    <strong>Allowed values</strong>
                </td>
                <td>
                    <strong>Allowed special characters</strong>
                </td>
            </tr>
        {% for field in cron.required-fields %}
            <tr>
                <td>
                    {{ field.name }}
                </td>
                <td>
                    {{ field.allowed-values }}
                </td>
                <td>
                    {{ field.special-characters }}
                </td>
            </tr>
        {% endfor %}
        </table>
    </div>

    <div role="tabpanel" class="tab-pane" id="special-characters">
        <table class="attribute-list">
            <tr>
                <td width="15%; fixed" align="right">
                    <strong>Special<br>character</strong>
                </td>
                <td width="15%; fixed">
                    <strong>Allowed<br>fields</strong>
                </td>
                <td>
                    <strong>Description</strong>
                </td>
            </tr>
        {% for character in cron.special-characters %}
            <tr>
                <td align="right">
                    <strong>{{ character.character }}</strong><br>
                    ({{ character.name }})
                </td>
                <td>
                    {{ character.allowed-in }}
                </td>
                <td class="description">
                    {{ character.description | markdownify }}

                    <strong>Example:</strong> {{ character.example | markdownify }}
                </td>
            </tr>
        {% endfor %}
        </table>
    </div>
</div>


---

When creating a cron expression, keep in mind that:

1. The order of the values in the expression matters. The order will always be `[minute] [hour] [day of month] [month] [day of week]`.
2. An expression must have all five values noted above to be considered valid.
3. 

---

## Limitations of cron scheduling

1. **Intervals (frequencies) must be a minimum of one minute**. Sub-minute intervals are not supported. [TODO]
2. **Advanced scheduling isn't available for all integrations**. Some database integrations don't currently support advanced scheduling. We are working on converting these integrations into Singer-powered taps, at which point advanced scheduling will be available.


- Note: This only controls the time an extraction begins. The completion of the replication job, including the time required to load extracted data, is not controllable using advanced scheduling.

- Blackout hours refer to jobs being scheduled, not actually running them

- If a replication job is still running when the next job is scheduled to begin, the second job will be skipped.

---

## Example replication schedules using cron {#example-replication-schedules}

<table class="attribute-list">
<tr>
<td>
<strong>
Expression
</strong>
</td>

<td>
<strong>
Translation
</strong>
</td>
</tr>
{% for example in cron.examples %}
<tr>
<td>
{{ example.expression | markdownify }}
</td>
<td>
{{ example.translation }}
</td>
</tr>
{% endfor %}
</table>

---

## Troubleshooting