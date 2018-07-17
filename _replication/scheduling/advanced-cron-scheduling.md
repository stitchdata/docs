---
title: Advanced Replication Scheduling Using Cron Expressions
permalink: /replication/replication-scheduling/advanced-cron-scheduling
keywords: replicate, replication, replication frequency, frequency, anchor time, scheduling, schedule, interval, change replication time
tags: [replication]

summary: "The Advanced Scheduler feature allows you to specify granular start times for data extraction. Using cron expressions, you can specify the exact times, days of the week, or even days of the month data extraction should begin."
type: "scheduling"
toc: true
weight: 4

enterprise-cta:
  title: "This is an Enterprise feature"
  url: "?utm_medium=docs&utm_campaign=cron-scheduling"
  copy: |
    **Advanced replication scheduling is only available on an Enterprise plan**. Cron scheduling allows you to fine-tune an integration's replication schedule, ensuring you have the data you need when you need it. [Contact Stitch Sales for more info]({{ site.sales | append: page.enterprise-cta.url }}).

---

{% include enterprise-cta.html %}

{{ page.summary }}

**Note**: All replication scheduling methods (Replication Frequency, Anchor Scheduling, and Advanced Scheduling) define when data extractions begin. They do not control how long a replication job runs or when data is loaded into a destination.

In this guide, we'll cover:

