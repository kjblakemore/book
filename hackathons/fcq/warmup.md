{% data src="fcq.clean.json" %}
{% enddata %}

# Warmup

Next, complete the following warmup exercises as a team.


## How many unique subject codes?

{% lodash %}

return _.compact(_.uniq(_.pluck(data, 'Subject'))).length

{% endlodash %}

They are {{ result }} unique subject codes.


## How many computer science (CSCI) courses?

{% lodash %}
return _.filter(data, {'CrsPBADept': 'CSCI'}).length
{% endlodash %}

They are {{ result }} computer science courses.

## What is the distribution of the courses across subject codes?

{% lodash %}

var groups = _.groupBy(data, 'Subject')
return _.mapValues(groups, function(g) {
    return g.length
})

{% endlodash %}

<table>
{% for key, value in result %}
    <tr>
        <td>{{key}}</td>
        <td>{{value}}</td>
    </tr>
{% endfor %}
</table>

## What subset of these subject codes have more than 100 courses?

{% lodash %}

var grps = _.groupBy(data, 'Subject')
return _.pick(_.mapValues(grps, function(d){
    return d.length
}), function(x){
    return x > 100
})

{% endlodash %}

<table>
{% for key, value in result %}
    <tr>
        <td>{{key}}</td>
        <td>{{value}}</td>
    </tr>
{% endfor %}
</table>


## What subset of these subject codes have more than 5000 total enrollments?

{% lodash %}

var grps = _.groupBy(data, 'Subject')
return _.pick(_.mapValues(grps, function(d){
    var numberEnrolled = _.pluck(d, 'N.ENROLL')
    return _.sum(numberEnrolled)
}), function(x){
    return x > 5000
})

{% endlodash %}

<table>
{% for key, value in result %}
    <tr>
        <td>{{key}}</td>
        <td>{{value}}</td>
    </tr>
{% endfor %}
</table>


## What are the course numbers of the courses Tom (PEI HSIU) Yeh taught?

{% lodash %}

return _.pluck( 
    _.filter(data, function(d) {
        return _.find(d.Instructors, {'name': 'YEH, PEI HSIU'})
    }), 'Course'                                       
)

{% endlodash %}

They are {{result}}.