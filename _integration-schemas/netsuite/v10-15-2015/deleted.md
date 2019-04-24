---
tap: "netsuite"	
version: "10-15-2015"	

name: "netsuite_deleted"	
doc-link: 
description: |	
  The `{{ table.name }}` table contains info about deleted records.	

replication-method: "Full Table"	
abstract: true	

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "deleted"

attributes:	
 - name: "internalId"	
   type: "integer"	
   primary-key: true	
   description: |
     The record ID.

 - name: "type"	
   type: "string"	
   primary-key: true	
   description: "The type of record that was deleted. For example: `invoice`"	

 - name: "deletedDate"	
   type: "date-time"	
   description: |
     The time the record was deleted.	
  
 - name: "customRecord"	
   type: "boolean"	
   description: "Indicates if the deleted record was a custom record."	

 - name: "name"	
   type: "string"	
   description: "The name of the record that was deleted. For example: `Invoice #INV197`"
---