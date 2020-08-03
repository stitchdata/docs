---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-sftp-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "SFTP Source Form Property"
api-type: "platform.sftp"
display-name: "SFTP"

source-type: "database"
docs-name: "sftp"
db-type: "sftp"

is-filesystem: true

property-description: |
  CSV files on an FTP server

description: |
  Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append:"#setup-requirements" }}) for requirements for CSV files.


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-common-fields: false
uses-feature-fields: false
uses-start-date: true

object-attributes:
  - name: "host"
    required: true
    internal: false
    type: "string"
    description: "The host address (endpoint) of the SFTP server."
    value: "ftp.example-website.com"

  - name: "port"
    required: true
    internal: false
    type: "integer"
    description: "The port of the SFTP server. The default is `22`."
    value: "22"

  - name: "username"
    required: true
    internal: false
    type: "string"
    description: |
      The username of the SFTP user. If using SSH, this should be the same user that adds the Stitch public key to their `authorized_keys` file. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#configure-ssh-for-server" }}) for instructions.
    value: "<USERNAME>"

  - name: "password"
    required: false
    internal: false
    type: "string"
    description: |
      **Optional**: You only need to provide a password if you aren't using SSH.
    value: "<PASSWORD>"

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

         **Note**: If undefined, data will be loaded to the table in an append-only fashion. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#loading-details" }}) for more info.
      - **date_overrides** - A comma-separated list of header fields in the CSV that should be typed as `datetime` fields in the destination. For example: `updated_at,created_at`

         **Note:** If columns aren't specified and values can't be parsed as dates, Stitch will load data for the columns as nullable strings. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#discovery--data-types" }}) for more info.
      - **delimiter** - The field separator delimiter used in the CSV files. Accepted values are:

         - `,` - Comma
         - `|` - Pipe
         - `\t` - Tab

    value: |
      [{\"search_pattern\":\"customers.csv\",\"search_prefix\":\"exports\/files\",\"table_name\":\"customers\",\"key_properties\":\"id\",\"date_overrides\":\"created_at\",\"delimiter\":\",\"},{\"search_pattern\":\"orders.csv\",\"search_prefix\":\"exports\/files\",\"table_name\":\"orders\",\"key_properties\":\"id\",\"date_overrides\":\"updated_at\",\"delimiter\":\",\"}]
---