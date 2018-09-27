---
tap: "amplitude"
# version: "1.0"

name: "merge_ids_[project_id]"
doc-link: https://amplitude.zendesk.com/hc/en-us/articles/115001902492-Query-Snowflake#column-schema
description: |
  {{ table.name }} tables contain info about merged users. These are users whose records have been merged with other user records to eliminate duplicates.

  For example: If an anonymous user logs events anonymously before signing in, they will go from being anonymous to a recognized user. Without merging the user's records, it'll look like two users with two sets of events, rather than one user completing a series of events.

  For more info on how {{ integration.display_name }} handles merging users, [refer to their documentation](https://amplitude.zendesk.com/hc/en-us/articles/115003135607){:target="new"}.

  **Note**: Each table will have the project ID appended. For example: If a project has an ID of `168342`, the merged ID table for the project will be named `merge_ids_168432`.

replication-method: "Key-based Incremental"

attributes:
  - name: "amplitude_id"
    type: "number"
    primary-key: true
    description: "The {{ integration.display_name }} being merged into a user's original {{ integration.display_name }} ID. "

  - name: "merge_server_time"
    type: "date-time"
    primary-key: true
    description: "The server time when the user's new {{ integration.display_name }} was associated with their original {{ integration.display_name }} ID."

  - name: "merged_amplitude_id"
    type: "number"
    primary-key: true
    description: "The originally assigned {{ integration.display_name }} ID when the user was first created."

  - name: "merge_event_time"
    type: "date-time"
    primary-key: true
    replication-key: true
    description: "The time when the user's new {{ integration.display_name }} ID was associated with their original {{ integration.display_name }} ID."
---