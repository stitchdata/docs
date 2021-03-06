---
tap: "slack"
version: "1"
key: "remote-file"

name: "remote_files"
doc-link: "https://api.slack.com/methods/files.remote.list"
singer-schema: "https://github.com/singer-io/tap-slack/blob/master/tap_slack/schemas/remote_files.json"
description: |
  The `{{ table.name }}` table contains info about remote files added to {{ integration.display_name }}.

# Commenting until the tap creator confirms the correct 
# behavior of this table, as it's currently broken.

replication-method: "Key-based Incremental"

api-method:
  name: "files.remote.list"
  doc-link: "https://api.slack.com/methods/files.remote.list"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The remote file ID."
    #foreign-key-id: "remote-file-id"

  - name: "updated"
    type: "date-time"
    description: "The time the file was last updated."
    replication-key: true  

  - name: "channels"
    type: "array"
    description: "The channels the remote file was shared in."
    subattributes:
      - name: "value"
        type: "string"
        description: "The channel ID."
        foreign-key-id: "channel-id"

  - name: "comments_count"
    type: "integer"
    description: ""

  - name: "created"
    type: "date-time"
    description: ""

  - name: "date_delete"
    type: "date-time"
    description: ""

  - name: "display_as_bot"
    type: "boolean"
    description: ""

  - name: "editable"
    type: "boolean"
    description: ""

  - name: "editor"
    type: "string"
    description: ""

  - name: "external_id"
    type: "string"
    description: ""

  - name: "external_type"
    type: "string"
    description: ""

  - name: "external_url"
    type: "uri"
    description: ""

  - name: "filetype"
    type: "string"
    description: ""

  - name: "groups"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: "The group ID."
        foreign-key-id: "group-id"

  - name: "has_rich_preview"
    type: "boolean"
    description: ""

  - name: "image_exif_rotation"
    type: "integer"
    description: ""

  - name: "ims"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "is_external"
    type: "boolean"
    description: ""

  - name: "is_public"
    type: "boolean"
    description: ""

  - name: "is_starred"
    type: "boolean"
    description: ""

  - name: "is_tombstoned"
    type: "boolean"
    description: ""

  - name: "last_editor"
    type: "string"
    description: ""

  - name: "mimetype"
    type: "string"
    description: ""

  - name: "mode"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "non_owner_editable"
    type: "boolean"
    description: ""

  - name: "num_stars"
    type: "integer"
    description: ""

  - name: "original_h"
    type: "integer"
    description: ""

  - name: "original_w"
    type: "integer"
    description: ""

  - name: "permalink"
    type: "uri"
    description: ""

  - name: "permalink_public"
    type: "uri"
    description: ""

  - name: "pinned_info"
    type: "object"
    description: ""

  - name: "pinned_to"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""
        foreign-key-id: "channel-id"

  - name: "pretty_type"
    type: "string"
    description: ""

  - name: "preview"
    type: "string"
    description: ""

  - name: "public_url_shared"
    type: "boolean"
    description: ""

  - name: "size"
    type: "integer"
    description: ""

  - name: "source_team"
    type: "string"
    description: "The source's team ID."
    foreign-key-id: "team-id"

  - name: "state"
    type: "string"
    description: ""

  - name: "thumb_1024"
    type: "uri"
    description: ""

  - name: "thumb_1024_h"
    type: "integer"
    description: ""

  - name: "thumb_1024_w"
    type: "integer"
    description: ""

  - name: "thumb_160"
    type: "uri"
    description: ""

  - name: "thumb_360"
    type: "uri"
    description: ""

  - name: "thumb_360_h"
    type: "integer"
    description: ""

  - name: "thumb_360_w"
    type: "integer"
    description: ""

  - name: "thumb_480"
    type: "uri"
    description: ""

  - name: "thumb_480_h"
    type: "integer"
    description: ""

  - name: "thumb_480_w"
    type: "integer"
    description: ""

  - name: "thumb_64"
    type: "uri"
    description: ""

  - name: "thumb_720"
    type: "uri"
    description: ""

  - name: "thumb_720_h"
    type: "integer"
    description: ""

  - name: "thumb_720_w"
    type: "integer"
    description: ""

  - name: "thumb_80"
    type: "uri"
    description: ""

  - name: "thumb_800"
    type: "uri"
    description: ""

  - name: "thumb_800_h"
    type: "integer"
    description: ""

  - name: "thumb_800_w"
    type: "integer"
    description: ""

  - name: "thumb_960"
    type: "uri"
    description: ""

  - name: "thumb_960_h"
    type: "integer"
    description: ""

  - name: "thumb_960_w"
    type: "integer"
    description: ""

  - name: "thumb_tiny"
    type: "string"
    description: ""

  - name: "timestamp"
    type: "date-time"
    description: ""

  - name: "title"
    type: "string"
    description: ""
  
  - name: "url_private"
    type: "uri"
    description: ""

  - name: "url_private_download"
    type: "uri"
    description: ""

  - name: "user"
    type: "string"
    description: "The ID of the user who shared the remote file."
    foreign-key-id: "user-id"

  - name: "user_team"
    type: "string"
    description: "The ID of the team that the `user` belongs to."
    foreign-key-id: "team-id"

  - name: "username"
    type: "string"
    description: ""
---