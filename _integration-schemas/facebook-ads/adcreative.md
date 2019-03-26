---
tap: "facebook-ads"
version: 1.0

name: "adcreative"
doc-link: https://developers.facebook.com/docs/reference/ads-api/adcreative/
singer-schema: https://github.com/singer-io/tap-facebook/blob/master/tap_facebook/schemas/adcreative.json
description: |
  The `adcreative` table contains info about the creatives used in ads in your Facebook Ads account.

  **This is a Core Object table**.

replication-method: "Full Table"
attribution-window: true
api-method:
  name: adCreative - Reading
  doc-link: https://developers.facebook.com/docs/marketing-api/reference/ad-creative/#Reading

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The ID of the creative."
    foreign-key-id: "ad-creative-id"

  - name: "body"
    type: "string"
    description: "The body of the ad."

  - name: "image_url"
    type: "string"
    description: "The URL for the image for the creative."

  - name: "account_id"
    type: "string"
    description: "The ID of the account associated with the creative."
    foreign-key-id: "account-id"

  - name: "actor_id"
    type: "string"
    description: "The actor ID (page ID) of the creative."

  - name: "adLabels"
    type: "array"
    description: "Details about the ad labels applied to the creative."
    subattributes:
      - name: "id"
        type: "string"
        primary-key: true
        description: "The ad label ID."
        foreign-key-id: "ad-label-id"

      - name: "created_time"
        type: "date-time"
        description: "The time the ad label was created."

      - name: "name"
        type: "string"
        description: "The name of the ad label."

      - name: "updated_time"
        type: "date-time"
        description: "The last time the ad label was updated."

  - name: "applink_treatment"
    type: "string"
    description: "The deep link fallback behavior for [dynamic product ads](https://developers.facebook.com/docs/marketing-api/dynamic-product-ads/ads-management) if the app is not installed."

  - name: "branded_content_sponsor_page_id"
    type: "string"
    description: "The sponsor page ID of the creative."

  - name: "call_to_action_type"
    type: "string"
    description: "The call to action button text and header text of legacy ads."

  - name: "effective_instagram_story_id"
    type: "string"
    description: "The ID of the Instagram post used in the ad."

  - name: "effective_object_story_id"
    type: "string"
    description: "The ID of the page post used in an ad."

  - name: "title"
    type: "string"
    description: "The title for an ad link."

  - name: "name"
    type: "string"
    description: "The name of the creative in the creative library."

  - name: "image_crops"
    type: "array"
    description: "Details about the crop specifications (aspect ratios) for images in different ad placements."
    doc-link: "https://developers.facebook.com/docs/marketing-api/reference/ads-image-crops/"
    schema-link: "https://github.com/singer-io/tap-facebook/blob/master/tap_facebook/schemas/shared/ads_image_crops.json"
    subattributes: &crop-specifications
      - name: "100x100"
        type: "array"
        description: "The crop specification for 100x100."
        subattributes:
          - name: "value"
            type: "integer"
            description: "The value of the crop specification."

      - name: "100x72"
        type: "array"
        description: "The crop specification for 100x72."
        subattributes:
          - name: "value"
            type: "integer"
            description: "The value of the crop specification."

      - name: "191x100"
        type: "array"
        description: "The crop specification for 191x100."
        subattributes:
          - name: "value"
            type: "integer"
            description: "The value of the crop specification."

      - name: "400x150"
        type: "array"
        description: "The crop specification for 400x150."
        subattributes:
          - name: "value"
            type: "integer"
            description: "The value of the crop specification."

      - name: "400x500"
        type: "array"
        description: "The crop specification for 400x500."
        subattributes:
          - name: "value"
            type: "integer"
            description: "The value of the crop specification."

      - name: "600x360"
        type: "array"
        description: "The crop specification for 600x360."
        subattributes:
          - name: "value"
            type: "integer"
            description: "The value of the crop specification."

      - name: "90x160"
        type: "array"
        description: "The crop specification for 90x160."
        subattributes:
          - name: "value"
            type: "integer"
            description: "The value of the crop specification."

  - name: "instagram_actor_id"
    type: "string"
    description: "The Instagram actor ID associated with the creative."

  - name: "instagram_permalink_url"
    type: "string"
    description: "The Instagram permalink associated with the creative."

  - name: "instagram_story_id"
    type: "string"
    description: "The ID of the Instagram post for creating ads."

  - name: "link_og_id"
    type: "string"
    description: "The Open Graph (OG) ID for the link in the creative if the landing page has OG tags."

  - name: "object_id"
    type: "string"
    description: "The ID of the [promoted object](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign/promoted-object) or object that is relevant to the ad and ad type."

  - name: "object_story_id"
    type: "string"
    description: "The ID of the page post that is used in the creative."

