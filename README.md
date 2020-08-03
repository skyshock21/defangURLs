# defangURLs
Read malicious URLs from a file, sorts ascending, removes duplicates, defangs them, and writes them to another file   

# Read From File, Defang, Output To Sorted List

The script defangURLs.py is a wrapper for defang.py by Johan Nestaas (https://bitbucket.org/johannestaas/defang/src/master/).  It allows you to input a text file containing potentially malicious URLs, and it will output a text file of defanged URLs, duplicates removed, and sorted in ascending order.  It can serve as a library to be imported as well.

## Run Application

Requires python package defang

```
pip install defang
```

In the directory where the script is stored run:

```
python defangURLs.py SomeFile.txt
```

If running properly, the file created will contain a list of sanitized URLs for use in threat reporting
