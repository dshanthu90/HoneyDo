# HoneyDo
Task List Management

Login as user  will call the retrieve task list for that user 
GET http://192.168.1.2:5000/honeydo/honeycombs/{combID}/Tasks

Response
{

“Tasks” : [
{“id” : <>, 
“taskName” : <>,
“date” : <>}, 
…]

}


Retrieve Task List - all task list tab
GET http://192.168.1.2:5000/honeydo/honeycombs/{combID}/Tasks?userId=123455
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length:

{
“Tasks” : [
{“id” : <>, 
“taskName” : <>,
“assigned : <>,
“date” : <>}, 
…]
}





Create Task 
POST  http://192.168.1.2:5000/honeydo/honeycombs/{combID}/Tasks/ 

form {
Task title 
Assignee 
Task Due
}



Update Task 
PUT  http://192.168.1.2:5000/honeydo/honeycombs/{combID}/Tasks/{taskID}

{
“Type” : 
“UserID” :
“TaskDate” :
“DoneStatus” : 
}

