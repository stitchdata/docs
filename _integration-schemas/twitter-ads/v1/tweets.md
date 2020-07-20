---
tap: "twitter-ads"
version: "1"
key: "tweet"

name: "tweets"
doc-link: "https://developer.twitter.com/en/docs/ads/creatives/api-reference/tweets#get-accounts-account-id-scoped-timeline"
singer-schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/tweets.json"
description: |
  The `{{ table.name }}` table contains info about the scheduled and published Tweets associated with an account's full promotable user. **Note**: This table doesn't include draft Tweets.

replication-method: "Key-based Incremental"

api-method:
  name: "Get Tweets"
  doc-link: "https://developer.twitter.com/en/docs/ads/creatives/api-reference/tweets#get-accounts-account-id-scoped-timeline"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
    foreign-key-id: "tweet-id"

  - name: "created_at"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "account_id"
    type: "string"
    description: ""
    foreign-key-id: "account-id"

  - name: "coordinates"
    type: "object"
    description: ""
    subattributes:
      - name: "coordinates"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "number"
            description: ""

      - name: "type"
        type: "string"
        description: ""

  - name: "entities"
    type: "object"
    description: ""
    subattributes:
      - name: "hashtags"
        type: "array"
        description: ""
        subattributes:
          - name: "indices"
            type: "array"
            description: ""
            subattributes:
              - name: "value"
                type: "integer"
                description: ""

          - name: "text"
            type: "string"
            description: ""

      - name: "media"
        type: "array"
        description: ""
        subattributes:
          - name: "display_url"
            type: "string"
            description: ""

          - name: "expanded_url"
            type: "string"
            description: ""

          - name: "id"
            type: "integer"
            description: ""

          - name: "id_str"
            type: "string"
            description: ""

          - name: "indices"
            type: "array"
            description: ""
            subattributes:
              - name: "value"
                type: "integer"
                description: ""

          - name: "media_url"
            type: "string"
            description: ""

          - name: "media_url_https"
            type: "string"
            description: ""

          - name: "sizes"
            type: "object"
            description: ""
            subattributes:
              - name: "large"
                type: "object"
                description: ""
                subattributes:
                  - name: "h"
                    type: "integer"
                    description: ""

                  - name: "resize"
                    type: "string"
                    description: ""

                  - name: "w"
                    type: "integer"
                    description: ""

              - name: "medium"
                type: "object"
                description: ""
                subattributes:
                  - name: "h"
                    type: "integer"
                    description: ""

                  - name: "resize"
                    type: "string"
                    description: ""

                  - name: "w"
                    type: "integer"
                    description: ""

              - name: "small"
                type: "object"
                description: ""
                subattributes:
                  - name: "h"
                    type: "integer"
                    description: ""

                  - name: "resize"
                    type: "string"
                    description: ""

                  - name: "w"
                    type: "integer"
                    description: ""

              - name: "thumb"
                type: "object"
                description: ""
                subattributes:
                  - name: "h"
                    type: "integer"
                    description: ""

                  - name: "resize"
                    type: "string"
                    description: ""

                  - name: "w"
                    type: "integer"
                    description: ""

      - name: "polls"
        type: "array"
        description: ""
        subattributes:
          - name: "duration_minutes"
            type: "integer"
            description: ""

          - name: "end_datetime"
            type: "date-time"
            description: ""

          - name: "options"
            type: "array"
            description: ""
            subattributes:
              - name: "position"
                type: "integer"
                description: ""

              - name: "text"
                type: "string"
                description: ""

      - name: "symbols"
        type: "array"
        description: ""
        subattributes:
          - name: "indices"
            type: "array"
            description: ""
            subattributes:
              - name: "value"
                type: "integer"
                description: ""

          - name: "text"
            type: "string"
            description: ""

      - name: "urls"
        type: "array"
        description: ""
        subattributes:
          - name: "display_url"
            type: "string"
            description: ""

          - name: "expanded_url"
            type: "string"
            description: ""

          - name: "indices"
            type: "array"
            description: ""
            subattributes:
              - name: "value"
                type: "integer"
                description: ""

          - name: "url"
            type: "string"
            description: ""

      - name: "user_mentions"
        type: "array"
        description: ""
        subattributes:
          - name: "id"
            type: "integer"
            description: ""
            foreign-key-id: "user-id"

          - name: "id_str"
            type: "string"
            description: ""

          - name: "indices"
            type: "array"
            description: ""
            subattributes:
              - name: "value"
                type: "integer"
                description: ""

          - name: "name"
            type: "string"
            description: ""

          - name: "screen_name"
            type: "string"
            description: ""

  - name: "extended_entities"
    type: "object"
    description: ""
    subattributes:
      - name: "media"
        type: "array"
        description: ""
        subattributes:
          - name: "additional_media_info"
            type: "object"
            description: ""
            subattributes:
              - name: "description"
                type: "string"
                description: ""

              - name: "embeddable"
                type: "boolean"
                description: ""

              - name: "monetizable"
                type: "boolean"
                description: ""

              - name: "title"
                type: "string"
                description: ""

          - name: "display_url"
            type: "string"
            description: ""

          - name: "expanded_url"
            type: "string"
            description: ""

          - name: "id"
            type: "integer"
            description: ""

          - name: "id_str"
            type: "string"
            description: ""

          - name: "indices"
            type: "array"
            description: ""
            subattributes:
              - name: "value"
                type: "integer"
                description: ""

          - name: "media_url"
            type: "string"
            description: ""

          - name: "media_url_https"
            type: "string"
            description: ""

          - name: "sizes"
            type: "object"
            description: ""
            subattributes:
              - name: "large"
                type: "object"
                description: ""
                subattributes:
                  - name: "h"
                    type: "integer"
                    description: ""

                  - name: "resize"
                    type: "string"
                    description: ""

                  - name: "w"
                    type: "integer"
                    description: ""

              - name: "medium"
                type: "object"
                description: ""
                subattributes:
                  - name: "h"
                    type: "integer"
                    description: ""

                  - name: "resize"
                    type: "string"
                    description: ""

                  - name: "w"
                    type: "integer"
                    description: ""

              - name: "small"
                type: "object"
                description: ""
                subattributes:
                  - name: "h"
                    type: "integer"
                    description: ""

                  - name: "resize"
                    type: "string"
                    description: ""

                  - name: "w"
                    type: "integer"
                    description: ""

              - name: "thumb"
                type: "object"
                description: ""
                subattributes:
                  - name: "h"
                    type: "integer"
                    description: ""

                  - name: "resize"
                    type: "string"
                    description: ""

                  - name: "w"
                    type: "integer"
                    description: ""

          - name: "video_info"
            type: "object"
            description: ""
            subattributes:
              - name: "aspect_ratio"
                type: "array"
                description: ""
                subattributes:
                  - name: "value"
                    type: "integer"
                    description: ""

              - name: "duration_millis"
                type: "integer"
                description: ""

              - name: "variants"
                type: "array"
                description: ""
                subattributes:
                  - name: "bitrate"
                    type: "integer"
                    description: ""

                  - name: "content_type"
                    type: "string"
                    description: ""

                  - name: "url"
                    type: "string"
                    description: ""

  - name: "favorite_count"
    type: "integer"
    description: ""

  - name: "favorited"
    type: "boolean"
    description: ""

  - name: "filter_level"
    type: "string"
    description: ""

  - name: "id_str"
    type: "string"
    description: ""

  - name: "in_reply_to_screen_name"
    type: "string"
    description: ""

  - name: "in_reply_to_status_id"
    type: "integer"
    description: ""

  - name: "in_reply_to_status_id_str"
    type: "string"
    description: ""

  - name: "in_reply_to_user_id"
    type: "integer"
    description: ""
    foreign-key-id: "user-id"

  - name: "in_reply_to_user_id_str"
    type: "string"
    description: ""

  - name: "is_quote_status"
    type: "boolean"
    description: ""

  - name: "lang"
    type: "string"
    description: ""

  - name: "matching_rules"
    type: "array"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""

      - name: "id_str"
        type: "string"
        description: ""

      - name: "tag"
        type: "string"
        description: ""

  - name: "place"
    type: "object"
    description: ""
    subattributes:
      - name: "attributes"
        type: "object"
        description: ""
        # subattributes: 

      - name: "bounding_box"
        type: "object"
        description: ""
        subattributes:
          - name: "coordinates"
            type: "array"
            description: ""
            subattributes:
              - name: "value"
                type: "array"
                description: ""
                subattributes:
                  - name: "value"
                    type: "array"
                    description: ""
                    subattributes:
                      - name: "value"
                        type: "number"
                        description: ""

          - name: "type"
            type: "string"
            description: ""

      - name: "country"
        type: "string"
        description: ""

      - name: "country_code"
        type: "string"
        description: ""

      - name: "full_name"
        type: "string"
        description: ""

      - name: "id"
        type: "string"
        description: ""
        # foreign-key-id: "place-id"

      - name: "name"
        type: "string"
        description: ""

      - name: "place_type"
        type: "string"
        description: ""

      - name: "url"
        type: "string"
        description: ""

  - name: "possibly_sensitive"
    type: "boolean"
    description: ""

  - name: "quote_count"
    type: "integer"
    description: ""

  - name: "quote_status_id"
    type: "integer"
    description: ""

  - name: "quote_status_id_str"
    type: "string"
    description: ""

  - name: "quoted_status"
    type: "object"
    description: ""
    # subattributes: 

  - name: "reply_count"
    type: "integer"
    description: ""

  - name: "retweet_count"
    type: "integer"
    description: ""

  - name: "retweeted"
    type: "boolean"
    description: ""

  - name: "retweeted_status"
    type: "object"
    description: ""
    # subattributes: 

  - name: "source"
    type: "string"
    description: ""

  - name: "text"
    type: "string"
    description: ""

  - name: "truncated"
    type: "boolean"
    description: ""

  - name: "user"
    type: "object"
    description: ""
    subattributes:
      - name: "created_at"
        type: "date-time"
        description: ""

      - name: "default_profile"
        type: "boolean"
        description: ""

      - name: "default_profile_image"
        type: "boolean"
        description: ""

      - name: "derived"
        type: "object"
        description: ""
        subattributes:
          - name: "locations"
            type: "array"
            description: ""
            subattributes:
              - name: "country"
                type: "string"
                description: ""

              - name: "country_code"
                type: "string"
                description: ""

              - name: "full_name"
                type: "string"
                description: ""

              - name: "geo"
                type: "object"
                description: ""
                subattributes:
                  - name: "coordinates"
                    type: "array"
                    description: ""
                    subattributes:
                      - name: "value"
                        type: "number"
                        description: ""

                  - name: "type"
                    type: "string"
                    description: ""

              - name: "locality"
                type: "string"
                description: ""

              - name: "region"
                type: "string"
                description: ""

              - name: "sub_region"
                type: "string"
                description: ""

      - name: "description"
        type: "string"
        description: ""

      - name: "entities"
        type: "object"
        description: ""
        subattributes:
          - name: "description"
            type: "object"
            description: ""
            subattributes:
              - name: "urls"
                type: "array"
                description: ""

          - name: "url"
            type: "object"
            description: ""
            subattributes:
              - name: "urls"
                type: "array"
                description: ""
                subattributes:
                  - name: "display_url"
                    type: "string"
                    description: ""

                  - name: "expanded_url"
                    type: "string"
                    description: ""

                  - name: "indices"
                    type: "array"
                    description: ""
                    subattributes:
                      - name: "value"
                        type: "integer"
                        description: ""

                  - name: "url"
                    type: "string"
                    description: ""

      - name: "favourites_count"
        type: "integer"
        description: ""

      - name: "followers_count"
        type: "integer"
        description: ""

      - name: "friends_count"
        type: "integer"
        description: ""

      - name: "id"
        type: "integer"
        description: ""
        subattributes: "user-id"

      - name: "id_str"
        type: "string"
        description: ""

      - name: "listed_count"
        type: "integer"
        description: ""

      - name: "location"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "profile_banner_url"
        type: "string"
        description: ""

      - name: "profile_image_url_https"
        type: "string"
        description: ""

      - name: "protected"
        type: "boolean"
        description: ""

      - name: "screen_name"
        type: "string"
        description: ""

      - name: "statuses_count"
        type: "integer"
        description: ""

      - name: "url"
        type: "string"
        description: ""

      - name: "verified"
        type: "boolean"
        description: ""

      - name: "withheld_in_countries"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "withheld_scope"
        type: "string"
        description: ""
---