---
tap: "mixpanel"
version: "1"
key: "engage"

name: "engage"
doc-link: "https://developer.mixpanel.com/docs/data-export-api#section-engage"
singer-schema: "https://github.com/singer-io/tap-mixpanel/blob/master/tap_mixpanel/schemas/engage.json"
description: |
  The `{{ table.name }}` table contains info about user profiles.

  The schema for this table is dynamic, meaning that the columns Stitch detects are dependent upon the properties provided upon upload in {{ integration.display_name }}. For every property available in {{ integration.display_name }} for `{{ table.name }}` records, Stitch will display a column in the integration's **Tables to Replicate** tab.

replication-method: "Full Table"

api-method:
  name: "Export formatted data (Engage)"
  doc-link: "https://developer.mixpanel.com/docs/data-export-api#section-engage"

attributes:
  - name: "distinct_id"
    type: "string"
    primary-key: true
    description: "The profile ID."

  - name: "OTHER_ATTRIBUTES"
    type: "varies"
    description: |
      For every property available in {{ integration.display_name }} for `{{ table.name }}` records, Stitch will display a column in the integration's **Tables to Replicate** tab.
---