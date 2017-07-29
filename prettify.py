# -*- coding: utf-8 -*-	
import pyperclip
import simplejson as json
import time

def format_clipboard_to_json():

	recent_value = ""
	while True:
	    cb_content = pyperclip.paste()
	    if cb_content != recent_value:
	    	try:
	    		parsed = json.loads(cb_content)
	    		# must pass `sort_keys=True` because json isn't guaranteed to parse
	    		# and return the same sort order each time
	    		pretty_content = json.dumps(parsed, sort_keys=True, indent=2)
	    		pyperclip.copy(pretty_content)
	    		pretty_content = cb_content
	    	except ValueError:
	    		pass

	    time.sleep(2)

if __name__ == '__main__':
	format_clipboard_to_json()


