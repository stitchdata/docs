#!/usr/bin/env ruby
require 'optparse'
require 'json'
require 'yaml'

if ARGV.length < 1
  puts "Usage: schema_to_yaml.rb schema_file [schema_file2 ...]"
  puts "       schema_to_yaml.rb catalog_file"
  puts "       schema_to_yaml.rb /path/to/schemas"
  puts " * If a schema has $ref values, the ref will be resolved relative to the location of the file being processed."
  exit -1
end

INDENTATION_LENGTH = 2

$file_root = "."

def write_attribute(node, breadcrumb)
  if node["$ref"]
    ref_data = read_file(File.join($file_root, node["$ref"]))
    puts node
    puts ref_data
    node = ref_data
  end

  if node['type'].is_a?(String)
    types = [node['type']]
  else
    types = node['type'].select { |t|  t != 'null' }
  end
  prepend_size = breadcrumb.length() * INDENTATION_LENGTH
  $yaml_output += ["- name: \"#{breadcrumb.last}\"",
                    "  type: \"#{types.first}\"",
                    "  description: \"#{node['description']}\"\n\n"].map do |l|
    l.prepend( " " * prepend_size)
  end.join("\n")
end

def visit(nodes, breadcrumb)
  if !nodes['properties']
    write_attribute(nodes, breadcrumb)
  else
    nodes['properties'].keys().each do |n|
      next_crumbs = breadcrumb.clone()
      next_crumbs.push(n)

      #visting a node
      if nodes['properties'][n]['properties']
        write_attribute({'type' => ['object'], 'description' => ""}, next_crumbs)
        prepend_size = next_crumbs.length() * INDENTATION_LENGTH
        $yaml_output += "  object-attributes: \n".prepend(" " * prepend_size)

        visit(nodes['properties'][n], next_crumbs)
      elsif nodes['properties'][n]['items'] && nodes['properties'][n]['items'].class() == Hash
        write_attribute({'type' => ['object'], 'description' => ""}, [n])
        prepend_size = next_crumbs.length() * INDENTATION_LENGTH
        $yaml_output += "  object-attributes: \n".prepend(" " * prepend_size)

        visit(nodes['properties'][n]['items'], next_crumbs)
      elsif nodes['properties'][n]['items'] && nodes['properties'][n]['items'].class() == Array
        nodes['properties'][n]['items'].each_with_idx do |idx, item|
          child_crumbs = next_crumbs.clone()
          child_crumbs.append(idx)
          visit(nodes['properties'][n]['items'][idx], child_crumbs)
        end #item
      else
        visit(nodes['properties'][n], next_crumbs)
      end #if

    end # properties
  end
  return nodes
end

def read_file(file_name)
  if !File.exists?(file_name)
    puts "unable to find schema file #{file_name}"
    exit -1
  end

  return JSON.parse(File.read(file_name))
end

file_names = ARGV

# If a directory is passed in, grab all json files from it, recursively
if File.directory?(file_names[0])
  file_names = Dir.glob(File.join(file_names[0], "**/*.json"))
end

file_name = file_names[0]
file_data = read_file(file_name)

if file_data.key?("streams")
  $file_root = File.dirname(file_name)
  # Indicates that discovery output was passed in
  for stream in file_data["streams"];
    $yaml_output = ""
    new_schema = visit(stream['schema'], [])

    puts($yaml_output)

    File.open(stream['stream'] + ".md", "w") do |f|
      f.write($yaml_output)
    end

    puts("Wrote " + stream['stream'] + ".md to the current directory!")
  end
else
  # Indicates that a schema file was passed in
  for file_name in file_names;
    $file_root = File.dirname(file_name)
    file_data = read_file(file_name)
    $yaml_output = ""
    new_schema = visit(file_data, [])

    puts($yaml_output)

    out_name = File.basename(file_name, File.extname(file_name))
    File.open(out_name + ".md", "w") do |f|
      f.write($yaml_output)
    end

    puts("Wrote " + out_name +  ".md to the current directory!")
  end
end
