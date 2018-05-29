#!/usr/bin/env ruby
require 'optparse'
require 'json'
require 'yaml'

options = {}
# OptionParser.new do |opts|
#   opts.banner = "Usage: example.rb [options]"

#   opts.on('-n', '--sourcename NAME', 'Source name') { |v| options[:source_name] = v }
#   opts.on('-h', '--sourcehost HOST', 'Source host') { |v| options[:source_host] = v }
#   opts.on('-p', '--sourceport PORT', 'Source port') { |v| options[:source_port] = v }

# end.parse!

#puts options

if ARGV.length == 0
  puts "Usage: example.rb <Schema File>"
  exit
end

puts ARGV

# puts "What JSON file you want to convert?"
#   file = gets.chomp
#   file.downcase!
#   jsonFile = File.read("#{file}.json")
# jsonParsed = JSON.parse(jsonFile)
# outputArray = []
# jsonParsed["properties"].each do |key, value|
#   nameLine = "- name: \"" + key.to_s + "\""
#   typeLine = "\n  type: \"" + value["type"] + "\""
#   # typeLine = "\n  type: \"" + value["type"][1] + "\""
#   if value["description"]
#     descriptionLine = "\n  description: \"" + value["description"] + "\"\n"
#   else
#     descriptionLine = "\n  description:\n"
#   end
#   # if value["type" == "array"]
#   #   attributesLine = "\n array-attributes:"
#   # end
#   outputArray << nameLine + typeLine + descriptionLine
#   # + attributesLine
# end

# puts outputArray
# yaml = YAML.dump(outputArray)
# File.write("#{file}.yaml", yaml)
