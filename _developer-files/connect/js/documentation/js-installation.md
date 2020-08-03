---
title: Installation
product-type: "connect"
content-type: "js-doc"
order: 3

sections:
  - content: |
      Visit the [Stitch JS GitHub repo]({{ js.releases }}) and download the latest release.

      In your application, add this `<script>` tag just before the closing `<body>` tag of the page(s) you want it to run on:

      {% capture code %}<script type="text/javascript" src="<FILE_PATH>/stitch-client.umd.min.js"></script>
      {% endcapture %}

      {% include layout/code-snippet.html language="html" code=code %}

      Make sure to replace `<FILE_PATH>` with the directory location of the `stitch-client.umd.min.js` file.
---