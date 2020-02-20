---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-heap-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Heap Source Form Property"
api-type: "platform.heap"
display-name: "Heap"

source-type: "saas"
docs-name: "heap"

## This is used to fill in the description that displays in the source form property rollup and under the object itself.

property-description: "data dumps in Amazon S3 buckets"

## Full copy is: "Heap connections read data from [data dumps in Amazon S3 buckets] and correspond to source type: platform.heap."

# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "account_id"
    type: "string"
    required: true
    description: |
      Your Amazon Web Services account ID. Refer to the [Heap documentation]({{ doc-link | append: "#retrieve-aws-account-id" }}) for instructions on retrieving this info.
    value: "123456789123"

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

      This value can be anything, but it must be the same as the role name provided in the AWS console when creating the Stitch IAM role.

      Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#create-stitch-iam-role" }}){:target="new"} for more info.
    value: "stitch_heap_CNTl5Br9"

  - name: "bucket"
    type: "string"
    required: true
    description: |
      The name of the bucket Stitch should replicate {{ form-property.display-name }} data from. {{ form-property.display-name }} [requires that bucket names](https://docs.heapanalytics.com/docs/heap-sql-retroactive-s3-specification#section-data-delivery){:target="new"} be prefixed with `heap-rs3-`. 
    value: "heap-rs3-<BUCKET_NAME>"
---