---
tap: "netsuite-suite-analytics"
version: "1"
key: "subsidiary"

name: "subsidiaries"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/subsidiaries.html"
description: |
  The `{{ table.name }}` table contains info about the subsidiary records in your NetSuite account. A subsidiary represents a separate company within your global organization. 

replication-method: "Key-based Incremental"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "date_last_modified"
    type: "date-time"
    replication-key: true
    description: "The time the subsidiary was last modified."

  - name: "subsidiary_id"
    type: "integer"
    netsuite-primary-key: true
    description: "The subsidiary ID. {{ integration.netsuite-primary-key-description | flatify }}"
    foreign-key-id: "subsidiary-id"

  - name: "address"
    type: "string"
    description: "The subsidiary address."

  - name: "address1"
    type: "string"
    description: "The first line of the subsidiary's address."

  - name: "address2"
    type: "string"
    description: "The second line of the subsidiary's address."

  - name: "base_currency_id"
    type: "integer"
    description: "The base currency of the subsidiary."

  - name: "city"
    type: "string"
    description: "The city associated with the subsidiary's address."

  - name: "country"
    type: "string"
    description: "The country associated with the subsidiary's address."

  - name: "edition"
    type: "string"
    description: "The NetSuite edition."

  - name: "federal_number"
    type: "string"
    description: "The federal tax ID of the subsidiary."

  - name: "fiscal_calendar_id"
    type: "integer"
    description: "The fiscal calendar of the subsidiary."
    # foreign-key-id: "fiscal-calendar-id"

  - name: "full_name"
    type: "string"
    description: "The full name of the subsidiary."

  - name: "is_elimination"
    type: "string"
    description: "Whether the subsidiary is an elimination subsidiary."

  - name: "is_moss"
    type: "string"
    description: "Whether the subsidiary uses the MOSS taxation scheme."

  - name: "isinactive"
    type: "string"
    description: "Whether the subsidiary is inactive."

  - name: "isinactive_bool"
    type: "string"
    description: "Whether the subsidiary is inactive."

  - name: "legal_name"
    type: "string"
    description: "The legal name of the subsidiary."

  - name: "moss_nexus_id"
    type: "integer"
    description: "The ID of the Nexus that uses the MOSS taxation scheme."

  - name: "name"
    type: "string"
    description: "The name of the subsidiary."

  - name: "parent_id"
    type: "integer"
    description: "The parent subsidiary."
    # foreign-key-id: "subsidiary-id"

  - name: "purchaseorderamount"
    type: "number"
    description: "The purchase order amount."

  - name: "purchaseorderquantity"
    type: "number"
    description: "The purchase order quantity."

  - name: "purchaseorderquantitydiff"
    type: "number"
    description: "The purchase order quantity difference."

  - name: "receiptamount"
    type: "number"
    description: "The receipt amount."

  - name: "receiptquantity"
    type: "number"
    description: "The receipt quantity."

  - name: "receiptquantitydiff"
    type: "number"
    description: "The receipt quantity difference."

  - name: "return_address"
    type: "string"
    description: "The return address of the subsidiary."

  - name: "return_address1"
    type: "string"
    description: "The first line of the return address."

  - name: "return_address2"
    type: "string"
    description: "The second line of the return address."

  - name: "return_city"
    type: "string"
    description: "The city of the return address."

  - name: "return_country"
    type: "string"
    description: "The country of the return address."

  - name: "return_state"
    type: "string"
    description: "The state of the return address."

  - name: "return_zipcode"
    type: "string"
    description: "The zip code of the return address."

  - name: "shipping_address"
    type: "string"
    description: "The shipping address of the subsidiary."

  - name: "shipping_address1"
    type: "string"
    description: "The first line of the shipping address."

  - name: "shipping_address2"
    type: "string"
    description: "The second line of the shipping address."

  - name: "shipping_city"
    type: "string"
    description: "The city of the shipping address."

  - name: "shipping_country"
    type: "string"
    description: "The country of the shipping address."

  - name: "shipping_state"
    type: "string"
    description: "The state of the shipping address."

  - name: "shipping_zipcode"
    type: "string"
    description: "The zip code of the shipping address."

  - name: "state"
    type: "string"
    description: "The state associated with the subsidiary's address."

  - name: "state_tax_number"
    type: "string"
    description: "The subsidiary's state tax ID."

  - name: "subsidiary_extid"
    type: "string"
    description: "The subsidiary's external ID."

  - name: "tran_num_prefix"
    type: "string"
    description: "The transaction number prefix associated with the subsidiary."

  - name: "url"
    type: "string"
    description: "The URL of the subsidiary."

  - name: "zipcode"
    type: "string"
    description: "The zip code associated with the subsidiary's address."
---