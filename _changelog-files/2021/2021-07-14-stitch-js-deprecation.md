---
title: "Stitch Connect JavaScript (Stitch.js) deprecation"
content-type: "changelog-entry"
date: 2021-07-14
entry-type: deprecation
entry-category: connect-api

functionality:
  - js: "addSource"
    api-endpoint: |
      {{ site.data.connect.core-objects.sources.create.method | upcase }} {{ site.data.connect.core-objects.sources.create.name | flatify }}
    api-link: "{{ site.data.connect.core-objects.sources.create.anchor }}"
    guide: &create-configure-source |
      [Create and configure a source]({{ site.data.urls.connect.guides.create-configure-a-source }})

  - js: "authorizeSource"
    api-endpoint: &edit-source-endpoint |
      {{ site.data.connect.core-objects.sources.update.method | upcase }} {{ site.data.connect.core-objects.sources.update.name | flatify }}
    api-link: &edit-source-link "{{ site.data.connect.core-objects.sources.update.anchor }}"
    guide: |
      [Configure OAuth for a source]({{ site.data.urls.connect.guides.configure-connection-oauth }})

  - js: "displayDiscovery"
    api-endpoint: |
      {{ site.data.connect.core-objects.streams.list.method | upcase }} {{ site.data.connect.core-objects.streams.list.name | flatify }}
    api-link: "{{ site.data.connect.core-objects.streams.list.anchor }}"
    guide: |
      [Field selection compatability rules]({{ site.data.urls.connect.guides.field-selection-compatibility-rules }})

  - js: "selectStreamsForSource"
    api-endpoint: |
      {{ site.data.connect.core-objects.streams.update.method | upcase }} {{ site.data.connect.core-objects.streams.update.name | flatify }}
    api-link: "{{ site.data.connect.core-objects.streams.update.anchor }}"
    guide: |
      [Select streams and fields]({{ site.data.urls.connect.guides.select-streams-and-fields }}) 

  - js: "editSource"
    api-endpoint: *edit-source-endpoint
    api-link: *edit-source-link
    guide: *create-configure-source
---
As of today, the Stitch Connect JavaScript client, or Stitch.js, has been deprecated.

**What does this mean?**

Stitch.js will continue to function, but Stitch will no longer formally support its use.

**Does this affect the Connect API?**

The only endpoint affected by this change is the [Create a Session]({{ site.data.urls.connect.api | prepend: site.baseurl | prepend: site.home | append: site.data.connect.core-objects.sessions.create.anchor }}) endpoint. All other endpoints in the Connect API remain unchanged.

**When will it stop functioning?**

We don't have a sunset, or end-of-life, date set just yet. If and when a sunset date is chosen, we'll communicate it here and through other support channels.

**What should you do instead?**

If you're using Stitch.js, transition to using parallel functionality in the Connect API.

The following table lists all Stitch.js functions, the Connect API endpoint that provides the same functionality, and links to resources that explain how to perform the functions in the API.

<table style="font-size: 13px;">
  <tr>
    <td>
      <strong>Stitch.js function</strong>
    </td>
    <td>
      <strong>Connect API endpoint</strong>
    </td>
    <td>
      <strong>How-to guide</strong>
    </td>
  </tr>
  {% for function in entry.functionality %}
    <tr>
      <td>
        {{ function.js }}
      </td>
      <td>
        <a href="{{ site.data.urls.connect.api | prepend: site.baseurl | prepend: site.home | append: function.api-link | flatify }}">
          {{ function.api-endpoint | flatify }}
        </a>
      </td>
      <td>
        {{ function.guide | flatify | markdownify }}
      </td>
    </tr>
  {% endfor %}
</table>

**What about performing OAuth for sources?**

The Connect API can still perform OAuth for sources that support it. Check out the [Configure OAuth for a Data Source with the Connect API guide]({{ site.data.urls.connect.guides.configure-connection-oauth | prepend: site.baseurl | prepend: site.home }}) for step-by-step instructions. 