---
tap: "snapchat-ads"
version: "1"
key: ""

name: "media"
doc-link: https://developers.snapchat.com/api/docs/#get-all-media
singer-schema: https://github.com/singer-io/tap-snapchat-ads/blob/master/tap_snapchat_ads/schemas/media.json
description: "This stream retrieves all media entities associated with an ad account"

replication-method: "Key-based Incremental"

table-key-properties: "id"
valid-replication-keys: "updated_at"

attributes:
  - name: "id"
    type: "string"
    description: "Id of the media"
    primary-key: true

  - name: "updated_at"
    type: "date-time"
    description: "Date and time at which the media was updated"
    replication-key: true

  - name: "created_at"
    type: "date-time"
    description: "Date and time at which the media was created/uploaded"

  - name: "name"
    type: "string"
    description: "Name of the media"

  - name: "ad_account_id"
    type: "string"
    description: "Id of the Ad Account"

  - name: "type"
    type: "string"
    description: "Media type. Example: Image, Video, LENS_PACKAGE"

  - name: "media_status"
    type: "string"
    description: "Status of the media availability."

  - name: "file_name"
    type: "string"
    description: "Name of the media file"

  - name: "download_link"
    type: "string"
    description: "Link to download the media file"

  - name: "file_size_in_bytes"
    type: "integer"
    description: "Size of the meida file in bytes"

  - name: "is_demo_media"
    type: "boolean"
    description: ""

  - name: "hash"
    type: "string"
    description: ""

  - name: "visibility"
    type: "string"
    description: ""

  - name: "image_metadata"
    type: "object"
    description: "Metadata of the image uploaded"
    subattributes:
      - name: "height_px"
        type: "integer"
        description: "Height of the image in pixels"
      
      - name: "width_px"
        type: "integer"
        description: "Widht of the image in pixels"
      
      - name: "image_format"
        type: "string"
        description: "Format of the image uploaded. Example: PNG, JPG etc.."

  - name: "video_metadata"
    type: "object"
    description: "Metadata of the video uploaded"

  - name: "lens_package_metadata"
    type: "object"
    description: "Metadata for lens media created by Lens Studio"
---