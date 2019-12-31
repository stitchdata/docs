---
title: ""
product-type: "import-api"
content-type: "overview"
order: 1

sections:
  - content: |
      {{ site.data.import-api.api.description }}

    subsections:
      - title: "Before you get started"
        anchor: "before-you-get-started"
        content: |
          Before you get started, it's important to note that the Import API cannot **extract** data from a source - it can only receive data.

          To **pull** data from a source, consider creating a [Singer tap]({{ site.singer }}){:target="new"} instead. Singer is an open source project that allows you to write and collaborate on scripts that move data between databases, web APIs, files queues, and anything else you can think of. Refer to [Singer.io]({{ site.singer }}){:target="new"} for more info and examples.


---
Import API integrations are unique from Stitch's other integration offerings:

- **No need for scheduling replication.** Import API integrations process data as it's received, meaning there's no need to schedule replication. For this reason, you won't see the Replication Frequency setting in the {{ app.page-names.int-settings }} page.
- **No extraction logs.** The Import API doesn't make requests to sources to extract data. Import API integrations only receive data that is sent to them. For this reason, there won't be an Extraction Logs tab for these integrations in Stitch. 

   If you encounter issues with data once it's sent to an Import API integration, refer to the [Troubleshooting Import API data guide]({{ link.import-api.guides.troubleshooting-data | prepend: site.baseurl }}).