- [The uses for Advanced Scheduling](#uses)
- [The basics of cron scheduling](#basics)
- [Examples of replication schedules using cron expressions](#examples)
- [Limitations of cron scheduling in Stitch](#limitations)
- [Troubleshooting validation errors](#troubleshooting)
- [Additional cron resources](#resources)

---

## Uses for Advanced Scheduling {#uses}

Using Advanced Scheduling, you can:

1. **Run reports on specified days**. For example: You need reports for a 9:00AM meeting you have every Wednesday. You could create a replication schedule that runs a replication job on Tuesday nights at midnight, which would ensure fresh data is available on Wednesday morning when you need it. Reports could be scheduled to run at 7:00AM, giving you time before your meeting to review the data and resolve replication issues, should any arise.

2. **Whitelist hours for starting data extractions.** For example: You know that your production database is under heavy load from 1:00PM to 5:00PM. To avoid adding additional load, you can create a schedule that prevents extractions from starting during this time. **Note**: An extraction may run over into "blackout" hours as the Advanced Scheduler only controls the times jobs **start**. [See the Limitations section for more info](#limitations).

3. **Reduce your row usage**. Only scheduling data extractions when you need them can not only reduce load on data sources and your destination, it can reduce your overall row usage in Stitch.

4. **Reduce the re-replication of data.** Because replication scheduling applies to all selected tables in an integration, tables using Full Table Replication will replicate in full each time a replication job runs. Reducing the number of replication jobs overall will decrease the number of times the same record is replicated.

---

## Advanced Scheduling basics {#basics}

Stitch's Advanced Scheduler feature uses cron scheduling to create replication schedules. In this section, we'll:

- [Introduce you to cron and cron expressions](#intro-to-cron)
- [Describe cron expression syntax](#con-expression-syntax)
- [Explain how to format a cron expression](#cron-expression-field-values)
- [Explain how specifying days works](#specifying-days)

### Introduction to cron {#intro-to-cron}

So, what's cron? **Cron** is a time-based scheduler used in Unix-like operating systems such as Mac OS, Linux, etc. Tasks, or jobs, created through cron are called **cron jobs**.

To create a cron job - in this case, an integration's replication schedule - a **cron expression** is used. A cron expression describes the details of the schedule, and when combined, translates to the schedule Stitch will use to replicate data from the integration.

Using a cron expression, you can create a replication schedules such as _"At 12:00AM every day"_ or _"At 7:00PM every Monday, Wednesday, and Friday"_.

### Cron expression syntax {#cron-expression-syntax}

A cron expression in Stitch is made up of five fields that describe the elements of the schedule, separated by spaces.

Fields in the expression must be in the following order, and an expression must have all five fields to be considered valid:

```conf
[minute] [hour] [day of month] [month] [day of week]
```

### Formatting cron expressions {#cron-expression-field-values}

{% assign cron = site.data.ui.cron-scheduling %}

Now that we've covered the syntax of a cron expression, we'll move onto the values you can enter in these fields:

- The **Required fields** tab contains the allowed values and special characters for each field
- The **Special characters** tab contains examples and explanations for each special character, and where it may be used

<ul id="profileTabs" class="nav nav-tabs">
    <li class="active"><a href="#required-fields" data-toggle="tab">Required fields</a></li>
    <li><a href="#special-characters" data-toggle="tab">Special characters</a></li>
</ul>
<div class="tab-content">
    <div role="tabpanel" class="tab-pane active" id="required-fields">
        <span class="h4">Required fields</span>

        <p>See the <strong>Special characters</strong> tab for explanations and examples of how asterisks, commas, and hyphens are used.</p>

        <p><strong>Note</strong>: Entering anything other than a field's allowed values or special characters will result in an error when you try to save the integration's settings. Refer to the <a href="#troubleshooting-cron-errors">Troubleshooting section</a> for help resolving these errors.</p>
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

        <p>The fields in a cron expression can contain:</p>

        <ul>
            <li>An asterisk (<code>*</code>), or</li>
            <li>A single integer (ex: <code>5</code>), or</li>
            <li>A list of integers separated by commas (ex: <code>1,2,3</code>), or</li>
            <li>An an inclusive range, denoted by two numbers separated by a hyphen (ex: <code>1-5</code>), or</li>
            <li>A combination of lists and inclusive ranges (ex: <code>1,5,10-20</code>)</li>
        </ul>

        <p>Refer to the <a href="#examples">Example replication schedules section</a> for examples, or the <strong>Special characters</strong> tab for more info on lists and ranges.</p> 
    </div>

    <div role="tabpanel" class="tab-pane" id="special-characters">
        <span class="h4">Special characters</span>

        <p>Each field in a cron expression has its own list of allowed special characters. These characters allow you to select all values, a list of values, or a range of values. Fields may also contain both a range and a list. Refer to the <a href="#examples">Example replication schedules section</a> for examples.</p> 

        <p><strong>Note</strong>: Entering anything other than a field's allowed values or special characters will result in an error when you try to save the integration's settings. Refer to the <a href="#troubleshooting-cron-errors">Troubleshooting section</a> for help resolving these errors.</p>
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
<br>

### Specifying days in cron expressions {#specifying-days}

Stitch's implementation of cron is [POSIX](http://pubs.opengroup.org/onlinepubs/7908799/xcu/crontab.html){:target="new"} compliant. The POSIX standard has subtle rules about how the `day of month`, `month`, and `day of week` fields affect the schedule on which the integration will run. This section will focus on the behavior of those fields.

{% include note.html content="**Field restriction**: In this section, _restricted_ means that a field contains anything other than an asterisk. An asterisk will select all values for a field." %}

In POSIX, the specification of days is made using the `day of month` and `day of week` fields. How days are specified depends on which fields are restricted. In the table below are explanations of how each field combination will behave, example expressions, and the schedule the expression will translate to.

<table class="attribute-list">
    <tr>
        <td width="35%; fixed">
            <strong>
                Explanation
            </strong>
        </td>
        <td width="30%; fixed">
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
    {% for explanation in cron.day-specification-examples %}
        {% for example in explanation.examples %}
            {% capture total-examples %}
                {{ forloop.length }}
            {% endcapture %}
        {% endfor %}

        <tr>
            <td rowspan="{{ total-examples | strip }}">
                {{ explanation.explanation | markdownify }}
            </td>

            {% for example in explanation.examples %}
                {% case forloop.first %}
                    {% when true %}
                            <td>
                                {{ example.expression | markdownify | strip }}
                            </td>
                            <td>
                                {{ example.translation | strip }}
                            </td>
                        </tr>
                    {% else %}
                        <tr>
                            <td>
                                {{ example.expression | markdownify | strip }}
                            </td>
                            <td>
                                {{ example.translation | strip }}
                            </td>
                        </tr>
                {% endcase %}
            {% endfor %}
    {% endfor %}
</table>


---

## Example replication schedules {#examples}

{% capture resource-callout %}
**Want to test an expression?** Use [{{ cron.resource-names.crontab }}]({{ cron.resource-urls.crontab }}){:target="new"} to test expressions and see the schedule that will be created.
{% endcapture %}

{% include tip.html content=resource-callout %}

Based on scheduling feedback we've collected, we've put together a list of some of the most commonly requested replication schedules. The cron expressions in the table below can be copied and pasted directly into an integration's settings page in Stitch.

**Note**: When creating your own cron expressions, keep in mind that there are some [limitations](#limitations).

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

## Limitations of cron scheduling {#limitations}

While using cron expressions will give you the most control over your integrations' replication schedules, there are some limitations to keep in mind:

1. **Advanced scheduling isn't available for all integrations**. Some database integrations don't currently support advanced scheduling. We are working on converting these integrations into Singer-powered taps, at which point advanced scheduling will be available.

2. **Days of the week in specific months can't be specified** due to the implementation of cron Stitch use, which is called POSIX. THe POSIX standard [has subtle rules for specifying days](#specifying-days).

   For example: The expression `* * * 1 1` translates to _"every day in the first month (January) and the first day of every week (Monday)"_, **not** _"every Monday in January"_.

3. **Advanced Scheduling can only be used to whitelist extraction start times**. This means that a job could start during a whitelisted time period but continue running beyond that window, depending on the duration of the extraction.

   For example: An integration has a schedule that tells it to run every 20 minutes between the hours of noon and 2:00PM, starting at noon.

   On average, extractions for this integration take between 2-5 minutes. However, the extraction that starts at 1:40PM takes longer than average, causing the job to continue running even after the 2:00PM mark:

   ![Grid showing a timeline of extraction starts during whitelisted extraction hours]({{ site.baseurl }}/images/replication/cron-extraction-whitelist-example.png)

---

## Troubleshooting {#troubleshooting-cron-errors}

{% assign cron-errors = site.data.errors.cron-scheduling.errors %}

If there's an illegal value or the expression syntax is incorrect, Stitch will display an error towards the top of the {{ app.page-names.int-settings }} page when you attempt to save the changes to the integration.

Before you can move on, you'll need to resolve what's causing the error.

<table class="attribute-list">
    <tr>
        <td width="50%; fixed">
            <strong>
                Error
            </strong>
        </td>

        <td>
            <strong>
                Solution
            </strong>
        </td>
    </tr>
    {% for error in cron-errors %}
        <tr>
            <td>
<pre>
{{ error.message | strip }}
</pre>
            </td>
            <td>
                <strong>Meaning</strong>
                {{ error.meaning | markdownify }}
                <hr>
                <strong>Solution</strong>
                {{ error.fix-it | markdownify }}
            </td>
        </tr>
    {% endfor %}
</table>

---

## Additional cron resources {#resources}

{% for resource in cron.resource-list %}
- [**{{ resource.name }}**]({{ resource.url }}) - {{ resource.description }}
{% endfor %}