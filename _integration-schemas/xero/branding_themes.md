---
tap: "xero"
version: "1.0"

name: "branding_themes"
doc-link: &api-doc https://developer.xero.com/documentation/api/branding-themes
singer-schema: https://github.com/singer-io/tap-xero/blob/master/tap_xero/schemas/branding_themes.json
description: |
  The `branding_themes` table contains info about your branding themes. A branding theme is customization you can apply to customer-facing documents such as invoices, statements, quotes, etc.

replication-method: "Full Table"

api-method:
  name: getBrandingThemes
  doc-link: *api-doc

attributes:
  - name: "BrandingThemeID"
    type: "string"
    primary-key: true
    description: "The branding theme ID."

  - name: "Name"
    type: "string"
    description: "The name of the branding theme."

  - name: "CreatedDateUTC"
    type: "date-time"
    description: "The date the branding theme was created, in UTC."

  - name: "SortOrder"
    type: "integer"
    description: "The ranked order of the branding theme. The default branding theme has a value of `0`."
---