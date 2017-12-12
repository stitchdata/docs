---
tap: "harvest"
# version:

name: "projects"
doc-link: http://help.getharvest.com/api-v1/projects-api/projects/create-and-show-projects#projects-parameters
singer-schema: https://github.com/singer-io/tap-harvest/blob/master/tap_harvest/schemas/projects.json
description: |
  The `projects` table contains info about the projects in your Harvest account.

replication-method: "Incremental"
api-method:
  name: showAllProjects
  doc-link: http://help.getharvest.com/api-v1/projects-api/projects/create-and-show-projects/#show-all-projects

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The project ID."
    # foreign-keys:
    #   - table: "project_users"
    #     attribute: "project_id"
    #   - table: "project_tasks"
    #     attribute: "project_id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the project was last updated."

  - name: "client_id"
    type: "integer"
    description: "The ID of the client associated with the project."
    # foreign-keys:
    #   - table: "clients"
    #     attribute: "id"

  - name: "name"
    type: "string"
    description: "The name of the project."

  - name: "code"
    type: "string"
    description: "The code applied to the project."

  - name: "active"
    type: "boolean"
    description: "Indicates if the project is active or archived."

  - name: "billable"
    type: "boolean"
    description: "Indicates if the project is billable."

  - name: "bill_by"
    type: "string"
    description: |
      The method by which the project is invoiced. Possible values:

      - `Project`
      - `Tasks`
      - `People`
      - `None`

  - name: "hourly_rate"
    type: "number"
    description: "If billed by Project Hourly rate, this is the hourly rate the project will be billed at."

  - name: "budget"
    type: "number"
    description: "The budget for the project."

  - name: "budget_by"
    type: "string"
    description: |
      The method by which the project is budgeted. Possible values:

      - `Project` - hours per project
      - `Project_Cost` - total project fees
      - `Task` - hours per task
      - `Person` - hours per person
      - `None` - no budget

  - name: "notify_when_over_budget"
    type: "boolean"
    description: "Indicates if notification emails should be sent when a project reaches the budget threshold set in `over_budget_notification_percentage`."

  - name: "over_budget_notification_percetange"
    type: "integer"
    description: "The percentage value to trigger over budget email alerts."

  - name: "over_budget_notified_at"
    type: "string"
    description: "The date of the last over budget notification. This will be `nil` if no notifications have been sent."

  - name: "show_budget_to_all"
    type: "boolean"
    description: |
      Indicates if the project budget should be shown to all employees. 

      **Note**: This doesn't apply to Total Fee Projects, or projects that have a `budget_by` value of `Project_Cost`.

  - name: "created_at"
    type: "date-time"
    description: "The time the project was created."

  - name: "starts_on"
    type: "string"
    description: "The start date of the project."

  - name: "ends_on"
    type: "string"
    description: "The end date of the project."

  - name: "estimate"
    type: "number"
    description: "The estimate for the project."

  - name: "estimate_by"
    type: "string"
    description: "The method by which the project is estimated."

  - name: "hint_earliest_record_at"
    type: "string"
    description: "The date of the earliest record for the project."

  - name: "hint_latest_record_at"
    type: "string"
    description: "The date of the most recent record for the project."

  - name: "notes"
    type: "string"
    description: "Any notes entered about the project."

  - name: "cost_budget"
    type: "number"
    description: "The budget value for Total Project Fees projects, or projects that have a `budget_by` value of `Project_Cost`."

  - name: "cost_budget_include_expenses"
    type: "boolean"
    description: "Indicates if the budgets of Total Project Fees projects should include tracked expenses."
---