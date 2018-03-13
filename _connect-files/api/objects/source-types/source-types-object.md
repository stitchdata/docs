---
content-type: "api-object"
endpoint: "source-types"

title: "Source Type"
description: "Source types define the information needed to configure a data source."
endpoint-url: "/source-types"
version: "4"

object-attributes:
  - name: "report_card"
    type: "report card object"
    url: "{{ page.anchors.data-structures.report-cards }}"
    description: "The Report Card object corresponding to the source's `type`. For example: `platform.marketo` or `platform.hubspot`."
---