# Start of object_story_spec

  - name: "object_story_spec"
    type: "object"
    description: "Details about the specifications of a creative that are used to create a new unpublished page post."
    doc-link: "https://github.com/singer-io/tap-facebook/blob/master/tap_facebook/schemas/adcreative.json#L137"
    subattributes:
      - name: "instagram_actor_id"
        type: "string"
        description: "The Instagram user that the story will be posted to."

    # Start object_story_spec__link_data

      - name: "link_data"
        type: "object"
        description: "Details about the specifications for link or [carousel ads](https://developers.facebook.com/docs/marketing-api/guides/carousel-ads/)."
        doc-link: "https://developers.facebook.com/docs/marketing-api/reference/ad-creative-link-data/"
        subattributes:
          - name: "additional_image_index"
            type: "integer"
            description: "The index (zero based) of the image from the additional images array to use as the ad image for a dynamic product ad."

        # Start object_story_spec__link_data__app_link_spec

          - name: "app_link_spec"
            type: "object"
            doc-link: "https://developers.facebook.com/docs/marketing-api/reference/ad-creative-link-data-app-link-spec/"
            description: |
              Details about the native deeplinks attached to the post. 

              Stitch will replicate data for the following deeplink types:

              - [`android`](https://developers.facebook.com/docs/graph-api/reference/android-app-link/)
              - [`ios`](https://developers.facebook.com/docs/graph-api/reference/ios-app-link/)
              - [`ipad`](https://developers.facebook.com/docs/graph-api/reference/ios-app-link/)
              - [`iphone`](https://developers.facebook.com/docs/graph-api/reference/ios-app-link/)
            subattributes: &native-deeplinks
              - name: "android"
                type: "array"
                description: "Details about native deeplinks used on Android."
                subattributes:
                  - name: "app_name"
                    type: "string"
                    description: "The name of the native app in the Android store."

                  - name: "class"
                    type: "string"
                    description: "The full classified class name of the app for intent generation."

                  - name: "package"
                    type: "string"
                    description: "The fully classified package name of the app for intent generation."

                  - name: "url"
                    type: "string"
                    description: "The native Android URL that will be navigated to."

              - name: "ios"
                type: "array"
                description: "Details about native deeplinks used on iOS."
                subattributes:
                  - name: "app_name"
                    type: "string"
                    description: "The name of the native app in the iTunes store."

                  - name: "app_store_id"
                    type: "string"
                    description: "The ID of the native app in the iTunes store."
                    foreign-key-id: "app-store-id"

                  - name: "url"
                    type: "string"
                    description: "The native iOS URL that will be navigated to."

              - name: "ipad"
                type: "array"
                description: "Details about native deeplinks used on iPads."
                subattributes:
                  - name: "app_name"
                    type: "string"
                    description: "The name of the native app in the iTunes store."

                  - name: "app_store_id"
                    type: "string"
                    description: "The ID of the native app in the iTunes store."
                    foreign-key-id: "app-store-id"

                  - name: "url"
                    type: "string"
                    description: "The native iOS URL that will be navigated to."
                    description: ""

              - name: "iphone"
                type: "array"
                description: "Details about native deeplinks used on iPhones."
                subattributes:
                  - name: "app_name"
                    type: "string"
                    description: "The name of the native app in the iTunes store."

                  - name: "app_store_id"
                    type: "string"
                    description: "The ID of the native app in the iTunes store."
                    foreign-key-id: "app-store-id"

                  - name: "url"
                    type: "string"
                    description: "The native iOS URL that will be navigated to."

        # End object_story_spec__link_data__link_spec

          - name: "attachment_style"
            type: "string"
            description: "The style of the attachment."

          - name: "branded_content_sponsor_page_id"
            type: "string"
            description: "The ID of the branded content sponsor page."

          - name: "branded_content_sponsor_relationship"
            type: "string"
            description: "The branded content sponsor relationship option."

        # Start object_story_spec__link_data__call_to_action

          - name: "call_to_action"
            type: "object"
            description: "Details about the call to action button."
            doc-link: "https://developers.facebook.com/docs/marketing-api/reference/ad-creative-link-data-call-to-action-value/"
            subattributes: &call-to-action
              - name: "app_destination"
                type: "string"
                description: "The app destination type."

              - name: "app_link"
                type: "string"
                description: "The deep link to the app."

              - name: "application"
                type: "string"
                description: "The application related to the action."

              - name: "event_id"
                type: "string"
                description: "The ID of the Facebook event which shows the event info."

              - name: "lead_gen_form_id"
                type: "string"
                description: "The ID of the [Lead Ad](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/) form."

              - name: "link"
                type: "string"
                description: "The destination link when the CTA button is clicked."

              - name: "link_caption"
                type: "string"
                description: "The caption shown in the attachment."

              - name: "link_format"
                type: "string"
                description: "The link format of video attachments."

              - name: "page"
                type: "string"
                description: "Teh ID of the Facebook page which the CTA button links to."

              - name: "product_link"
                type: "string"
                description: "The Open Graph object URL for canvas virtual good ads."

        # End object_story_spec__link_data__call_to_action

          - name: "caption"
            type: "string"
            description: "The link caption."

        # Start object_story_spec__link_data__child_attachments

          - name: "child_attachments"
            type: "array"
            description: "Details about the link objects required for carousel ads."
            doc-link: "https://developers.facebook.com/docs/marketing-api/reference/ad-creative-link-data-child-attachment/"
            subattributes:
              - name: "image_hash"
                type: "string"
                description: "The image hash of an uploaded image for the attachment."

              - name: "link"
                type: "string"
                description: "The link of the attachment."

            # Start object_story_spec__link_data__child_attachments__call_to_action

              - name: "call_to_action"
                type: "object"
                description: "Details about the call to associated with the link object."
                subattributes: *call-to-action

              # End object_story_spec__link_data__child_attachments__call_to_action

              - name: "type"
                type: "string"
                description: ""

              - name: "description"
                type: "string"
                description: "The description of each attachment on Facebook."

              - name: "caption"
                type: "string"
                description: "If the attachment is a video, the display URL shown at the end of the video."

              - name: "picture"
                type: "string"
                description: "The URL of an image for this attachment."

              - name: "static_card"
                type: "boolean"
                description: "Indicates if the card is forced to render statically, even in a dynamic ad."

              - name: "video_id"
                type: "string"
                description: "The ID of an uploaded video, if the attachment is a video. This is not supported for Instagram ads."

            # Start object_story_spec__link_data__child_attachments__image_crops

              - name: "image_crops"
                type: "array"
                description: "Details about the crop specifications (aspect ratios) for images in different ad placements for carousel ads."
                doc-link: "https://developers.facebook.com/docs/marketing-api/reference/ads-image-crops/"
                schema-link: "https://github.com/singer-io/tap-facebook/blob/master/tap_facebook/schemas/shared/ads_image_crops.json"
                subattributes: *crop-specifications

              # End object_story_spec__link_data__child_attachments__image_crops

          # End object_story_spec__link_data__child_attachments

          - name: "multi_share_optimized"
            type: "boolean"
            description: "Indicates if orders and links are automatically selected and ordered."

          - name: "link"
            type: "string"
            description: "The link URL."

        # Start object_story_spec__link_data__image_crops

          - name: "image_crops"
            type: "array"
            description: "Details how images should be cropped."
            doc-link: "https://developers.facebook.com/docs/marketing-api/reference/ads-image-crops/"
            schema-link: "https://github.com/singer-io/tap-facebook/blob/master/tap_facebook/schemas/shared/ads_image_crops.json"
            subattributes: *crop-specifications

          # End object_story_spec__link_data__image_crops

          - name: "description"
            type: "string"
            description: "The link description."

          - name: "event_id"
            type: "string"
            description: "The ID of a Facebook event."

          - name: "force_single_link"
            type: "boolean"
            description: "Indicates if a post is forced to render in a single link format."

          - name: "multi_share_end_card"
            type: "boolean"
            description: "Indicates if end cards that display the page icon should not be removed."

          - name: "message"
            type: "string"
            description: "The main body of the post."

          - name: "image_hash"
            type: "string"
            description: "The hash of an image in your image library with Facebook."

          - name: "picture"
            type: "string"
            description: "The URL of a picture to use in the post."

          - name: "name"
            type: "string"
            description: "The name of the link."

          - name: "offer_id"
            type: "string"
            description: "The ID of a Facebook native offer."
            foreign-key-id: "offer-id"

          - name: "page_welcome_message"
            type: "string"
            description: "The welcome text from page to user on Messenger after a user performs a send message action on an ad."

        # Start object_story_spec__link_data__retailer_item_ids

          - name: "retailer_item_ids"
            type: "array"
            description: "The product IDs provided by the advertiser for collections."
            subattributes:
              - name: "value"
                type: "string"
                description: "The ID of the product."

        # End object_story_spec__link_data__retailer_item_ids

          - name: "show_multiple_images"
            type: "boolean"
            doc-link: "https://developers.facebook.com/docs/marketing-api/dynamic-product-ads/ads-management/"
            description: "Used with `force_single_link` (`true`) to show a single dynamic item in carousel format using multiple images from the catalog."

      - name: "page_id"
        type: "string"
        description: "The ID of a Facebook page."
        foreign-key-id: "page-id"

    # End object_story_spec__link_data

    # Start object_story_spec__photo_data

      - name: "photo_data"
        type: "object"
        description: "Details about the spec for a photo page post."
        doc-link: "https://developers.facebook.com/docs/marketing-api/reference/ad-creative-photo-data/"
        subattributes:
          - name: "branded_content_sponsor_page_id"
            type: "string"
            description: "The ID of the branded content sponsor page ID."

          - name: "branded_content_sponsor_relationship"
            type: "string"
            description: "The branded content sponsor relationship option."

          - name: "caption"
            type: "string"
            description: "The description of the image."

          - name: "image_hash"
            type: "string"
            description: "The hash of the image in your image library with Facebook."

          - name: "page_welcome_message"
            type: "string"
            description: "The welcome text from page to user on Messenger once a user performs a send message action on an ad."

          - name: "url"
            type: "string"
            description: "The URL of an image to use in the ad."

    # End object_story_spec__photo_data

    # Start object_story_spec__template_data

      - name: "template_data"
        type: "object"
        description: ""
        subattributes:
          - name: "additional_image_index"
            type: "integer"
            description: "The index (zero based) of the image from the additional images array to use as the ad image for a dynamic product ad."

        # Start object_story_spec__template_data_app_link_spec

          - name: "app_link_spec"
            type: "object"
            description: |
              Details about the native deeplinks attached to the post. 

              Stitch will replicate data for the following deeplink types:

              - [`android`](https://developers.facebook.com/docs/graph-api/reference/android-app-link/)
              - [`ios`](https://developers.facebook.com/docs/graph-api/reference/ios-app-link/)
              - [`ipad`](https://developers.facebook.com/docs/graph-api/reference/ios-app-link/)
              - [`iphone`](https://developers.facebook.com/docs/graph-api/reference/ios-app-link/)

            subattributes: *native-deeplinks

        # End object_story_spec__template_data__app_link_spec

          - name: "attachment_style"
            type: "string"
            description: "The style of the attachment."

          - name: "branded_content_shared_to_sponsor_status"
            type: "string"
            description: "The branded content shared to sponsor option."

          - name: "branded_content_sponsor_page_id"
            type: "string"
            description: "The ID of the branded content sponsor page."

          - name: "branded_content_sponsor_relationship"
            type: "string"
            description: "The branded content sponsorship option."

        # Start object_story_spec__template_data__call_to_action

          - name: "call_to_action"
            type: "object"
            description: "Details about the call to associated with the link object."
            doc-link: "https://developers.facebook.com/docs/marketing-api/reference/ad-creative-link-data-call-to-action-value/"
            subattributes: *call-to-action

        # End object_story_spec__template_data__call_to_action

          - name: "caption"
            type: "string"
            description: "The link caption."

        # Start object_story_spec__template_data__child_attachments

          - name: "child_attachments"
            type: "array"
            description: "Details about the link objects required for carousel ads."
            doc-link: "https://developers.facebook.com/docs/marketing-api/reference/ad-creative-link-data-child-attachment/"
            subattributes:
              - name: "image_hash"
                type: "string"
                description: "The image hash of an uploaded image for the attachment."

              - name: "link"
                type: "string"
                description: "The link of the attachment."

            # Start object_story_spec__template_data__child_attachments__call_to_action

              - name: "call_to_action"
                type: "object"
                description: "Details about the call to associated with the link object."
                subattributes: *call-to-action

            # End object_story_spec__template_data__child_attachments__call_to_action

          - name: "description"
            type: "string"
            description: "The link description."

          - name: "event_id"
            type: "string"
            description: "The ID of a Facebook event."

          - name: "force_single_link"
            type: "boolean"
            description: "Indicates if the post will be forced to render in single link format."

        # Start object_story_spec__template_data__child_attachments__image_crops

          - name: "image_crops"
            type: "array"
            description: "Details about the crop specifications (aspect ratios) for images in different ad placements."
            doc-link: "https://developers.facebook.com/docs/marketing-api/reference/ads-image-crops/"
            schema-link: "https://github.com/singer-io/tap-facebook/blob/master/tap_facebook/schemas/shared/ads_image_crops.json"
            subattributes: *crop-specifications

        # End object_story_spec__template_data__child_attachments__image_crops

          - name: "image_hash"
            type: "string"
            description: "The hash of an image in your image library with Facebook."

          - name: "link"
            type: "string"
            description: "The link URL."

          - name: "message"
            type: "string"
            description: "The main body of the post."

          - name: "multi_share_end_card"
            type: "boolean"
            description: "Indicates if end cards that display the page icon should not be removed."

          - name: "multi_share_optimized"
            type: "boolean"
            description: "Indicates if orders and links are automatically selected and ordered."

          - name: "name"
            type: "string"
            description: "The name of the link."

          - name: "offer_id"
            type: "string"
            description: "The ID of a Facebook native offer."
            foreign-key-id: "offer-id"

          - name: "page_welcome_message"
            type: "string"
            description: "The welcome text from page to user on Messenger after a user performs a send message action on an ad."

          - name: "picture"
            type: "string"
            description: "The URL of a picture to use in the post."

        # Start object_story_spec__template_data__child_attachments__retailer_item_ids

          - name: "retailer_item_ids"
            type: "array"
            description: "The product IDs provided by the advertiser for collections."
            subattributes:
              - name: "value"
                type: "string"
                description: "The ID of the product."

        # End object_story_spec__template_data__child_attachments__retailer_item_ids

          - name: "show_multiple_images"
            type: "boolean"
            description: "Used with `force_single_link` (`true`) to show a single dynamic item in carousel format using multiple images from the catalog."
            doc-link: "https://developers.facebook.com/docs/marketing-api/dynamic-product-ads/ads-management/"

    # End object_story_spec__template_data

    # Start object_story_spec__text_data

      - name: "text_data"
        type: "object"
        description: "Details about the text page post used for the ad."
        subattributes:
          - name: "message"
            type: "string"
            description: "The text of the page post."

    # End object_story_spec__text_data

    # Start object_story_spec__video_data

      - name: "video_data"
        type: "object"
        description: "Details about the specifications for a video ad."
        subattributes:
          - name: "branded_content_shared_to_sponsor_status"
            type: "string"
            description: "The branded content shared to sponsor option."

          - name: "branded_content_sponsor_page_id"
            type: "string"
            description: "The ID of the branded content sponsor page."

          - name: "branded_content_sponsor_relationship"
            type: "string"
            description: "The branded content sponsorship option."

        # Start object_story_spec__video_data__call_to_action

          - name: "call_to_action"
            type: "object"
            description: "Details about the call to associated with the link object."
            subattributes: *call-to-action

          - name: "force_single_link"
            type: "boolean"
            description: "Indicates if the post will be forced to render in single link format."

          - name: "image_hash"
            type: "string"
            description: "The hash of an image in your image library with Facebook."

          - name: "image_url"
            type: "string"
            description: "The URL of the image to use as a thumbnail."

          - name: "link_description"
            type: "string"
            description: "The link description of the video."

          - name: "message"
            type: "string"
            description: "The main body of the post."

          - name: "name"
            type: "string"
            description: "The name of the link."

          - name: "offer_id"
            type: "string"
            description: "The ID of a Facebook native offer."
            foreign-key-id: "offer-id"

          - name: "page_welcome_message"
            type: "string"
            description: "The welcome text from page to user on Messenger after a user performs a send message action on an ad."

        # Start object_story_spec__video_data__retailer_item_ids

          - name: "retailer_item_ids"
            type: "array"
            description: "The product IDs provided by the advertiser for collections."
            subattributes:
              - name: "value"
                type: "string"
                description: "The ID of the product."

        # End object_story_spec__video_data__retailer_item_ids

          - name: "targeting"
            type: "array"
            description: "The post gating for the video."
            subattributes:

          - name: "video_id"
            type: "string"
            description: "The ID of the video that the user has permission to or a video in the ad account video library."

    # End object_story_spec__video_data

  # End object_story_spec

  - name: "object_type"
    type: "string"
    description: |
      The type of object being advertised. Possible values are:

      - `APPLICATION` - For apps on Facebook.
      - `DOMAIN`
      - `EVENT`
      - `INVALID` - Returned when invalid `object_ids` are supplied or the authorizing user doesn't have permission to see the object.
      - `PAGE`
      - `PHOTO`
      - `SHARE`
      - `STATUS`
      - `STORE_ITEM` - For iTunes and Google Play store destinations.
      - `VIDEO`

  - name: "object_url"
    type: "string"
    description: "The destination URL for link ads not connected to a page."

  - name: "product_set_id"
    type: "string"
    description: "The ID of the product set for the creative."
    foreign-key-id: "product-set-id"

  - name: "status"
    type: "string"
    description: "The status of the creative. Possible values are `ACTIVE` or `DELETED`."

  - name: "template_url"
    type: "string"
    description: "The tracking URL for dynamic product ads."

# Start template_url_spec

  - name: "template_url_spec"
    type: "object"
    description: "Details about the template link specifications used to create ad creatives."
    subattributes: 

    # Start template_url_spec__android

      - name: "android"
        type: "object"
        description: 
        subattributes:
          - name: "app_name"
            type: "string"
            description: "The name of the Android app."

          - name: "package"
            type: "string"
            description: "The fully qualified package name for intent generation and store linking."

          - name: "url"
            type: "string"
            description: "The custom URL scheme for the Android app."

    # End template_url_spec__android

    # Start template_url__spec__config

      - name: "config"
        type: "object"
        description:
        subattributes:
          - name: "app_id"
            type: "string"
            description: "The ID of the Facebook app where the deeplink information is stored."

    # End template_url_spec__config

    # Start template_url__spec__ios

      - name: "ios"
        type: "object"
        description:
        subattributes:
          - name: "app_name"
            type: "string"
            description: "The display name of the iOS app."

          - name: "app_store_id"
            type: "string"
            description: "The app ID for the App Store."
            foreign-key-id: "app-store-id"

          - name: "url"
            type: "string"
            description: "The custom URL scheme for the iOS app."

    # End template_url_spec__ios

    # Start template_url__spec__ipad

      - name: "ipad"
        type: "object"
        description:
        subattributes:
          - name: "app_name"
            type: "string"
            description: "The display name of the iOS app."

          - name: "app_store_id"
            type: "string"
            description: "The app ID for the App Store."
            foreign-key-id: "app-store-id"

          - name: "url"
            type: "string"
            description: "The custom URL scheme for the iOS app."

    # End template_url_spec__ipad

    # Start template_url__spec__iphone

      - name: "iphone"
        type: "object"
        description:
        subattributes:
          - name: "app_name"
            type: "string"
            description: "The display name of the iOS app."

          - name: "app_store_id"
            type: "string"
            description: "The app ID for the App Store."
            foreign-key-id: "app-store-id"

          - name: "url"
            type: "string"
            description: "The custom URL scheme for the iOS app."

    # End template_url_spec__iphone

    # Start template_url__spec__web

      - name: "web"
        type: "object"
        description:
        subattributes:
          - name: "should_fallback"
            type: "string"
            description: "Indicates if the web URL should be used as a fallback. If `false`, the content is only meant to be viewed on a native app."

          - name: "url"
            type: "string"
            description: "The web URL."

    # End template_url_spec__web

    # Start template_url__spec__windows_phone

      - name: "windows_phone"
        type: "object"
        description:
        subattributes:
          - name: "app_id"
            type: "string"
            description: "The app ID as a GUID for the app store."
            # foreign-key-id: "windows-app-id"

          - name: "app_name"
            type: "string"
            description: "The display name of the app."

          - name: "url"
            type: "string"
            description: "The custom URL scheme for the Windows Phone app."

    # End template_url_spec__windows_phone

# End template_url_spec

  - name: "thumbnail_url"
    type: "string"
    description: "The URL to a thumbnail used for the creative."

  - name: "image_hash"
    type: "string"
    description: "The image has for an image used in the creative."

  - name: "url_tags"
    type: "string"
    description: "The query string parameters which will replace or be appended to URLs clicked from page post ads, messages of the post, and canvas app install creatives."

  - name: "video_id"
    type: "string"
    description: "The ID of the video in the creative."

  - name: "link_url"
    type: "string"
    description: "Used to identify a specific landing tab on the page by the page's tab URL."
---