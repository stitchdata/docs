---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-mysql-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "MySQL Source Form Property"
api-type: "mysql"
display-name: "MySQL"

source-type: "database"
docs-name: "mysql"
db-type: "mysql"

description: ""


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

## See these fields in _data/connect/common/database-sources.yml > all-databases
## This object will also list the fields in the `mysql` list ^

uses-common-fields: true
uses-feature-fields: true
uses-feature-fields: true

object-attributes:
  - name: "check_hostname"
    type: "string"
    required: false
    description: |
      **Optional**: This property works with the `verify_mode` property to validate that the hostname of the database server matches the name in the provided certificate. Accepted values are:

      - `true`
      - `false`

      **Note**: If you don't want to use a custom CA, this property and the `verify_mode` property should both be enabled (`true`).
    value: "true"
    
  - name: "ssl_ca"
    type: "string"
    required: false
    description: |
      **Optional**: The certificate (typically a CA or server certificate) Stitch should verify the SSL connection against. The connection will succeed only if the server's certifcate verifies against the certificate provided.

      **Note**: Providing a certifcate via this property isn't required to use SSL. This is only if Stitch should verify the connection against a specific certificate.
    value: "<SSL_CERTIFICATE>"
  
  - name: "ssl_cert"
    type: "string"
    required: false
    description: |
      **Optional**: If `ssl_client_auth_enabled: true`, the SSL client authentication cerficiate stitch should use. The `ssl_key` property must also be provided to ensure the connection is successful.
    value: "<CA_CERTIFICATE>"

  - name: "ssl_client_auth_enabled"
    type: "string"
    required: false
    description: |
      **Optional**: Indicates if SSL client authentication should be used. Accepted values are:

      - `true`
      - `false`
    value: "true"

  - name: "ssl_key"
    type: "string"
    required: false
    description: |
      **Optional**: If `ssl_client_auth_enabled: true`, the SSL client authentication key stitch should use. The `ssl_ca` property must also be provided to ensure the connection is successful.
    value: "<CA_KEY>"
    
  - name: "verify_mode"
    type: "string"
    required: false
    description: |
      **Optional**: SSL certificate verification is enabled when a Certificate Authority (CA) is provided. If `true`, Stitch will enforce it in lieu of a custom CA. Accepted values are:

      - `true`
      - `false'

      **Note**: If you don't want to use a custom CA, this property and the `check_hostname` property should both be enabled (`true`).
    value: "true"
---