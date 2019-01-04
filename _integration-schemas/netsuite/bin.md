---
tap: "netsuite"
# version: "10-15-2015"

name: "netsuite_bin"
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/bin.html
description: |
  The `{{ table.name }}` table contains info about the bins in your NetSuite instance.



replication-method: "Full Table"
primary-key: "internalId"
abstract: false

permissions:
- name: "Bins"
  level: "View"
  location: "Lists"

attributes:
  - name: "internalId"
    type: "integer"
    primary-key: true
    description: "The bins ID."

  - name: "Your Selected Fields"
    description: |
      Other fields selected by you. For a list of available attributes, refer to [{{ integration.display_name }}'s documentation]({{ table.doc-link }}){:target="new"}. **Note**: You will need to log into your {{ integration.display_name }} account to view the documentation.
---