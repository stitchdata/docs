---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Connecting Other Data Sources to Stitch
permalink: /integrations/connecting-other-data-sources-to-stitch
keywords: integrations unsupported other data sources where is integration

summary: "Don't see an integration you want in Stitch? Learn about your options for getting data from not-currently-supported data sources into Stitch."

layout: general
toc: true

level: "guide"
key: "other-data-sources"
weight: 4

# -------------------------- #
#   RELATED SIDEBAR LINKS    #
# -------------------------- #

related:
  - title: "Set up your Stitch data pipeline"
    link: "{{ link.getting-started.onboarding | prepend: site.baseurl }}"

  - title: "All integrations"
    link: "{{ site.baseurl }}/integrations"

  - title: "Import API reference"
    link: "{{ link.import-api.getting-started }}"

  - title: "Incoming Webhooks"
    link: "{{ link.integrations.stitch-incoming-webhooks }}"


# -------------------------- #
#         GUIDE INTRO        #
# -------------------------- #

intro: |
  {% include misc/data-files.html %}

  If you don't see the integration you want in Stitch, don't worry - there are options! In this guide, we'll cover the best methods for getting data from not-currently-supported data sources into Stitch:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}


# -------------------------- #
#      CONTENT SECTIONS      #
# -------------------------- #

sections:
  - title: "Build a Singer tap"
    anchor: "build-a-singer-tap"
    summary: "Build a Singer tap (recommended)"
    content: |
      Stitch’s source integrations are powered by [Singer]({{ site.singer }}){:target="new"}, an open source standard for ETL that allows data engineers to replicate data from any source to any destination. Stitch runs these Singer integrations — known as taps — in our infrastructure, allowing you to leave the orchestration, security, and reliability of your data pipelines to us.

      This is the approach we recommend.

    subsections:
      - title: "How Singer taps work"
        anchor: "how-singer-taps-work"
        content: |
          Singer's extensible platform makes it easy to add any data source you need. You can build a Singer tap and use the [Stitch target]({{ site.singer | append:"/target/stitch/" }}){:target="new"}, which is our Import API, to push the data to Stitch, where the data will be processed like data from any other integration.

          The process will look something like this:

          1. Build the Singer tap.
          2. In your Stitch account, create an [Import API]({{ link.import-api.getting-started | prepend: site.baseurl }}) integration.
          3. Configure the Singer tap to send the data to the Stitch target.
          4. Run the tap and send data to Stitch.
          5. Stitch receives and processes the data.

      - title: "Tap building options"
        anchor: "tap-building-options"
        content: |
          You can build a Singer tap by:

          - **Taking the do-it-yourself/community approach**. If you're the hands-on type, consider building your own Singer tap. This approach ensures that your data extraction logic functions exactly as you need and intend it to. Community integrations are data sources built and maintained by the Singer community, and commercial support is available for Community integrations as part of an Enterprise plan.

          - **Using a Stitch implementation partner.** Stitch has a large and growing network of [implementation partners](https://www.stitchdata.com/partners/#implementation){:target="new"} who are experienced at writing and supporting Singer taps. If you can't or are unable to build the tap yourself, one of our implementation partners can help.

          - **Contracting a Stitch build**. As part of an Enterprise contract, Stitch can build and commercially support custom integrations for your team. We’ll work with you to establish requirements, ensuring the deliverable is to your exact specifications. Contact [Stitch Sales]({{ site.sales }}){:target="new"} for more info.

  - title: "Use the Import API"
    anchor: "use-import-api"
    summary: "Use the Import API"
    content: |
      The Import API is a REST API that allows you to push any arbitrary data into your destination. Data sent to the Import API is processed and sent through Stitch like data from any other integration. To use this method, you can write a script or application that pushes data to the Import API.

      For example: With the Import API, you can push data from sources like [Google Sheets](https://github.com/stitchdata/google-sheets-integration){:target="new"} to Stitch. 

      Refer to the [Import API docs]({{ link.integrations.import-api | prepend: site.baseurl }}) for more info and code samples.

  - title: "Use Incoming Webhooks"
    anchor: "use-incoming-webhooks"
    summary: "Use Incoming Webhooks"
    content: |
      If the data source you want to use is webhook-based, you can use Stitch's Incoming Webhook integration. This integration functions as a receiving point for data pushed by the source webhook.

      This generic integration can be used with dozens of services, even if there isn't a dedicated integration for it in Stitch. The service you're using must meet the following requirements to be compatible with Incoming Webhooks:

      1. The webhook's payload (delivery) must come via a `POST` request.
      2. The request body (data) must be valid JSON.
      3. The request body must be less than 4MB in size.

      Refer to the [Incoming Webhooks docs]({{ link.integrations.stitch-incoming-webhooks | prepend: site.baseurl }}) for more info.

  - title: "Suggest an integration"
    anchor: "suggest-integration"
    summary: "Suggest an integration"
    content: |
      Otherwise, you can use the **Suggest Integration** button on the Integrations page in the Stitch app. We're always looking to add new integrations to our offerings.
      <br><br>
---