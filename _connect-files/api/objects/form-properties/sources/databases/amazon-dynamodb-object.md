---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/connect-templates/database-source-form-property/
## FOR INSTRUCTIONS & REFERENCE INFO

## PLEASE REMOVE COMMENTS WHEN FINISHED


# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

content-type: "api-form"
form-type: "source"
key: "source-form-properties-amazon-dynamodb-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Amazon DynamoDB Source Form Property"
api-type: "platform.dynamodb"
display-name: "Amazon DynamoDB"

source-type: "database"
docs-name: "amazon-dynamodb"
db-type: "dynamodb"

property-description: |
  CSV files in an Amazon DynamoDB bucket

description: |
  Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append:"#setup-requirements" }}) for requirements for CSV files.


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-common-fields: false
uses-feature-fields: false
uses-start-date: true

object-attributes:
  - name: "account_id"
    type: "string"
    required: true
    description: |
      The user's Amazon Web Services (AWS) Account ID. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#retrieve-aws-account-id" }}) for more info.
    value: "123456789101"

  - name: "external_id"
    type: "string"
    required: true
    description: |
      The external ID associated with the Amazon Web Services (AWS) Identity Access Management (IAM) role used by Stitch. In AWS, external IDs are used to increase role security when granting access to accounts that you don't own or have administrative access to. Stitch will provide this ID when accessing {{ form-property.display-name }}.

      This value can be anything, but it must be the same as the external ID provided in the AWS console when creating the Stitch IAM role. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#create-stitch-iam-role" }}) for more info.
    value: "stitch_connection_12345"
    
  - name: "role_name"
    type: "string"
    required: true
    description: |
      The name of the AWS IAM role Stitch should assume when extracting data from Amazon S3. This role will have the permissions in the IAM policy associated with the role.

      Refer to our [{{ form-property.display-name }} documentation]({{ doc-link | append: "#grant-access-bucket-iam" }}){:target="new"} for more info about the IAM policy, role, and how to create them in AWS.
    value: "<ROLE_NAME>"

  - name: "use_local_dynamo"
    type: "string"
    required: false
    description: ""
    value: "True/False"

  - name: "region_name"
    type: "string"
    required: true
    description: ""
    value: "<YOUR_REGION>"  
---