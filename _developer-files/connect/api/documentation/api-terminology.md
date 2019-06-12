---
product-type: "connect"
content-type: "api-terms"

all-terms:
  - name: "Partner ID"
    definition: |
      {{ site.data.connect.general.authentication.partner-id | flatify }}

  - name: "Partner key"
    definition: |
      {{ site.data.connect.general.authentication.partner-key | flatify }}

  - name: "Stitch client account"
    definition: |
      {{ site.data.tooltips.stitch-client-account }}

  - name: "Client account access token"
    definition: |
      {{ site.data.connect.general.authentication.client-account-access-token }}

  - name: "Ephemeral token"
    definition: |
      {{ site.data.connect.general.authentication.ephemeral-token | flatify }}

  - name: "Destination"
    definition: |
      {{ site.data.tooltips.destination }}

  - name: "Session"
    definition: |
      {{ site.data.tooltips.session }}

  - name: "Source"
    definition: |
      {{ site.data.tooltips.source | flatify }}

  - name: "Stream"
    definition: |
      A table in a data source.

  - name: "Connection check"
    definition: |
      {{ site.data.tooltips.connection-check }}

  - name: "Structure sync"
    definition: |
      {{ site.data.tooltips.structure-sync }} This is also referred to as discovery.
---