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

1. Using a SQL or command line tool, login to your Redshift database as an administrator. 
2. The query below is run against tables in the `information_schema` and will find all first-order dependency for the schema noted in the error notification.

   Run the query below, replacing what’s in the `[square brackets]` with the table name:

   ```sql
   SELECT DISTINCT c_p.oid AS tbloid
     ,n_p.nspname AS schemaname
     ,c_p.relname AS NAME
     ,n_c.nspname AS refbyschemaname
     ,c_c.relname AS refbyname
     ,c_c.oid AS viewoid
   FROM pg_class c_p
   JOIN pg_depend d_p ON c_p.relfilenode = d_p.refobjid
   JOIN pg_depend d_c ON d_p.objid = d_c.objid
   JOIN pg_class c_c ON d_c.refobjid = c_c.relfilenode
   LEFT JOIN pg_namespace n_p ON c_p.relnamespace = n_p.oid
   LEFT JOIN pg_namespace n_c ON c_c.relnamespace = n_c.oid
   WHERE d_c.deptype = 'i'::"char"
   AND c_c.relkind = 'v'::"char"
   AND name = '[table_name]'
   ```
3. Now that you’ve found the dependent view, you can run a command to drop it. To ensure all dependent views are dropped, use the `CASCADE` option. Remember to use the correct schema and dependent view name when running this yourself:

   ```sql
   DROP VIEW [error_schema].[dependent_view] CASCADE;
   ```
4. After Stitch has completed its replication cycle, you can re-create your views. If you opted not to initially [re-create your views as late binding views](#late-binding-views), this may be a good time to do so.

   **Note**: the amount of time required to perform table alterations depends on the size of the table in question. While dropping dependent views for an hour or two is typically sufficient to complete the process, some very large tables may require more time. 

---

## Contact Support

If new data still hasn't entered your warehouse after converting to late binding views or dropping dependent views overnight, reach out to support.