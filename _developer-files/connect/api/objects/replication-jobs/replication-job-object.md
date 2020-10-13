---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-object"
endpoint: "replication-jobs"
order: 9


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Replication Job"
description: "{{ api.core-objects.replication-jobs.description | flatify }}"
endpoint-url: "/sources/{source_id}/sync"

intro-short: "Start and stop replication jobs" # Used in the API functionality section of the docs


# -------------------------- #
#        VERSION INFO        #
# -------------------------- #

latest-version: "4"
versions:
  - number: "4"
    deprecated: false


# -------------------------- #
#      AVAILABLE METHODS     #
# -------------------------- #

available-methods:
  - id: "start-a-job"
    title: "Start a replication job"
    method: "post"
    short: "{{ site.data.connect.core-objects.replication-jobs.post.short | flatify }}"

  - id: "stop-a-job"
    title: "Stop a replication job"
    method: "delete"
    short: "{{ site.data.connect.core-objects.replication-jobs.delete.short | flatify }}"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "job_name"
    type: "string"
    description: "A unique identifier for the replication job."


# -------------------------- #
#           EXAMPLES         #
# -------------------------- #

examples:
  - code: |
      {
      "job_name": "116078.120643.sync.c12fb0a7-7e4a-11e9-abdc-0edc2c318fba"
      }
---