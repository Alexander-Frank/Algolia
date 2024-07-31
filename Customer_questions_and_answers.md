### Question 1:
<em>Hello,

I'm new to search engines, and there are a lot of concepts I'm not educated on. To make my onboarding smoother, it'd help if you could provide me with some definitions of the following concepts:
- Records
- Indexing

I'm also struggling with understanding what types of metrics would be useful to include in the "Custom Ranking." 

Cheers,
George</em>

### Answer 1:

Hi George,

Thanks for reaching out. I'm happy to help, at some point we are all new to a topic.

A record represents the individual search entity and holds its attributes. For example: if you're selling smartphones and want to make your inventory searchable, a record can represent an individual phone and details (attributes) about it which can help people to find (filter) suitable products. An example record could look like this:

```json
[
  {
    "objectID": 42,
    "title": "Google Pixel 8Pro",
    "manufacturer": "Google",
    "os": "Android",
    "avg_customer_rating": 4.5,
    "price": 699
  }
]
```
These records are then sent over to Algolia and used to make up your index.

If you want to learn more about what a record is, I suggest looking at [this algolia guide](https://www.algolia.com/doc/guides/sending-and-managing-data/prepare-your-data/in-depth/what-is-in-a-record/).

Your index is usually made up of many records. The index is the place where the data that you want to search is stored. It's highly optimized for search operations, so that people searching for something will receive the right results fast. 

*Indexing* itself is the task of processing the records in our system. That's something that happens automatically and usually only takes a few seconds, when you update or add new records.

Regarding custom ranking, the attributes used for that depend on your records and the available data. The Algolia ranking takes care of all the default criteria, like word matching and geo location. Therefore, typical examples of custom ranking attributes include popularity or rating. Sticking to our phone selling example from above, a good custom ranking criteria could be the `avg_customer_rating`. 

To learn more about ranking, check out this [page](https://www.algolia.com/doc/guides/managing-results/must-do/custom-ranking/).

Since custom rankings depend on your individual setup, I suggest we schedule a quick meeting for tomorrow at 10am German time. Let me know if another time works better for you.

Hope this helps you, let me know if there is anything else I can help you with.

Looking forward to speaking to you soon!<br>
Alex

---

### Question 2:
<em>Hello,

Sorry to give you the kind of feedback that I know you do not want to hear, but I really hate the new dashboard design. Clearing and deleting indexes are now several clicks away. I am needing to use these features while iterating, so this is inconvenient.

Regards,
Matt</em>

### Answer 2:

Hi Matt,

I'm sorry to hear that you don't like the new dashboard design.

Just to make sure we're on the same page, when you mention "several clicks away", what exactly are you referring to?
[Clearing and deleting](https://www.algolia.com/doc/guides/sending-and-managing-data/manage-indices-and-apps/manage-indices/how-to/delete-indices/#:~:text=Clear%20records%20from%20an%20index%20in%20the%20Algolia%20dashboard,-If%20you%20only&text=On%20the%20left%20sidebar%2C%20select%20Search.,-Select%20your%20Algolia&text=Select%20Manage%20index%20%3E%20Clear.,to%20confirm%20and%20click%20Clear.) can be handled with 3 clicks from a selected index, by clicking on "Manage index" --> "Clear/Delete" --> Type `CLEAR` and click "Clear".

If that's what you're referring to, have you considered using the API to automate this process or build a custom UI for clearing/deleting?

I'm happy to provide you with a script which can handle the deleting/clearing. Let me know if that's something you're interested in.

In any way, thanks for the feedback! I'll reach out to the engineering team and position this as a product feature. In the meantime, let me know if you need any further assistance!

Kind regards,<br>
Alex

---

### Question 3:
<em>Hi,

I'm looking to integrate Algolia in my website. Will this be a lot of development work for me? What's the high level process look like?

Regards,
Leo</em>

### Answer 3:

Hi Leo,

Great to hear from you. Getting a first integration done is usually very fast and doesn't include a lot of development work. Check out our [quickstart](https://www.algolia.com/doc/guides/getting-started/quick-start/) if you haven't already done that.

If you're using a platform like [Shopify](https://www.algolia.com/doc/integration/shopify/getting-started/quick-start/?client=ruby) or [Netlify](https://www.algolia.com/doc/tools/crawler/netlify-plugin/quick-start/) we even offer Integrations to speed up your implementation.

That being said, depending on your environment and how your data is currently structured it may require some preparation. In addition, setting up and configuring all the features Algolia offers can take additional time.

The high level process looks like this:
- Create an Algolia Account
- Prepare and add your data
- Add Algolia to your application

I know this is very high level. In order for me to give you more guided feedback, I'll need some more details on how you're planning to integrate Algolia and your current setup.

Feel free to send me some details via email. Alternatively we can set up a quick call to discuss any questions you have.


Looking forward to heraing from you and have a great day!<br>
Alex
