---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-mailchimp-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "MailChimp Source Form Property"
api-type: "platform.mailchimp"
display-name: "MailChimp"

source-type: "saas"
docs-name: "mailchimp"

description: ""


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "page_size"
    type: "string"
    required: false
    description: |
      An optional parameter used to reduce the amount of data requested in a single API request. Refer to the [{{ form-property.display-name }} repository](https://github.com/singer-io/tap-mailchimp/pull/12){:target="new"} for more info.
    value: "250"
---