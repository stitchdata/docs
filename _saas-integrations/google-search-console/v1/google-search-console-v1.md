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
permalink: /integrations/saas/google-search-console ## Add if there are multiple versions: /v1
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

tap-name: "Google Search Console" ## Ex: Intercom, not intercom
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
tier: "Free"

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
      **An admin account**. Admin access is required in your {{ integration.display_name }} account to change certain settings.

setup-steps:
  - title: "Set up your {{ integration.display_name }}"
    anchor: "set-up-console"
    content: |
      If you don't have any URLs set up in your {{ integration.display_name }} account, use the following instructions. If you do, you can skip to [step 2](#create-project).
      1. Login to your Google account and navigate to [{{ integration.display_name }}](https://search.google.com/search-console).
      2. Add the domains or websites for your organization. If adding a domain, it will cover all URLs across all of its subdomains. If adding a website, only the entered websites will be counted for.
      3. Verify your site ownership by clicking **CONTINUE**. Depending on your verification method, this can take up to a day.
      4. Once your link(s) are verified, add them to the `sitemap.xml` files in the **Sitemaps** section of your {{ integration.display_name }} account. Click **Submit**.

  - title: "Create a {{ integration.display_name }} project"
    anchor: "create-project"
    content: |
      You can skip to [step 3](#enable-apis) if you already have a project in your {{ integration.display_name }} account. If not, use the following instructions.
      1. Login to your [**Google Cloud Console**](https://console.cloud.google.com).
      2. Click **Create New Project**.
      3. Enter a **Project name** and select a project **Location**.
      4. Click **CREATE**.

  - title: "Enable {{ integration.display_name }} API"
    anchor: "enable-apis"
    content: |
      1. Login to your **Google Cloud Platform**. Make sure you are inside the project that you will use for your {{ integration.display_name }} integration.
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
      1. Staying in the **APIs & Services** section, click on **OAuth consent screen** in the left-hand menu panel.
      2. Select your project.
      3. Make the **Application type** `Public`.
      4. Make the **Application name** `tap-google-search-console`.
      5. Add an image for a logo to help you identify your app.
      6. In the **Support email** field, enter your email that you will use for this app.
      7. In the **Scope** section, click **Add scope**.
      8. Add the following scope: `Google Search Console API ../auth/webmasters.readonly`.
      9. In the **Authorized domains** section, add your domains that you added from [step 1](#set-up-console).
      10. Click **SAVE**.
      11. You will be taken to a screen that says **OAuth grant limits**. The default raise limit is one hour. You may increase the raise limit up to 30 days.

  - title: "Create OAuth credentials"
    anchor: "create-credentials"
    content: |
      1. Staying in the **APIs & Services** section, click on **Credentials** in the left-hand menu panel.
      2. Click on the **Create credentials** dropdown menu.
      3. Select **OAuth client ID**.
      4. In the **Create OAuth client ID** page, select **Web application** for the Application type.
      5. In the **Name** field, enter `tap-google-search-console`.
      6. In the **Authorized redirect URIs** section, add your domains that you added from [step 1](#set-up-console).
      7. Click **CREATE**.

  - title: "add integration"
    content: |
      4. In the **Site Urls** field, enter the URLs you added to your sitemap file in [step 1](#set-up-console).
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data" ## remove this if the integration doesn't support at least table selection


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/google-search-console


# Remove this if you don't need it:
# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |
---
{% assign integration = page %}
{% include misc/data-files.html %}