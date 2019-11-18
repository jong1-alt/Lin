c = get_config()
c.NotebookApp.notebook_dir="C:\\Users\\F121324609\\notebooks"

import webbrowser
webbrowser.register('chrome',None,
    webbrowser.GenericBrowser('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'))
c.NotebookApp.browser='chrome'

