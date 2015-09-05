{% import './data.html' as data %}

# Report

As a class, we brainstormed and came up with a long list of further questions we can ask based
on the "self-introduction" data. Out of these questions, our team chose to tackle on
the following:

# What percentage of students are in the CS department?

{% lodash %}
var LANGUAGES = ['c', 'python', 'ruby', 'haskell', 'javascript', 'java', 'c++', 'c#', 'js']

/* Parse comments to use later */
function parse_comments(comments) {
	var uid = comments.user.login
	var created = comments.created_at
	var updated = Number(comments.updated_at > comments.created_at)
	var lines = comments.body.split('\r\n')
	var name = (lines[0].split(':'))[1]
	var major = (lines[1].split(':'))[1]
	var lang = (lines[2].split(':'))[1].toLowerCase().split(/\s|,/)	
	lang = _.intersection((_.includes(lang, 'js')? _.remove(lang, ['js']).concat('javascript'):lang), LANGUAGES)	
	var food = (lines[3].split(':'))[1].toLowerCase()
	return {'Uid': uid, 'Created': created, 'Updated': updated, 'Name': name, 'Major': major, 'Lang': lang, 'Food': food}
}

data.students = (data.comments).map(parse_comments)

var cs_students = _.filter(data.students, function(student) {
	var major = student.Major
	return major.indexOf('Computer Science') != -1 || major.indexOf('CS') != -1 || major.indexOf('CSCI') != -1 || major.indexOf('cs') != -1
})

return cs_students.length / data.students.length

{% endlodash %}

The answer is {{result}}

# What are the favorite languages?

{% lodash %}
var languages = _.countBy(_.reduce(_.pluck(data.students, 'Lang'), function(memo, lang) {
  		return memo.concat(lang)
	})
)

var languages_sorted = _.keys(languages).sort(function(a,b){return languages[b]-languages[a]})

return [languages_sorted]
{% endlodash %}

The favorite languages in decreasing order of popularity are: {{result}}

# How many students commented on the introduction issue before the first class.

{% lodash %}
var FIRST_CLASS_TIME = "2015-08-24T10:00:00Z"
var early_comments = _.reduce(_.pluck(data.students, 'Created'), function(memo, created) {
	return memo + Number(created <= FIRST_CLASS_TIME)
}, 0)
return [early_comments]
{% endlodash %}

The answer is {{result}}

# How many students updated their comments.

{% lodash %}
var updaters = _.reduce(_.pluck(data.students, 'Updated'), function(memo, updated) {
	return memo + updated
}, 0)

return [updaters]
{% endlodash %}

The answer is {{result}}

