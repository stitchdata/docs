---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Multiple Destinations Overview
permalink: /destinations/multiple-destinations
keywords: destination, destinations, data warehouse, data warehouses, warehouse, stitch etl, etl, multiple destinations

summary: "If you're looking to map your Stitch integrations to more than one destination, this guide will help you set them up."

destination: false
content-type: "destination-general"
type: "all"
key: "multiple-destinations"

layout: general
toc: true


# -------------------------- #
#         GUIDE INTRO        #
# -------------------------- #

intro: |
  You can now add multiple destinations to your Stitch account! In this guide, you will learn everything you need to know on how to fully utilize this feature. Before selecting destinations, we recommend reading our guide on [how to choose a destination]({{ link.destinations.overviews.choose-destination | prepend: site.baseurl }}) to ensure you're making the decision that best suits your data warehousing needs.


# -------------------------- #
#      CONTENT SECTIONS      #
# -------------------------- #

sections:
  - title: "Multiple Destination basics"
    anchor: "basics"
    summary: "Some Multiple Destination basics"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "What are multiple destinations?"
        anchor: "basics--what-are-multiple-destinations"
        content: |
          This feature allows you to load data from your integrations into more than one destination in your Stitch account.

      - title: "How can I use multiple destinations?"
        anchor: "basics--how-can-i-use-multiple-destinations"
        content: |
          **You have multiple environments**. You may want to ensure you have clean data. To do this you can house your quality assurance and production environments in the same Stitch account instead of having to maintain two unique warehouses to ingest data from each other.

          **You want to separate your raw data ingestion from your transformed data ingestion**. You can use multiple destinations in your Stitch to load raw data from integrations into a data lake for transformation, then load your transformed data into a separate warehouse.
      
      - title: "Who can use multiple destinations?"
        anchor: "basics--who-can-use-multiple-destinations"
        content: |
          Clients on a Stitch Advanced or Premium plan can use this feature.

      - title: "How many destinations can I have?"
        anchor: "basics--how-many-destinations-can-i-have"
        content: |
          The default limit is 3 destinations per Stitch Advanced account, and five destinations per Stitch Premium account. To increase this limit, you must pay an add-on per additional destination. Stitch can support up to 10 destinations per account.
        
      - title: "Can I send data from one integration to multiple destinations?"
        anchor: "basics--sending-data-to-multiple-destinations"
        content: |
          You can't connect a single integration to multiple destinations, but you can create multiple integrations for the same data source and connect them to different destinations. The easiest way to do this is to use the connection cloning feature:
          
            1. Create a first integration and connect it to a destination.
            2. Follow the instructions in the [connection cloning documentation]({{ site.data.urls.integrations.connection-cloning | prepend: site.baseurl | prepend: site.home }}) to clone the integration and select a different destination.
        
      - title: "What happens to my other destinations if I downgrade my plan?"
        anchor: "basics--what-happens-when-i-downgrade-my-plan"
        content: |
          Stitch will place a hold on your account if your destination count is higher than your destination limit. When a hold is placed or lifted, you will receive an email from Stitch notifying you of the changes.

      - title: "What happens when I delete a destination?"
        anchor: "basics--deleting-a-destination"
        content: |
          When you delete a destination, two things will happen. All post-load webhooks linked to the deleted destination will also be deleted. You will have to re-add them again if you still would like to use them in your other destinations. You will also have to choose if all data sources mapped to the deleted destination will be paused for replication or deleted. To continue replication of data, you must go back into the integration setup and re-map to where the data will be loaded. 


  - title: "Modifying destinations"
    anchor: "changing-multiple-destinations"
    summary: "An overview on how to add, remove, and edit your destinations"
    content: |
      In this section, you will learn how to add, delete, or edit a destination when you have more than one.

    subsections:
      - title: "Adding another destination through the Stitch app"
        anchor: "adding-destinations-app"
        content: |
          1. Login to your Stitch account.
          2. Click **Destinations** in the top navigation.
          3. Click **Add Destination** in the top right portion of the page.
          4. Select the destination you would like to setup. If you aren't sure of which destination you should pick, follow [this guide]({{ link.destinations.overviews.choose-destination | prepend: site.baseurl }}) to help you make the decision that best suits your needs.

      - title: "Adding another destination through the Stitch Connect API"
        anchor: "adding-destinations-api"
        content: |
          If you want to add an aditional destination through the API, check out our [Create a Destination with the Connect API]({{ link.connect.guides.create-configure-a-destination | prepend: site.baseurl }}) guide.

      - title: "Deleting a destination"
        anchor: "deleting-destinations"
        content: |
          {% capture deleting-destinations%}
          You will be asked to pause or delete any source integrations you have mapped to the destination, and all post-load webhooks will automatically be removed.
          {% endcapture %}

          {% include important.html first-line="**Some things to take note of when deleting a destination**" content=deleting-destinations %}

          1. Login to your Stitch account.
          2. Click **Destinations** in the top navigation.
          3. Select the destination you would like to remove.
          4. On the setup page of your destination, click **Delete Destination** at the bottom of the setup.
          5. Select whether you want to pause replication for the integration sources that you have mapped to the destination, or delete them.
          6. Confirm that you want to remove the source by typing `DELETE` in the text box.
          7. Click **Remove Destination**.

            
      - title: "Editing a destination"
        anchor: "editing-destinations"
        content: |
          1. Login to your Stitch account.
          2. Click **Destinations** in the top navigation.
          3. Select the destination you would like to edit.
          4. Make the edits you want to make. Currently you can edit the name and description. All other available edits are specific to the data warehouse you have.
          5. Save your changes.
          

  - title: "Mapping to your destinations"
    anchor: "mapping-to-destinations"
    summary: "The data transformations Stitch performs"
    content: |
      In this section you will learn how to map your data sources in Stitch to your destinations.
      

    subsections:
      - title: "Mapping through the Stitch app"
        anchor: "mapping-integrations-app"
        content: |
          To map a source to a destination through the Stitch app is a very simple process. Within your setup page, you will be able to select which destination you would like to map your integration to.

          1. Login to your Stitch account.
          2. Click **Integrations** in the top navigation.
          3. Select the integration you would like to map to your destination.
          4. In the **Target Destination** section, select your destination. If you don't want to map to a destination, select **No Destination**.
          5. Save your changes.

      - title: "Mapping through the Stitch Connect API"
        anchor: "mapping-integrations-app"
        content: |
          Mapping your data sources to via the Stitch Connect API is also a very simple process and you can do it in the Sources POST. Check out our docs on [how to create a source]({{ link.connect.api | prepend: site.baseurl | append: "#create-a-source" }}) to learn how to do this.
          
---