---
title: "Facebook Ads (v1): Integration updates"
content-type: "changelog-entry"
date: 2026-06-22
entry-type: improvement
entry-category: integration
connection-id: facebook-ads
connection-version: 1
pull-request: "https://github.com/singer-io/tap-facebook/pull/269"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration with multiple updates.

For v1.26.0:

**New:**
- Added `ads_insights_comscore_market` table for market-level geographic insights.

**Deprecated:**
- `ads_insights_dma` table deprecated due to Meta API changes (June 22, 2026).

**Action required:**
- If using `ads_insights_dma`, switch to `ads_insights_comscore_market`.

**Reference:** [Meta announcement](https://developers.facebook.com/blog/post/2026/03/13/transitioning-to-comscore-markets-for-automotive-model-ads)