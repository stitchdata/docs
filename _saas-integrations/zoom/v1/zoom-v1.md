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

title: Zoom
permalink: /integrations/saas/zoom
keywords: zoom, integration, schema, etl zoom, zoom etl, zoom schema
layout: singer
# input: false

key: "zoom-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "zoom"
display_name: "Zoom"

singer: true
status-url: "https://status.zoom.us/"

tap-name: "Zoom"
repo-url: https://github.com/singer-io/tap-zoom

this-version: "1"

api: |
  [Zoom REST API v2](https://marketplace.zoom.us/docs/api-reference/introduction){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false

api-type: "platform.zoom"

historical: ""
frequency: "1 hour"
tier: "Free"

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
      **Account Privileges**. **Admin privileges** if you plan to connect to Stitch using a {{ integration.display_name }} OAuth app. **Developer role** if you plan to connect to Stitch using a {{ integration.display_name }} JSON Web Tokens (JWT) app.
      
  - item: |
      Either a {{ integration.display_name }} OAuth or JWT app. If you don't have either of those and would like to create an OAuth app, [click here)](https://marketplace.zoom.us/docs/guides/build/oauth-app) for more information. If you would like to make a JWT app instead, [click here](https://marketplace.zoom.us/docs/guides/build/jwt-app).

requirements-info:
  If using a {{ integration.display_name }} OAuth App to connect to Stitch, make sure that the following scopes are added to the app:
    - account:read:admin
    - meeting:read:admin
    - report:read:admin
    - user:read:admin
    - webinar:read:admin

setup-steps:
  - title: "Obtain tokens"
    anchor: "obtain-tokens"
    content: |
      1. Login to your {{ integration.display_name }} account on the [{{ integration.display_name }} App Marketplace](https://marketplace.zoom.us/){:target="new"}.
      2. Click **Manage** in the upper right corner of the page.
      3. Click on the OAuth or JWT app you'd like to use to connect to Stitch.
      4. If using a JWT app, copy the **JWT**. If using an OAuth app, copy the **Client ID**, **Client Secret**, and **Refresh Token**.
      5. Keep your token(s) readily available for the next step.
  - title: "add integration"
    content: |
      4. If connecting to Stitch with a {{ integration.display_name }} OAuth app, paste the **Client ID**, **Client Secret**, and **Refresh Token** you obtained in [step 1](#obtain-tokens) into their respective fields.
      5. If connecting to Stitch with a {{ integration.display_name }} JWT app, paste the **JWT** you obtained in [step 1](#obtain-tokens) into its respective field.
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data" ## remove this if the integration doesn't support at least table selection


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/zoom


# Remove this if you don't need it:
# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |
---
{% assign integration = page %}
{% include misc/data-files.html %}