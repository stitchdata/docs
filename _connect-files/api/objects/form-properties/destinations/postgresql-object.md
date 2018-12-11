---
content-type: "api-form"
form-type: "destination"
key: "destination-form-properties-postgresql-object"

title: "PostgreSQL Destination Form Property"
api-type: "postgres"
display-name: "PostgreSQL"

docs-name: "postgres"
db-type: "postgres"

description: ""

uses-common-fields: true
object-attributes:
  - name: "sslrootcert"
    type: "string"
    required: false
    description: |
      **Optional**: The certificate (typically a CA or server certificate) Stitch should verify the SSL connection against. The connection will succeed only if the server's certificate verifies against the certificate provided.

      **Note**: Providing a certificate via this property isn't required to use SSL. This is only if Stitch should verify the connection against a specific certificate.
    value: |
      "<OPTIONAL_SSL_CERTIFICATE>"
---