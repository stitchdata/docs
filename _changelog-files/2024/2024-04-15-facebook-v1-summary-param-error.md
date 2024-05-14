---
title: "Facebook Ads (v1) bug fix: Summary param error"
content-type: "changelog-entry"
date: 2024-04-15
entry-type: bug-fix
entry-category: integration
connection-id: facebook-ads
connection-version: 1
pull-request: "https://github.com/singer-io/tap-facebook/pull/239"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to fix the following error:

```
Status:  400
Response:
  {
    "error": {
      "message": "(#100) Cannot include cost_per_inline_post_engagement, unique_inline_link_click_ctr, frequency, video_play_curve_actions, unique_ctr, ctr, spend, unique_clicks, unique_inline_link_clicks, video_p100_watched_actions, campaign_name in summary param because they weren't there while creating the report run. All available values are: ",
      "type": "OAuthException",
      "code": 100,
      "fbtrace_id": "*************"
    }
  }
```

While awaiting for Facebook's fix, a workaround is now available. A new retry logic has been implemented, you can now retry the request for a successful data retrieval.
