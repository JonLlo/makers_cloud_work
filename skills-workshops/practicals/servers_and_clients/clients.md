Clients 1
=========

## Learn to

* Learn about something by playing with a toy version

## Introduction

In [Servers 1](servers.md) we played around with a toy server. We used the terminal command `telnet` to connect to it. `telnet` was our client.

We're going to build our own client today.

## Exercise 1

Here's our server for today:

```ruby
require 'socket'

server = TCPServer.new(2345)

puts "The server is running. Open a new terminal to run the client."

socket = server.accept

socket.puts "HELLO CLIENT WHAT IS YOUR NAME?"
name = socket.gets.chomp
socket.puts "THAT'S A LOVELY NAME #{name}"

socket.close
```

And here's our client:

```ruby
require 'socket'

socket = TCPSocket.new('localhost', 2345)

puts socket.gets
puts "Wow what a rude server... I'm going to say Sarah"
socket.puts "Sarah"
puts socket.gets

socket.close
```

Get the server running. Then in another terminal window, run the client.

You should see something like this:

```
$ ruby client.rb
HELLO CLIENT WHAT IS YOUR NAME?
Wow what a rude server... I'm going to say Sarah
THAT'S A LOVELY NAME Sarah
```

## Exercise 2

Experiment and play around with the code to learn how it works.

For example: try to get the client and server talking to each other forever (or until you terminate them).

If you are on the same wifi network as another computer, you can try using the
client on one person's laptop to connect to the server on another person's
laptop.

Or anything you like! What do you want to know about how these things work
together? How can you play around with these examples to find out?

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=practicals/servers_and_clients/clients.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=practicals/servers_and_clients/clients.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=practicals/servers_and_clients/clients.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=practicals/servers_and_clients/clients.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=practicals/servers_and_clients/clients.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
