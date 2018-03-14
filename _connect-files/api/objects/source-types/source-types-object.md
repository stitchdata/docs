---
content-type: "api-object"
endpoint: "source-types"

title: "Source Type"
description: "{{ api.core-objects.source-types.description }}"
endpoint-url: "/source-types"
version: "4"

object-attributes:
  - name: "report_card"
    type: "object"
    sub-type: "report card"
    url: "{{ api.data-structures.report-cards.section }}"
    description: "The Report Card object corresponding to the source's `type`. For example: `platform.marketo` or `platform.hubspot`."
---