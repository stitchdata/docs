---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Understanding Integration Versioning and Upgrades in Stitch
keywords: integrations, integration, version, version number, integration status, status, version status
permalink: /integrations/identify-an-integration-version
summary: "Learn about the integration versioning process in Stitch and how to identify the version your integrations are using."

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

  To ensure we're providing improvements and fixes without breaking your downstream processes, Stitch versions its integrations. This allows you to understand what's coming and make any necessary changes before you decide to upgrade.

  In this guide, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}


# -------------------------- #
#      CONTENT SECTIONS      #
# -------------------------- #

sections:
  - title: "Understand integration versioning in Stitch"
    anchor: "understand-versioning"
    summary: "How versioning works in Stitch"
    content: |
      In this section, we'll cover:

      {% for subsection in section.subsections %}
      - [{{ subsection.summary }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "Version numbers"
        anchor: "version-numbers"
        summary: "How to read version identifiers"
        content: |
          {% include note.html type="single-line" content="**Note**: Versions in the docs do not refer to supported versions (if applicable) for an integration. For example: `PostgreSQL (v1)` doesn't mean Stitch only supports version 1 of PostgreSQL - it's just referring to Stitch's version of a PostgreSQL connection." %}

          If you've [previously checked an integration's version](#identify-version-in-stitch), you might've noticed that version numbers in Stitch and what we have in the docs look a little different.

          In the docs, we only use the **major version identifier** when referring to an integration's version. For example: You might see `1.0.8` in Stitch, but in the docs we'll use `1` (or `v1`) to refer to the version. Check out the [next section](#identify-version-in-stitch) for an example.

          **Note**: For some integrations, you'll see a version that's formatted like a date, such as `v15-10-2015`. These are legacy versions that pre-date the [Singer]() framework and indicate that an integration isn't backed by a Singer tap. Refer to the [Legacy integration versions](#legacy-integration-versions) section for more info.

      - title: "Version upgrades"
        anchor: "version-upgrades"
        summary: "How the version upgrade process works"
        content: |
          Most of the time, you'll only need to upgrade an integration's version when we release a new major version. Minor versions and patches are typically applied automatically.

          When a new major version is made generally available (or **Released**, as noted in the [next section](#version-statuses)), a few things will happen:

          1. The preceeding version is removed from Stitch. New connections can only be created using the new version, but existing connections will continue to run.
          1. We'll communicate a **deprecation date** for the preceeding version, at which point Stitch will no longer offer support for it.
          1. After a period of time, we'll communicate a **sunset date** for the preceeding version. Integrations using the now-sunset version will stop running.

          Upgrading to a new major version requires you to re-create the integration in your account and re-replicate historical data.

          **Note**: If you delete the original integration and re-use its namespace (schema name), the re-replication will count towards your row usage. However, if you use a new namespace, the first seven days of replication will be subject to the [free historical data load]({{ link.billing.faq | prepend: site.baseurl | append: "#historical-data-loads" }}) and not count towards your usage.

      - title: "Version statuses"
        anchor: "version-statuses"
        summary: "The statuses each version goes through during its lifecycle"
        content: |
          The following table describes each of the statuses an integration version can be in at a given time:

          - **Name**: The name of the status. **Note**: We use these status names mainly in the Stitch Docs - only versions in `beta` will have a `beta` flag in Stitch.
          - **Status in API**: The `pipeline_state` value the status corresponds to in the API. Contained in a [`details` object]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.data-structures.details.section }}), the `pipeline_state` attribute indicates the current version status of an integration.
          - **Availability**: Indicates the availability of the version in Stitch or the API:
              - **Unavailable**: The version isn't available. New connections can't be created.
              - **Private**: The version is available only to accounts who have been granted access.
              - **Available**: The version is generally available, depending on the plan type required for the integration. For example: If an integration is **{{ site.data.stitch.subscription-plans.advanced.name }} or {{ site.data.stitch.subscription-plans.premium.name }}**, only users of these plans will have access to it.
          - **Description**: A description of the status, including in-app and support availability

          {% assign version-statuses = site.data.stitch.version-statuses %}

          <table>
            <tr>
              <td width="20%; fixed">
                <strong>Name</strong>
              </td>
              <td width="20%; fixed">
                <strong>Status(es) in API</strong>
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
                  <strong>
                    {{ status.display-name }}
                  </strong>
                </td>
                <td>
                  <code>{{ status.api }}</code>
                </td>
                <td>
                  {{ status.availability | capitalize }}
                </td>
                <td>
                  <ul>
                  {% for note in version-statuses[status.name]notes %}
                    <li style="margin-top: 0px;">{{ note | flatify | markdownify }}</li>
                  {% endfor %}
                  </ul>
                </td>
              </tr>
            {% endfor %}
          </table>

  - title: "Identify an integration's version"
    anchor: "identify-version-in-stitch"
    summary: "How to identify an integration's version in Stitch"
    content: |
      To ensure you're viewing the documentation for the correct version of your integration, you should first check its version in Stitch.

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
    summary: "Legacy integration versions"
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