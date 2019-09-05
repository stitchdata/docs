---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

content-type: "api-object"
endpoint: "replication-jobs"
order: 9


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Replication Job"
endpoint-url: "/sources/{source_id}/sync"

description: "{{ api.core-objects.replication-jobs.description | flatify }}"
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
    short: "{{ api.core-objects.replication-jobs.post.short | flatify }}"

  - id: "stop-a-job"
    title: "Stop a replication job"
    method: "delete"
    short: "{{ api.core-objects.replication-jobs.delete.short | flatify }}"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "job_name"
    type: "string"
    description: "A unique identifier for the replication job."
---