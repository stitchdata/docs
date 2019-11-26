---
title: Trello
permalink: /integrations/saas/trello
keywords: trello, integration, schema, etl trello, trello etl, trello schema
summary: "Connection instructions and schema details for Stitch's Trello integration."
layout: singer
old-schema-template: true

key: "trello-setup"

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "trello"
display_name: "Trello"

singer: false
status-url: "http://www.trellostatus.com/"

this-version: "15-12-2015"

api: |
  [{{ integration.display_name }} REST API](https://developers.trello.com/reference){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true

historical: "1 year"
frequency: "30 minutes"
tier: "Free"

anchor-scheduling: true
cron-scheduling: false

table-selection: false
column-selection: false

extraction-logs: false
loading-reports: true

## Row usage details

row-usage-hog: true
row-usage-hog-reasons:
  data-structure: true
  data-volume: true
  lots-of-full-table: false


# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

tables:
## Actions
  - name: "trello_actions"
    doc-link: https://developers.trello.com/advanced-reference/board#get-1-boards-board-id-actions
    description: "info about the actions related to cards, including the lists that a card belongs to."
    notes: 
    replication-method: "Key-based Incremental"
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
    replication-method: "Key-based Incremental"
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
    replication-method: "Key-based Incremental"
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

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **To be a member of every {{ integration.display_name }} board you want to replicate.** If a board is private and the user isn't a member, Stitch will be unable to access it. Before beginning the setup process, verify that the user setting up the integration has access to all the boards you want to replicate.

      You can use [Trello's Developer Sandbox](https://developers.trello.com/sandbox) - no coding knowledge needed - to check your access by simply entering your API Key (see below) and authenticating. Select the **Get Boards** option and click **Execute** to see a JSON list of the boards the user has access to.

setup-steps:
  - title: "Retrieve your developer API keys from {{ integration.display_name }}"
    anchor: "retrieve-trello-api-keys"
    content: |
      1. Sign into your {{ integration.display_name }} account.
      2. Go to the [{{ integration.display_name }} Developer API Keys page](https://trello.com/app-key/){:target="new"}.
      3. Locate the **Key** and **Secret** fields. 

      Leave this page open for now - you'll need it to complete the setup in Stitch.
  - title: "add integration"
    content: |
      4. Enter your {{ integration.display_name }} API Key and Secret into their respective fields.
  - title: "historical sync"
  - title: "replication frequency"
---
{% assign integration = page %}
{% include misc/data-files.html %}