# JSON schema automation

## Import from singer repository
If a tap repository has a schemas folder containing JSON schemas, you can use the [Import JSON schemas](https://github.com/stitchdata/docs/actions/workflows/import_json_schemas.yml) GitHub Action to get these files, format them, and push them to the docs repository. All you need is write access to the repository in order to run the GitHub Action.

1. Go to [Import JSON schemas](https://github.com/stitchdata/docs/actions/workflows/import_json_schemas.yml) and click **Run workflow**.
2. Enter the name of the Singer repository, `tap-pendo` for example.
3. Enter the name of the branch to use if needed. If no branch is specified, the default branch will be used.
4. Click **Run workflow**

The workflow runs and performs the following actions:
- Creates a new branch on the docs repository.
- Retrieves the JSON files from the specified tap repository.
- Formats the JSON files to make them compatible with the HTML templates used to display them. For more details, see [Formatting details](#formatting-details).
- Updates the YAML file containing table details (adds new tables, marks missing tables as not found).
- Checks that the primary keys, replication keys, and foreign keys listed are still found in the schema. If any issues are found, a text file with the list of errors will be added to the integration version folder.
- Commits and pushes the changes.
- Creates a pull request from the new branch to the master branch on the docs repository.

Once the workflow is done, a member of the documentation team will review the pull request and make any updates needed in the YAML files.

## Generate from catalog file
For integration that don't have their JSON schemas in their repositories, you can use the [Get JSON schemas from catalog JSON file](https://github.com/stitchdata/docs/actions/workflows/get_json_schema_from_catalog.yml) GitHUb Action to add the schema files from a file generated from the tap's discovery mode.

1. Run the discovery mode and get the catalog JSON file.
2. Create a new branch on the docs repository, add the catalog file in the `scripts/json` folder and push your changes.
3. Go to [Get JSON schemas from catalog JSON file](https://github.com/stitchdata/docs/actions/workflows/get_json_schema_from_catalog.yml) and click **Run workflow**.
4. Enter the name of the tap.
5. Enter the major version of the tap.
6. Enter the name of the docs repository branch where you added the JSON file.
7. Enter the name of the JSON file that you added.
8. If you want a pull request to be automatically created by the workflow, select the corresponding check box.
9. Click **Run workflow**.

The workflow runs and performs the following actions:
- Splits the catalog file into separate JSON files for each stream and adds them in the correct folder
- Formats the JSON files to make them compatible with the HTML templates used to display them. For more details, see [Formatting details](#formatting-details).
- Updates the YAML file containing table details (adds new tables, marks missing tables as not found).
- Checks that the primary keys, replication keys, and foreign keys listed are still found in the schema. If any issues are found, a text file with the list of errors will be added to the integration version folder.
- Deletes the catalog file.
- Commits and pushes the changes.
- If the check box is selected, creates a pull request from the your branch to the master branch on the docs repository. Otherwise, you can create your own pull request.

Once the pull request is created, a member of the documentation team will review the pull request and make any updates needed in the YAML files.

## Formatting details
The workflows format JSON files to fix some issues that would prevent the correct display of the schema tables in the documentation. Here are the changes made:

- References to other JSON content, using `$ref` are replaced with the actual referenced content.
- Elements with a `format` element, `"format": "date-time"` for example, are updated so that the format appears as in the `type` element instead.
- Object elements that don't have a `properties` child element as a container for the object's properties are updated to add this `properties` container, because it is needed to display the elements in the object. 

## Foreign keys automation
The [Generate foreign keys](https://github.com/stitchdata/docs/actions/workflows/generate_foreign_keys.yml) GitHUb Action runs every time a change to a `*-foreign-keys.yml` file is push on any branch other than `master`.

It takes the content of the `keys` element in the file and uses it to create the `tables` element, which contains the same content, but organized by table. Each table has a list of all other tables that can be joined to it, and all elements that can be used to perform the join. This is used to create to foreign keys table displayed in the table reference documentation.