{% data src="fcq.clean.json" %}
{% enddata %}

# Report

As a class, we brainstormed and came up with a long list of further questions we
can ask based on the FCQ data. Out of these questions, our team chose to tackle on
the following questions. Each member on our team is reponsible for one question

## What is the ranking of Departments within the College of Engineering & Applied Sciences, based on average course rating and average instructor rating? (by Kevin)

{% lodash %}

/* First filter by college, then group by department */
var departments = 
_.groupBy(
	_.filter(data, {'CrsPBAColl': 'EN'}), 
	'CrsPBADept')

/* Then collect course and instructor ratings for each depatment, ignoring null ratings. */
var course_ratings = 
_.mapValues(departments,
	function(d) {
		return _.filter(
			_.pluck(d, 'AvgCourse'),
			function(rating) {return rating != null}
		)
	}
)
	
var instructor_ratings = 
_.mapValues(departments,
	function(d) {
		return _.filter(
			_.pluck(d, 'AvgInstructor'),
			function(rating) {return rating != null}
		)
	}
)

/* Next, calculate average rating per department */
var avg_course_ratings = 
_.mapValues(course_ratings, 
	function(c) {return _.sum(c)/c.length}
)
var avg_instructor_ratings = 
_.mapValues(instructor_ratings, 
	function(c) {return _.sum(c)/c.length}
)

/* Finally convert object to array type and sort by ratings */
var sorted_avg_course_ratings =
_.sortByOrder(
	_.pairs(avg_course_ratings),
	function(c) {return c[1]},
	'desc'
)		
var sorted_avg_instructor_ratings =
_.sortByOrder(
	_.pairs(avg_instructor_ratings),
	function(c) {return c[1]},
	'desc'
)	

return [sorted_avg_course_ratings, sorted_avg_instructor_ratings]

{% endlodash %}

<p><b>Average Course Ratings</b></p>
<table>
{% for course in result[0] %}
    <tr>
        <td>{{course[0]}}</td>
        <td>{{course[1]}}</td>
    </tr>
{% endfor %}
</table>

<p><b>Average Instructor Ratings</b></p>
<table>
{% for course in result[1] %}
    <tr>
        <td>{{course[0]}}</td>
        <td>{{course[1]}}</td>
    </tr>
{% endfor %}
</table>

## How does retention compare across departments? (by Zach)

{% lodash %}

/* Group by department, then calculate the average withdrawel rate */
var grps = _.groupBy(data, 'CrsPBADept')
var result =_.mapValues(grps, function(d){
    return _.sum(_.pluck(d, 'PCT.WDRAW'))/d.length
})

/* Convert object to array and sort by withdrawal rate */
result = _.sortByOrder(_.pairs(result),function(d){return d[1]},'desc')
return result

{% endlodash %}

<p><b>Average Course Withdrawal Rate</b></p>
<table>
{% for department in result %}
    <tr>
        <td>{{department[0]}}</td>
        <td>{{department[1]}}</td>
    </tr>
{% endfor %}
</table>


## What is the distribution of instructor type (e.g., Lecturer, Assistant Professor, Instructor) across departments? (by Karen)

{% lodash %}
/* First group by department */
var departments = _.groupBy(data, 'CrsPBADept')

/* Then collect titles for all classes in each department */
var titles = _.mapValues(departments, function(d) {
	return _.pluck(_.flatten(_.pluck(d, 'Instructors')), 'title')
})

/* Finally, compute length for each title */
var grps = _.mapValues(titles, function(d) {
	return _.mapValues(_.groupBy(d, function(title) {return title}), 'length')
})

return grps
{% endlodash %}

{% for dept, titles in result %}
<p><b>{{dept}}</b></p>	
<table>
	{% for title, count in titles %}
    <tr>
        <td>{{title}}</td>
        <td>{{count}}</td>
    </tr>
	{% endfor %}
</table>
{% endfor %}

## What class has the highest GPA with the least amount of time spent each week? (by John)

{% lodash %}

/* First, extract all courses with the easiest work load */
var courses = _.groupBy(data, 'Workload.Hrs_Wk')['0-3']

/* Then, find those which have a 4.0 grade, remove duplicates and sort. */
return easy_As = _.unique(_.pluck(_.filter(courses, {'AVG_GRD': 4.0}), 'CourseTitle')).sort()

{% endlodash %}

<p><b>Easy A Courses</b></p>
<table>
{% for course in result %}
    <tr>
        <td>{{course}}</td>
    </tr>
{% endfor %}
</table>

## Which course level has the lowest retention? (by Andrew)

{% lodash %}

/* Group by level, then calculate average course withdrawal rate for each level */
var grps = _.groupBy(data, 'Level')
var result =_.mapValues(grps, function(d){
    return _.sum(_.pluck(d, 'PCT.WDRAW'))/d.length
})

/* Convert object to array and sort by withdrawal rate */
result = _.sortByOrder(_.pairs(result),function(d){return d[1]},'desc')
return result

{% endlodash %}

<p><b>Average Course Withdrawal Rate</b></p>
<table>
{% for level in result %}
    <tr>
        <td>{{level[0]}}</td>
        <td>{{level[1]}}</td>
    </tr>
{% endfor %}
</table>
