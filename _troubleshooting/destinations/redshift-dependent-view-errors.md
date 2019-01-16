---
title: Redshift View Dependency Errors
keywords: troubleshooting, destination, trouble, issue, help, error, errors, redshift, panoply, late binding views, view dependency, dependent view, view, cascade
permalink: /troubleshooting/destinations/redshift-dependent-view-errors
tags: [troubleshooting_destinations, troubleshooting_errors]

summary: "If you've received a 'Dependent Views' error for your Redshift or Panoply data warehouse, you may need to temporarily drop dependent objects."
type: "redshift-destination, error, replication"
promote: "false"


solutions-pros-cons:
  - option: "Late Binding Views"
    anchor: "late-binding-views"
    pros:
      - item: "Dependency errors from [widening `VARCHAR` columns]({{ link.destinations.storage.varchar-widening | prepend: site.baseurl }}) will become a non-issue."
      - item: "Dependency errors from underlying table schema changes - such as adding a new column - will become a non-issue."
    cons:
      - item: |
          Views may 'break' when a [column splits due to multiple data types]({{ link.destinations.storage.column-splitting | prepend: site.baseurl }}). This is because Stitch currently renames the original column to append the data type. For example: `sales_order` becomes `sales_order__st`.

          In this scenario, the view will need to be re-created as definitions for existing views cannot be changed.
  - option: "Manual Drop & Cascade"
    anchor: "locate-drop-dependent-views"
    pros:
      - item: "When re-created after dropping, views can be updated to add/remove columns, allowing you to capture schema changes as-needed."
    cons:
      - item: "Dependency errors will still occur from `VARCHAR` widening, underlying schema changes, etc."
      - item: "As a manual process, this requires someone to spend time locating, dropping, and re-creating dependent views."
      - item: "Dependent views cannot be re-created until Stitch finishes updating the underlying object."
---
{% include misc/data-files.html %}

> ERROR: cannot drop table [schema_name].[table_name] column [column_name] because other objects depend on it
>
> Hint: Use DROP ... CASCADE to drop the dependent objects too.

Typically, this error - along with missing views and incorrect data in views - are a result of how Stitch handles altered table structures and views with dependencies in Redshift.

---

## Structural Changes in Tables

A table's structure can change for a few reasons:

- A new column has been added to the source table
- A new column has been added to the table as a result of [column/data type splitting]({{ link.destinations.storage.column-splitting | prepend: site.baseurl }})
- A new column has been added to the table as a result of [`VARCHAR` widening]({{ link.destinations.storage.varchar-widening | prepend: site.baseurl }})

When a table's structure changes, dependent views must be temporarily [dropped](http://docs.aws.amazon.com/redshift/latest/dg/r_DROP_VIEW.html) so Stitch can re-create the underlying table.

Because we don’t want to affect your work without your say-so, Stitch will not automatically drop views with dependencies.

---

## Workarounds

Depending on your workflow and needs, there are two ways you can approach this issue:

