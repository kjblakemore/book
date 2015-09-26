{% data src="birdstrike.json" %}
{% enddata %}

# Report

As a team, answer a subset of the questions submitted during the hackathon.
But instead of using Tableau, you will need to write Javascript/Lodash code
to derive your answers. Similar to before, each team member is responsible for
one question. But everyone should work together to come up with a good solution.
Your answer should consist of Lodash code and a brief writeup.
Utilize `_.map`, `_.filter`, `_.group` ...etc. Do not se any for loop.

This time, the data is not already prepared for you in a nice JSON format. You
will need to do it on your own, replacing the placeholder `birdstrike.json` with
real data.

#1 Which airline have to incur most repair cost due to damage ? ( sumi6109).
{% lodash %}
var group = _.groupBy(data, "Aircraft.Airline");
var repair_sum = _.mapValues(group, function(n){

   var repair = _.pluck(n, "Cost.Repair")
   return _.sum(repair)
})
var max = _.max(repair_sum);

var highest_repair =  _.pick(repair_sum, function(d){
   return d == max;
});

return highest_repair 

return result
{% endlodash %}
<table>
{% for key, value in result %}
    <tr>
        <td>{{key}}</td>
        <td>{{value}}</td>
    </tr>
{% endfor %}
</table>

#2 Which Airport has the highest number struck? (zhya215 ).

{% lodash %}
var group = _.groupBy(data, "Airport.Name");
var total_sum = _.mapValues(group, function(n){
   return n.length;
});
var max = _.max(total_sum);
var highest =  _.pick(total_sum, function(d){
   return d == max;
});
return highest
{% endlodash %}
<table>
{% for key, value in result %}
    <tr>
        <td>{{key}}</td>
        <td>{{value}}</td>
    </tr>
{% endfor %}
</table>

#3 Which plane model strikes the most birds? (twagar95) 

{% lodash %}
var group = _.groupBy(data,"Aircraft.Make");
var result = _.mapValues(group, function(n){
	return n.length
});
var max = _.max(result);

var highest =  _.pick(result, function(d){
   return d == max;
});
return highest
{% endlodash %}
<table>
{% for key, value in result %}
    <tr>
        <td>{{key}}</td>
        <td>{{value}}</td>
    </tr>
{% endfor %}
</table>

#4 What state had the highest number of bird strikes?  (drewdinger).

{% lodash %}
var group = _.groupBy(data,"Origin");
var result = _.mapValues(group, function(n){
	return n.length
});
var max = _.max(result);

var highest =  _.pick(result, function(d){
   return d == max;
});
return highest
{% endlodash %}
<table>
{% for key, value in result %}
    <tr>
        <td>{{key}}</td>
        <td>{{value}}</td>
    </tr>
{% endfor %}
</table>

#5 (What airports have the most expensive average accident) by (Karen Blakemore)
{% lodash %}
/* First group by airport */
var airports = _.groupBy(data, 'Airport.Name')
/* Then collect costs of birdhits */
var costByAirport = _.mapValues(airports, function(d) {
	return _.pluck(d, 'Cost.Total')
})
/* Next, calculate averge cost for each airport */
var avgCostByAirport = _.mapValues(costByAirport, function(d) {
	var nums = _.map(d, function(n) {
		return _.parseInt(n.split(',').join(''))
	})
	return _.sum(nums)/nums.length
})
/* Finally, convert object to array type and sort by avg cost */
var sortedAvgCostByAirport = _.sortByOrder(
	_.pairs(avgCostByAirport),
	function(d) {return d[1]},
	'desc'
)
/* Just return top 10 */
var topTenAvgCostByAirport = _.take(sortedAvgCostByAirport, 10)
return topTenAvgCostByAirport
{% endlodash %}
<p><b>Top 10 Airports With Most Expensive Average Accident</b></p>
<table>
{% for airport in result %}
    <tr>
        <td>{{airport[0]}}</td>
        <td>{{airport[1]}}</td>
    </tr>
{% endfor %}
</table>
