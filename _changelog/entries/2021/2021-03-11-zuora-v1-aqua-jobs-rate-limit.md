---
title: "Zuora (v1) improvement: Updated discovery process for new enforced limit on AQuA jobs"
content-type: "changelog-entry"
date: 2021-03-11
entry-type: updated-feature
entry-category: "integration"
connection-id: "zuora"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-zuora/pull/53"
---

{{ site.data.changelog.metadata.single-integration | flatify }}

The new discovery process helps avoid {{ this-connection.display_name }} integration failures due to the new enforcement of limits on AQuA jobs. For more information on {{ this-connection.display_name }}'s AQuA API, click [here](https://knowledgecenter.zuora.com/Central_Platform/API/AB_Aggregate_Query_API/AA_AQuA_API_Introduction){:target="new"}.