---
tap: "netsuite"
version: "10-15-2015"

name: "netsuite_billing_schedule"
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2015_1/schema/record/billingschedule.html
description: |
  The `{{ table.name }}` table contains info about the accounts in your NetSuite instance.

replication-method: "Full Table"
primary-key: "internalId"
abstract: false

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "billing-schedule"

attributes:
  - name: "internalId"
    type: "integer"
    primary-key: true
    description: "The account ID."

  - name: "Additional fields"
    description: |
      For a list of available attributes, refer to [{{ integration.display_name }}'s documentation]({{ table.doc-link }}){:target="new"}. **Note**: You will need to log into your {{ integration.display_name }} account to view the documentation. 
---