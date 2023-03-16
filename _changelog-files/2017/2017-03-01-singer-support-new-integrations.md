---
title: "Support for Singer Taps - 10 new integrations!"
content-type: "changelog-entry"
date: 2017-03-01
entry-type: "new-feature"
entry-category: integration
connections:
  - id: "braintree"
    type: "integration"
    version: "1"
    
  - id: "closeio"
    type: "integration"
    version: "2017-03-01"

  - id: "freshdesk"
    type: "integration"
    version: "1"
    
  - id: "gitlab"
    type: "integration"
    version: "1"
    
  - id: "hubspot"
    type: "integration"
    version: "01-03-2017"

  - id: "marketo"
    type: "integration"
    version: "1"
    
  - id: "outbrain"
    type: "integration"
    version: "1"
    
  - id: "referral-saasquatch"
    type: "integration"
    version: "1"
    
  - id: "shippo"
    type: "integration"
    version: "1"
    
  - id: "wootric"
    type: "integration"
    version: "1"
---
Stitch now has built-in support for Singer Taps, the data extraction component of the the just launched simple, composable, open source ETL [Singer project]({{ site.singer }}){:target="new"}. This exciting new standard will make getting data out of any source and into Stitch (or elsewhere) simpler and more straightforward.

To learn more about Singer, check out the [launch blog post](https://blog.stitchdata.com/introducing-singer-simple-composable-open-source-etl-a4a6da7eac19#.ecejuna9t){:target="new"}.

By supporting this standard, Stitch now supports these integrations:

{{ site.data.changelog.metadata.integration-list | flatify }}