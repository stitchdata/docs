---
tap: "harvest"
version: "2.0"

name: "user_project_tasks"
doc-link:
singer-schema: https://github.com/singer-io/tap-harvest/blob/master/tap_harvest/schemas/user_project_tasks.json
description: |
  The `{{ table.name }}` table contains pairs of user IDs and project task IDs.

   This data can be used to see lists of all the project tasks associated with a user, and join tables together to get a comprehensive look at the user's projects.

replication-method: "Key-based Incremental"

api-method:
  name: 
  doc-link:

attributes:
  - name: "user_id"
    type: "integer"
    description: "The user ID."
    foreign-key-id: "user-id"

  - name: "project_task_id"
    type: "integer"
    description: "The project task ID."
    foreign-key-id: "project-task-id"
---