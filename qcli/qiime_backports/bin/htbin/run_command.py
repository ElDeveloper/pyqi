#!/usr/bin/env python
import cgi

from qcli.interface.cli import clmain, cli
from qcli.qiime_backports.bin.htbin.util import get_cmd_obj, format_page_header, format_page_footer


form = cgi.FieldStorage()
 
cmd_name = form.getvalue('command')
cmd_interface_class = get_cmd_obj(cmd_name)
cmd = cmd_interface_class.CommandConstructor()
#cmd_interface = cmd_interface_class()
brief_desc = cmd.BriefDescription
long_desc = cmd.LongDescription
 
print format_page_header()
print "<h2>%s</h2>" % cmd_name
print brief_desc
print "<br/>"
print long_desc
print "<form method='POST' action='command_results.py'>"
print "<table border='1'>"
for parameter in cmd.Parameters:
    print "<tr><td>{0}</td><td><input type='text' value='{1}' id='qiime_parameter_{0}' name='qiime_parameter_{0}' /></td></tr>".format(parameter.Name, parameter.Default)
print "</table>"
print "<input type='hidden' name='{0}' id='{0}' value='{1}' />".format('command', cmd_name)
print "<input type='submit' value='Run!' />"
print "</form>"
print format_page_footer()
