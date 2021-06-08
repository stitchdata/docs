---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Identifying An Integration's Version and Status
keywords: integrations, integration, version, version number, integration status, status, version status
permalink: /integrations/identify-an-integration-version
summary: "Identify the version an integration is running using its Extraction Logs."

layout: general
toc: false
input: false
feedback: true

key: "identify-integration-version"
content-type: "guide"


# -------------------------- #
#         GUIDE INTRO        #
# -------------------------- #

intro: |
  {% include misc/data-files.html %}

  To ensure you're viewing the documentation for the correct version of your integration, you should first check its version in Stitch.

  In this guide, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}


# -------------------------- #
#      CONTENT SECTIONS      #
# -------------------------- #

sections:
  - title: "Understand integration versioning in Stitch"
    anchor: "understand-integration-versioning"
    summary: "How versioning works in Stitch"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "Version statuses"
        anchor: "version-statuses"
        content: |
          The following table describes each of the statuses an integration version can be in at a given time:

          - **Name**: The name of the status. **Note**: We use these status names mainly in the Stitch Docs - only versions in `beta` will have a `beta` flag in Stitch.
          - **Status in API**: The `pipeline_state` value the status corresponds to in the API. Contained in a [`details` object]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.data-structures.details.section }}), the `pipeline_state` attribute indicates the current version status of an integration.
          - **Availability**: Indicates the availability of the version in Stitch or the API:
              - **Unavailable**: The version isn't available. New connections can't be created.
              - **Private**: The version is available only to accounts who have been granted access.
              - **Available**: The version is generally available, depending on the plan type required for the integration. For example: If an integration is **Enterprise**, only users of an Enterprise plan will have access to it.
          - **Description**: A description of the status, including in-app and support availability

          {% assign version-statuses = site.data.stitch.version-statuses %}

          <table>
            <tr>
              <td width="15%; fixed">
                <strong>Name</strong>
              </td>
              <td width="20%; fixed">
                <strong>Status in API</strong>
              </td>
              <td>
                <strong>Availability</strong>
              </td>
              <td>
                <strong>Description</strong>
              </td>
            </tr>
            {% for status in version-statuses.all %}
              <tr>
                <td>
                  <strong>{{ status.name | capitalize | replace:"-"," " }}</strong>
                </td>
                <td>
                  <code>{{ status.api }}</code>
                </td>
                <td>
                  {{ status.availability | capitalize }}
                </td>
                <td>
                  {{ version-statuses[status.name]description | flatify | markdownify }}
                </td>
              </tr>
            {% endfor %}
          </table>

  - title: "Identify an integration's version"
    anchor: "identify-version-in-stitch"
    summary: "How to identify an integration's version in Stitch"
    content: |
      1. [Sign into your Stitch account]({{ site.sign-in }}){:target="new"}.
      2. On the {{ app.page-names.dashboard }} page, click the {{ integration.display_name }} integration you want to check.
      3. Click the **Extraction Logs** tab:
         - If you see **No logs available for this integration yet.**, the version of the integration doesn't support the Extraction Logs feature. Refer to the [Legacy integration versions section](#legacy-integration-versions) below for more info.
         - **If you see a list of Extraction Logs:**

           Open the most recent set of logs and look at the first line:

           ![Integration version information highlighted in an integration's extraction logs]({{ site.baseurl }}/images/integrations/general-extraction-log-version.png)

           The string following `tap-<name> version` is the version of the integration you're using. In this example, that's `1.0.8`, which corresponds to **v1**.

           **Note**: Only major version identifiers are reflected in integration documentation, i.e. `1` versus `1.0.8`.

  - title: "Legacy integration versions"
    anchor: "legacy-integration-versions"
    summary: ""
    content: |
      The integrations in the table below only have a single running version, which is listed in the table. When and if these integrations are converted to Singer taps, they will support [Extraction Logs]({{ link.replication.extraction-logs | prepend: site.baseurl }}) and you'll be able to identify their version using the method above.

      {% assign legacy-db-integrations = site.database-integrations | where:"singer",false %}

      {% assign all-legacy-integrations = site.saas-integrations | where:"singer",false | concat: legacy-db-integrations | sort_natural:"display_name" %}

      <table class="attribute-list">
      <tr>
      <td class="attribute-name"><strong>Integration</strong></td>
      <td><strong>Version</strong></td>
      <td><strong>Release date</strong></td>
      </tr>
      {% for integration in all-legacy-integrations %}
      {% include shared/versioning/integration-version-logic.html connection-type="integration" item-name="integration" %}

      {% if this-version.status == "released" %}
      <tr>
      <td class="attribute-name">
      <a href="{{ integration.url | prepend: site.baseurl }}">{{ integration.display_name }}</a>
      </td>
      <td>
      {{ integration.this-version | prepend: "v" }}
      </td>
      <td>
      {{ this-version.date-released }}
      </td>
      </tr>
      {% endif %}
      {% endfor %}
      </table>
---