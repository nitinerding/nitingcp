#!/Users/D073341/jirapython/bin/python
# This script shows how to connect to a JIRA instance with a
# username and password over HTTP BASIC authentication.

from collections import Counter
from jira import JIRA
import re
import os
import json
import sys
import imp



# By default, the client will connect to a JIRA instance started from the Atlassian Plugin SDK.
# See
# https://developer.atlassian.com/display/DOCS/Installing+the+Atlassian+Plugin+SDK
# for details.
jira = JIRA(basic_auth=('CX_SRETECH', '[3O~%ki:pHb5CwLlINli'), options={'server': 'https://jira.hybris.com'})    # a username/password tuple


block_size = 1000
block_num = 0
count = 0

while True:
 start_idx = block_num*block_size
 issues = jira.search_issues('project=SREKYXF', start_idx, block_size)
 #print issues
 if len(issues) == 0:
 # Retrieve issues until there are no more to come
    break
 block_num += 1
 for issue in issues:
     if issue.fields.assignee is None and "Access request for XF cluster as test" in issue.fields.summary and "Todo" in issue.fields.status.name:
        count += 1
        #print issue.key, issue.fields.summary, issue.fields.assignee, issue.fields.description
        filename = (issue.key).encode('utf8')
        print "=========================================================="
        print 'Updating issue:' + filename + ' with following information'
        desc = (issue.fields.description).encode('utf8')
        with open(filename, 'w') as the_file:
             the_file.write(desc)

        with open(filename) as f:
             lines = f.readlines()
             for line in lines:
                 line = line.strip()
                 if line:
                     for item in line.split("\n"):
                        if "Name" in item:
                            username = item.strip().split(':')
                            username = username[1]
                            print "  Username:" + username
                        if "Email" in item:
                            emailid = item.strip().split(':')
                            emailid = emailid[1]
                            print "  Email:" + emailid
                        if "Retention" in item:
                            retention = item.strip().split(':')
                            retention = retention[1]
                            print "  Retention Period:" + retention
        jira.add_comment(issue, 'SCRIPT Testing Message: The access for extension factory for user ' + username + ' that has email addess' + emailid + ' with a retention period ' + retention + ' has been completed')

        print "Changed Issue STATUS from Todo to In Progress"
        transitions = jira.transitions(issue)
        #for t in transitions:
        #    print t['id'], t['name']
        jira.transition_issue(issue, '31')
        #jira.transition_issue(issue, '31', assignee={'name': 'CX_SRETECH'})
        #31 In Progress
        #51 Awaiting Review
        #61 Todo
        #71 Closed
        print "=========================================================="

#print count
if count == 0:
  print "No New access Request ticket in queue"
