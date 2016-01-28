# Mongodb Drills


## 1- Find the listing detail information for the Evernote app.

{% mongoquery %}

{"n":"com.evernote"}

{% endmongoquery %}

{{ data | json }}

There are {{ data.length }} apps.
The star rating of the first Evernote app is: {{ data[0].rate }}

## 2- How many apps developed by GO Launcher EX?
{% mongoquery %}

{"crt":"GO Launcher EX"},{"n":1}

{% endmongoquery %}

{{ data | json }}

There are {{ data.length }} apps.

## 3- How many apps have been downloaded more than 10,000,000?
{% mongoquery %}

{"dct": {"$gt": 10000000}}

{% endmongoquery %}

{{ data | json }}

There are {{ data.length }} apps that have been downloaded more than 10,000,000 times.

## 4- How many apps have the word "share" in their description?
Hint: the desc field is indexed with a text index. Use the $text operator.

{% mongoquery %}

{"$text": {"$search": "share"}}

{% endmongoquery %}

{{ data | json }}

There are {{ data.length }} apps that have the word "share" in their description.


## 5- Find apps that are categorized in any of the following categories: Productivity, Business, or Finance?
Hint: Use the $in operator.

{% mongoquery %}

{"cat": {"$in": ["Productivity", "Business", "Finance"]}}

{% endmongoquery %}

{{ data | json }}

There are {{data.length}} apps that are categorized as Productivity, Business or Finance.

## 6- Find apps that have been downloaded 10,000,000 or more but have star rating lower than 3 stars?
{% mongoquery %}

{"$and": [{"dct": {"$gte": 10000000}}, {"rate": {"$lt": 3}}]}

{% endmongoquery %}

{{ data | json }}

There is {{ data.length }} app.

Hint: The query matches one app in the dataset and the link to its Google Play listing page is:
https://play.google.com/store/apps/details?id={{data[0].n}} Read the reviews to find out why?

## 7- Find the title and creator of apps that have been rated above 4 stars by 1,000,000 or more users?
{% mongoquery %}

{"$and": [{"dct": {"$gte": 1000000}}, {"rate": {"$gt": 4}}]}

{% endmongoquery %}

{{ data | json }}

There are {{ data.length }} apps.

{% set numbers = [0,1,2,3,4,5,6,7,8,9] %}
<p><b>Ten Apps with High Ratings and Many Downloads</b></p>
<table>
	<tr>
		<th>Title</th>
		<th>Creator</th>
	</tr>
{% for i in numbers %}
    <tr>
        <td>{{data[i].n}}</td>
        <td>{{data[i].crt}}</td>
    </tr>
{% endfor %}
</table>


## 8- Find apps whose content rating is Teen but not categorized in any of the following categories: Card, Entertainment, Comics, and Puzzle?
{% mongoquery %}

{"$and": [{"crat": "Teen"}, {"cat": {"$not": {"$in": ["Card", "Entertainment", "Comics", "Puzzle"]}}}]}

{% endmongoquery %}

{{ data | json }}

There are {{ data.length }} apps.

## 9- Find the title, category, download count, and star rating of apps with the phrase "in-app purchase" in their description and download count greater than 10,000,000?
{% mongoquery %}

{"$and": [{"$text": {"$search": "\"in-app purchase\""}}, {"dct": {"$gt": 10000000}}]}

{% endmongoquery %}

{{ data | json }}

There are {{ data.length }} apps.

<p><b>Apps Downloaded Frequently From an App</b></p>
<table>
	<tr>
		<th>Title</th>
		<th>Category</th>
		<th>Downloads</th>
		<th>Rating</th>
	</tr>
{% for app in data %}
    <tr>
        <td>{{app.n}}</td>
        <td>{{app.cat}}</td>
        <td>{{app.dct}}</td>
        <td>{{app.rate}}</td>
    </tr>
{% endfor %}
</table>

## 10- Find the title and address of the creator of apps with download count greater than 1,000,000 and star rating greater than 4.5?
Hint: ensure that the results include apps that have creator address (not equal "")

{% mongoquery %}

{"$and": [{"dct": {"$gt": 1000000}}, {"rate": {"$gt": 4.5}}, {"cadd": {"$ne": ""}}]}


{% endmongoquery %}

{{ data | json }}

There are {{ data.length }} apps.

<p><b>Title and Creator Address of Apps with High Ratings and Many Downloads</b></p>
<table>
	<tr>
		<th>Title</th>
		<th>Address</th>
	</tr>
{% for app in data %}
    <tr>
        <td>{{app.n}}</td>
        <td>{{app.cadd}}</td>
    </tr>
{% endfor %}
</table>

## 11- Find the title, category, download count, and rating of apps with download count of 1,000,000 or more but have no privacy statements?

{% mongoquery %}

{"$and": [{"dct": {"$gte": 1000000}}, {"purl": {"$eq": ""}}]}

{% endmongoquery %}

{{ data | json }}

There are {{ data.length }} apps.

<p><b>Ten Apps with High Download Counts, but no Privacy Statements</b></p>
<table>
	<tr>
		<th>Title</th>
		<th>Category</th>
		<th>Downloads</th>
		<th>Rating</th>
	</tr>
{% set numbers = [0,1,2,3,4,5,6,7,8,9] %}
{% for i in numbers %}
    <tr>
        <td>{{data[i].n}}</td>
        <td>{{data[i].cat}}</td>
        <td>{{data[i].dct}}</td>
        <td>{{data[i].rate}}</td>
    </tr>
{% endfor %}
</table>

## 12- Find apps that have been released or updated this month (September 2015)?

{% mongoquery %}

{"dtp": {"$regex": "^September.*2015$"}}

{% endmongoquery %}

{{ data | json }}

There are {{ data.length }} apps
