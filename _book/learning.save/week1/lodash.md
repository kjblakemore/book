# Lodash 101

[Lodash](https://lodash.com/docs) is one of the most popular utility-belt library.
It can make you very productive and effective in writing Javascript programs.

Read Lodash's page on npm [here](https://www.npmjs.com/package/lodash). How many times
was it downloaded just last week alone?

It was downloadeed 4,326,487 times.

## Examples

### Array of numbers

{% set data = [1,2,3,4,5] %}

Let's create a data array with the contents: {{data}}. This array has {{ data.length }} items.

To get the first item, we can use lodash's [_.first](https://lodash.com/docs#first).

{% lodash %}
return _.first(data)
{% endlodash %}

The result is {{ result }}.

To get the first 3 elements, we can use lodash's [_.take](https://lodash.com/docs#take)

{% lodash %}
return _.take(data, 3)
{% endlodash %}

The result is {{ result }}.

### Array of objects

Let's create a data array consisting of objects.

{% set data = [{name: 'John', age: 45}, {name: 'Mary', age: 32}, {name: 'Peter', age: 54}] %}

We can dump the content using the `dump` filter.

{{ data | dump }}

To retrieve the name field from each object in this array, lodash's
[_.pluck](https://lodash.com/docs#pluck) is very handy.

{% lodash %}
return _.pluck(data, 'name')
{% endlodash %}

The result is {{ result }}.

We can even display the result nicely as a bullet list

<ul>
{% for d in result %}
<li>
    {{d}}
</li>
{% endfor %}
</ul>

Using [_.find](https://lodash.com/docs#find), we can look up an object by its field.

Let's try to find out how old Mary is.

{% lodash %}
return _.find(data, {name: 'Mary'})
{% endlodash %}

Mary is {{ result.age }} years-old.

## Challenges

Now it's your turn to take the following learning challenges.

### Data

{% set data = [{name: 'John', age: 45}, {name: 'Mary', age: 32}, {name: 'Peter', age: 54}, {name: 'Jane', age: 12}] %}

The data is

{{ data | dump}}

### Q: What are the ages of these people?

{% lodash %}
ages = _.pluck(data, 'age')
return ages
{% endlodash %}

The ages are {{ result }}


### Q. What is the youngest age?

{% lodash %}
min_age = _.min(ages)
return min_age
{% endlodash %}

The youngest age is {{ result }}.

### Q. What is the oldest age?

{% lodash %}
return _.max(ages)
{% endlodash %}

The oldest age is {{ result }}.

### Q. Who is the youngest person?

{% lodash %}
return _.find(data, {age: min_age})
{% endlodash %}

The youngest person is {{ result.name }}.
