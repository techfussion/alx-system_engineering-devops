#!/usr/bin/env ruby

sender = ARGV[0].scan(/\[from:(.+?)\]/).flatten
receiver = ARGV[0].scan(/\[to:(.+?)\]/).flatten
flags = ARGV[0].scan(/\[flags:(.+?)\]/).flatten
puts [sender, receiver, flags].flatten.join(',')
