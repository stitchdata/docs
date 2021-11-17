---
title: Getting access
product-type: "connect"
content-type: "overview"
order: 2

sections:
  - content: |
      {% capture access-notice %}
      **Note**: For individual Stitch users, access to the API is available during the Free Trial or as part of an {{ site.data.stitch.subscription-plans.unlimited.name }} or {{ site.data.stitch.subscription-plans.unlimited-plus.name }} plan. 
      {% endcapture %}

      {% include note.html type="single-line" content=access-notice %}

      To use the Connect API, you'll need an API access token. This is necessary for authenticating to the API. Refer to the [Authentication reference]({{ link.connect.api | prepend: site.baseurl | append: "#authentication" }}) for more info.

      To learn more about using the Connect JavaScript Client, check out the [JavaScript Reference]({{ js.section | prepend: site.baseurl | flatify }}). **Note**: This feature has been deprecated and shouldn't be built against for production use.
---