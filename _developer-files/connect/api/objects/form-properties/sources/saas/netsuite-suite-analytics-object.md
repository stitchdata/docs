---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-netsuite-suite-analytics-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "NetSuite Suite Analytics Source Form Property"
api-type: "platform.netsuite-suite-analytics"
display-name: "NetSuite Suite Analytics"

source-type: "saas"
docs-name: "netsuite-suite-analytics"

description: ""

property-description: |
  NetSuite SuiteAnalytics


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-common-fields: true

object-attributes:
  - name: "account_id"
    type: "string"
    required: true
    description: |
      The account ID for the NetSuite account being connected, as found on the account's **Set Up SuiteAnalytics Connect** page. Refer to the [{{ form-property.display-name }} docs](#retrieve-suite-analytics-connect) for more info.
    value: "123456"

  - name: "host"
    type: "string"
    required: true
    description: |
      The host address for the NetSuite account being connected, as found on the account's **Set Up SuiteAnalytics Connect** page. Refer to the [{{ form-property.display-name }} docs](#retrieve-suite-analytics-connect) for more info.
    value: "<NETSUITE_ACCOUNT_ID>.connect.api.netsuite.com"

  - name: "password"
    type: "string"
    required: true
    description: |
      The password for the Stitch NetSuite user. Refer to the [{{ form-property.display-name }} docs](#create-stitch-netsuite-user) for more info.
    value: "<PASSWORD>"
  
  - name: "port"
    type: "string"
    required: true
    description: |
      The port for the NetSuite account being connected, as found on the account's **Set Up SuiteAnalytics Connect** page. Refer to the [{{ form-property.display-name }} docs](#retrieve-suite-analytics-connect) for more info.
    value: "1708"

  - name: "role_id"
    type: "string"
    required: true
    description: |
      The internal ID of the role assigned to the Stitch NetSuite user. Refer to the [{{ form-property.display-name }} docs](#get-role-internal-id) for more info.
    value: "1001"

  - name: "username"
    type: "string"
    required: true
    description: |
      The username for the Stitch NetSuite user. Refer to the [{{ form-property.display-name }} docs](#create-stitch-netsuite-user) for more info.
    value: "<USERNAME>"
---