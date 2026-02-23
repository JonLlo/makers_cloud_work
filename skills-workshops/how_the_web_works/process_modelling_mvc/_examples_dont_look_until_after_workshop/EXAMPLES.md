# Process Model Examples

Here are sequence diagrams that model the processes.

They were made using the [Mermaid Live Editor](https://mermaid-js.github.io/mermaid-live-editor) that turns text into diagrams.

The Mermaid code used to generate the images is captured here, so that these diagrams can be updated in the future.

## Home page

![home page sequence diagram](home.png)

Mermaid code:
```
sequenceDiagram
	User->>+Browser: enter home page URL
	Browser->>+Controller: GET /
    Controller->>+View: render :index
    View->>+Controller: HTML
	Controller->>-Browser: 200 OK, HTML
	Browser->>-User: see home page
```

## Add item

Mermaid code:
```
sequenceDiagram
	User->>+Browser: clicks `Add a todo list item`
	Browser->>+Controller: GET /add-item
	Controller->>-Browser: 200 OK, HTML
	Browser->>-User: see form
	User->>+Browser: types in form boxes,presses submit
    Browser->>+Controller: POST /add-item formdata
    Controller->>+Model: Todolist.add_item('item','cat')
    Controller->>-Browser: 303 Redirect '/todolist'
    Browser->>+Controller: GET /todolist
    Controller->>+Model: Todolist.items
    Model->>-Controller: Array of item objects
    Controller->>+View: render :todos with @items
    View->>-Controller: HTML
    Controller->>-Browser: 200 OK, body HTML
    Browser->>-User: see to list
 ```
 ![add item sequence diagram](add_item.png)

 ## By category

 Mermaid code:

``` sequenceDiagram
   User->>+Browser: clicks `View to do list by category`
   Browser->>+Controller: GET /bycategory?category=Finance
   Controller->>+Model: Todolist.by_category("Finance")
   Model->>-Controller: Array of item objects
   Controller->>+View: render :todos with @items
   View->>-Controller: HTML
   Controller->>-Browser: 200 OK, body HTML
   Browser->>-User: see to list

   ```

![by category](by_category.png)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=how_the_web_works/process_modelling_mvc/_examples_dont_look_until_after_workshop/EXAMPLES.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=how_the_web_works/process_modelling_mvc/_examples_dont_look_until_after_workshop/EXAMPLES.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=how_the_web_works/process_modelling_mvc/_examples_dont_look_until_after_workshop/EXAMPLES.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=how_the_web_works/process_modelling_mvc/_examples_dont_look_until_after_workshop/EXAMPLES.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=how_the_web_works/process_modelling_mvc/_examples_dont_look_until_after_workshop/EXAMPLES.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
