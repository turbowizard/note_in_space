# Note In Space Server
### REST HTTP noteinspace interface
Running with [Flask](https://github.com/pallets/flask)

## Installation
**requirements:**  
  
- [noteinspace](https://github.com/turbowizard/Note_In_Space/tree/master/noteinspace)  
- flask - `pip install flask` 
 
clone or download  
open `app.py` in editor, set `sf = '<PATH/FILE>.json'` (line 3)  
`python  app.py`  
`* Running on http://127.0.0.1:5007/ (Press CTRL+C to quit)`
## APIs
**methods api : descriptoin**  
GET /api/notes : get all notes  
POST /api/notes : create new note, POST data: JSON : [Note()](https://github.com/turbowizard/Note_In_Space/tree/master/noteinspace)  
GET /api/notes/<int:note_id> : get note by id  
DELETE /api/notes/<int:note_id> : delete note by id  
GET /api/notes/recent/<int:recent_count> : get recent by count  
GET /api/spaces : get all spaces  
GET /api/spaces/<string:space> get notes in space  
Example: http://127.0.0.1:5007/api/notes  
