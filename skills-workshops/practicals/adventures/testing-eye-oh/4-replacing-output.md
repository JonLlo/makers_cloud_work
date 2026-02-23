
## 4. Replacing Output

### Learning Objectives
- [ ] Explain that ruby has a `StringIO` object that can be used as a pseudo IO object

### Intro

Let's use `StringIO`. If we assign the `$stdout` variable the value of a `StringIO` instance, we can then write to it using `#puts`.

```ruby
# in pry
> replacement_output = StringIO.new
=> #<StringIO:0x00007fbc80276868>
> $stdout = replacement_output
=> #<StringIO:0x00007fbc80276868>

```

Then try the following, either

```ruby
> puts 'Hi, Pair Partner!'  # remember that #puts is called implicitly on the default value stored in $stdout
```

or explicitly either:

```ruby
replacement_output.puts 'Hi, Pair Partner!'
# or
$stdout.puts 'Hi, Pair Partner!'
```

Where's the output gone?!

### To complete this challenge, you will need to:

- [ ] Discuss with your partner what you observe
- [ ] Find where the string has been stored
- [ ] Using pry, see what exactly has been stored and discuss what you see

### Resources

- [ruby docs - StringIO](http://ruby-doc.org/stdlib-2.5.0/libdoc/stringio/rdoc/StringIO.html)

[Back to project map](./README.md#project-map)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=practicals/adventures/testing-eye-oh/4-replacing-output.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=practicals/adventures/testing-eye-oh/4-replacing-output.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=practicals/adventures/testing-eye-oh/4-replacing-output.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=practicals/adventures/testing-eye-oh/4-replacing-output.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=practicals/adventures/testing-eye-oh/4-replacing-output.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
