---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Connection Cloning
permalink: /integrations/connection-cloning
keywords: source cloning, connection cloning, cloning, integration cloning

summary: "Want to clone one of your sources in Stitch without having to create a new one from scratch? Learn how with your existing connections."

layout: general
toc: false
level: "guide"
key: "connection-cloning"

# -------------------------- #
#         GUIDE INTRO        #
# -------------------------- #

intro: |
  You can now clone your Stitch source connections! In this guide, you will learn everything you need to know how to fully utilize this feature.


# -------------------------- #
#      CONTENT SECTIONS      #
# -------------------------- #

sections:
  - title: "Connection cloning basics"
    anchor: "basics"
    summary: "Some source cloning basics"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "What is connection cloning?"
        anchor: "basics--what-is-connection-cloning"
        content: |
          This feature allows you to create a simple clone of an existing source connection in your Stitch account. All of your table and field selections can be cloned exactly. You have the option to change the name, and destination of your new connection, but the schema name must be unique.

      - title: "How can I use connection cloning?"
        anchor: "basics--how-to-use-connection-cloning"
        content: |
          **You have multiple destinations**. You may have more than one destination that needs to be loaded with data from the same source. Use the source cloning feature to do this without having to create another connection and re-enter the same information.

          **You need several of the same sources, but with different table and field selections**. In the source's integration setup, you can choose whether or not you want to keep the same table and field selection. Make sure you choose not to keep the same selection when cloning, and then you will be able to select your tables and fields for replication. Keep in mind this feature will not be available if:
            1. The original connection has incomplete table or field selection.
            2. The source doesn't support table selection.

      - title: "Which sources are available to clone?"
        anchor: "basics--which-sources-are-available"
        content: |
          More and more sources are becoming available to clone. To determine if your specific connection can be cloned, you will see that you have the option to clone on your connection's settings page. Currently, cloning is not available for connections that are deprecated.

      - title: "Is there a limit on the amount of connections I can clone?"
        anchor: "basics--connection-cloning-limit"
        content: |
          Nope - clone as many times as you need!



  - title: "How to clone your connection"
    anchor: "clone-your-connection"
    content: |
      {% capture cloning-connections%}
      Some OAuth sources will be prompted to re-authorize. Also, all cloned connetions will be paused upon creation. You will need to turn it on when you're ready to begin replicating data.
      {% endcapture %}

      {% include important.html first-line="**Some things to take note of when cloning a connection**" content=cloning-connections %}

      1. Log into your Stitch account.
      2. Click **Integrations** in the top navigation.
      3. Click on the connection you wish to clone to open the integration summary.
      4. Navigate to the **Settings** tab and the configure page will open.
      5. Click **Clone Integration** to open the cloning setup page.
      6. On the clone setup page, make any changes needed for your new connection and select a target destination for your data. If you'd like to keep the same table and field selection, make sure you check that box.
      7. Click **Authorize** to test and create your new connection.
      8. Turn on your new connection to begin the replication process.
---
