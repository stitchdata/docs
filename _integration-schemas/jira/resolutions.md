---
tap: "jira"
version: "1"

name: "resolutions"
doc-link: "https://developer.atlassian.com/cloud/jira/platform/rest/v2/#api-api-2-projectCategory-post"
singer-schema: "https://github.com/singer-io/tap-jira/blob/master/tap_jira/schemas/resolutions.json"
description: |
  The `{{ table.name }}` table contains info about issue resolutions.

  **Note**: To replicate this data, the `Administer {{ integration.display_name }}` [global {{ integration.display_name }} permission]({{ integration.global-permissions-doc }}){:target="new"} is required. Refer to [{{ integration.display_name }}'s API documentation]({{ table.doc-link }}){:target="new"} for more info.

replication-method: "Full Table"

api-method:
    name: "Get resolutions"
    doc-link: "https://developer.atlassian.com/cloud/jira/platform/rest/v2/#api-api-2-projectCategory-post"
    
attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The resolution ID."
    # foreign-key-id: "resolution-id"

  - name: "description"
    type: "string"
    description: "The description of the issue resolution."

  - name: "iconUrl"
    type: "string"
    description: "The URL of the icon for the issue resolution."

  - name: "name"
    type: "string"
    description: "The name of the issue resolution."

  - name: "self"
    type: "uri"
    description: "The URL of the issue resolution."
---