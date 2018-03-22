---
tap: "zuora"
version: 1.0

name: "product"
doc-link: http://knowledgecenter.zuora.com/DC_Developers/SOAP_API/E1_SOAP_API_Object_Reference/Product#Field_Descriptions
description: |
  The `product` table contains info about your company's product offerings.


replication-method: "Incremental"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The product ID."
    ## foreign-keys:
    ##   - table-name: "invoiceItem"
    ##     attribute: "productId"

    ##   - table-name: "productRatePlan"
    ##     attribute: "productId"

  - name: "updatedDate"
    type: "date-time"
    replication-key: true
    description: "The date when the product was last updated."

  - name: "allowFeatureChanges"
    type: "boolean"
    description: "If `true`, users can add and remove features while creating or amending subscriptions."

  - name: "category"
    type: "string"
    description: |
      The product's category. Possible values are:

      - `Base Products`
      - `Add On Services`
      - `Miscellaneous Products`

  - name: "createdById"
    type: "string"
    description: "The ID of the Zuora user who created the product."

  - name: "createdDate"
    type: "date-time"
    description: "The date the product was created."

  - name: "description"
    type: "string"
    description: "The description of the product."

  - name: "effectiveEndDate"
    type: "date-time"
    description: "The date when the product expires and can't be subscribed to anymore."

  - name: "effectiveStartDate"
    type: "date-time"
    description: "The date when the product becomes available and can be subscribed to."

  - name: "name"
    type: "string"
    description: "The name of the product."

  - name: "sku"
    type: "string"
    description: "The unique SKU for the product."

  - name: "updatedById"
    type: "string"
    description: "The ID of the Zuora user who last updated the product."

---