---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Multiple Destinations Overview
permalink: /destinations/multiple-destinations
keywords: destination, destinations, data warehouse, data warehouses, warehouse, stitch etl, etl, multiple destinations

summary: "If you're looking to map your Stitch integrations to more than one destination, this guide will help you set them up."

layout: general
toc: true

key: "multiple-destinations"

type: "all"
destination: false

# -------------------------- #
#         GUIDE INTRO        #
# -------------------------- #

intro: |
  You can now add multiple destinations to your Stitch account! In this guide, you will learn everything you need to know on how to fully utilize this feature. Before selecting destinations, we recommend reading our guide how how to choose a destination (link those docs) to ensure you're making the decision that best suits your data warehousing needs.


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
          QA and PROD loads
          Webhooks
          ask Akshat for more use cases

      
      - title: "Who can use multiple destinations?"
        anchor: "basics--who-can-use-multiple-destinations"
        content: |
          LEARN THE NEW PRICING PLAN TO ANSWER THIS QUESTION

      - title: "How many destinations can I have?"
        anchor: "basics--how-many-destinations-can-i-have"
        content: |
          As of now, you can have up to five destinations per account.
        
      - title: "Can I send data from one integration to multiple destinations?"
        anchor: "basics--sending-data-to-multiple-destinations"
        content: |
          Yes, you can! Head over to the [**Mapping your destinations**](#mapping-to-destinations) section for instructions on how to do that.
        
#      - title: "What happens to my other destinations if I downgrade my plan?"
#        anchor: "basics--who-can-use-multiple-destinations"
#        content: For the initial launch, nothing will be done, but the plan in the future is that a hold will be issued for plan downgrades.

      - title: "What happens when I delete a destination?"
        anchor: "basics--who-can-use-multiple-destinations"
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
          4. Select the destination you would like to setup. If you aren't sure of which destination you should pick, follow this guide to help you make the decision that best suits your needs. (link the "choosing a destination" page)

      - title: "Adding another destination through the Stitch Connect API"
        anchor: "adding-destinations-api"
        content: 
          If you want to add through the API, (link docs)

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
          4. Make the edits you want to make. Currently you can edit the name & description. All other available edits are specific to the data warehouse you have.
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
          To map a source to a destination through the Stitch app is a very simple process. Within your setup page, you will be able to select which destination you would like to map your intgration to.

          1. Login to your Stitch account.
          2. Click **Integrations** in the top navigation.
          3. Select the integration you would like to map to your destinations.
          4. In the **Target Destination** section, select your destinations. If you don't want to map to a destination, select **No Destination**.
          5. Save your changes.

      - title: "Mapping through the Stitch Connect API"
        anchor: "mapping-connect-api"
        content: |


          
---