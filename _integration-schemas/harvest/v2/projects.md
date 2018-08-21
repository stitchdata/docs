---
tap: "harvest"
version: "2.0"

name: "projects"
doc-link: https://help.getharvest.com/api-v2/projects-api/projects/projects/
singer-schema: https://github.com/singer-io/tap-harvest/blob/master/tap_harvest/schemas/projects.json
description: |
  The `{{ table.name }}` table contains info about the projects in your Harvest account.

replication-method: "Key-based Incremental"

api-method:
  name: List all projects
  doc-link: https://help.getharvest.com/api-v2/projects-api/projects/projects#list-all-projects

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The project ID."

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the project was last updated."

  - name: "client_id"
    type: "integer"
    description: "The ID of the client associated with the project."
    foreign-key-id: "client-id"

  - name: "name"
    type: "string"
    description: "The name of the project."

  - name: "code"
    type: "string"
    description: "The code applied to the project."

  - name: "is_active"
    type: "boolean"
    description: "If `true`, the project is active."

  - name: "is_billable"
    type: "boolean"
    description: "Indicates if the project is billable."

  - name: "is_fixed_fee"
    type: "boolean"
    description: "If `true`, the project is a fixed-fee project."

  - name: "bill_by"
    type: "string"
    description: "The method by which the project is invoiced." 

  - name: "hourly_rate"
    type: "number"
    description: "The rate for projects that are billed by Project Hourly Rate."

  - name: "budget"
    type: "number"
    description: "The budget for the project."

  - name: "budget_by"
    type: "string"
    description: "The method by which the project is budgeted."

  - name: "budget_is_monthly"
    type: "boolean"
    description: "If `true`, the budget resets every month."

  - name: "notify_when_over_budget"
    type: "boolean"
    description: "Indicates if notification emails should be sent when a project reaches the budget threshold set in `over_budget_notification_percentage`."

  - name: "over_budget_notification_percentage"
    type: "integer"
    description: "The percentage value to trigger over budget email alerts."

  - name: "over_budget_notification_date"
    type: "date-time"
    description: "The date of the last over budget notification. This will be `null` if no notifications have been sent."

  - name: "show_budget_to_all"
    type: "boolean"
    description: |
      Indicates if the project budget should be shown to all employees. 

      **Note**: This doesn't apply to Total Fee Projects, or projects that have a `budget_by` value of `Project_Cost`.

  - name: "cost_budget"
    type: "number"
    description: "The budget value for Total Project Fees projects, or projects that have a `budget_by` value of `Project_Cost`."

  - name: "cost_budget_include_expenses"
    type: "boolean"
    description: "Indicates if the budgets of Total Project Fees projects should include tracked expenses."

  - name: "fee"
    type: "number"
    description: "The amount to be invoiced for the project. Only used by fixed-fee projects."

  - name: "notes"
    type: "string"
    description: "Any notes entered about the project."

  - name: "starts_on"
    type: "string"
    description: "The start date of the project."

  - name: "ends_on"
    type: "string"
    description: "The end date of the project."

  - name: "created_at"
    type: "string"
    description: "The time the project was created."
---