---
title: Trello
permalink: /integrations/saas/trello
tags: [saas_integrations]
keywords: trello, integration, schema, etl trello, trello etl, trello schema
summary: "Connection instructions and schema details for Stitch's Trello integration."
format: ## controls formatting options in template
  schema-list: true
  table-desc: true
  list: expand

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "trello"
display_name: "Trello"
singer: false
author: "Stitch"
author-url: "https://www.stitchdata.com"
status-url: "http://www.trellostatus.com/"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
icon: /images/integrations/icons/trello.svg
whitelist:
  tables: false
  columns: false

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

tables:
## Actions
  - name: "trello_actions"
    doc-link: https://developers.trello.com/advanced-reference/board#get-1-boards-board-id-actions
    description: "info about the actions related to cards, including the lists that a card belongs to."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Action ID (<code>id</code>)
      - name: data__board__id
      - name: data__board__name
      - name: data__card__id
      - name: data__card__name
      - name: idmembercreator
      - name: member__avatarhash
      - name: member__fullname
      - name: member__id
      - name: member__initials
      - name: member__username
      - name: membercreator__avatarhash
      - name: membercreator__fullname
      - name: membercreator__id
      - name: membercreator__initials
      - name: membercreator__username
      - name: type

## Boards
  - name: "trello_boards"
    doc-link: https://developers.trello.com/advanced-reference/member#get-1-members-idmember-or-username-boards
    description: "details about all the boards that the connection (authorizing user) is a member of."
    notes: 
    replication-method: "Full Table"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Board ID (<code>id</code>)
      - name: closed
      - name: datelastactivity
      - name: datelastview
      - name: desc
      - name: descdata
      - name: idorganization
      - name: invitations
      - name: invited
      - name: labelnames__black
      - name: labelnames__blue
      - name: labelnames__green
      - name: labelnames__lime
      - name: labelnames__orange
      - name: labelnames__pink
      - name: labelnames__purple
      - name: labelnames__red
      - name: labelnames__sky
      - name: labelnames__yellow
      - name: name
      - name: prefs__permissionlevel
      - name: prefs__voting
      - name: prefs__comments
      - name: prefs__invitations
      - name: prefs__selfjoin
      - name: prefs__cardcovers
      - name: prefs__calendarfeedenabled
      - name: prefs__background
      - name: prefs__backgroundimage
      - name: prefs__backgroundimagesscaled<code>*</code>
      - name: prefs__backgroundtile
      - name: prefs__backgroundbrightness
      - name: prefs__canbepublic
      - name: prefs__canbeorg
      - name: prefs__canbeprivate
      - name: prefs__caninvite
      - name: memberships<code>*</code>
      - name: powerups<code>*</code>
      - name: shortlink
      - name: shorturl
      - name: starred
      - name: subscribed
      - name: url

## Cards
  - name: "trello_cards"
    doc-link: https://developers.trello.com/advanced-reference/card#get-1-cards-card-id-or-shortlink
    description: "info about the latest state of all the cards that the connection (authorizing user) has access to."
    notes: &replication |
      This table is updated based on the `actions` table.
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Card ID (<code>id</code>)
      - name: desc
      - name: checkitemstates<code>*</code>
      - name: idchecklists<code>*</code>
      - name: idlabels<code>*</code>
      - name: idmembers<code>*</code>
      - name: labels<code>*</code>
      - name: closed
      - name: datelastactivity
      - name: due
      - name: duecomplete
      - name: idattachmentcover
      - name: idboard
      - name: idlist
      - name: idshort
      - name: manualcoverattachment
      - name: name
      - name: pos
      - name: shorturl
      - name: url
      - name: badges__attachments
      - name: badges__checkitems
      - name: badges__checkitemschecked
      - name: badges__comments
      - name: badges__description
      - name: badges__due
      - name: badges__duecomplete
      - name: badges__subscribed
      - name: badges__viewingmembervoted
      - name: badges__votes

## Checklists
  - name: "trello_checklists"
    doc-link: https://developers.trello.com/advanced-reference/checklist#get-1-checklists-idchecklist
    description: "info about the latest state of all the checklists on cards that the connection (authorizing user) has access to."
    notes: *replication
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Checklist ID (<code>id</code>)
      - name: idboard
      - name: idcard
      - name: name
      - name: pos
      - name: "checkitems<code>*</code>: Contains columns for <code>idchecklist, name, pos,</code> and <code>state</code>."

## Lists
  - name: "trello_lists"
    doc-link: https://developers.trello.com/advanced-reference/board#get-1-boards-board-id-lists
    description: "info about all the lists the connection (authorizing user) has access to."
    notes: 
    replication-method: "Full Table"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: List ID (<code>id</code>)
      - name: closed
      - name: idboard
      - name: name
      - name: pos
      - name: subscribed

## Users
  - name: "trello_users"
    doc-link: 
    description: "info about the users in your Trello account/organization."
    notes: 
    replication-method: "Full Table"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: User ID (<code>id</code>)
      - name: fullname
      - name: username
---
{% assign integration = page %}
{% include misc/data-files.html %}



{% contentfor setup %}
Connecting your Trello data to Stitch is a four-step process:

1. [Retrieve your Developer API Keys from Trello](#retrieve-trello-api-keys)
2. [Add Trello as a Stitch data source](#add-stitch-data-source)
3. [Define the Historical Sync](#define-historical-sync)
4. [Define the Replication Frequency](#define-rep-frequency)

{% capture access %}
**Stitch & Accessing Trello Data**<br>
Stitch will only have access to the boards that the user who creates the integration has access to. If a board is private and the user isn't a member, Stitch will be unable to access it. Before beginning the setup process, verify that the user setting up the integration has access to all the boards you want to replicate.
<br><br>
You can use [Trello's Developer Sandbox](https://developers.trello.com/sandbox) - no coding knowledge needed - to check your access by simply entering your API Key (see below) and authenticating. Select the **Get Boards** option and click **Execute** to see a JSON list of the boards the user has access to.
{% endcapture %}
{% include important.html content=access %}

### Retrieving Your Developer API Keys from Trello {#retrieve-trello-api-keys}
1. Sign into your Trello account.
2. Go to the [Trello Developer API Keys page](https://trello.com/app-key/).
3. Locate the **Key** and **Secret** fields. 

Leave this page open for now - you'll need it to complete the setup in Stitch.

{% include integrations/shared-setup/connection-setup.html %}
4. Enter your Trello API Key and Secret into their respective fields.

{% include integrations/saas/setup/historical-sync.html %}

{% include integrations/shared-setup/replication-frequency.html %}

{% include integrations/shared-setup/initial-syncs.html %}
{% endcontentfor %}
