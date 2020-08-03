---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-amazon-s3-csv-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Amazon S3 CSV Source Form Property"
api-type: "platform.s3-csv"
display-name: "Amazon S3 CSV"

source-type: "database"
docs-name: "amazon-s3-csv"
db-type: "s3-csv"

is-filesystem: true

property-description: |
  CSV files in an Amazon S3 bucket

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

  - name: "bucket"
    type: "string"
    required: true
    description: "The name of the bucket Stitch should replicate data from. This value should not contain any URLs, `https`, or S3 parts."
    value: "com-test-stitch-bucket"

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

  - name: "tables"
    type: "string"
    required: true
    description: |
      A series of properties defining the CSV files to be tracked as tables. For every table configuration, this property will contain a JSON object with the following properties. **Note**: Every property should be an escaped string.

      Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append:"#setup-requirements" }}) for requirements for CSV files.

      - **search_pattern** - The search criteria Stitch should use when selecting CSV files for extraction. This can be the name of a single file or a regular expression. For example: `customers.csv` or `*\.csv`
      - **search_prefix** - The directory path Stitch should limit the file search to. For example: `exports/data`
      - **table_name** - The name of the table as it should appear in the destination. For example: `customers`
      - **key_properties** - A comma-separated list of header fields in the CSV files Stitch can use to uniquely identify records. For example: `_id,date`

         **Note**: If undefined, data will be loaded to the table in an append-only fashion. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#primary-keys-append-only" }}) for more info.
      - **date_overrides** - A comma-separated list of header fields in the CSV that should be typed as `datetime` fields in the destination. For example: `updated_at,created_at`

         **Note:** If columns aren't specified and values can't be parsed as dates, Stitch will load data for the columns as nullable strings. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#determining-data-types" }}) for more info.
      - **delimiter** - The field separator delimiter used in the CSV files. Accepted values are:

         - `,` - Comma
         - `|` - Pipe
         - `\t` - Tab

    value: |
      [{\"search_pattern\":\"customers.csv\",\"search_prefix\":\"exports\/files\",\"table_name\":\"customers\",\"key_properties\":\"id\",\"date_overrides\":\"created_at\",\"delimiter\":\",\"},{\"search_pattern\":\"orders.csv\",\"search_prefix\":\"exports\/files\",\"table_name\":\"orders\",\"key_properties\":\"id\",\"date_overrides\":\"updated_at\",\"delimiter\":\",\"}]
---