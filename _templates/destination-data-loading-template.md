---
title: DESTINATION Loading Behavior
permalink: /data-structure/destination-data-loading-behavior
tags: [destination_destination]
keywords: destination, destination data warehouse, destination data warehouse, destination etl, etl to destination
summary: "Learn how Stitch will load data from your integrations and handle various scenarios into a DESTINATION destination."

toc: false
category: "data loading"
type: "destination"
datatable: true
---
{% include misc/data-files.html %}

<script>
$(document).ready(function(){

    $('table.display').DataTable( {
        paging: false,
        stateSave: true,
        searching: true
    }
        );
});
</script>

{% assign destination = site.data.[page.type] %}

{% include destinations/data-loading-behavior.html %}