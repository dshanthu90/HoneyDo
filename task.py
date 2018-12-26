from flask import (request, url_for, jsonify, flash)
import datetime as dt
from HoneyDo import (db, app )
from werkzeug.utils import redirect


@app.route('/honeydo/honeycombs/<int:combId>/tasks/<int:userId>', methods='GET','POST')
# Comb id is not being used anywhere
# if user Id is passed, it will retrieve task list for that user
# If user id is not passed in the url, it will retrieve all task list which is not done
def task_list_fun(combId, userId):
    if request.method == 'POST':
        v_task_detail  = request.form['Task Description']
        v_task_due  = request.form['Due']
        v_task_created_by = userId
        v_task_assigned = request.form['Assigned To']
        v_task_status = 0
        error = None

        if not v_task_detail:
            error = 'Task Description is required.'
        if not v_task_due:
            v_task_due = dt.date.today
        if not v_task_assigned:
            v_task_assigned = userId

        if error is not None:
            flash(error)
        else:
            dbo = db.connect_db()
            dbo.execute(
                'INSERT INTO task_list(task_detail,task_due,task_created_by, task_assigned, task_status) VALUES(?,?,?,?,?)',
                (v_task_detail,v_task_due,v_task_created_by, v_task_assigned, v_task_status)
            )
            dbo.commit()
            return redirect(url_for('task_list'))
     if userId is not None :
        task_list = db.execute(
        'SELECT task_desc FROM task_list WHERE task_assigned=? AND task_status = 0 ', (userId))
     else :
         task_list = db.execute(
             'SELECT  task_desc from task_list WHERE task_status = 0')
    return jsonify(task_list)