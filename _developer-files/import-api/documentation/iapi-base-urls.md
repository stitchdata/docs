---
title: Base URLs
product-type: "import-api"
content-type: "api-doc"
order: 2

sections:
  - content: |
      {% assign eu-region = site.data.stitch.regions | where:"id","europe" | first %}
      The base URL you use to interact with the Import API depends on the [data pipeline region]({{ link.security.supported-operating-regions | prepend: site.baseurl }}) your Stitch account is in.

      For example: If your account is in the {{ eu-region.name }} (`{{ eu-region.region }}`) region, you'll use this base URL in your requests to the Import API: `{{ site.data.import-api.base-urls.europe }}`.

      {% include tip.html content="Use the **Select your region** menu at the top right corner of this page to select your data pipeline region. This will display all API requests in this reference with the correct base URL for your region." %}

      **Not sure what data pipeline region your account is in?** [Click here for help]({{ link.security.supported-operating-regions | prepend: site.baseurl | append: "#identify-data-pipeline-region" }}).

      <table>
      <tr>
      <td>
      <strong>
      Data pipeline region
      </strong>
      </td>
      <td>
      <strong>
      Import API base URL
      </strong>
      </td>
      </tr>
      {% for region in site.data.stitch.regions %}
      <tr>
      <td>
      {{ region.name }} ({{ region.region }})
      </td>
      <td>
      {{ site.data.import-api.base-urls[region.id] }}
      </td>
      </tr>
      {% endfor %}
      </table>

      Your base URL is currently set to: <code class='apiUrl'></code>

      **Note**: If your requests uses the incorrect base URL, the API will respond with a `401 - Unauthorzied` code and an error.
---