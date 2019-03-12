---
tap: "bigcommerce"
version: "1.0"

name: "products"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-bigcommerce/blob/master/tap_bigcommerce/schemas/products.json"
description: |
  The `{{ table.name }}` table contains info about the products in your {{ integration.display_name }} store.

  **Note**: During the initial replication job for a {{ integration.display_name }} integration, all products will be replicated. On subsequent replication jobs, only new and updated product records will be replicated.

replication-method: "Key-based Incremental"
api-method:
    name: "Get all products"
    doc-link: "https://developer.bigcommerce.com/api-reference/catalog/catalog-api/products/getproducts"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The product ID."
    foreign-key-id: "product-id"

  - name: "date_modified"
    type: "date-time"
    replication-key: true
    description: "The date the order was last modified, in RFC 2822 format."

  - name: "availability"
    type: "string"
    description: |
      The availability of the product. Possible values are:

      - `available` - The product can be purchased on the storefront
      - `disabled` - The product is listed in the storefront but can't be purchased
      - `preorder` - The product is listed for pre-order

  - name: "availability_description"
    type: "string"
    description: "A description of the product's `availability` that displays under the product title on the checkout page. This usually tells the customer how long it usually takes to ship this product. For example: `Usually ships in 24 hours`"

  - name: "base_variant_id"
    type: "integer"
    description: "The ID of the base variant associated with a simple product. This value will be null for complex products."

  - name: "bin_picking_number"
    type: "string"
    item-type: "product"
    description: &bin-picking-number "The BIN picking number for the {{ attribute.item-type }}."

  - name: "brand_id"
    type: "integer"
    description: "The ID of the brand associated with the product."

  - name: "brand_name"
    type: "string"
    description: "The name of the brand associated with the product."

  - name: "bulk_pricing_rules"
    type: "array"
    description: "The bulk pricing rules associated with the product."
    array-attributes:
      - name: "id"
        type: "integer"
        primary-key: true
        description: "The bulk pricing rule ID."

      - name: "amount"
        type: "number"
        description: "The value of the adjustment by the bulk pricing rule."

      - name: "quantity_max"
        type: "integer"
        description: "The maximum inclusive quantity of a product needed to satisfy the rule. Must be greater than the `quantity_min` value."

      - name: "quantity_min"
        type: "integer"
        description: "The minimum inclusive quantity of a product needed to satisfy the rule."

      - name: "type"
        type: "string"
        description: |
          The type of adjustment made when the rule is satisfied. Possible values are:

          - `price` - The adjustment amount per product
          - `percent` - The adjustment as a percentage of the original price
          - `fixed` - The adjusted aboslute price of the product

  - name: "calculated_price"
    type: "number"
    item-type: "product"
    description: &calculated-price "The price of the {{ attribute.item-type }} as seen on the storefront. This will be equal to the `sale_price` if set, otherwise this will be equal to `price`."

  - name: "categories"
    type: "array"
    description: "A list of IDs for the categories that the product belongs to."
    array-attributes:
      - name: "value"
        type: "integer"
        primary-key: true
        description: "The category ID."

  - name: "condition"
    type: "string"
    description: |
      The product condition, which is shown on the product page if `is_condition_shown: true`. Possible values are:

      - `New`
      - `Used`
      - `Refurbished`

  - name: "cost_price"
    type: "number"
    item-type: "product"
    description: &cost-price "The cost price of the {{ attribute.item-type }}."

  - name: "custom_fields"
    type: "object"
    description: "Custom fields associated with the product."
    object-attributes:
      - name: "id"
        type: "integer"
        description: "The ID of the custom field."

      - name: "name"
        type: "string"
        description: "The name of the custom field."

      - name: "value"
        type: "string"
        description: "The value of the custom field."

  - name: "custom_url"
    type: "object"
    description: "The custom URL for the product on the storefront."
    object-attributes:
      - name: "is_customized"
        type: "boolean"
        description: "Indicates if the product URL has been customized."

      - name: "url"
        type: "string"
        description: "The custom URL for the product."

  - name: "date_created"
    type: "date-time"
    description: "The date the order was created, in RFC 2822 format."

  - name: "depth"
    type: "number"
    item-type: "product"
    description: &depth "The depth of the {{ attribute.item-type }}, which can be used when calculating shipping costs."

  - name: "description"
    type: "string"
    description: "The product description, which can include HTML formatting."

  - name: "fixed_cost_shipping_price"
    type: "number"
    item-type: "product"
    description: &fixed-cost-shipping "The fixed shipping cost for the {{ attribute.item-type }}."

  - name: "gift_wrapping_options_list"
    type: "array"
    description: "A list of gift wrapping option IDs associated with the product."
    array-attributes:
      - name: "value"
        type: "integer"
        primary-key: true
        description: "The gift wrapping option ID."

  - name: "gift_wrapping_options_type"
    type: "string"
    description: |
      The type of the gift wrapping options available for the product. Possible values are:

      - `any` - Allows any gift wrapping options in the store
      - `none` - Disallows gift wrapping on the product
      - `list` - Gift wrapping options listed in `gift_wrapping_options_list` are allowed for the product

  - name: "gtin"
    type: "string"
    description: "The Global Trade Item Number for the product."

  - name: "height"
    type: "number"
    item-type: "product"
    description: &height "The height of the {{ attribute.item-type }}, which can be used when calculating shipping costs."

  - name: "images"
    type: "array"
    description: "Images associated with the product."
    array-attributes:
      - name: "id"
        type: "integer"
        primary-key: true
        description: "The image ID."

      - name: "product_id"
        type: "integer"
        primary-key: true
        description: "The ID of the product associated with the image."
        foreign-key-id: "product-id"

      - name: "date_modified"
        type: "date-time"
        description: "The date the image was last modified, in RFC 2822 format."

      - name: "description"
        type: "string"
        description: "The description for the image."

      - name: "image_file"
        type: "string"
        description: "The local path to the original image file uploaded to {{ integration.display_name }}."

      - name: "is_thumbnail"
        type: "boolean"
        description: "Indicates if the image is to be used as the product's thumbnail."

      - name: "sort_order"
        type: "integer"
        description: "The order in which the image will be displayed on the product page. Higher integers give the image a lower priority."

      - name: "url_standard"
        type: "string"
        description: "The standard URL for the image."

      - name: "url_thumbnail"
        type: "string"
        description: "The thumbnail URL for the image."

      - name: "url_tiny"
        type: "string"
        description: "The tiny URL for the image."

      - name: "url_zoom"
        type: "string"
        description: "The zoom URL for the image."

  - name: "inventory_level"
    type: "integer"
    item-type: "product"
    description: &inventory-level "The current inventory level of the {{ attribute.item-type }}."

  - name: "inventory_tracking"
    type: "string"
    item-type: "product"
    description: &inventory-tracking |
      The type of inventory tracking for the {{ attribute.item-type }}. Possible values are:

      - `none` - Inventory levels aren't tracked
      - `product` - Inventory levels are tracked using `inventory_level` and `inventory_warning_level`
      - `variant` - Inventory levels are tracked based on variants

  - name: "inventory_warning_level"
    type: "integer"
    item-type: "product"
    description: &inventory-warning-level "The inventory warning level for the {{ attribute.item-type }}."

  - name: "is_condition_shown"
    type: "boolean"
    description: "Indicates whether the product condition is shown to the customer on the product page."

  - name: "is_featured"
    type: "boolean"
    description: "Indicates whether the product should be included in the Featured Products panel when viewing the store."

  - name: "is_free_shipping"
    type: "boolean"
    item-type: "product"
    description: &free-shipping "Indicates whether the {{ attribute.item-type }} has free shipping."

  - name: "is_preorder_only"
    type: "boolean"
    description: |
      When `true`, the release date and the preorder status will be automatically removed.

      When `false`, the release date and preorder status will not be automatically removed; these settings must be changed in the {{ integration.display_name }} control panel.

  - name: "is_price_hidden"
    type: "boolean"
    description: "Indicates whether the product's price should be shown on the product page."

  - name: "is_visible"
    type: "boolean"
    description: "Indicates whether the product should be displayed to customers browsing the store."

  - name: "layout_file"
    type: "string"
    description: "The layout template file used to render the product category."

  - name: "map_price"
    type: "number"
    description: ""

  - name: "meta_description"
    type: "string"
    description: "The custom meta description for the product page."

  - name: "meta_keywords"
    type: "string"
    description: "The custom meata keywords for the product page."

  - name: "mpn"
    type: "string"
    description: "The Manufacturer Part Number for the product."

  - name: "name"
    type: "string"
    description: "The product name."

  - name: "open_graph_description"
    type: "string"
    description: "The description to use for the product."

  - name: "open_graph_title"
    type: "string"
    description: "The title of the product."

  - name: "open_graph_type"
    type: "string"
    description: "The type of the product."

  - name: "open_graph_use_image"
    type: "boolean"
    description: "Indicates whether the product image or open graph image is used."

  - name: "open_graph_use_meta_description"
    type: "boolean"
    description: "Indicates whether the product `description` or `open_graph_description` is used."

  - name: "open_graph_use_product_name"
    type: "boolean"
    description: "Indicates whether the product `name` or `open_graph_title` is used."

  - name: "option_set_display"
    type: "string"
    description: ""

  - name: "option_set_id"
    type: "integer"
    description: ""

  - name: "order_quantity_maximum"
    type: "integer"
    description: "The maximum quantity an order can contain when purchasing the product."

  - name: "order_quantity_minimum"
    type: "integer"
    description: "The minimum order an order must contain when purchasing the product."

  - name: "page_title"
    type: "string"
    description: "The custom title for the product page."

  - name: "preorder_message"
    type: "string"
    description: "The custom expected-date message to display on the product page."

  - name: "preorder_release_date"
    type: "string"
    description: "If the product is a preorder, this will contain the release date."

  - name: "price"
    type: "number"
    item-type: "product"
    description: &price "The price of the {{ attribute.item-type }}. **Note**: Depending on your store settings, this value may or may not include tax."

  - name: "price_hidden_label"
    type: "string"
    description: ""

  - name: "product_tax_code"
    type: "string"
    description: |
      The tax code associated with the product.

  - name: "related_products"
    type: "array"
    description: "A list of IDs of related products."
    array-attributes:
      - name: "value"
        type: "integer"
        primary-key: true
        description: "The related product ID."
        foreign-key-id: "product-id"

  - name: "retail_price"
    type: "number"
    description: "The retail cost of the product."

  - name: "reviews_count"
    type: "integer"
    description: "The number of times the product has been rated."

  - name: "reviews_rating_sum"
    type: "integer"
    description: "The total rating for the product."

  - name: "sale_price"
    type: "number"
    item-type: "product"
    description: &sale-price "The sale price for the {{ attribute.item-type }}."

  - name: "search_keywords"
    type: "string"
    description: "A comma-separated list of keywords used to locate the product when searching the store."

  - name: "sku"
    type: "string"
    item-type: "product"
    description: &sku "The {{ attribute.item-type }}'s SKU."

  - name: "sort_order"
    type: "integer"
    description: "The priority to give the product when included in product lists on category pages and search results."

  - name: "tax_class_id"
    type: "integer"
    description: "The ID of the tax class applied to the product."

  - name: "total_sold"
    type: "integer"
    description: "The total number of times the product has been sold."

  - name: "type"
    type: "string"
    description: |
      The product type. Possible values are:

      - `physical`
      - `ditial`

  - name: "upc"
    type: "string"
    item-type: "upc"
    description: &upc "The {{ attribute.item-type }}'s UPC."

  - name: "variants"
    type: "array"
    description: ""
    item-type: "variant"
    array-attributes:
      - name: "id"
        type: "integer"
        primary-key: true
        description: "The variant ID."

      - name: "product_id"
        type: "integer"
        primary-key: true
        description: "The product ID."
        foreign-key-id: "product-id"

      - name: "bin_picking_number"
        type: "string"
        description: *bin-picking-number

      - name: "calculated_price"
        type: "number"
        description: *calculated-price

      - name: "cost_price"
        type: "number"
        description: *cost-price

      - name: "depth"
        type: "number"
        description: *depth

      - name: "fixed_cost_shipping_price"
        type: "number"
        description: *fixed-cost-shipping

      - name: "height"
        type: "number"
        description: *height

      - name: "image_url"
        type: "string"
        description: "The image that will be displayed when this variant is selected on the storefront."

      - name: "inventory_level"
        type: "integer"
        description: *inventory-level

      - name: "inventory_warning_level"
        type: "integer"
        description: *inventory-warning-level

      - name: "is_free_shipping"
        type: "boolean"
        description: *free-shipping

      - name: "map_price"
        type: "number"
        description: ""

      - name: "option_values"
        type: "array"
        description: "A list of option and option value IDs that make up the variant."
        array-attributes:
          - name: "id"
            type: "integer"
            primary-key: true
            description: "The option value ID."

          - name: "option_id"
            type: "integer"
            primary-key: true
            description: "The option ID."

          - name: "label"
            type: "string"
            description: "The label of the option value."

          - name: "option_display_name"
            type: "string"
            description: "The name of the option."

      - name: "price"
        type: "number"
        description: *price

      - name: "purchasing_disabled"
        type: "boolean"
        description: "Indicates if the variant is available for purchase on the storefront."

      - name: "purchasing_disabled_message"
        type: "string"
        description: "The message that displays when the variant is disabled for purchasing and selected on the storefront."

      - name: "sale_price"
        type: "number"
        description: *sale-price

      - name: "sku"
        type: "string"
        description: *sku

      - name: "sku_id"
        type: "integer"
        description: "A reference to {{ integration.display_name }}'s v2 API SKU ID."

      - name: "upc"
        type: "string"
        description: *upc

      - name: "weight"
        type: "number"
        description: &weight "The weight of the {{ attribute.item-type }}, used to calculate shipping costs."

      - name: "width"
        type: "number"
        description: &width "The width of the {{ attribute.item-type }}, used to calculate shipping costs."

  - name: "videos"
    type: "array"
    description: ""
    array-attributes:
      - name: "id"
        type: "integer"
        primary-key: true
        description: "The product video ID."

      - name: "description"
        type: "string"
        description: "The description of the video."

      - name: "length"
        type: "string"
        description: "The length of the video."

      - name: "product_id"
        type: "integer"
        description: "The ID of the product associated with the video."

      - name: "sort_order"
        type: "integer"
        description: "The order in which the video will be displayed on the product page. Higher integers give a lower priority."

      - name: "title"
        type: "string"
        description: "The title of the video."

      - name: "type"
        type: "string"
        description: "The video type."

      - name: "video_id"
        type: "string"
        description: "The ID of the video on a host site."

  - name: "view_count"
    type: "integer"
    description: "The number of times the product has been viewed."

  - name: "warranty"
    type: "string"
    description: "The warranty information for the product, displayed on the product page."

  - name: "weight"
    type: "number"
    item-type: "product"
    description: *weight

  - name: "width"
    type: "number"
    item-type: "product"
    description: *width
---