---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-zendesk-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Zendesk Source Form Property"
api-type: "platform.zendesk"
display-name: "Zendesk"

source-type: "saas"
docs-name: "zendesk"

description: ""


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "subdomain"
    type: "string"
    required: true
    description: |
      The prefix of the {{ form-property.display-name }} subdomain Stitch should replicate data from.

      For example: If the address is `stitchdata.{{ form-property.display-name | downcase }}.com`, only `stitchdata` would be entered as the value.
    value: "<YOUR_{{ form-property.display-name | upcase }}_SUBDOMAIN>"
---