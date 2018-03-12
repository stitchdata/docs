---
title: Stitch Connect API
permalink: /stitch-connect/api
sidebar: api
layout: api
toc: false
summary: false

api-base-url: "https://api.stitchdata.com"
endpoint-tabs: true
contact-email: "product@stitchdata.com"
api-name: "Connect API"
api-type: "embed"

anchors:
  introduction: "#introduction"
  quick-start: "#quick-start"
  authentication: "#authentication"
  response-codes: "#response-codes"
  versioning: "#versioning"

# -------------------------- #
#        CORE OBJECTS        #
# -------------------------- #

  core-objects:
    section: "#core-objects"

  # -------------------------- #
  #          Accounts          #
  # -------------------------- #

    accounts:
      section: "#accounts"
      create-an-account: "#create-an-account"

  # -------------------------- #
  #        Destinations        #
  # -------------------------- #

    destinations:
      section: "#destinations"
      object: "#destination--object"
      create-a-destination: "#create-a-destination"
      update-a-destination: "#update-a-destination"
      list-destinations: "#list-destinations"

  # -------------------------- #
  #          Sessions          #
  # -------------------------- #

    sessions:
      section: "#sessions"
      object: "#session--object"
      create-a-session: "#create-a-session"

  # -------------------------- #
  #        Source Types        #
  # -------------------------- #

    source-types:
      section: "#source-types"
      object: "#source-type--object"
      get-a-source-type: "#get-a-source-type"
      list-source-types: "#list-source-types"

  # -------------------------- #
  #          Sources          #
  # -------------------------- #

    sources:
      section: "#sources"
      object: "#source--object"
      create-a-source: "#create-a-source"
      update-a-source: "#update-a-source"
      list-sources: "#list-sources"
      retrieve-a-source: "#retrieve-a-source"



# -------------------------- #
#       DATA STRUCTURES      #
# -------------------------- #

  data-structures:
    section: "#data-structures"

  # -------------------------- #
  #     Connection Checks      #
  # -------------------------- #

    connection-checks: "#connection-check-object"

  # -------------------------- #
  #      Connection Steps      #
  # -------------------------- #

    connection-steps: "#connection-step-object"

  # -------------------------- #
  #     Current Step Hints     #
  # -------------------------- #

    current-step-hints: "#current-step-hint-object"
    api-hints: "#current-step-api-hint-object"
    stitch-js-hints: "#current-step-stitch-js-hint-object"

  # -------------------------- #
  #         Properties         #
  # -------------------------- #

    properties: "#properties-object"

  # -------------------------- #
  #         Report Cards       #
  # -------------------------- #

    report-cards: "#report-card-object"



# -------------------------- #
#       FORM PROPERTIES      #
# -------------------------- #

  form-properties:
    section: "#form-properties"

  # -------------------------- #
  #     Destination Forms      #
  # -------------------------- #

    destination-forms:
      section: "#destination-form-properties"

      postgresql: "#destination-form-properties-postgresql-object"
      redshift: "#destination-form-properties-redshift-object"
      snowflake: "#destination-form-properties-snowflake-object"

  # -------------------------- #
  #        Source Forms        #
  # -------------------------- #

    source-forms:
      section: "#source-form-properties"

      hubspot: "#source-form-properties-hubspot-object"
      marketo: "#source-form-properties-marketo-object"
      salesforce: "#source-form-properties-salesforce-object"



# -------------------------- #
#          STITCH.JS         #
# -------------------------- #

  stitch-js:
    section: "#stitch-js"

  ## addSource(options)
    create-a-source: "#source-creation-function"

  ## authorizeSource(options)
    authorize-a-source: "#source-authorization-function"

  ## displayDiscoveryOutputForSource(options)
    source-discovery: "#source-discovery-function"

  ## selectStreamsForSource(options)
    select-streams: "#source-stream-selection-function"

  ## editSource(options)
    edit-source: "#source-editing-function"
---
