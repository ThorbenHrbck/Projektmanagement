# ToDos

Format:
- Taskname (i.e.: Create View for user page)
- Details (i.e.: use the format of manager page)
  - Acceptance Criteria (i.e.: needs to have button for adding users, colour schema has to be congruent)
                                

Task done?: 
- cross out in Tasks.md
- tell others, get review if necessary
- optional: define follow up tasks
- squash commits (commit message = task name) and merge branch in main


---
**Epics:**

A: Three roles with different Permissions: Projectmanager, User, Admin (User can mark tasks as done,
Admins can assign/change rights to users and managers, User can be assigned to projects by manager)


B: Project can be created, changed and deleted

C: A project has a name and includes tasks, times (Start/End etc.), and notes in a seperate field

---

ToDos:
1. Create roles (A)
   - 3 Roles
   - define rights  for roles
   - https://python.plainenglish.io/how-to-implement-role-based-access-control-rbac-in-django-a-step-by-step-guide-31c5e4053868)


2. Create Datamodel for tasks and projects (C)

   - projects include tasks, times, notes
   - no task without project
   - relation between tasks/projects and roles is defined
  


