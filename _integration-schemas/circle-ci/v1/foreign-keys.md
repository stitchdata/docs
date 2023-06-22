---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "circle-ci"

version: "1"

foreign-keys:
  - id: "pipeline-id"
    table: "pipelines"
    attribute: "id"
    all-foreign-keys:
      - table: "pipelines"
        join-on: "id"
      - table: "jobs"
        join-on: "_pipeline_id"
      - table: "workflows"
        join-on: "pipeline_id"    
        
  - id: "workflow-id"
    table: "workflows"
    attribute: "id"
    all-foreign-keys:
      - table: "workflows"
        join-on: "id"
      - table: "jobs"
        join-on: "_workflow_id"      
---