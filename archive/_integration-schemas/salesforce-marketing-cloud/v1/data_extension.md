---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-table-schema/
## FOR INSTRUCTIONS & REFERENCE INFO


tap: "salesforce-marketing-cloud"
version: "1"

name: "data_extension"
doc-link: https://developer.salesforce.com/docs/atlas.en-us.noversion.mc-apis.meta/mc-apis/dataextensionobject.htm
singer-schema: https://github.com/singer-io/tap-exacttarget/blob/master/tap_exacttarget/endpoints/data_extensions.py
description: |
  The `{{ table.name }}` table contains info about the data extensions in your {{ integration.display_name }} account. A table will be created for each [data extension](https://help.salesforce.com/articleView?id=mc_cab_data_extensions.htm&type=5){:target="new"} in your {{ integration.display_name }} account.

  For example: If there are two data extensions named `MobileAddress` and `MobileSubscription`, two tables would be created: `{{ table.name }}._MobileAddress` and `{{ table.name }}._MobileSubscription`

  **Note**: Retrieving data extension data requires [**Read, Write** permissions for Data Extensions](#add-api-component-to-package).

replication-method: "Full Table"

api-method:
  name: "Retrieve all data extensions"
  doc-link: "https://developer.salesforce.com/docs/atlas.en-us.noversion.mc-apis.meta/mc-apis/dataextensionobject.htm"

attributes:
  - name: "_CustomObjectKey"
    type: "string"
    primary-key: true
    description: "The data extension's custom object key."

  - name: "CategoryID"
    type: "integer"
    description: "The ID of the category the data extension is associated with."

  - name: "Custom fields"
    type: ""
    description: |
      The fields for the data extension, set in the **Email Studio** app of your {{ integration.display_name }} account. For example: If a data extension has `id`, `name`, and `date` fields, these are the fields that will display in Stitch.

      To view the fields for a given data extension, locate the data extension in the **Email Studio** app in your {{ integration.display_name }} account.
---