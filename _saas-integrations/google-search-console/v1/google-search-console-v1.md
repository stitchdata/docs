---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas/
## FOR INSTRUCTIONS & REFERENCE INFO


# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Google Search Console (v1)
permalink: /integrations/saas/google-search-console
keywords: google-search-console, integration, schema, etl google-search-console, google-search-console etl, google-search-console schema
layout: singer
# input: false

key: "google-search-console-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "google-search-console"
display_name: "Google Search Console"

singer: true
status-url: "https://www.google.com/appsstatus#hl=en&v=status"

tap-name: "Google Search Console"
repo-url: https://github.com/singer-io/tap-google-search-console

this-version: "1"

api: |
  [{{ integration.display_name }} API](https://developers.google.com/webmaster-tools/search-console-api-original/v3/how-tos/search_analytics){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true 

historical: "1 year"
frequency: "1 hour"
tier: "Standard"

api-type: "platform.google-search-console"

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true

# attribution-window: "# days"
# attribution-is-configurable: 

# setup-name: ""


# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.


# -------------------------- #
#      Incompatibilities     #
# -------------------------- #

## uncomment section below if integration is compatible with any Stitch destinations
## if incompatible with multiple destinations, create a section for each destination

## incompatible:
  ## [redshift]: "always,sometimes,never"
  ## reason: "copy" 

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **Admin access in {{ integration.display_name }}**. Admin access is required in your {{ integration.display_name }} account to change settings required to connect Stitch.

setup-steps:
  - title: "Set up your {{ integration.display_name }}"
    anchor: "set-up-console"
    content: |
      {% capture skip-urls %}
      **If you don't have any URLs set up in your {{ integration.display_name }} account**, use the following instructions. Otherwise skip to [step 2](#create-project).
      {% endcapture %}
      {% include note.html type="single-line" content=skip-urls %}
      1. Login to your Google account and navigate to [{{ integration.display_name }}](https://search.google.com/search-console){:target="new"}.
      2. Add the domains or websites for your organization. If adding a domain, it will cover all URLs across all of its subdomains. If adding a website, only the entered websites will be counted for.
      3. Verify your site ownership by clicking **CONTINUE**. Depending on your verification method, this can take up to a day.
      4. Once your link(s) are verified, add them to the `sitemap.xml` files in the **Sitemaps** section of your {{ integration.display_name }} account. Click **Submit**.

  - title: "Create a {{ integration.display_name }} project"
    anchor: "create-project"
    content: |
      {% capture skip-project %}
      **If you don't have a project set up in {{ integration.display_name }}** use the following instructions. Otherwise skip to [step 3](#enable-apis).
      {% endcapture %}
      {% include note.html type="single-line" content=skip-project %}
      1. Login to your [**Google Cloud Console**](https://console.cloud.google.com).
      2. Click **Create New Project**.
      3. Enter a **Project name** and select a project **Location**.
      4. Click **CREATE**.

  - title: "Enable {{ integration.display_name }} API"
    anchor: "enable-apis"
    content: |
      1. Login to your **Google Cloud Platform** account. Make sure you're in the project that you want to use for your {{ integration.display_name }} integration.
      2. Select **APIs & Services** from the left-hand menu panel. This will take you to the **APIs & Services** dashboard.
      3. In the dashboard, click **ENABLE APIS AND SERVICES**. You will be redirected to the **API Library**.
      4. Search for {{ integration.display_name }} and select `{{ integration.display_name }} API`.
      5. Click **ENABLE**.

  - title: "Verify API domain"
    anchor: "verify-api-domain"
    content: |    
      1. Staying in the **APIs & Services** section, click on **Domain verification** in the left-hand menu panel.
      2. Click **Add domain**.
      3. Add the domain you're using for this project.

  - title: "API OAuth consent"
    anchor: "oauth-consent"
    content: |
      1. Staying in the **APIs & Services** section, click on the **OAuth consent screen** in the left-hand menu panel.
      2. Select your project.
      3. Make the **Application type** `Public`.
      4. Make the **Application name** `tap-google-search-console`.
      5. Optionally, you can add an image for a logo to help you identify your app.
      6. In the **Support email** field, enter your email that you will use for this app.
      7. In the **Scope** section, click **Add scope**.
      8. Add the following scope: `Google Search Console API ../auth/webmasters.readonly`.
      9. In the **Authorized domains** section, add the domains that you added to {{ integration.display_name}} in [step 1](#set-up-console).
      10. Click **SAVE**.
      11. You will be taken to a screen that says **OAuth grant limits**. The default limit is 100 grants per minute, per day. You can request to raise the grant limit for your project by clicking **Raise limit**. You can also change the time interval grant resets. The options for time intervals are: `1h`, `6h`, `1d,`, `7d`, and `30d`.

  - title: "Create OAuth credentials"
    anchor: "create-credentials"
    content: |
      1. Staying in the **APIs & Services** section, click on **Credentials** in the left-hand menu panel.
      2. Click on the **Create credentials** dropdown menu.
      3. Select **OAuth client ID**.
      4. In the **Create OAuth client ID** page, select **Web application** for the Application type.
      5. In the **Name** field, enter `tap-google-search-console`.
      6. In the **Authorized redirect URIs** section, add the domains that you added in [step 1](#set-up-console).
      7. Click **CREATE**.

  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      1. In the **Site Urls** field, enter the URLs you added to your sitemap file in [step 1](#set-up-console). The URLs should be comma delimited and begin with `https://` or `http://`. Example: `https://yoursite.com, http://yourothersite.com`.
      
      **Note**: If you get an error saying that the user doesn't have sufficient permissions or that the URL is not a verified {{ integration.display_name}} site, try replacing `https://` or `http://` with `sc-domain:`. Example: `sc-domain:yoursite.com`.
  - title: "Define the historical replication start date"
    anchor: "define-historical-sync"
    content: |
      {% include integrations/saas/setup/historical-sync.html %}
  
  - title: "Create a replication schedule"
    anchor: "define-rep-frequency"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}

  - title: "Set objects to replicate"
    anchor: "setting-data-to-replicate"
    content: |
      {% include integrations/shared-setup/data-selection/object-selection.html %}


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/google-search-console/v1
---
{% assign integration = page %}
{% include misc/data-files.html %}
