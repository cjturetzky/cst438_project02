import cgi;

form = cgi.FieldStorage();
item_name = form.getvalue('item_name');
print(item_name);