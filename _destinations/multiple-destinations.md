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
  - title: "Requirements to obtain multiple destinations"
    anchor: "multiple-destinations-requirements"
    summary: "How to obtain multiple destinations for your Stitch account"
    content: |


  - title: "Modifying destinations"
    anchor: "changing-multiple-destinations"
    summary: "An overview on how to add, remove, and edit your destinations"
    content: |
      In this section, you will learn how to add, delete, or edit a destination when you have more than one.

    subsections:
      - title: "Adding another destination"
        anchor: "adding-destinations"
        content: |
          1. Login to your Stitch account.
          2. Click **Destinations** in the top navigation.
          3. Click **Add Destination** in the top right portion of the page.
          4. Select the destination you would like to setup. If you aren't sure of which destination you should pick, follow this guide to help you make the decision that best suits your needs. (link the choosing a "destination page")

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
          7. Make the edits you want to make. Currently you can edit the name & description. All other available edits are specific to the data warehouse you have.
          5. Save your changes.
          

  - title: "Mapping to your destinations"
    anchor: "mapping-to-destinations"
    summary: "The data transformations Stitch performs"
    content: |
      Mapping destinations through Stitch is simple
      

    subsections:
      - title: "Mapping through the Stitch app"
        anchor: "mapping-integrations-app"
        content: |
         To map a source to a destination through the Stitch app is a very simple process. Within your setup page, you will be able to select which

      - title: "Mapping through the Stitch Connect API"
        anchor: "mapping-connect-api"
        content: |
          
---