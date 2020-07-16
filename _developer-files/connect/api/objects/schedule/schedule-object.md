---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-structure"
key: "schedule-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Schedule"
description: |
  {% include misc/data-files.html %}
  {{ site.data.connect.data-structures.schedule.description | flatify }}

  Stitch supports three replication scheduling methods:

  - Replication Frequency
  - Anchor Scheduling
  - Advanced (cron) Scheduling

  Refer to the [Replication Scheduling for Sources Using the Connect API guide]({{ link.connect.guides.replication-scheduling-for-sources | prepend: site.baseurl }}) for more info and examples.


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "type"
    type: "string"
    description: |
      The type of schedule. Possible values are:

      - `interval` - Applicable to Replication Frequency and Anchor Scheduling
      - `cron` - Applicable to Advanced (cron) scheduling
    example-value: |
      interval

  - name: "interval"
    type: "number"
    description: |
      **Applicable to interval-based schedules only.** The interval used by the schedule, according to the `unit` value.

      For example: If `unit: minute` and `interval: 60.0`, the schedule is based on an interval of 60 minutes.
    example-value: |
      60.0

  - name: "unit"
    type: "string"
    description: |
      **Applicable to interval-based schedules only.** The unit of measurement for the schedule. This will be `minute`.
    example-value: |
      minute

  - name: "cron_expression"
    type: "string"
    description: |
      **Applicable to cron-based schedules only.** A valid Quartz cron expression representing the replication schedule for the integration.
    example-value: |
      0 0 12 ? * MON-FRI *

  - name: "next_fire_time"
    type: "timestamp"
    description: |
      A timestamp indicating the next time the source is scheduled to run a replication job.
    example-value: |
      2020-06-22T12:00:00Z
      

# -------------------------- #
#           EXAMPLES         #
# -------------------------- #

examples:
  - type: "Interval-based schedule"
    code: |
      {
        "type": "interval",
        "unit": "minute",
        "interval": 60.0,
        "next_fire_time": "2020-06-22T19:00:00Z"
      }

  - type: "Cron-based schedule"
    code: |
      {
        "type": "cron",
        "cron_expression": "0 0 12 ? * MON-FRI *",
        "next_fire_time": "2020-06-22T12:00:00Z"
      }
---