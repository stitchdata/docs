---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/connect-templates/source-form-property/
## FOR INSTRUCTIONS & REFERENCE INFO

# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-stripe-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Stripe Source Form Property"
api-type: "platform.stripe"
display-name: "Stripe"

source-type: "saas"
docs-name: "Stripe"

description: ""


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "date_window_size"
    type: "string"
    required: false
    description: "**Internal field.**"
    value: ""

  - name: "whitelist_map"
    type: "string"
    required: false
    description: |
      An optional parameter used to select individual fields from the [`data` attribute in the `events` stream](https://stripe.com/docs/api/events/object){:target="new"}.

      The fields in a `data` object are dependent on the event's `type`. For example: For an `invoice.*` event, the `data` object will contain an `invoice` object. Refer to [{{ form-property.display-name }}'s documentation](https://stripe.com/docs/api/events/types){:target="new"} for a list of supported event types and the fields a `data` object may contain for each event type.

      The value for this property is typed as a `{{ attribute.type | upcase }}` and takes the following form:

      ```json
      {
        "events": [
          ["data","<field_1_breadcrumb>"],
          ["data","<field_2_breadcrumb>"],
          ...
          ["data","<field_n_breadcrumb>"]
        ]
      }
      ```

      The `<field_breadcrumb>` value is the path to the field you want to track. For example: The following would select the `id`, `amount`, `plan`, `plan.id`, and `plan.active` fields:

      ```json
      {
        "events": [
          ["data","id"],
          ["data","amount"],
          ["data","plan"],
          ["data","plan","id"],
          ["data","plan","active"]
        ]
      }
      ```

      Fields for multiple event types may be included in the `{{ attribute.name }}` value.
      
    value: |
      "{\"events\":[[\"data\",\"id\"],[\"data\",\"amount\"],[\"data\",\"plan\"],[\"data\",\"plan\",\"id\"],[\"data\",\"plan\",\"active\"]]}"
---