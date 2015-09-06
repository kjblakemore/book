# Analysis

{% import './data.html' as data %}

After completing the warmup exercises, your task is to do four more slightly challenging analyses.

## How many students like sushi as their favorite food?

{% lodash %}
var LANGUAGES = ['c', 'python', 'ruby', 'haskell', 'javascript', 'java', 'c++', 'c#', 'js']

/* Parse comments to use later */
function parse_comments(comments) {
	var uid = comments.user.login
	var lines = comments.body.split('\r\n')
	var name = (lines[0].split(':'))[1]
	var major = (lines[1].split(':'))[1]
	var lang = (lines[2].split(':'))[1].toLowerCase().split(/\s|,/)	
	lang = _.intersection((_.includes(lang, 'js')? _.remove(lang, ['js']).concat('javascript'):lang), LANGUAGES)	
	var food = (lines[3].split(':'))[1].toLowerCase()
	return {'Uid': uid, 'Name': name, 'Major': major, 'Lang': lang, 'Food': food}
}

data.students = (data.comments).map(parse_comments)

var sushi_lovers = _.reduce(_.pluck(data.students, 'Food'), function(memo, food) {
	return memo + Number(food.indexOf('sushi') != -1)
}, 0)

return [sushi_lovers]
{% endlodash %}
The answer is {{result}}

## Who are the students liking Python the most?

{% lodash %}
var pythonistas = _.pluck(_.filter(data.students, 
	function(student) {
  		return _.includes(student.Lang, 'python')
	}), 'Name')

return [pythonistas]
{% endlodash %}
Their names are {{result}}.

# Are there more Javascript lovers or Java lovers?

{% lodash %}
var java_fans = _.filter(data.students, function(student){
	return _.includes(student.Lang, 'java')
})

var javascript_fans = _.filter(data.students, function(student) {
	return _.includes(student.Lang, 'javascript') || _.includes(student.Lang, 'js')
})

var java_vs_js = (java_fans.length > javascript_fans.length? 'Java': 'Javascript')

return [java_vs_js]
{% endlodash %}
The answer is {{result}}.

## Who likes the same food as `kjblakemore`?

{% lodash %}
var names = _.filter(data.students, function(student) {
		return student.food == _.result(_.find(data.students, function(student) {
  	return student.Uid == 'kjblakemore'
	}), 'Food')
})

return [names]
{% endlodash %}
Their names are {{result}}.
