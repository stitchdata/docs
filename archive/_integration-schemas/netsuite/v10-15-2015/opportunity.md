--- 
tap: "netsuite" 
version: "10-15-2015" 

name: "netsuite_opportunity" 
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2015_1/schema/record/opportunity.html
description: |
  The `{{ table.name }}` table contains info about opportunities.

replication-method: "Key-based Incremental" 
abstract: false 

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "opportunity"

attributes: 
  - name: "internalId" 
    type: "integer" 
    primary-key: true 
    description: |
      The opportunity ID.

  - name: "lastModifiedDate"  
    type: "date-time" 
    replication-key: true 
    description: |
      The time the opportunity was last updated.

  - name: "Additional fields" 
    description: |
      For a list of available attributes, refer to [{{ integration.display_name }}'s documentation]({{ table.doc-link }}){:target="new"}. **Note**: You will need to log into your {{ integration.display_name }} account to view the documentation. 
---