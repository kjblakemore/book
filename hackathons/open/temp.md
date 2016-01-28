# Report

Use only Javascript and SVG to produce a data analysis / visualization report.

# Authors

This report is prepared by
* [Karen Blakemore](https://github.com/kjblakemore)
* [Matt Schroeder](https://github.com/mattschroeder97)

<a name="top"/>
<div id="autonav"></div>

{% data src="GVP_Volcano_List.json" %}
{% enddata %}

{% viz %}

{% title %}

Which five countries have the most volcanoes? (by Matt)

{% solution %}

{% template %}

{% endviz %}

{% viz %}

{% title %}

What is the distribution of known eruptions? The chart shows eruptions every 1000 years from the current year through 9540 BCE. (by Karen)

{% solution %}

// Filter out eruptions with unknown dates
var knownEruptions = _.reject(data, {'Last Known Eruption': 'Unknown'})

// Group by eruption millennium
var groups = _.groupBy(knownEruptions, function(d) {
	var date = d['Last Known Eruption'].split(' ')
	year = _.parseInt(date[0])
	return Math.floor((date[1] == 'BCE' ? -year : year)/1000)
})

// Map to millennium and number of eruptions in that millennium
var counts = _.map(groups, function(value, key) {
	return {'name': key, 'count': value.length}
})

// Sort by millennium
var sortedCounts = _.sortByOrder(counts, function(d) {
	return _.parseInt(d.name)
})

function computeX(d, i) {
	return 55*i
}

function computeHeight(d, i) {
	return d.count * (400/434)
}

function computeWidth(d, i) {
	return 50
}

function computeY(d, i) {
    return 0
}

function computeColor(d, i) {
	return 'red'
}

var viz = _.map(counts, function(d, i){
            return {
                x: computeX(d, i),
                y: computeY(d, i),
                height: computeHeight(d, i),
                width: computeWidth(d, i),
                color: computeColor(d, i)
            }
         })

var result = _.map(viz, function(d){
         // invoke the compiled template function on each viz data
         return template({d: d})
     })
return result.join('\n')

{% template %}

<rect x="${d.x}"
      y="${d.y}"
      height="${d.height}"
      width="${d.width}"
      style="fill:${d.color};
             stroke-width:3;
             stroke:rgb(0,0,0)" />

{% endviz %}

