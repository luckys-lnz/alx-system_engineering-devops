#!/usr/bin/env ruby


# Your script should output: [SENDER],[RECEIVER],[FLAGS]
#+ The sender phone number or name (including country code if present)
#+ The receiver phone number or name (including country code if present)
#+ The flags that were used

input = ARGV[0]

if input.nil?
  puts "Please provide input."
else
  from = input.scan(/from:(.*?)\]/)
  to = input.scan(/to:(.*?)\]/)
  flags = input.scan(/flags:(.*?)\]/)

  if from.empty? || to.empty? || flags.empty?
    puts "Invalid input format."
  else
    puts "From: #{from.flatten.first}"
    puts "To: #{to.flatten.first}"
    puts "Flags: #{flags.flatten.first}"
  end
end

