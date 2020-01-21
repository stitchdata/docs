---
tap: "shippo"
version: "1"

name: "parcels"
doc-link: https://goshippo.com/docs/reference#parcels
singer-schema: 
description: |
  The `{{ table.name }}` table contains info about parcel objects. Parcels are used to create shipments, obtain rates, and print labels.

replication-method: "Key-based Incremental"
api-method:
  name: listAllParcels
  doc-link: https://goshippo.com/docs/reference?version=2016-10-25#parcels-list

attributes:
  - name: "object_id"
    type: "string"
    primary-key: true
    description: "The parcel ID."
    foreign-key-id: "parcel-id"

  - name: "object_updated"
    type: "date-time"
    replication-key: true
    description: "The last time the parcel was updated."

  - name: "object_state"
    type: "string"
    description: "The state of the parcel. Ex: `VALID`"

  - name: "object_created"
    type: "date-time"
    description: "The time the parcel was created."

  - name: "object_owner"
    type: "string"
    description: "The username of the user who created the parcel."

  - name: "template"
    type: "string"
    description: |
      This is the template defined for the parcel. A parcel template is a predefined package used by one or multiple carriers.

      Click the link in the left column for more info about possible values in Shippo's documentation.
    doc-link: https://goshippo.com/docs/reference?version=2016-10-25#parcel-templates

  - name: "length"
    type: "string"
    description: "The length of the parcel."

  - name: "width"
    type: "string"
    description: "The width of the parcel."

  - name: "height"
    type: "string"
    description: "The height of the parcel."

  - name: "distance_unit"
    type: "string"
    description: |
      The unit used for length, width, and height. Possible values are:

      - `cm`
      - `in`
      - `ft`
      - `mm`
      - `m`
      - `yd` 

  - name: "weight"
    type: "string"
    description: "The weight of the parcel."

  - name: "mass_unit"
    type: "string"
    description: |
      The unit used for weight. Possible values include:

        - `g`
        - `oz`
        - `lb`
        - `kg`

  - name: "metadata"
    type: "string"
    description: "Additional information about the parcel."

  - name: "extra"
    type: "object"
    description: |
      Optional extra services requested for each parcel in a multi-parcel shipment.

      Click the link in the left column for more info about possible values in Shippo's documentation.
    doc-link: https://goshippo.com/docs/reference?version=2016-10-25#parcels-extras

  - name: "test"
    type: "boolean"
    description: "Indicates if the parcel was created in test mode."
---