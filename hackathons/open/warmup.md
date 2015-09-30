# Warmup

Complete this warmup exercise to get an idea how to put all the different pieces
together to generate an end-to-end data analysis viz report.

<a name="top"/>
<div id="autonav"></div>

{% data src="../fcq/fcq.clean.json" %}
{% enddata %}

{% viz %}

{% title %}

What is the distribution of courses across colleges?

{% solution %}

var groups = _.groupBy(data, 'CrsPBAColl')

var counts = _.map(groups, function(value, key) {
    return {'name': key, 'count': _.pluck(value, 'Course').length}
})

console.log(counts)

var x = 0

function computeX(d, i) {
    return x
}

function computeHeight(d, i) {
    return d.count >= 400 ? 400 : d.count
}

function computeWidth(d, i) {
    var width = d.count < 400 ? 20 : (d.count/400) * 20
    x = x + width
    return width
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
console.log(viz)

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
