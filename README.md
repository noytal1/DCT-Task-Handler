# DCT-Task-Handler
A task-handler CLI tool that gets Task IDs from users, fetches the task description from a REST API and executes it on the OS.
The tool flow is as follows:

1. The user's input has to be provided with the following flags:
  * --name = User's full name
  * --dept = Department (in company, one word)
  * --id = Task ID
  If any flag is missing (or all of them), the tool will run an interactive CLI to get the missing input.

2. The tool gets the task description from the DCT REST API:
https://dct-tasks-db.herokuapp.com/tasks
The API returns a data object that contains the task info, of the following structure:
There are only 3 description types of the following patterns:
  * "Copy latest X file" = copy the most updated file of extension X
  * "Copy heaviest X file" = copy the heaviest file of extension X
  * "Copy the X file named with S" = copy the file of extension X that contains the string S
  in its name
  For example: "Copy latest log file" / "Copy the png file named with IMPORTANT"

3. If some task ID does not exist, an empty object will return.
  In such a case – notify the user and ask again for the ID; after 3 failures – exit.

4. The source root directory with all its content will be provided to you; the destination root directory can be in any location on your OS.

5. The tool only executes tasks with "Open" status. For any other status, notify the user that the task cannot be executed due to its status, then exit.

6. Under source/auth directory, there is a configuration file called permissions.json, that tells what are the allowed task types for each department:
  The key is the department name, and the value is the list of allowed tasks. The tool must verify that the required task is allowed for the department the user belongs to. If the user has no permissions, or their department does not appear in the list at all – notify and exit.

7. For every executed task, the tool creates a log file under 'logs' directory (should be located in destination root directory). The log should detail:
  * Task ID
  * The full username (that requested the task)
  * A full description of the task

Constraints:
1. Currently the DB holds only 5 tasks – use them for debug: 3582, 6911, 7080, 7599, 8843.
2. Assume user is not aware of the input's case sensitivity they provide.
3. The task description string will only contain single space characters.
4. All the required files in tasks will always be in destination path (no need to validate that).
5. If destination does not exist – create it.
6. If any file already exists in the destination – override it.
