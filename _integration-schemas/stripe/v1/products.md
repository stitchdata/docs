---
tap: "stripe"
version: "1.0"

name: "products"
doc-link: "https://stripe.com/docs/api/products"
singer-schema: "https://github.com/singer-io/tap-stripe/blob/master/tap_stripe/schemas/products.json"
description: |
  The `{{ table.name }}` table contains info about your products.
  
replication-method: "Key-based Incremental"

api-method:
    name: "List all products"
    doc-link: "https://stripe.com/docs/api/products/list"
    
attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "Unique identifier for the object."
    foreign-key-id: "product-id"

  - name: "object"
    type: "string"
    description: "The type of {{ integration.display_name }} object. This will be `product`."
    
  - name: "active"
    type: "boolean"
    description: "Whether the product is currently available for purchase."
    
  - name: "attributes"
    type: "array"
    description: "A list of up to 5 attributes that each SKU can provide values for (e.g., ["color", "size"]). Only applicable to products of type=good."
  
  - name: "caption"
    type: "string"
    description: "A short one-line description of the product, meant to be displayable to the customer. Only applicable to products of type=good."
    
  - name: "created"
    type: "date-time"
    description: "Time at which the product was created. Measured in seconds since the Unix epoch."

  - name: "deactivate_on"
    type: "array"
    description: "An array of connect application identifiers that cannot purchase this product. Only applicable to products of type=good."
    
  - name: "description"
    type: "string"
    description: "The product’s description, meant to be displayable to the customer. Only applicable to products of type=good."
     
  - name: "images"
    type: "array"
    description: "A list of up to 8 URLs of images for this product, meant to be displayable to the customer. Only applicable to products of type=good."
 
  - name: "livemode"
    type: "boolean"
    description: "Indicates if the object exists in live mode (`true`) or in test mode (`false`)."
   
  - name: "metadata"
    type: "object"
    description: "Additional information attached to the invoice line item."
    subattributes: &metadata
      - name: "ANYTHING"
        type: "ANYTHING"
        description: "This info will vary."

  - name: "name"
    type: "string"
    description: "The product’s name, meant to be displayable to the customer. Applicable to both service and good types."

  - name: "package_dimensions"
    type: "object"
    description: "The dimensions of this product for shipping purposes. A SKU associated with this product can override this value by having its own package_dimensions. Only applicable to products of type=good."
    subattributes:
      - name: "height"
        type: "decimal"
        description: "Height, in inches."

      - name: "length"
        type: "decimal"
        description: "Length, in inches."
        
      - name: "width"
        type: "decimal"
        description: "Width, in inches."

      - name: "weight"
        type: "decimal"
        description: "Weight, in ounces."

  - name: "shippable"
    type: "boolean"
    description: "Whether this product is a shipped good. Only applicable to products of type=good."

  - name: "statement_descriptor"
    type: "string"
    description: "Extra information about a product which will appear on your customer’s credit card statement. In the case that multiple products are billed at once, the first statement descriptor will be used. Only available on products of type=service."

  - name: "type"
    type: "string"
    description: "The type of the product. The product is either of type good, which is eligible for use with Orders and SKUs, or service, which is eligible for use with Subscriptions and Plans."

  - name: "unit_label"
    type: "string"
    description: "A label that represents units of this product, such as seat(s), in Stripe and on customers’ receipts and invoices. Only available on products of type=service."
     
  - name: "updated"
    type: "date-time"
    replication-key: true
    description: "The time at which the product was last updated."
 
  - name: "url"
    type: "string"
    description: " URL of a publicly-accessible webpage for this product. Only applicable to products of type=good."
     
---
