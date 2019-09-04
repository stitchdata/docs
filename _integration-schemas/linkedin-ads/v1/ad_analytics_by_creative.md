---
tap: "linkedin-ads"
version: "1.0"

name: "ad_analytics_by_creative"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-linkedin-ads/blob/master/tap_linkedin_ads/schemas/ad_analytics_by_creative.json"

description: ""

replication-method: "Key-based Incremental"


api-method:
    name: "Ads Reporting"
    doc-link: "https://docs.microsoft.com/en-us/linkedin/marketing/integrations/ads-reporting/ads-reporting#analytics-finder"

attributes:
  - name: "creative_id"
    type: "integer"
    foreign-key: true
    description: ""
    foreign-key-id: "creative-id"

  - name: "start_at"
    type: "date-time"
    primary-key: true
    description: ""
    foreign-key-id: "start-at"

  - name: "end_at"
    type: "date-time"
    description: "" 
    replication-key: true   

  - name: "action_clicks"
    type: "integer"
    description: "The count of clicks on the 'action' button in Sponsored InMail."
  
  - name: "ad_unit_clicks"
    type: "integer"
    description: "The count of clicks on the ad unit alongside the Sponsored InMail."
  
  - name: "comments"
    type: "integer"
    description: "The count of comments - Sponsored Updates only."
  
  - name: "company_page_clicks"
    type: "integer"
    description: "The count of clicks to view the company page."
  
  - name: "conversion_value_in_local_currency"
    type: "number"
    description: "The value of the conversions in the account's local currency."
  
  - name: "cost_in_local_currency"
    type: "number"
    description: "The cost in the account's local currency based on the pivot and timeGranularity."
  
  - name: "cost_in_usd"
    type: "number"
    description: "The cost in USD based on the pivot and timeGranularity."
  
  - name: "creative"
    type: "string"
    description: ""
  
  - name: "date_range"
    type: "object"
    description: "The date range of the report data point, specified in UTC. A start date is required."
    subattributes:
      - name: "end"
        type: "object"
        description: ""
        subattributes:
          - name: "day"
            type: "integer"
            description: ""
          - name: "month"
            type: "integer"
            description: ""
          - name: "year"
            type: "integer"
            description: ""
      - name: "start"
        type: "object"
        description: ""
        subattributes:
          - name: "day"
            type: "integer"
            description: ""
          - name: "month"
            type: "integer"
            description: ""
          - name: "year"
            type: "integer"
            description: ""
  
  - name: "external_website_conversions"
    type: "integer"
    description: "The count of conversions indicated by pixel loads on an external advertiser website."
  
  - name: "external_website_post_click_conversions"
    type: "integer"
    description: "The count of post-view conversions indicated by pixel loads on an external advertiser website."
  
  - name: "external_website_post_view_conversions"
    type: "integer"
    description: "The count of post-view conversions indicated by pixel loads on an external advertiser website."
  
  - name: "follows"
    type: "integer"
    description: "The follow count - Sponsored Updates only."
  
  - name: "full_screen_plays"
    type: "integer"
    description: "The tap counts on a video going into video view mode."
 
  - name: "impressions"
    type: "integer"
    description: "This is the count of 'impressions' for Direct Ads and Sponsored Updates and 'sends' for InMails."
  
  - name: "lead_generation_mail_contact_info_shares"
    type: "integer"
    description: ""
  
  - name: "lead_generation_mail_interest_clicks"
    type: "integer"
    description: "The number of times users shared contact info through the One Click Lead Gen for Sponsored InMail - Sponsored InMail only."
  
  - name: "likes"
    type: "integer"
    description: "The count of likes - Sponsored Updates only."
  
  - name: "one_click_lead_form_opens"
    type: "integer"
    description: "The count of times users opened the lead form for a One Click Lead Gen campaign."
  
  - name: "one_click_leads"
    type: "integer"
    description: "The count of leads generated through One Click Lead Gen."
  
  - name: "opens"
    type: "integer"
    description: "The count of opens of Sponsored InMail."
  
  - name: "other_engagements"
    type: "integer"
    description: "The count of user interactions with the ad unit that do not fit into any other more specific category."
  
  - name: "pivot"
    type: "string"
    description: ""
  
  - name: "pivot_value"
    type: "string"
    description: ""
  
  - name: "pivot_values"
    type: "null"
    description: "The value of the pivots for a specific record returned."
  
  - name: "shares"
    type: "integer"
    description: "The count of sends of Sponsored InMail."
  
  - name: "text_url_clicks"
    type: "integer"
    description: "The count of clicks on any links (anchor tags) that were included in the body of the Sponsored InMail."
  
  - name: "total_engagements"
    type: "integer"
    description: "The count of all user interactions with the ad unit."
  
  - name: "video_completions"
    type: "integer"
    description: "The count of video ads that played 97-100% of the video. This includes watches that skipped to this point if the serving location is ON_SITE."
  
  - name: "video_first_quartile_completions"
    type: "integer"
    description: "The count of video ads that played through the first quartile of the video. This includes watches that skipped to this point if the serving location is ON_SITE."
  
  - name: "video_midpoint_completions"
    type: "integer"
    description: ""
  
  - name: "video_starts"
    type: "integer"
    description: ""
  
  - name: "video_third_quartile_completions"
    type: "integer"
    description: ""
  
  - name: "video_views"
    type: "integer"
    description: "The count of video ads that played through the midpoint of the video. This includes watches that skipped to this point if the serving location is ON_SITE."
  
  - name: "viral_clicks"
    type: "integer"
    description: "The count of clicks on viral impressions - Sponsored Updates only."
  
  - name: "viral_comments"
    type: "integer"
    description: "The count of comments from viral impressions for this activity - Sponsored Updates only."
  
  - name: "viral_company_page_clicks"
    type: "integer"
    description: "The count of clicks to view the company page from viral impressions for this activity - Sponsored Updates only."
  
  - name: "viral_external_website_conversions"
    type: "integer"
    description: "The count of conversions indicated by pixel loads on an external advertiser website driven by a viral event."
  
  - name: "viral_external_website_post_click_conversions"
    type: "integer"
    description: "The count of post-click conversions indicated by pixel loads on an external advertiser website driven by a viral click."
  
  - name: "viral_external_website_post_view_conversions"
    type: "integer"
    description: "The count of post-view conversions indicated by pixel loads on an external advertiser website driven by a viral impression."
  
  - name: "viral_follows"
    type: "integer"
    description: "The count of follows from viral impressions for this activity - Sponsored Updates only."
  
  - name: "viral_full_screen_plays"
    type: "integer"
    description: "The count of taps on the video, going into video view mode."
  
  - name: "viral_impressions"
    type: "integer"
    description: "The count of viral impressions for this activity. Viral impressions are those resulting from users sharing a sponsored update to their own network of connections - Sponsored Updates only."
  
  - name: "viral_landing_page_clicks"
    type: "integer"
    description: "The count of clicks on viral impressions to take the user to the creative landing page - Sponsoerd Updates only."
  
  - name: "viral_likes"
    type: "integer"
    description: "The count of likes from viral impressions for this activity - Sponsored Updates only."
  
  - name: "viral_one_click_lead_form_opens"
    type: "integer"
    description: "The count of times users opened the lead form for viral impressions from a Lead Gen campaign."
  
  - name: "viral_one_click_leads"
    type: "integer"
    description: "The count of leads generated through One Click Lead Gen from viral impressions for this activity."
  
  - name: "viral_other_engagements"
    type: "integer"
    description: "The count of user interactions with viral impressions that do not fit into any other more specific category - Sponsored Updates only."
  
  - name: "viral_shares"
    type: "integer"
    description: "The count of shares from viral impressions for this activity - Sponsored Updates only."
  
  - name: "viral_total_engagements"
    type: "integer"
    description: "The count of all user interactions with a viral ad unit - Sponsored Updates only."
  
  - name: "viral_video_completions"
    type: "integer"
    description: "The count of viral video ads that played 97-100% of the video. This includes watches that skipped to this point."
  
  - name: "viral_video_first_quartile_completions"
    type: "integer"
    description: "The count of viral video ads that played through the first quartile of the video. This includes watches that skipped to this point."
  
  - name: "viral_video_midpoint_completions"
    type: "integer"
    description: "The count of viral video ads that played through the midpoint of the video. This includes watches that skipped to this point."
  
  - name: "viral_video_starts"
    type: "integer"
    description: "The count of viral video ads that were started by users. Since viral videos are automatically played for ON_SITE, this will be the same as viralImpressions if the servingLocation is ON_SITE."
  
  - name: "viral_video_third_quartile_completions"
    type: "integer"
    description: "The count of viral video ads that played through the third quartile of the video. This includes watches that skipped to this point."
  
  - name: "viral_video_views"
    type: "integer"
    description: "A viral video ad playing for at least 2 continuous seconds 50% in-view, or a click on the CTA, whichever comes first. An interaction with the video (like going to full screen mode) does not count as a view."
---
