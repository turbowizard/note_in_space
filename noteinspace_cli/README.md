# Note In Space CLI
### CLI to manage your notes
made with [click](https://github.com/pallets/click)
## installation
**requirements:**  
  
- [noteinspace](https://github.com/turbowizard/Note_In_Space/tree/master/noteinspace)  
- click - `pip install click` 
 
clone or download  
open `nis_cli.py` in editor, set `sf = '<PATH/FILE>.json'`
## usage
commands:
  
* nis_cli.py note - new note (--space optional)  
* nis_cli.py get_all - get all notes  
* nis_cli.py get_note `note_id`  
* nis_cli.py del_note `note_id`  
* nis_cli.py spaces - get all spaces  
* nis_cli.py del_space `space_name`  
* nis_cli.py in_space `space_name`  
* nis_cli.py recent `count`  
* nis_cli.py last
* nis_cli.py wipe
