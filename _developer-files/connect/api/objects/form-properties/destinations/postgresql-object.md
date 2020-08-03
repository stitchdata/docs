---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "destination"
key: "destination-form-properties-postgresql-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "PostgreSQL Destination Form Property"
api-type: "postgres"
display-name: "PostgreSQL"

docs-name: "postgres"
db-type: "postgres"

description: ""


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-common-fields: true
## See these fields in _data/connect/common/destination-forms.yml > all-destinations

object-attributes:
  - name: "sslrootcert"
    type: "string"
    required: false
    read-only: false
    description: |
      **Optional**: The certificate (typically a CA or server certificate) Stitch should verify the SSL connection against. The connection will succeed only if the server's certificate verifies against the certificate provided.

      **Note**: Providing a certificate via this property isn't required to use SSL. This is only if Stitch should verify the connection against a specific certificate.
    value: |
      "<OPTIONAL_SSL_CERTIFICATE>"
---