- **Option 1:** Use [Redshift's late binding views](http://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_VIEW.html#r_CREATE_VIEW_late-binding-views){:target="new"} to "detach" the dependent view from the underlying table, thus preventing future dependency errors. Late binding views are views that don't check underlying tables until the view is queried.
- **Option 2:**  Manually locate and drop cascade the dependent views when dependency errors arise.

### Solution Pros & Cons

Before you pick a solution, you should be aware of the pros and cons of each one:

{% for solution in page.solutions-pros-cons %}
##### [{{ forloop.index | prepend: "Option " }}: {{ solution.option }}](#{{ solution.anchor }})

<table width="100%">
	<tr>
		<th width="50%; fixed">Pros</th>
		<th width="50%; fixed">Cons</th>
	</tr>
	<tr>
		<td>
			<ul>
			{% for pro in solution.pros %}
				<li>{{ pro.item | flatify | markdownify }}</li>
			{% endfor %}
			</ul>
		</td>
		<td>
			<ul>
			{% for con in solution.cons %}
				<li>{{ con.item | flatify | markdownify }}</li>
			{% endfor %}
			</ul>
		</td>
	</tr>
</table>
{% endfor %}

---

## Next Steps

### Option 1: Re-Create Views as Late Binding Views {#late-binding-views}

When a view is created, you can add the `WITH NO SCHEMA BINDING` clause to the query to indicate that the view should not be bound to the underlying database objects. This will eliminate the dependency between the view and the object(s) it references:

```sql
CREATE VIEW sales_orders_view AS
	SELECT *
	FROM stitch_mysql.orders
	WITH NO SCHEMA BINDING;
```

**Note**: You can't update, insert into, or delete from a view. This means that if you want to add or remove columns, you need to re-create the view.

If you chose this option to resolve an error after a column was split and renamed, remember to include all the subsequent split columns when you re-create the view. For example: if `sales_order` 'split' into `sales_order__int` and `sales_order__st`, you'd want to include both columns to ensure all values are captured in the view.

---

### Option 2: Manually Locate & Temporarily Drop Dependent Views {#locate-drop-dependent-views}

#### Step 1: Create a View of Tables and Dependencies

{% include note.html type="first-line" content ="You need to have access to the `pg_catalog` schema and its tables and be able to run the `CREATE VIEW` command to complete this step." %}

First, you'll create a view called `view_dependencies` that lists the tables and view dependencies in your data warehouse. You will only need to perform this step once.

Using a SQL or command line tool, login to your Redshift database as an administrator and execute the following command. Our view will be created in the root of the database, but you can create it in a specific schema if you prefer:

```sql
CREATE VIEW view_dependencies AS
SELECT DISTINCT source_class.oid AS source_table_id,
                source_namespace.nspName AS source_table_schema,
                source_class.relName AS source_table_name, 
                dependent_class.oid AS dependent_view_id,
                dependent_namespace.nspName AS dependent_view_schema,
                dependent_class.relName AS dependent_view_name
           FROM pg_class source_class 
           JOIN pg_depend source_depend 
             ON source_class.relFileNode = source_depend.refObjId
           JOIN pg_depend dependent_depend 
             ON source_depend.objId = dependent_depend.objId
           JOIN pg_class dependent_class 
             ON dependent_depend.refObjId = dependent_class.relFileNode
      LEFT JOIN pg_namespace source_namespace 
             ON source_class.relNameSpace = source_namespace.oid
      LEFT JOIN pg_namespace dependent_namespace 
             ON dependent_class.relNameSpace = dependent_namespace.oid
          WHERE dependent_depend.depType = 'i'::"char"
            AND dependent_class.relKind = 'v'::"char"
```

The above command only selects [dependencies with a type](https://www.postgresql.org/docs/9.3/static/catalog-pg-depend.html) of `i`, or those that can only be dropped by running `DROP...CASCADE` on the dependent object itself. Additionally, only [dependent relations that are views](https://www.postgresql.org/docs/9.3/static/catalog-pg-class.html) (`relKind = 'v'`) are included in the results.

#### Step 2: Query the View to Locate Dependencies

Next, you'll query the `view_dependencies` view you created in Step 1 to locate the objects you need to drop. If the notification referenced the `closeio.closeio_leads` table, the query would look like this:

```sql
SELECT source_table_schema,
       source_table_name,
       dependent_view_schema,
       dependent_view_name
  FROM view_dependencies
 WHERE source_table_schema = 'closeio'
   AND source_table_name = 'closeio_leads'
```

And in the results:

| source_table_schema | source_table_name | dependent_view_schema | dependent_view_name   |
|---------------------|-------------------|-----------------------|-----------------------|
| closeio             | closeio_leads     | dbt                   | lead_addresses        |

Which indicates that the `lead_addresses` view in the `dbt` schema is the dependent object that's causing issues.

#### Step 3: Drop the Dependent View

Now that you’ve found the dependent view, you can run a command to drop it. Remember to save the view's definition somewhere before continuing if you want to re-create it later.

To ensure all dependent views are dropped, use the `CASCADE` option and replace the schema and view names as needed:

```sql
DROP VIEW dbt.lead_addresses CASCADE;
```

After Stitch has completed its replication cycle, you can re-create your views. If you opted not to initially [re-create your views as late binding views](#late-binding-views), this may be a good time to do so.

**Note**: The amount of time required to perform table alterations depends on the size of the table in question. While dropping dependent views for an hour or two is typically sufficient to complete the process, some very large tables may require more time. 

---

## Contact Support

If new data still hasn't entered your warehouse after converting to late binding views or dropping dependent views overnight, reach out to support.