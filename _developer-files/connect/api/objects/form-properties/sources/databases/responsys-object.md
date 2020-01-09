---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-responsys-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Responsys Source Form Property"
api-type: "platform.responsys"
display-name: "Responsys"

source-type: "database"
docs-name: "responsys"
db-type: "responsys"

is-filesystem: true

description: ""


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-common-fields: false
uses-feature-fields: false
uses-start-date: true

object-attributes:
  - name: "host"
    required: true
    type: "string"
    description: |
      The host address of the {{ form-property.display-name }} SFTP server. If the server is hosted by Oracle, this will likely be `files.responsys.net`.
    value: "<HOST_ADDRESS>"

  - name: "port"
    required: true
    type: "string"
    description: "The port of the SFTP server. As Stitch uses an SSH tunnel to connect to {{ form-property.display-name }}, this will likely be the default SSH port (`{{ port }}`)."
    value: "{{ port }}"

  - name: "username"
    required: true
    type: "string"
    description: "The username of the {{ integration }} database user."
    value: "<USERNAME>"

  - name: "path"
    required: true
    type: "string"
    description: "The file server path where completed {{ form-property.display-name }} export files are stored."
    value: "<PATH>"
---