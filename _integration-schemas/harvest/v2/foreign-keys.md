---
tap-reference: "harvest"
version: "2.0"

foreign-keys:
  - id: "client-id"
    attribute: "client_id"
    table: "clients"
    all-foreign-keys:
      - table: "clients"
        join-on: "id"
      - table: "contacts"
      - table: "estimates"
      - table: "expenses"
      - table: "invoices"
      - table: "projects"
      - table: "time_entries"
      - table: "user_projects"

  - id: "contact-id"
    attribute: "contact_id"
    table: "contacts"
    all-foreign-keys:
      - table: "contacts"
        join-on: "id"

  - id: "estimate-item-category-id"
    attribute: ""
    table: "estimate_item_categories"
    all-foreign-keys:
      - table: "estimate_item_categories"
        join-on: "id"

  - id: "estimate-line-item-id"
    attribute: ""
    table: "estimate_line_items"
    all-foreign-keys:
      - table: "estimate_line_items"
        join-on: "id"

  - id: "estimate-message-id"
    attribute: ""
    table: "estimate_messages"
    all-foreign-keys:
      - table: "estimate_messages"
        join-on: "id"

  - id: "estimate-id"
    attribute: "estimate_id"
    table: "estimates"
    all-foreign-keys:
      - table: "estimate_line_items"
      - table: "estimate_messages"
      - table: "estimates"
        join-on: "id"
      - table: "invoices"

  - id: "expense-category-id"
    attribute: "expense_category_id"
    table: "expense_categories"
    all-foreign-keys:
      - table: "expense_categories"
        join-on: "id"
      - table: "expenses"

  - id: "expense-id"
    attribute: "expense_id"
    table: "expenses"
    all-foreign-keys:
      - table: "expenses"
        join-on: "id"

  - id: "external-reference-id"
    attribute: "external_reference_id"
    table: "external_references"
    all-foreign-keys:
      - table: "external_references"
        join-on: "id"
      - table: "time_entries"
      - table: "time_entry_external_reference"

  - id: "invoice-item-categories"
    attribute: "invoice_item_category_id"
    table: "invoice_item_categories"
    all-foreign-keys:
      - table: "invoice_item_categories"
        join-on: "id"

  - id: "invoice-line-item-id"
    attribute: "invoice_line_item_id"
    table: "invoice_line_items"
    all-foreign-keys:
      - table: "invoice_line_items"
      - table: "invoices"
        join-on: "id"

  - id: "invoice-message-id"
    attribute: "invoice_message_id"
    table: "invoice_messages"
    all-foreign-keys:
      - table: "invoice_messages"
        join-on: "id"

  - id: "invoice-id"
    attribute: "invoice_id"
    table: "invoices"
    all-foreign-keys:
      - table: "expenses"
      - table: "invoice_line_items"
      - table: "invoice_messages"
      - table: "invoice-payments"
      - table: "invoices"
        join-on: "id"
      - table: "time_entries"

  - id: "invoice-payment-id"
    attribute: "invoice_payment_id"
    table: "invoice_payments"
    all-foreign-keys:
      - table: "invoice_payments"
        join-on: "id"

  - id: "project-id"
    attribute: "project_id"
    table: "projects"
    all-foreign-keys:
      - table: "expenses"
      - table: "invoice_line_items"
      - table: "project_tasks"
      - table: "project_users"
      - table: "projects"
        join-on: "id"
      - table: "time_entries"
      - table: "user_projects"

  - id: "project-task-id"
    attribute: "project_task_id"
    table: "project_tasks"
    all-foreign-keys:
      - table: "project_tasks"
        join-on: "id"
      - table: "user_project_tasks"

  - id: "project-user-id"
    attribute: "project_user_id"
    table: "project_users"
    all-foreign-keys:
      - table: "project_users"
        join-on: "id"

  - id: "role-id"
    attribute: "role_id"
    table: "roles"
    all-foreign-keys:
      - table: "roles"
        join-on: "id"
      - table: "user_roles"

  - id: "task-id"
    attribute: "task_id"
    table: "tasks"
    all-foreign-keys:
      - table: "external_references"
      - table: "tasks"
        join-on: "id"
      - table: "time_entries"

  - id: "time-entry-id"
    attribute: "time_entry_id"
    table: "time_entries"
    all-foreign-keys:
      - table: "time_entries"
        join-on: "id"
      - table: "time_entry_external_reference"

  - id: "user-id"
    attribute: "user_id"
    table: "users"
    all-foreign-keys:
      - table: "estimates"
        join-on: "creator_id"
      - table: "invoices"
        join-on: "creator_id"
      - table: "project_tasks"
      - table: "time_entries"
      - table: "users"
        join-on: "id"
      - table: "user_project_tasks"
      - table: "user_projects"
      - table: "user_roles"

  - id: "user-project-task-id"
    attribute: "user_project_task_id"
    table: "user_project_tasks"
    all-foreign-keys:
      - table: "user_project_tasks"
        join-on: "id"

  - id: "user-project-id"
    attribute: "user_project_id"
    table: "user_projects"
    all-foreign-keys:
      - table: "user_projects"
        join-on: "id"
---