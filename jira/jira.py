from jira import JIRA
import re

jac = JIRA('https://jira.hybris.com')

jira = JIRA(basic_auth=('CX_SRETECH', '[3O~%ki:pHb5CwLlINli'))

issue = jira.issue('SREKYXF-35')

print (issue)
