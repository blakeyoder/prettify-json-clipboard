# Prettifies JSON in your clipboard
___
Turn disappointing json into happy json!

:disappointed:
```
{"glossary":{"GlossDiv":{"GlossList":{"GlossEntry":{"Abbrev":"ISO 8879:1986","Acronym":"SGML","GlossDef":{"GlossSeeAlso":
["GML","XML"],"para":"A meta-markup language, used to create markup languages such as DocBook."},
"GlossSee":"markup","GlossTerm":"Standard Generalized Markup Language","ID":"SGML","SortAs":"SGML"}},"title":"S"},"title":"example glossary"}}
```
:smile:
```
{
  "glossary": {
    "GlossDiv": {
      "GlossList": {
        "GlossEntry": {
          "Abbrev": "ISO 8879:1986",
          "Acronym": "SGML",
          "GlossDef": {
            "GlossSeeAlso": [
              "GML",
              "XML"
            ],
            "para": "A meta-markup language, used to create markup languages such as DocBook."
          },
          "GlossSee": "markup",
          "GlossTerm": "Standard Generalized Markup Language",
          "ID": "SGML",
          "SortAs": "SGML"
        }
      },
      "title": "S"
    },
    "title": "example glossary"
  }
}
```
Installation:
1. Clone the repository
2. Create a new virtual env with `$ virtualenv venv`. See [docs](http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/) for more information on Python's virtual environment
3. `$ source project_name/bin/activate` 
4. `$ pip install requirements.txt`
5. `$ source start.sh` to run program

The program runs via the `nohup` command. This will prevent the process from being stopped on logout.
To force kill the process there are 2 commands you can run to find and kill this process.
```
$ lsof -c Python
$ kill -9 <PID>
```
